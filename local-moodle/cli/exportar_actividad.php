<?php
// Exporta una actividad del Moodle local como copia .mbz de actividad, sin datos de usuario.
//
//   php exportar_actividad.php --cmid=<id> --out=<directorio>
require(__DIR__ . '/_bootstrap.php');
require_once($CFG->dirroot . '/backup/util/includes/backup_includes.php');

[$opts] = cli_get_params(['cmid' => 0, 'out' => '.', 'help' => false], ['h' => 'help']);
if ($opts['help'] || !$opts['cmid']) {
    echo "Uso: php exportar_actividad.php --cmid=<id> --out=<directorio>\n";
    exit(0);
}

$cm = get_coursemodule_from_id('', (int)$opts['cmid'], 0, false, MUST_EXIST);
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
$section = $DB->get_field('course_sections', 'section', ['id' => $cm->section]);
$path = rtrim(veraqua_path($opts['out']), '/') . sprintf('/%s-s%02d-%s-cm%d.mbz',
    $DB->get_field('course', 'idnumber', ['id' => $cm->course]) ?: $cm->course, $section, $cm->modname, $cm->id);
$file->copy_content_to($path);
$file->delete();
$bc->destroy();
echo $path . "\n";
