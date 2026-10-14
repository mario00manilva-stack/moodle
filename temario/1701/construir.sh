#!/usr/bin/env bash
# Construye en el Moodle local los temas de 1701 que no están aún en el aula y exporta sus copias.
#   temario/1701/construir.sh [--borrador]
#
# Parte siempre de la instantánea. Las secciones que faltan en ella (secciones.tsv) se replican en
# local hasta la del último tema: en el aula las crea sistemas, y una entrega no puede salir antes.
set -euo pipefail
cd "$(dirname "$0")/../.."
M=temario/1701
C=local-moodle/cli
local-moodle/setup.sh >/dev/null
local-moodle/restaurar_instantaneas.sh >/dev/null
last=$(ls -d $M/tema[0-9][0-9] | tail -1 | sed 's/.*tema//; s/^0//')
while IFS=$'\t' read -r num name; do
  [ "$num" -le "$last" ] && php $C/seccion_local.php --course=1701 --section="$num" --name="$name"
done < $M/secciones.tsv
for t in $M/tema[0-9][0-9]; do
  python3 -I $t/presentacion.py >/dev/null
  ids=()
  for f in $t/0*.json; do ids+=("$(php $C/crear_desde_plantilla.php --course=1701 --spec=$f)"); done
  out=entregas/1701-$(basename $t)
  rm -rf "$out" && mkdir -p "$out"
  for id in "${ids[@]}"; do php $C/exportar_actividad.php --cmid="$id" --out="$out" "$@"; done
done
