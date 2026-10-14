<?php
// Crea una actividad duplicando otra del mismo curso (la "plantilla") y cambiándole el contenido.
// Así un tema nuevo hereda exactamente los ajustes de los temas ya montados en el aula
// (finalización, intentos, calificación, tipos de entrega...).
//
//   php crear_desde_plantilla.php --course=<idnumber|id> --spec=ruta/actividad.json
//
// Ficha (rutas relativas a la ficha):
//   {"plantilla": "<nombre exacto de la actividad modelo>", "section": 3, "name": "...",
//    "intro_file": "x.html",              opcional, descripción
//    "scorm_package": "x.zip",             scorm: paquete nuevo
//    "gift_file": "x.gift",                quiz: preguntas nuevas (banco propio del cuestionario)
//    "question_category": "Tema 3 · ...",  quiz: nombre de la categoría de preguntas
//    "activity_file": "x.html",            assign: instrucciones de la entrega
//    "duedate": "2026-11-20",              assign: fecha de entrega, o null para quitarla
//    "availability": "anterior"}           restricción: "anterior" (completar la actividad anterior
//                                          con finalización) o "ninguna"
//
// Una restricción que apunte a una actividad concreta no sobrevive a la copia de actividad: en el
// aula quedaría apuntando a una actividad inexistente y bloquearía la actividad para siempre. Si la
// plantilla tiene una, la ficha debe decir qué hacer con "availability".
//
// Como crear_actividad.php, se niega a crear en una sección inexistente.
require(__DIR__ . '/_bootstrap.php');
require_once($CFG->dirroot . '/course/lib.php');
require_once($CFG->dirroot . '/question/editlib.php');
require_once($CFG->dirroot . '/question/format.php');
require_once($CFG->dirroot . '/question/format/gift/format.php');
require_once($CFG->dirroot . '/mod/quiz/locallib.php');
require_once($CFG->dirroot . '/mod/scorm/locallib.php');

[$opts] = cli_get_params(['course' => '', 'spec' => '', 'help' => false], ['h' => 'help']);
if ($opts['help'] || !$opts['course'] || !$opts['spec']) {
    echo "Uso: php crear_desde_plantilla.php --course=<idnumber|id> --spec=actividad.json\n";
    exit(0);
}

$specfile = veraqua_path($opts['spec']);
$specdir = dirname($specfile);
$spec = json_decode(file_get_contents($specfile), true, 512, JSON_THROW_ON_ERROR);
$path = fn(string $f) => $specdir . '/' . $f;
$read = fn(string $f) => file_get_contents($path($f));

$course = veraqua_get_course($opts['course']);
$section = $DB->get_record('course_sections', ['course' => $course->id, 'section' => (int)$spec['section']]);
if (!$section) {
    cli_error("La sección {$spec['section']} no existe en {$course->shortname}. Pídela antes de construir sobre ella.");
}
$template = null;
foreach (get_fast_modinfo($course)->get_cms() as $cm) {
    if ($cm->name === $spec['plantilla']) {
        $template = $cm;
    }
}
if (!$template) {
    cli_error("No encuentro la actividad plantilla «{$spec['plantilla']}» en {$course->shortname}.");
}
foreach (get_fast_modinfo($course)->get_cms() as $cm) {
    if ($cm->name === $spec['name']) {
        cli_error("Ya existe una actividad llamada «{$spec['name']}» en {$course->shortname} (cmid {$cm->id}).");
    }
}

$availability = null;
if (array_key_exists('availability', $spec)) {
    $availability = match ($spec['availability']) {
        'anterior' => '{"op":"&","showc":[true],"c":[{"type":"completion","cm":-1,"e":1}]}',
        'ninguna', null => null,
    };
} else if ($template->availability && preg_match('/"cm":\s*[1-9]/', $template->availability)) {
    cli_error("La plantilla tiene una restricción ligada a una actividad concreta ({$template->availability}). "
        . 'Indica "availability": "anterior" o "ninguna" en la ficha.');
}

$new = \core_courseformat\formatactions::cm($course->id)->duplicate(
    cmid: $template->id, targetsectionid: $section->id, newname: $spec['name']);
$cmid = $new->id;
$cm = get_coursemodule_from_id('', $cmid, 0, false, MUST_EXIST);
$context = context_module::instance($cmid);
$instance = $DB->get_record($cm->modname, ['id' => $cm->instance], '*', MUST_EXIST);

if (isset($spec['intro_file'])) {
    $instance->intro = $read($spec['intro_file']);
    $instance->introformat = FORMAT_HTML;
}

switch ($cm->modname) {
    case 'scorm':
        $fs = get_file_storage();
        $fs->delete_area_files($context->id, 'mod_scorm', 'package');
        $fs->delete_area_files($context->id, 'mod_scorm', 'content');
        $zip = $path($spec['scorm_package']);
        $fs->create_file_from_pathname(['contextid' => $context->id, 'component' => 'mod_scorm',
            'filearea' => 'package', 'itemid' => 0, 'filepath' => '/', 'filename' => basename($zip)], $zip);
        $instance->reference = basename($zip);
        $instance->sha1hash = '';
        $instance->revision++;
        $DB->update_record('scorm', $instance);
        $DB->delete_records('scorm_scoes', ['scorm' => $instance->id]);
        $instance->cmid = $cmid;
        $instance->cmidnumber = $cm->idnumber;
        scorm_parse($instance, true);
        $instance = $DB->get_record('scorm', ['id' => $instance->id]);
        break;

    case 'quiz':
        $settings = \mod_quiz\quiz_settings::create($instance->id);
        $structure = $settings->get_structure();
        for ($slot = $structure->get_question_count(); $slot >= 1; $slot--) {
            $structure->remove_slot($slot);
        }
        // Preguntas en el banco propio del cuestionario: la copia de actividad las lleva consigo.
        $category = question_get_default_category($context->id, true);
        $category->name = $spec['question_category'] ?? $spec['name'];
        $DB->update_record('question_categories', $category);
        $gift = new qformat_gift();
        $gift->setCategory($category);
        $gift->setContexts([$context]);
        $gift->setCourse($course);
        $gift->setFilename($path($spec['gift_file']));
        $gift->setRealfilename(basename($spec['gift_file']));
        $gift->setMatchgrades('error');
        $gift->setCatfromfile(false);
        $gift->setContextfromfile(false);
        $gift->setStoponerror(true);
        ob_start();
        $ok = $gift->importpreprocess() && $gift->importprocess() && $gift->importpostprocess();
        $log = ob_get_clean();
        if (!$ok) {
            cli_error("Error importando {$spec['gift_file']}:\n" . strip_tags($log));
        }
        $page = 0;
        foreach ($gift->questionids as $qid) {
            quiz_add_quiz_question($qid, $instance, ++$page);
        }
        \mod_quiz\quiz_settings::create($instance->id)->get_grade_calculator()->recompute_quiz_sumgrades();
        $instance = $DB->get_record('quiz', ['id' => $instance->id]);
        break;

    case 'assign':
        if (isset($spec['activity_file'])) {
            $instance->activity = $read($spec['activity_file']);
            $instance->activityformat = FORMAT_HTML;
        }
        if (array_key_exists('duedate', $spec)) {
            $instance->duedate = $spec['duedate'] ? strtotime($spec['duedate'] . ' 00:00 Europe/Madrid') : 0;
            $instance->gradingduedate = 0;
        }
        break;
}

if (array_key_exists('availability', $spec)) {
    $DB->set_field('course_modules', 'availability', $availability, ['id' => $cmid]);
}
if (isset($spec['intro_file']) || $cm->modname === 'assign') {
    $instance->timemodified = time();
    $DB->update_record($cm->modname, $instance);
}
// Todo lo que se entrega llega oculto: se publica en el aula tras revisarlo.
set_coursemodule_visible($cmid, 0);
rebuild_course_cache($course->id, true);
echo $cmid . "\n";
