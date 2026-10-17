// Sustituye el contenido antiguo de los módulos 1697 (MF2518_2) y 1732 (MF2519_2) por los temas 15–22 del
// temario, organizados por unidades formativas como el 1701. Acordado con Mario el 17/10/2026: lo antiguo
// se oculta (no se borra) y deja de contar para la finalización.
//
//   node tools/aula/sustituir_temario.js --modulo=1697|1732 [--courseid=3] [--aplicar]
//   node tools/aula/subsecciones_uf.js --courseid=3 --aplicar          (temas plegables)
//   node tools/aula/examen_final.js --modulo=1697                       (examen nuevo)
//   DESBLOQUEAR_FINALIZACION_CURSO=1 node tools/aula/sustituir_temario.js --modulo=1697 --finalizacion
//
// Pasos: oculta lo antiguo, renombra y oculta el examen final antiguo, crea cada UF con la cabecera
// «TEMA N» y las cuatro actividades de cada tema (diapositivas en ventana al 80 %, autocomprobación tras las
// diapositivas, foro tras la autocomprobación) y deja el examen al final. Se puede repetir.
const fs = require('fs');
const path = require('path');
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => { const [k, v = true] = a.replace(/^--/, '').split('='); return [k, v]; }));
const ROOT = path.resolve(__dirname, '..', '..');
const MODULOS = {
  1697: { courseid: 3, ocultarCms: [8, 10, 11, 12, 13], ufs: [
    { nombre: 'UF1 · Almacenamiento de productos químicos (APQ) y fichas de datos de seguridad (30 h)', temas: [15, 16] },
    { nombre: 'UF2 · Preparación, transporte ADR y gestión de residuos (30 h)', temas: [17, 18] },
  ] },
  1732: { courseid: 2, ocultarSecciones: true, ufs: [
    { nombre: 'UF1 · Marco normativo, riesgos específicos y medidas preventivas (30 h)', temas: [19, 20] },
    { nombre: 'UF2 · Equipos de protección, plan de emergencias y primeros auxilios (30 h)', temas: [21, 22] },
  ] },
};
const modulo = String(args.modulo);
const M = MODULOS[modulo];
if (!M) throw new Error('--modulo=1697|1732');
const courseid = Number(args.courseid || M.courseid);
const EXAMEN = `Examen final · Módulo ${modulo}`;
const EXAMEN_ANTIGUO = `${EXAMEN} (versión anterior)`;
const SECCION_EXAMEN = 'Examen final del módulo';
const PANTALLA = { popup: 1, width: '80%', height: '80%', hidetoc: 3, nav: 0, skipview: 0 };
const IMG = path.join(ROOT, 'recursos', 'cabeceras', 'temas');
const num = s => Number(s.number ?? s.section);
const nombre = s => s.title ?? s.name;
const log = (...m) => console.log(args.aplicar || args.finalizacion ? '' : '[prueba]', ...m);
const tras = cm => JSON.stringify({ op: '&', showc: [true], c: [{ type: 'completion', cm, e: 1 }] });
const curso = (page, action, ids, extra = {}) => A.ajax(page, 'core_courseformat_update_course', { action, courseid, ids, ...extra });

async function crearCabecera(page, seccion, n, titulo) {
  const img = path.join(IMG, `${modulo}-tema${String(n).padStart(2, '0')}.jpg`);
  return A.crearActividad(page, { courseid, seccion, modulo: 'label', nombre: `TEMA ${n}`,
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

// Crea (si faltan) la cabecera y las cuatro actividades del tema n al final de la sección de la UF.
async function subirTema(page, ufId, n) {
  const dir = path.join(ROOT, 'temario', modulo, `tema${n}`);
  const fichas = fs.readdirSync(dir).filter(f => /^0\d-.*\.json$/.test(f)).sort()
    .map(f => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')));
  const leer = f => fs.readFileSync(path.join(dir, f), 'utf8');
  const seccionActual = async () => num((await A.estado(page, courseid)).secciones.find(s => String(s.id) === String(ufId)));
  let { actividades } = await A.estado(page, courseid);
  const ids = [];
  const cab = actividades.find(a => a.name === `TEMA ${n}`);
  ids.push(cab ? Number(cab.id) : await crearCabecera(page, await seccionActual(), n, fichas[0].name));
  log(`  TEMA ${n}: cabecera ${cab ? 'ya existía' : 'creada'}`);
  let scormCm = null;
  let quizCm = null;
  for (const f of fichas) {
    const previa = actividades.find(a => a.name === f.name);
    let cmid = previa && Number(previa.id);
    if (!previa) {
      const seccion = await seccionActual();
      if (f.scorm_package) {
        cmid = await A.crearActividad(page, { courseid, seccion, modulo: 'scorm', nombre: f.name,
          valores: { ...A.AJUSTES.scorm, ...PANTALLA, 'introeditor[text]': '' },
          ficheros: { packagefile: path.resolve(dir, f.scorm_package) } });
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
    }
    log(`  · ${f.name}: ${previa ? 'ya existía' : 'creada'} (cm ${cmid})`);
    if (f.scorm_package) scormCm = cmid;
    if (f.gift_file) {
      quizCm = cmid;
      const base = page.url().split('/').slice(0, 3).join('/');
      await page.goto(`${base}/mod/quiz/edit.php?cmid=${cmid}`);
      if (!(await page.locator('li.slot').count())) {
        const r = await A.preguntasCuestionario(page, cmid, path.join(dir, f.gift_file));
        log(`    preguntas: ${r.añadidas} añadidas`);
      }
    }
    ids.push(cmid);
  }
  await curso(page, 'cm_show', ids);
}

(async () => {
  const { browser, page } = await abrir();
  try {
    let { secciones, actividades } = await A.estado(page, courseid);
    const esUF = s => /^UF\d/.test(nombre(s) || '');

    if (args.finalizacion) {
      // Finalización del curso: las actividades de los temas de cada UF más el examen final nuevo.
      const cms = secciones.filter(s => esUF(s) || s.component === 'mod_subsection').flatMap(s => s.cmlist || [])
        .map(id => actividades.find(a => String(a.id) === String(id)))
        .filter(a => a && ['scorm', 'quiz', 'assign', 'forum'].includes(a.module)).map(a => Number(a.id));
      const examen = actividades.find(a => a.name === EXAMEN);
      if (!examen) throw new Error(`No encuentro «${EXAMEN}»: ejecuta antes examen_final.js`);
      await A.finalizacionCurso(page, courseid, [...cms, Number(examen.id)]);
      console.log(`Finalización del curso: ${cms.length} actividades de los temas + el examen final`);
      return;
    }

    // 1. Lo antiguo, oculto.
    for (const id of M.ocultarCms || []) {
      const a = actividades.find(x => Number(x.id) === id);
      if (!a) continue;
      log(`Ocultar «${a.name}» (cm ${id})`);
      if (args.aplicar) await curso(page, 'cm_hide', [id]);
    }
    if (M.ocultarSecciones) {
      for (const s of secciones.filter(s => !s.component && num(s) > 0 && !esUF(s) && nombre(s) !== SECCION_EXAMEN)) {
        log(`Ocultar la sección ${num(s)} «${nombre(s)}»`);
        if (args.aplicar) await curso(page, 'section_hide', [Number(s.id)]);
      }
    }
    // 2. El examen final antiguo, renombrado y oculto (examen_final.js crea el nuevo).
    const viejo = actividades.find(a => a.name === EXAMEN);
    if (viejo && !actividades.some(a => a.name === EXAMEN_ANTIGUO)) {
      log(`Examen antiguo (cm ${viejo.id}) → «${EXAMEN_ANTIGUO}», oculto`);
      if (args.aplicar) {
        await A.editarActividad(page, Number(viejo.id), { name: EXAMEN_ANTIGUO });
        await curso(page, 'cm_hide', [Number(viejo.id)]);
      }
    }
    // 3. Cada UF con sus temas.
    for (const uf of M.ufs) {
      ({ secciones } = await A.estado(page, courseid));
      let sec = secciones.find(s => !s.component && nombre(s) === uf.nombre);
      log(`${uf.nombre}: ${sec ? 'sección ' + num(sec) : 'se crea'}`);
      if (!args.aplicar) continue;
      if (!sec) {
        const ultima = Math.max(...secciones.filter(s => !s.component).map(num));
        await A.crearSeccion(page, courseid, ultima + 1, uf.nombre);
        ({ secciones } = await A.estado(page, courseid));
        sec = secciones.find(s => !s.component && nombre(s) === uf.nombre);
      }
      if (!sec.visible) await curso(page, 'section_show', [Number(sec.id)]);
      for (const n of uf.temas) await subirTema(page, sec.id, n);
    }
    // 4. El examen, al final.
    if (args.aplicar) {
      ({ secciones } = await A.estado(page, courseid));
      const normales = secciones.filter(s => !s.component);
      const ex = normales.find(s => nombre(s) === SECCION_EXAMEN);
      const ultima = normales.reduce((a, b) => (num(a) > num(b) ? a : b));
      if (ex && ex.id !== ultima.id) {
        await curso(page, 'section_move_after', [Number(ex.id)], { targetsectionid: Number(ultima.id) });
        log(`Sección «${SECCION_EXAMEN}» movida al final`);
      }
      ({ secciones, actividades } = await A.estado(page, courseid));
      for (const s of secciones.filter(x => !x.component)) {
        const cms = (s.cmlist || []).map(id => actividades.find(a => String(a.id) === String(id))).filter(Boolean);
        console.log(`${num(s)} · ${nombre(s)} · visible=${s.visible} · ${cms.map(c => c.name + (c.visible ? '' : ' [oculta]')).join(' | ')}`);
      }
    } else console.log('(sin --aplicar: no se ha cambiado nada)');
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
