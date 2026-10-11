# Formación Veraqua – automatización de Moodle

Herramientas para que Claude cree y mantenga el contenido de la formación en
https://formacion.veraqua.es a través de la API de servicios web de Moodle.

## 1. Activar la API en Moodle (lo hace un administrador, una sola vez)

1. **Administración del sitio → General → Funciones avanzadas**: activar *Habilitar servicios web*.
2. **Administración del sitio → Servidor → Servicios web → Administrar protocolos**: activar **REST**.
3. Crear un usuario dedicado, p. ej. `claude-bot`, con un rol que tenga
   `webservice/rest:use` y permisos de edición de curso (rol *Profesor/editingteacher*
   en los cursos de la formación, o *Gestor* en su categoría).
4. **Servicios web → Servicios externos → Agregar**: servicio `Claude`, habilitado,
   *Solo usuarios autorizados*. Añadirle estas funciones:

   | Para qué | Funciones |
   |---|---|
   | Leer | `core_webservice_get_site_info`, `core_course_get_courses`, `core_course_get_categories`, `core_course_get_contents`, `core_enrol_get_enrolled_users` |
   | Crear/editar cursos | `core_course_create_courses`, `core_course_update_courses`, `core_course_duplicate_course` |
   | Secciones (temas) | `core_courseformat_update_course` (Moodle ≥ 4.0), `core_course_edit_section` |
   | Ficheros | `core_files_upload` |
   | Visibilidad/borrado de actividades | `core_course_edit_module`, `core_course_delete_modules` |

5. Autorizar al usuario `claude-bot` en el servicio y crear un **token**
   (*Servicios web → Administrar tokens*). Compartir el token por un canal seguro;
   no se guarda en este repositorio.

## 2. Uso del cliente

```bash
export MOODLE_URL=https://formacion.veraqua.es
export MOODLE_TOKEN=...            # el token del paso 5
python3 tools/moodle_client.py info          # comprueba conexión y funciones permitidas
python3 tools/moodle_client.py courses
python3 tools/moodle_client.py contents 2
python3 tools/moodle_client.py dump 2 export
```

## 3. Limitación importante: crear actividades

La API estándar de Moodle **no tiene funciones para crear actividades**
(páginas, cuestionarios, libros, etiquetas…); solo cursos, secciones y ficheros.
Para que Claude pueda generar el contenido hay dos vías:

- **Plugin local propio** (recomendado): un plugin pequeño (`local_veraquaapi`)
  que expone funciones como `create_page`, `create_label`, `create_quiz`, usando la API
  interna `create_module()` de Moodle. Se instala una vez en el servidor.
- **Copias de seguridad (.mbz)**: Claude genera el curso como copia de seguridad y
  un administrador la restaura. Más manual y sin edición incremental.

## 4. Flujo de trabajo propuesto

Claude trabaja en un curso o sección **oculto** ("borrador"); una vez al día
revisáis lo creado y lo hacéis visible. El contenido fuente (textos, preguntas)
se versiona también en este repositorio para tener historial de cambios.
