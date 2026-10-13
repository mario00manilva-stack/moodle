<?php
// Carga común de los scripts CLI del Moodle local.
define('CLI_SCRIPT', true);
// Moodle cambia el directorio de trabajo al cargar: se guarda antes para resolver rutas relativas.
define('VERAQUA_CWD', getcwd());
require(getenv('MOODLE_SRC') ?: '/opt/moodle-src/config.php');
require_once($CFG->libdir . '/clilib.php');
\core\session\manager::set_user(get_admin());

/** Devuelve el curso por idnumber (preferente) o por id numérico. */
function veraqua_get_course(string $ref): stdClass {
    global $DB;
    $course = $DB->get_record('course', ['idnumber' => $ref]);
    if (!$course && ctype_digit($ref)) {
        $course = $DB->get_record('course', ['id' => (int)$ref]);
    }
    if (!$course) {
        cli_error("Curso no encontrado: $ref");
    }
    return $course;
}

/** Resuelve una ruta pasada por línea de comandos respecto al directorio desde el que se llamó. */
function veraqua_path(string $path): string {
    return $path !== '' && $path[0] === '/' ? $path : VERAQUA_CWD . '/' . $path;
}
