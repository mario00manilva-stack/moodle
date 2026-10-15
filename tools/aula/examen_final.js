// Examen final de cada módulo (acordado con Mario el 15/10/2026): 20 preguntas de opción múltiple y
// verdadero/falso, aprobado con 5, 3 intentos y preguntas barajadas en cada intento. Va en una sección
// «Examen final del módulo» al final del curso y cuenta para la finalización del curso.
//
//   DESBLOQUEAR_FINALIZACION_CURSO=1 node tools/aula/examen_final.js --modulo=1701 [--courseid=4]
//
// Se puede repetir: lo que ya existe no se vuelve a crear.
const path = require('path');
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => { const [k, v = true] = a.replace(/^--/, '').split('='); return [k, v]; }));
const CURSOS = { 1701: 4, 1697: 3, 1732: 2 };
const modulo = String(args.modulo);
const courseid = Number(args.courseid || CURSOS[modulo]);
const GIFT = path.resolve(__dirname, '..', '..', 'temario', modulo, 'examen-final.gift');
const SECCION = 'Examen final del módulo';
const NOMBRE = `Examen final · Módulo ${modulo}`;
const num = s => Number(s.number ?? s.section);

(async () => {
  const { browser, page } = await abrir();
  try {
    const base = page.url().split('/').slice(0, 3).join('/');
    let { secciones, actividades } = await A.estado(page, courseid);
    let sec = secciones.find(s => !s.component && (s.title ?? s.name) === SECCION);
    if (!sec) {
      const ultima = Math.max(...secciones.filter(s => !s.component).map(num));
      await A.crearSeccion(page, courseid, ultima + 1, SECCION);
      ({ secciones, actividades } = await A.estado(page, courseid));
      sec = secciones.find(s => !s.component && (s.title ?? s.name) === SECCION);
      console.log(`Sección «${SECCION}» creada (${num(sec)})`);
    }
    let quiz = actividades.find(a => a.name === NOMBRE);
    let cmid = quiz && Number(quiz.id);
    if (!cmid) {
      cmid = await A.crearActividad(page, { courseid, seccion: num(sec), modulo: 'quiz', nombre: NOMBRE,
        valores: { ...A.AJUSTES.quiz, shuffleanswers: 1,
          'introeditor[text]': '<p>Examen final del módulo: 20 preguntas de opción múltiple y de verdadero o falso. Se aprueba con un 5 sobre 10. Tienes 3 intentos y las preguntas cambian de orden en cada intento.</p>',
          showdescription: 1 } });
      console.log(`Cuestionario «${NOMBRE}» creado (cm ${cmid})`);
    }
    await A.ajax(page, 'core_courseformat_update_course', { action: 'cm_show', courseid, ids: [cmid] }).catch(() => {});
    if (sec && !sec.visible) await A.ajax(page, 'core_courseformat_update_course', { action: 'section_show', courseid, ids: [Number(sec.id)] });

    await page.goto(`${base}/mod/quiz/edit.php?cmid=${cmid}`);
    if (!(await page.locator('li.slot').count())) {
      const r = await A.preguntasCuestionario(page, cmid, GIFT);
      console.log(`Preguntas añadidas: ${r.añadidas}`);
    }
    // Barajar las preguntas de la sección del cuestionario en cada intento.
    await page.goto(`${base}/mod/quiz/edit.php?cmid=${cmid}`);
    const datos = await page.evaluate(() => {
      const chk = document.querySelector('input[id^="shuffle-"]');
      return { quizid: Number((document.querySelector('input[name="quizid"]') || {}).value || 0),
        seccion: chk ? Number(chk.id.replace('shuffle-', '')) : 0, marcado: chk ? chk.checked : null,
        html: document.body.innerHTML.match(/"quizid":\s*"?(\d+)/)?.[1] };
    });
    const quizid = datos.quizid || Number(datos.html);
    if (!datos.marcado) {
      const r = await page.evaluate(async ({ quizid, seccion }) => {
        const fd = new URLSearchParams({ sesskey: M.cfg.sesskey, quizid, class: 'section', field: 'updateshufflequestions', id: seccion, newshuffle: 1 });
        const res = await fetch(`${M.cfg.wwwroot}/mod/quiz/edit_rest.php`, { method: 'POST', body: fd });
        return res.text();
      }, { quizid, seccion: datos.seccion });
      console.log('Barajar preguntas:', r.slice(0, 120));
    }
    await page.goto(`${base}/mod/quiz/edit.php?cmid=${cmid}`);
    const fin = await page.evaluate(() => ({ preguntas: document.querySelectorAll('li.slot').length,
      barajar: (document.querySelector('input[id^="shuffle-"]') || {}).checked }));
    console.log(`Comprobación: ${fin.preguntas} preguntas · barajar=${fin.barajar}`);

    // Finalización del curso: las actividades que ya se exigían más el examen.
    await page.goto(`${base}/course/completion.php?id=${courseid}`);
    const actuales = await page.$$eval('input[type=checkbox][name^="criteria_activity["]:checked',
      els => els.map(e => Number(e.name.match(/\[(\d+)\]/)[1])));
    if (!actuales.includes(cmid)) {
      await A.finalizacionCurso(page, courseid, [...actuales, cmid]);
      console.log(`Finalización del curso: ${actuales.length} actividades + el examen final`);
    } else console.log(`Finalización del curso: el examen ya cuenta (${actuales.length} actividades)`);
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
