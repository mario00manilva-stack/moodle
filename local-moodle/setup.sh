#!/usr/bin/env bash
# Levanta un Moodle 5.2.2 local (PHP CLI + PostgreSQL) para construir el temario.
# download.moodle.org no es accesible desde el entorno: instalación en inglés
# (el contenido del temario va en español igualmente).
# Idempotente: se puede ejecutar al inicio de cada sesión.
# Versión fijada en v5.2.2 (2026042002.00): producción es 2026042002.01 y un .mbz
# solo restaura en una versión igual o superior.
set -euo pipefail

MOODLE_TAG=v5.2.2
SRC=/opt/moodle-src
DATA=/opt/moodledata
DB=moodle_local
PORT=8080
WWWROOT="http://localhost:${PORT}"

if [ ! -d "$SRC" ]; then
  git clone -q --depth 1 --branch "$MOODLE_TAG" https://github.com/moodle/moodle.git "$SRC"
fi
if [ ! -f "$SRC/vendor/autoload.php" ]; then
  (cd "$SRC" && composer install --no-dev --classmap-authoritative -q --no-interaction)
fi

service postgresql start >/dev/null
if ! su postgres -c "psql -tAc \"SELECT 1 FROM pg_roles WHERE rolname='moodle'\"" | grep -q 1; then
  su postgres -c "psql -qc \"CREATE USER moodle WITH PASSWORD 'moodle'\""
fi
if ! su postgres -c "psql -tAc \"SELECT 1 FROM pg_database WHERE datname='$DB'\"" | grep -q 1; then
  su postgres -c "createdb -O moodle -E UTF8 $DB"
fi

mkdir -p "$DATA"
# Requisito de instalación de Moodle 5.x (producción usa el mismo valor).
echo "max_input_vars = 5000" > /etc/php/8.3/cli/conf.d/99-moodle.ini
if [ ! -f "$SRC/config.php" ]; then
  cat > "$SRC/config.php" <<PHP
<?php
unset(\$CFG);
global \$CFG;
\$CFG = new stdClass();
\$CFG->dbtype    = 'pgsql';
\$CFG->dblibrary = 'native';
\$CFG->dbhost    = 'localhost';
\$CFG->dbname    = '$DB';
\$CFG->dbuser    = 'moodle';
\$CFG->dbpass    = 'moodle';
\$CFG->prefix    = 'mdl_';
\$CFG->dboptions = ['dbport' => 5432];
\$CFG->wwwroot   = '$WWWROOT';
\$CFG->dataroot  = '$DATA';
\$CFG->admin     = 'admin';
\$CFG->directorypermissions = 02777;
\$CFG->timezone = 'Europe/Madrid';
require_once(__DIR__ . '/lib/setup.php');
PHP
fi

if ! su postgres -c "psql -d $DB -tAc \"SELECT 1 FROM information_schema.tables WHERE table_name='mdl_config'\"" | grep -q 1; then
  php "$SRC/admin/cli/install_database.php" --agree-license --lang=en \
    --fullname="VERAQUA FORMACIÓN (local)" --shortname="veraqua-local" \
    --adminuser=admin --adminpass='Local-Admin-1' --adminemail=admin@example.invalid
  php "$SRC/admin/cli/cfg.php" --name=forcetimezone --set=Europe/Madrid
fi

echo "Moodle local listo en $SRC ($(php -r "define('CLI_SCRIPT',1);require '$SRC/config.php';echo \$CFG->release;"))"
