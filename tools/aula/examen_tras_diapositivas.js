// La autocomprobación de cada tema solo se abre cuando el alumno ha visto todas las diapositivas
// (presentación SCORM del mismo tema completada). Acordado con Mario el 15/10/2026.
//
//   node tools/aula/examen_tras_diapositivas.js --courseid=4 [--aplicar]
//
// Sin --aplicar solo muestra lo que haría. Se puede repetir.
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => { const [k, v = true] = a.replace(/^--/, '').split('='); return [k, v]; }));
const courseid = Number(args.courseid);

// Añade la condición a las que ya tenga la actividad (sin duplicarla).
function conPresentacion(actual, scormCm) {
  const cond = { type: 'completion', cm: Number(scormCm), e: 1 };
  let a = null;
  try { a = actual ? JSON.parse(actual) : null; } catch (e) { a = null; }
  if (!a || !Array.isArray(a.c) || !a.c.length) return JSON.stringify({ op: '&', showc: [true], c: [cond] });
  if (a.c.some(c => c.type === 'completion' && Number(c.cm) === cond.cm)) return JSON.stringify(a);
  if (a.op !== '&') return JSON.stringify({ op: '&', showc: [true, true], c: [cond, a] });
  return JSON.stringify({ ...a, c: [...a.c, cond], showc: [...(a.showc || a.c.map(() => true)), true] });
}

(async () => {
  const { browser, page } = await abrir();
  try {
    const { secciones, actividades } = await A.estado(page, courseid);
    for (const s of secciones.filter(s => !s.component)) {
      const del = mod => actividades.filter(a => String(a.sectionid) === String(s.id) && a.module === mod);
      const [scorms, quizzes] = [del('scorm'), del('quiz')];
      if (!quizzes.length) continue;
      if (scorms.length !== 1) { console.log(`«${s.title ?? s.name}»: ${scorms.length} presentaciones, se deja como está`); continue; }
      for (const q of quizzes) {
        console.log(`«${q.name}» se abrirá al completar «${scorms[0].name}»`);
        if (args.aplicar) {
          await A.editarActividad(page, Number(q.id), {}, async (p) => {
            const actual = await p.inputValue('form.mform [name="availabilityconditionsjson"]', { timeout: 3000 }).catch(() => '');
            if (actual && actual !== '{"op":"&","c":[],"showc":[]}') console.log(`  tenía: ${actual}`);
            return { availabilityconditionsjson: conPresentacion(actual, scorms[0].id) };
          });
        }
      }
    }
    if (!args.aplicar) console.log('(sin --aplicar: no se ha cambiado nada)');
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
