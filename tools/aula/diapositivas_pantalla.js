// Las presentaciones se abren en una ventana nueva a pantalla completa, sin el índice lateral de SCORM
// ni la columna de miniaturas (paquetes con <deck-stage no-rail>). Pedido por Mario el 15/10/2026.
//
//   node tools/aula/diapositivas_pantalla.js [--courseid=4] [--sin-paquete]
//
// Se puede repetir. La finalización de las actividades no cambia.
const fs = require('fs');
const path = require('path');
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => { const [k, v = true] = a.replace(/^--/, '').split('='); return [k, v]; }));
const ROOT = path.resolve(__dirname, '..', '..');
const E = path.join(ROOT, 'entregas');
const AJUSTES = { popup: 1, width: '100%', height: '100%', hidetoc: 3, nav: 0, skipview: 0 };

// Paquete de cada presentación según el curso y el nombre de la actividad.
function paquete(courseid, nombre) {
  const n = (nombre.match(/^Tema (\d+)\b/) || [])[1];
  if (courseid === 3 && /Diapositivas del módulo/.test(nombre)) return path.join(E, 'snapshot-norail', 'MF2518_2-UF1-scorm-v3.zip');
  if (courseid === 2 && n) return path.join(E, `1732-T${n}-scorm.zip`);
  if (courseid === 4 && n) {
    if (Number(n) <= 2) return path.join(E, 'snapshot-norail', `MF2522_2-UF1-T${n}-scorm.zip`);
    return fs.readdirSync(E).filter(f => new RegExp(`^MF2522_2-UF\\d-T${n}-scorm\\.zip$`).test(f)).map(f => path.join(E, f))[0];
  }
  return null;
}

(async () => {
  const { browser, page } = await abrir();
  try {
    for (const courseid of args.courseid ? [Number(args.courseid)] : [4, 2, 3]) {
      const { actividades } = await A.estado(page, courseid);
      for (const s of actividades.filter(a => a.module === 'scorm')) {
        const zip = args['sin-paquete'] ? null : paquete(courseid, s.name);
        if (!args['sin-paquete'] && !zip) { console.log(`${courseid} · ${s.name}: sin paquete conocido, solo ajustes`); }
        await A.editarActividad(page, Number(s.id), AJUSTES, zip ? async (p) => {
          const itemid = await p.inputValue('form.mform input[name="packagefile"]');
          await A.subirBorrador(p, itemid, zip);
          return {};
        } : undefined);
        console.log(`${courseid} · ${s.name}: ventana nueva${zip ? ' + ' + path.basename(zip) : ''}`);
      }
    }
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
