// Correcciones del 1701 acordadas con Mario el 14/10/2026 («corrige todo lo que veas mal»):
// - Tema 2: nombres con el formato de los demás temas y foro propio (no tenía).
// - Talleres de los Temas 1 y 2 sin fechas, como los demás (las de septiembre de 2026 ya pasaron).
// - Cada foro se abre al completar la autocomprobación de su tema.
//   node tools/aula/correcciones_1701.js --courseid=4
const fs = require('fs');
const path = require('path');
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => a.replace(/^--/, '').split('=')));
const courseid = Number(args.courseid);
const ROOT = path.resolve(__dirname, '..', '..');
const SIN_FECHAS = { 'allowsubmissionsfromdate[enabled]': null, 'duedate[enabled]': null, 'cutoffdate[enabled]': null, 'gradingduedate[enabled]': null };

(async () => {
  const { browser, page } = await abrir();
  try {
    let { secciones, actividades } = await A.estado(page, courseid);
    const sec = n => secciones.find(s => !s.component && Number(s.number ?? s.section) === n);
    const delTema = (n, mod) => sec(n).cmlist.map(id => actividades.find(a => String(a.id) === String(id))).filter(a => a.module === mod);
    const porNombre = nombre => actividades.find(a => a.name === nombre);

    // Tema 2: nombres.
    const s2 = sec(2);
    if ((s2.title || s2.name) !== 'MF2522_2 · UF1 · Tema 2') {
      await A.ajax(page, 'core_update_inplace_editable', { component: 'format_topics', itemtype: 'sectionname', itemid: Number(s2.id), value: 'MF2522_2 · UF1 · Tema 2' });
      console.log('Sección 2 renombrada: MF2522_2 · UF1 · Tema 2');
    }
    for (const [viejo, nuevo] of [['Tema 2. Vaciado de vasos', 'Tema 2 · Vaciado de vasos'],
      ['Taller 1.2 · Maniobras de vaciado y bombas de achique.', 'Taller 1.2 · Maniobras de vaciado y bombas de achique']]) {
      const a = porNombre(viejo);
      if (a) { await A.editarActividad(page, Number(a.id), { name: nuevo }); console.log(`Renombrada: ${nuevo}`); }
    }

    // Talleres 1.1 y 1.2 sin fechas.
    for (const n of [1, 2]) for (const a of delTema(n, 'assign')) {
      await A.editarActividad(page, Number(a.id), SIN_FECHAS); console.log(`Sin fechas: ${a.name}`);
    }

    // Foro del Tema 2.
    const quiz2 = delTema(2, 'quiz')[0];
    if (!delTema(2, 'forum').length) {
      const cmid = await A.crearActividad(page, { courseid, seccion: 2, modulo: 'forum', nombre: 'Foro 1.2 · «¿A qué arqueta va el agua?»',
        valores: { ...A.AJUSTES.forum, 'introeditor[text]': fs.readFileSync(path.join(ROOT, 'temario/1701/tema02/foro.html'), 'utf8'),
          availabilityconditionsjson: '' } });
      console.log(`Foro 1.2 creado y oculto (cm ${cmid})`);
      ({ secciones, actividades } = await A.estado(page, courseid));
    }

    // Cada foro, tras la autocomprobación de su tema.
    for (const s of secciones.filter(s => !s.component && Number(s.number ?? s.section) >= 1)) {
      const n = Number(s.number ?? s.section);
      const quiz = delTema(n, 'quiz')[0];
      for (const foro of delTema(n, 'forum')) {
        if (!quiz) continue;
        const json = JSON.stringify({ op: '&', showc: [true], c: [{ type: 'completion', cm: Number(quiz.id), e: 1 }] });
        await A.editarActividad(page, Number(foro.id), { availabilityconditionsjson: json, completiongradeitemnumber: null });
        console.log(`Tema ${n}: «${foro.name}» se abre al completar «${quiz.name}»`);
      }
    }
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
