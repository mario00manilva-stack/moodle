<?php
// Exporta una actividad del Moodle local como copia .mbz de actividad, sin datos de usuario.
//
//   php exportar_actividad.php --cmid=<id> --out=<directorio>
//
// Una actividad entregada no se vuelve a entregar: el restaurador de producción añade, no
// reemplaza, y una segunda copia aparecería al lado de la primera. Cada exportación se anota
// en registro-entregas.tsv (raíz del repositorio) y se rechaza otra con el mismo curso, tipo y
// nombre. Las correcciones de lo ya entregado se hacen en el aula, no aquí.
require(__DIR__ . '/_bootstrap.php');
require_once($CFG->dirroot . '/backup/util/includes/backup_includes.php');

[$opts] = cli_get_params(['cmid' => 0, 'out' => '.', 'help' => false], ['h' => 'help']);
$registro = dirname(__DIR__, 2) . '/registro-entregas.tsv';
if ($opts['help'] || !$opts['cmid']) {
    echo "Uso: php exportar_actividad.php --cmid=<id> --out=<directorio>\n";
    exit(0);
}

$cm = get_coursemodule_from_id('', (int)$opts['cmid'], 0, false, MUST_EXIST);
$courseref = $DB->get_field('course', 'idnumber', ['id' => $cm->course]) ?: $cm->course;
$section = $DB->get_field('course_sections', 'section', ['id' => $cm->section]);
foreach (file_exists($registro) ? file($registro, FILE_IGNORE_NEW_LINES) : [] as $line) {
    [, $c, , $type, $name] = array_pad(explode("\t", $line), 6, '');
    if ($c === (string)$courseref && $type === $cm->modname && $name === $cm->name) {
        cli_error("Ya entregada: $line\nLas correcciones se hacen en el aula; una sustitución completa se acuerda antes con sistemas.");
    }
}
$bc = new backup_controller(backup::TYPE_1ACTIVITY, $cm->id, backup::FORMAT_MOODLE,
    backup::INTERACTIVE_NO, backup::MODE_GENERAL, get_admin()->id);
foreach (['users' => 0, 'role_assignments' => 0, 'comments' => 0, 'badges' => 0,
          'userscompletion' => 0, 'logs' => 0, 'grade_histories' => 0] as $name => $value) {
    $plan = $bc->get_plan();
    if ($plan->setting_exists($name)) {
        $setting = $plan->get_setting($name);
        if ($setting->get_status() == backup_setting::NOT_LOCKED) {
            $setting->set_value($value);
        }
    }
}
$bc->execute_plan();
$file = $bc->get_results()['backup_destination'];
$path = rtrim(veraqua_path($opts['out']), '/') . sprintf('/%s-s%02d-%s-cm%d.mbz',
    $courseref, $section, $cm->modname, $cm->id);
$file->copy_content_to($path);
$file->delete();
$bc->destroy();
file_put_contents($registro, implode("\t", [date('Y-m-d'), $courseref, $section, $cm->modname,
    $cm->name, basename($path)]) . "\n", FILE_APPEND);
echo $path . "\n";
