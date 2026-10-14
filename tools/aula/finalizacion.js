// Aplica los criterios de finalización acordados a las actividades de los temas de un curso:
// presentación vista entera, autocomprobación aprobada (5 sobre 10), taller entregado y foro con
// al menos un mensaje.
//
// Con --curso, además, el curso se completa al completar todas esas actividades (y solo esas).
// Hay que volver a lanzarlo con --curso cada vez que se sube un tema nuevo.
//
//   node tools/aula/finalizacion.js --courseid=4 --secciones=1-5 [--curso]
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => a.replace(/^--/, '').split('=')));
const courseid = Number(args.courseid);
const [desde, hasta] = args.secciones.split('-').map(Number);

(async () => {
  const { browser, page } = await abrir();
  try {
    const { secciones, actividades } = await A.estado(page, courseid);
    const delCurso = [];
    for (const s of secciones.filter(s => !s.component)) {
      const n = Number(s.number ?? s.section);
      if (n < desde || n > hasta) continue;
      for (const id of s.cmlist) {
        const cm = actividades.find(a => String(a.id) === String(id));
        const valores = A.FINALIZACION[cm.module];
        if (!valores) { console.log(`  s${n} ${cm.module} «${cm.name}»: sin criterio, se deja igual`); continue; }
        if (!('soloCurso' in args)) await A.editarActividad(page, Number(id), valores);
        delCurso.push(Number(id));
        console.log(`  s${n} ${cm.module} «${cm.name}»: criterio aplicado`);
      }
    }
    if ('curso' in args || 'soloCurso' in args) {
      const r = await A.finalizacionCurso(page, courseid, delCurso);
      console.log(`Finalización del curso: completar las ${delCurso.length} actividades de los temas ${desde}–${hasta}`);
    }
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
