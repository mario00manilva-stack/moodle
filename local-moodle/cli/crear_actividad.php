<?php
// Crea una actividad en el Moodle local a partir de una ficha JSON del temario.
//
//   php crear_actividad.php --course=<idnumber|id> --spec=ruta/actividad.json
//
// La sección debe existir ya (se construye siempre sobre la instantánea de producción:
// una copia de actividad se restaura en la sección con el mismo número).
// Tipos: page, label, book. Las rutas de ficheros son relativas a la ficha.
require(__DIR__ . '/_bootstrap.php');
require_once($CFG->dirroot . '/course/lib.php');
require_once($CFG->dirroot . '/course/modlib.php');

[$opts] = cli_get_params(['course' => '', 'spec' => '', 'help' => false], ['h' => 'help']);
if ($opts['help'] || !$opts['course'] || !$opts['spec']) {
    echo "Uso: php crear_actividad.php --course=<idnumber|id> --spec=actividad.json\n";
    exit(0);
}

$specfile = veraqua_path($opts['spec']);
$specdir = dirname($specfile);
$spec = json_decode(file_get_contents($specfile), true, 512, JSON_THROW_ON_ERROR);
$read = fn(string $f) => file_get_contents($specdir . '/' . $f);

$course = veraqua_get_course($opts['course']);
$section = (int)$spec['section'];
if (!$DB->record_exists('course_sections', ['course' => $course->id, 'section' => $section])) {
    cli_error("La sección $section no existe en {$course->shortname}. Pídela antes de construir sobre ella.");
}

$mi = (object)[
    'modulename' => $spec['type'],
    'course' => $course->id,
    'section' => $section,
    'visible' => (int)($spec['visible'] ?? 1),
    'name' => $spec['name'] ?? '',
    'introeditor' => ['text' => $spec['intro'] ?? '', 'format' => FORMAT_HTML, 'itemid' => 0],
    'showdescription' => 0,
    'cmidnumber' => $spec['idnumber'] ?? '',
];

switch ($spec['type']) {
    case 'page':
        $mi->content = $read($spec['content_file']);
        $mi->contentformat = FORMAT_HTML;
        $mi->display = 5; // RESOURCELIB_DISPLAY_OPEN.
        $mi->printintro = 0;
        $mi->printlastmodified = 1;
        break;
    case 'label':
        $mi->introeditor['text'] = $read($spec['content_file']);
        break;
    case 'book':
        $mi->numbering = $spec['numbering'] ?? 1; // BOOK_NUM_NUMBERS.
        $mi->navstyle = 1;
        $mi->customtitles = 0;
        break;
    default:
        cli_error("Tipo no soportado: {$spec['type']}");
}

$cm = create_module($mi);

if ($spec['type'] === 'book') {
    $page = 0;
    foreach ($spec['chapters'] as $ch) {
        $DB->insert_record('book_chapters', [
            'bookid' => $cm->instance,
            'pagenum' => ++$page,
            'subchapter' => (int)($ch['subchapter'] ?? 0),
            'title' => $ch['title'],
            'content' => $read($ch['file']),
            'contentformat' => FORMAT_HTML,
            'hidden' => 0,
            'timecreated' => time(),
            'timemodified' => time(),
            'importsrc' => '',
        ]);
    }
}
rebuild_course_cache($course->id, true);
echo $cm->coursemodule . "\n";
