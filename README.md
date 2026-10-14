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

Además hay un token REST **de solo lectura** (4 funciones, caducidad de 3 meses, acotado a la
categoría del certificado; ve también lo oculto) para consultar el estado real del aula antes de cada
entrega: `tools/moodle_client.py`. Al caducar, sistemas lo regenera.

## Acuerdo vigente (14/10/2026)

- Sistemas da una **cuenta de edición propia** con un rol recortado: crea y edita contenido y secciones,
  pero no cambia nombre, código ni categoría de los módulos, no asigna roles ni ve calificaciones ni
  participantes. Con ella se sube directamente al aula; las copias `.mbz` quedan como respaldo.
- **Sin revisión previa:** los temas se suben **ocultos** en cuanto están montados. Mario los revisa en el
  aula y pide los retoques (imágenes, textos), que se hacen directamente en el aula.
- Credenciales en variables del entorno de Claude (`MOODLE_USER`, `MOODLE_PASSWORD`, `MOODLE_TOKEN`),
  nunca en el repositorio.

## Reglas (no negociables)

- **Construir siempre sobre la instantánea.** La copia de actividad se restaura en la sección con
  el mismo número; si ese número no existe en producción, Moodle la deja en la primera sección sin
  avisar. `crear_actividad.php` se niega a crear en una sección inexistente: si hace falta una
  sección nueva, se pide antes a sistemas.
- **El aula manda sobre lo publicado.** Erratas, retoques de texto y ajustes de una actividad ya
  entregada se corrigen en el aula, por la interfaz. El Moodle local es borrador, no fuente.
- **Por entrega solo va lo nuevo:** actividades nuevas, secciones nuevas y cambios de estructura.
- **Una actividad entregada no se vuelve a entregar.** El restaurador añade, no reemplaza: una
  segunda copia aparecería al lado de la primera. `exportar_actividad.php` lo impide con
  `registro-entregas.tsv` (curso, tipo y nombre). Si hay que sustituir una entera, sistemas la borra
  en el aula y restaura la nueva, con aviso previo.
- Antes de cada restauración, sistemas hace una instantánea previa del módulo.
- No cambiar `idnumber`, nombre, `shortname` ni categoría de los módulos: la receta de producción
  los revierte en cada despliegue.
- La marca se escribe siempre **VERAQUA**.
- Moodle local fijado en **v5.2.4** (`2026042004.00`): un `.mbz` solo restaura en una versión igual
  o superior, y producción está en 5.2.4+ (`2026042004.02`) según las instantáneas del 14/10/2026.
  Al subir producción (5.3 LTS), subir `MOODLE_TAG` en `setup.sh` sin pasarse.
- Ningún `.mbz` entra en el repositorio (ver `.gitignore`).

## Uso

```bash
local-moodle/setup.sh                        # instala/arranca/actualiza Moodle local (idempotente)
local-moodle/restaurar_instantaneas.sh       # restaura instantaneas/<idnumber>.mbz y fija el idnumber

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

## Subida directa al aula (cuenta de edición)

```bash
# Usuario y contraseña de la cuenta automatizacion-aula en MOODLE_USER y MOODLE_PASSWORD (entorno)
node tools/aula/subir_tema.js --courseid=4 --tema=temario/1701/tema03
```

Crea la sección del tema si falta (nombre de `secciones.tsv`) y las cuatro actividades **ocultas**,
enviando los formularios estándar de Moodle con los ajustes de las actividades del Tema 1
(`tools/aula/acciones.js`). Las preguntas se importan en GIFT al banco propio de cada cuestionario
y se añaden una por página. Se puede repetir: no duplica actividades ni preguntas.
Probado antes contra una copia local del aula (`php -S localhost:8080 -t public` en /opt/moodle-src).
Ids en el aula: 1732 → 2, 1697 → 3, 1701 → 4.

## Finalización en los tres módulos (14/10/2026)

- **1701**: temas 1–5 con presentación vista, autocomprobación aprobada (5/10, 3 intentos), taller
  entregado y foro con un mensaje; el curso se completa con las 20 actividades.
- **1697**: lo mismo sobre sus actividades de la sección General (presentación, autoevaluación, las dos
  tareas y el foro del caso práctico); el curso se completa con esas 5.
- **1732**: solo tiene el libro y el foro de avisos; no hay actividades a las que aplicarlo.
- El foro de avisos, los libros y el glosario no cuentan para la finalización.
