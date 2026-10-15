// Reorganiza el curso 1701 en unidades formativas: una sección por UF y, dentro, los temas en orden,
// cada uno con su cabecera (etiqueta «TEMA N») y sus cuatro actividades. Así la portada
// muestra el progreso de cada UF (acordado con Mario el 15/10/2026).
//
//   node tools/aula/reorganizar_uf.js --courseid=4 [--aplicar]
//
// Los ids de las actividades no cambian: la finalización y las restricciones siguen valiendo. Las
// secciones antiguas de cada tema se borran cuando quedan vacías (o se ocultan si no se puede).
// Se puede repetir.
const fs = require('fs');
const path = require('path');
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => { const [k, v = true] = a.replace(/^--/, '').split('='); return [k, v]; }));
const courseid = Number(args.courseid);
const IMG = path.resolve(__dirname, '..', '..', 'recursos', 'cabeceras', 'temas');
const UF = [
  { nombre: 'UF1 · Vaciado, limpieza y conservación del vaso y anexos (50 h)', temas: [1, 2, 3, 4] },
  { nombre: 'UF2 · Tratamiento físico-químico del agua y calidad del aire (80 h)', temas: [5, 6, 7, 8] },
  { nombre: 'UF3 · Mantenimiento electromecánico e hidráulico (80 h)', temas: [9, 10, 11, 12] },
  { nombre: 'UF4 · Protocolos de autocontrol y registro SILOÉ (30 h)', temas: [13, 14] },
];
const num = s => Number(s.number ?? s.section);
const etiqueta = n => `TEMA ${n}`;
const log = (...m) => console.log(args.aplicar ? '' : '[prueba]', ...m);

async function seccionUF(page, nombre) {
  let { secciones } = await A.estado(page, courseid);
  let s = secciones.find(x => !x.component && (x.title ?? x.name) === nombre);
  if (s || !args.aplicar) return s;
  const normales = secciones.filter(x => !x.component);
  await A.crearSeccion(page, courseid, Math.max(...normales.map(num)) + 1, nombre);
  ({ secciones } = await A.estado(page, courseid));
  return secciones.find(x => !x.component && (x.title ?? x.name) === nombre);
}

async function crearCabecera(page, ufSec, n, titulo) {
  const img = path.join(IMG, `1701-tema${String(n).padStart(2, '0')}.jpg`);
  return A.crearActividad(page, { courseid, seccion: num(ufSec), modulo: 'label', nombre: etiqueta(n),
    valores: { 'introeditor[format]': 1, completion: 0 },
    preparar: async (p) => {
      let html = `<h3 class="veraqua-tema" style="margin:1.5rem 0 .5rem">${titulo}</h3>`;
      if (fs.existsSync(img)) {
        const itemid = await p.inputValue('form.mform input[name="introeditor[itemid]"]');
        const sub = await A.subirBorrador(p, itemid, img);
        html = `<p class="veraqua-cabecera-tema"><img src="${sub.url}" alt="${titulo}" class="img-fluid" style="width:100%;height:auto;border-radius:12px"></p>`;
      }
      return { 'introeditor[text]': html };
    } });
}

(async () => {
  const { browser, page } = await abrir();
  try {
    for (const uf of UF) {
      const ufSec = await seccionUF(page, uf.nombre);
      log(`${uf.nombre}: ${ufSec ? 'sección ' + num(ufSec) : 'se creará'}`);
      for (const n of uf.temas) {
        let { secciones, actividades } = await A.estado(page, courseid);
        const vieja = secciones.find(x => !x.component && /\bTema (\d+)$/.test(x.title ?? x.name) && Number((x.title ?? x.name).match(/(\d+)$/)[1]) === n);
        if (!vieja) { log(`  Tema ${n}: ya está en su UF`); continue; }
        const cms = (vieja.cmlist || []).map(id => actividades.find(a => String(a.id) === String(id))).filter(Boolean);
        const scorm = cms.find(a => a.module === 'scorm');
        const titulo = scorm ? scorm.name : `Tema ${n}`;
        log(`  Tema ${n} (${titulo}): ${cms.length} actividades desde la sección ${num(vieja)}`);
        if (!args.aplicar) continue;
        // La numeración cambia al borrar secciones: se relee la sección de la UF por su id.
        const ufAhora = secciones.find(x => String(x.id) === String(ufSec.id));
        let cab = actividades.find(a => a.name === etiqueta(n));
        const cabId = cab ? Number(cab.id) : await crearCabecera(page, ufAhora, n, titulo);
        const ids = [cabId, ...cms.map(a => Number(a.id))];
        for (const id of ids) {
          await A.ajax(page, 'core_courseformat_update_course', { action: 'cm_move', courseid, ids: [id], targetsectionid: Number(ufSec.id) });
        }
        await A.ajax(page, 'core_courseformat_update_course', { action: 'cm_show', courseid, ids });
        ({ secciones } = await A.estado(page, courseid));
        const v = secciones.find(x => String(x.id) === String(vieja.id));
        if (v && !(v.cmlist || []).length) {
          try {
            await A.ajax(page, 'core_courseformat_update_course', { action: 'section_delete', courseid, ids: [Number(v.id)] });
            log(`    sección antigua borrada`);
          } catch (e) {
            await A.ajax(page, 'core_courseformat_update_course', { action: 'section_hide', courseid, ids: [Number(v.id)] });
            log(`    no se pudo borrar la sección antigua (${e.message.slice(0, 80)}): oculta`);
          }
        }
      }
    }
    if (args.aplicar) {
      const { secciones, actividades } = await A.estado(page, courseid);
      for (const s of secciones.filter(x => !x.component)) {
        const cms = (s.cmlist || []).map(id => actividades.find(a => String(a.id) === String(id)));
        console.log(`${num(s)} · ${s.title ?? s.name} · visible=${s.visible} · ${cms.length} elementos`);
      }
    } else console.log('(sin --aplicar: no se ha cambiado nada)');
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
