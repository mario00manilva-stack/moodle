<?php
// SOLO PARA EL MOODLE LOCAL: crea una sección que sistemas ya ha creado (o va a crear) en el aula,
// con el mismo número y nombre, para poder construir sobre ella. Nunca sustituye a pedirla.
//
//   php seccion_local.php --course=<idnumber|id> --section=3 --name="MF2522_2 · UF1 · Tema 3"
require(__DIR__ . '/_bootstrap.php');
require_once($CFG->dirroot . '/course/lib.php');
[$opts] = cli_get_params(['course' => '', 'section' => 0, 'name' => '']);
$course = veraqua_get_course($opts['course']);
$num = (int)$opts['section'];
$last = (int)$DB->get_field_sql('SELECT MAX(section) FROM {course_sections} WHERE course = ? AND component IS NULL', [$course->id]);
if ($num !== $last + 1) {
    cli_error("La siguiente sección libre es la " . ($last + 1) . ", no la $num.");
}
$s = course_create_section($course, $num);
course_update_section($course, $s, ['name' => $opts['name']]);
echo "Sección $num creada en local: {$opts['name']}\n";
