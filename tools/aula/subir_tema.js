// Sube al aula un tema del temario: crea su sección (si falta) y sus cuatro actividades, ocultas.
//
//   node tools/aula/subir_tema.js --courseid=4 --tema=temario/1701/tema03
//
// Lee las mismas fichas que el Moodle local (01-presentacion.json, 02-autocomprobacion.json,
// 03-taller.json, 04-foro.json) y el nombre de la sección de temario/<curso>/secciones.tsv.
// Se puede repetir: lo que ya existe en el aula con el mismo nombre no se vuelve a crear.
const fs = require('fs');
const path = require('path');
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => a.replace(/^--/, '').split('=')));
const ROOT = path.resolve(__dirname, '..', '..');
const temaDir = path.resolve(ROOT, args.tema);
const courseid = Number(args.courseid);
const ficha = f => JSON.parse(fs.readFileSync(path.join(temaDir, f), 'utf8'));
const leer = f => fs.readFileSync(path.join(temaDir, f), 'utf8');

(async () => {
  const fichas = fs.readdirSync(temaDir).filter(f => /^0\d-.*\.json$/.test(f)).sort().map(f => ficha(f));
  const seccion = fichas[0].section;
  const secciones = fs.readFileSync(path.join(path.dirname(temaDir), 'secciones.tsv'), 'utf8')
    .trim().split('\n').map(l => l.split('\t'));
  const nombreSeccion = (secciones.find(([n]) => Number(n) === seccion) || [])[1];
  if (!nombreSeccion) throw new Error(`Sin nombre para la sección ${seccion} en secciones.tsv`);

  const { browser, page } = await abrir();
  try {
    const s = await A.crearSeccion(page, courseid, seccion, nombreSeccion);
    console.log(`Sección ${seccion} «${nombreSeccion}»: ${s.creada ? 'creada' : 'ya existía'}`);
    const { actividades } = await A.estado(page, courseid);

    // La autocomprobación se abre al ver todas las diapositivas del tema (15/10/2026) y el foro, al
    // completar la autocomprobación (14/10/2026).
    const tras = cm => JSON.stringify({ op: '&', showc: [true], c: [{ type: 'completion', cm, e: 1 }] });
    let quizCm = null;
    let scormCm = null;
    for (const f of fichas) {
      const previa = actividades.find(a => a.name === f.name);
      let cmid = previa && Number(previa.id);
      if (previa) {
        console.log(`· ${f.name}: ya existe (cm ${cmid})`);
      } else if (f.scorm_package) {
        cmid = await A.crearActividad(page, { courseid, seccion, modulo: 'scorm', nombre: f.name,
          valores: { ...A.AJUSTES.scorm, 'introeditor[text]': '' },
          ficheros: { packagefile: path.resolve(temaDir, f.scorm_package) } });
      } else if (f.gift_file) {
        cmid = await A.crearActividad(page, { courseid, seccion, modulo: 'quiz', nombre: f.name,
          valores: { ...A.AJUSTES.quiz, 'introeditor[text]': '', availabilityconditionsjson: scormCm ? tras(scormCm) : '' } });
      } else if (f.activity_file) {
        cmid = await A.crearActividad(page, { courseid, seccion, modulo: 'assign', nombre: f.name,
          valores: { ...A.AJUSTES.assign, 'introeditor[text]': '', 'activityeditor[text]': leer(f.activity_file) } });
      } else if (f.intro_file) {
        cmid = await A.crearActividad(page, { courseid, seccion, modulo: 'forum', nombre: f.name,
          valores: { ...A.AJUSTES.forum, 'introeditor[text]': leer(f.intro_file),
            availabilityconditionsjson: f.availability === 'anterior' && quizCm ? tras(quizCm) : '' } });
      }
      if (!previa) console.log(`· ${f.name}: creada y oculta (cm ${cmid})`);
      if (f.scorm_package) scormCm = cmid;
      if (f.gift_file) quizCm = cmid;
      if (f.gift_file) {
        const base = page.url().split('/').slice(0, 3).join('/');
        await page.goto(`${base}/mod/quiz/edit.php?cmid=${cmid}`);
        const slots = await page.locator('li.slot').count();
        if (slots) {
          console.log(`  preguntas: ya tiene ${slots}`);
        } else {
          const r = await A.preguntasCuestionario(page, cmid, path.join(temaDir, f.gift_file));
          console.log(`  preguntas: ${r.añadidas} añadidas`);
        }
      }
    }
  } finally {
    await browser.close();
  }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
