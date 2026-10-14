#!/usr/bin/env bash
# Construye el Tema 3 de 1701 en el Moodle local, sobre la instantánea, y exporta las copias.
#   temario/1701/tema03/construir.sh [--borrador]
set -euo pipefail
cd "$(dirname "$0")/../../.."
T=temario/1701/tema03
C=local-moodle/cli
local-moodle/setup.sh >/dev/null
local-moodle/restaurar_instantaneas.sh >/dev/null
# La sección 3 la crea sistemas en el aula; en local se replica para construir encima.
php $C/seccion_local.php --course=1701 --section=3 --name="MF2522_2 · UF1 · Tema 3"
python3 -I $T/presentacion.py >/dev/null
ids=()
for f in $T/0*.json; do ids+=("$(php $C/crear_desde_plantilla.php --course=1701 --spec=$f)"); done
out=entregas/1701-tema03
rm -rf "$out" && mkdir -p "$out"
for id in "${ids[@]}"; do php $C/exportar_actividad.php --cmid="$id" --out="$out" "$@"; done
