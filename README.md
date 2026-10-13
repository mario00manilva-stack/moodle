# Temario de VERAQUA FORMACIÓN

Herramientas para construir el temario de los módulos del certificado
`SEA_C_006_4B` (cursos con idnumber `1732`, `1697` y `1701`) y entregarlo al aula
https://formacion.veraqua.es como copias `.mbz` de actividad.

## Flujo acordado con sistemas

1. Sistemas envía una **instantánea sin expediente** de cada módulo (`.mbz` de curso, `users=0`).
2. Se restaura en un **Moodle 5.2.2 local** (`local-moodle/setup.sh`) y se construye encima.
3. Cada actividad nueva se exporta como **copia de actividad** (`exportar_actividad.php`).
4. Sistemas la añade al módulo con `admin/cli/restore_backup.php --courseid=…` tras hacer su
   propia instantánea previa.

Además hay un token REST **de solo lectura** (4 funciones, caducidad de 3 meses) para consultar el
estado real del aula antes de cada entrega: `tools/moodle_client.py`.

## Reglas (no negociables)

- **Construir siempre sobre la instantánea.** La copia de actividad se restaura en la sección con
  el mismo número; si ese número no existe en producción, Moodle la deja en la primera sección sin
  avisar. `crear_actividad.php` se niega a crear en una sección inexistente: si hace falta una
  sección nueva, se pide antes a sistemas.
- **Solo entregas aditivas.** Si alguna vez hay que reemplazar, se avisa antes.
- No cambiar `idnumber`, nombre, `shortname` ni categoría de los módulos: la receta de producción
  los revierte en cada despliegue.
- La marca se escribe siempre **VERAQUA**.
- Moodle local fijado en **v5.2.2** (`2026042002.00`): un `.mbz` solo restaura en una versión igual
  o superior, y producción está en `2026042002.01` (salto a 5.3 LTS previsto).
- Ningún `.mbz` entra en el repositorio (ver `.gitignore`).

## Uso

```bash
local-moodle/setup.sh                        # instala/arranca Moodle local (idempotente)
php /opt/moodle-src/admin/cli/restore_backup.php --file=instantaneas/1732.mbz --categoryid=1

php local-moodle/cli/crear_actividad.php --course=1732 --spec=temario/1732/s02-libro.json
php local-moodle/cli/exportar_actividad.php --cmid=<id> --out=entregas/
```

Ficha de actividad (rutas relativas a la ficha):

```json
{"type": "book", "name": "Tema 2 · …", "section": 2, "intro": "<p>…</p>",
 "chapters": [{"title": "Introducción", "file": "t2-01.html"},
              {"title": "Detalle", "file": "t2-02.html", "subchapter": 1}]}
{"type": "page",  "name": "Bienvenida", "section": 1, "content_file": "bienvenida.html"}
{"type": "label", "section": 1, "content_file": "aviso.html"}
```

Probado en local: un libro con subcapítulos y una página, exportados y restaurados con
`--courseid` en otro curso, aparecen en las mismas secciones, con su contenido y sin usuarios.
Cuestionarios (GIFT) pendientes.

## Cliente de lectura

```bash
export MOODLE_URL=https://formacion.veraqua.es MOODLE_TOKEN=…   # variables del entorno, nunca en git
python3 tools/moodle_client.py info
python3 tools/moodle_client.py call core_course_get_courses_by_field field=idnumber value=1732
```
