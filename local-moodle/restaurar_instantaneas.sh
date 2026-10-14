#!/usr/bin/env bash
# Restaura en el Moodle local las instantáneas de producción (instantaneas/<idnumber>.mbz)
# y les devuelve el idnumber, que la restauración en curso nuevo no conserva.
# Borra antes el curso local con ese idnumber: el local es borrador, el aula manda.
set -euo pipefail
cd "$(dirname "$0")/.."
SRC=/opt/moodle-src
for f in instantaneas/*.mbz; do
  idn=$(basename "$f" .mbz)
  php -r "define('CLI_SCRIPT',1); require '$SRC/config.php'; require_once(\$CFG->dirroot.'/course/lib.php');
    if (\$c = \$DB->get_record('course', ['idnumber' => '$idn'])) { delete_course(\$c, false); }"
  id=$(php "$SRC/admin/cli/restore_backup.php" --file="$PWD/$f" --categoryid=1 | sed -n 's/.*Restored course ID: \([0-9]*\).*/\1/p')
  php -r "define('CLI_SCRIPT',1); require '$SRC/config.php'; \$DB->set_field('course', 'idnumber', '$idn', ['id' => $id]);"
  echo "$idn -> curso local $id"
done
