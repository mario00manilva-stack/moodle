// Acciones sobre el aula con la sesión web de la cuenta de la herramienta.
//
// Todo pasa por las páginas y servicios AJAX estándar de Moodle (los mismos que usa la interfaz),
// sin plugins. Las actividades se crean enviando el formulario de edición de Moodle con los ajustes
// de las actividades del Tema 1, y siempre ocultas.
const fs = require('fs');
const path = require('path');

/** Llama a un servicio AJAX de Moodle con la sesión del navegador. */
async function ajax(page, methodname, args) {
  const res = await page.evaluate(async ({ methodname, args }) => {
    const r = await fetch(`${M.cfg.wwwroot}/lib/ajax/service.php?sesskey=${M.cfg.sesskey}&info=${methodname}`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify([{ index: 0, methodname, args }]),
    });
    return r.json();
  }, { methodname, args });
  const out = Array.isArray(res) ? res[0] : res;
  if (!out || out.error) throw new Error(`${methodname}: ${JSON.stringify(out && (out.exception || out.error) || res)}`);
  return out.data;
}

/** Estado del curso: secciones (número, id, nombre) y actividades (id, nombre, módulo, sección, visible). */
async function estado(page, courseid) {
  await asegurarCurso(page, courseid);
  const st = JSON.parse(await ajax(page, 'core_courseformat_get_state', { courseid }));
  return { secciones: st.section, actividades: st.cm };
}

async function asegurarCurso(page, courseid) {
  if (!page.url().includes(`/course/view.php?id=${courseid}`)) {
    await page.goto(`${page.url().split('/').slice(0, 3).join('/')}/course/view.php?id=${courseid}`);
  }
}

/** Crea la sección número `numero` con su nombre, si no existe. Solo añade al final: nunca renumera. */
async function crearSeccion(page, courseid, numero, nombre) {
  let { secciones } = await estado(page, courseid);
  const normales = secciones.filter(s => !s.component);
  const existe = normales.find(s => Number(s.number ?? s.section) === numero);
  if (existe) return { id: existe.id, creada: false };
  const ultima = Math.max(...normales.map(s => Number(s.number ?? s.section)));
  if (numero !== ultima + 1) throw new Error(`La siguiente sección libre es la ${ultima + 1}, no la ${numero}.`);
  const anterior = normales.find(s => Number(s.number ?? s.section) === ultima);
  await ajax(page, 'core_courseformat_update_course', { action: 'section_add', courseid, ids: [], targetsectionid: Number(anterior.id) });
  ({ secciones } = await estado(page, courseid));
  const nueva = secciones.filter(s => !s.component).find(s => Number(s.number ?? s.section) === numero);
  if (!nueva) throw new Error(`No aparece la sección ${numero} tras crearla.`);
  await ajax(page, 'core_update_inplace_editable', { component: 'format_topics', itemtype: 'sectionname', itemid: Number(nueva.id), value: nombre });
  return { id: nueva.id, creada: true };
}

/** Sube un fichero al área de borrador `itemid` (como el selector de archivos de Moodle). */
async function subirBorrador(page, itemid, ruta) {
  const html = await page.content();
  const m = html.match(/"id":"?(\d+)"?,"name":"[^"]*","type":"upload"/) || html.match(/"type":"upload"[^}]*?"id":"?(\d+)"?/);
  if (!m) throw new Error('No encuentro el repositorio de subida en la página.');
  const b64 = fs.readFileSync(ruta).toString('base64');
  const res = await page.evaluate(async ({ itemid, repo, name, b64 }) => {
    const bytes = Uint8Array.from(atob(b64), c => c.charCodeAt(0));
    const fd = new FormData();
    fd.append('repo_upload_file', new Blob([bytes]), name);
    for (const [k, v] of Object.entries({ sesskey: M.cfg.sesskey, repo_id: repo, itemid, author: 'VERAQUA FORMACIÓN',
      savepath: '/', title: name, overwrite: 1, ctx_id: M.cfg.contextid, client_id: 'herramienta', env: 'filepicker' })) fd.append(k, v);
    const r = await fetch(`${M.cfg.wwwroot}/repository/repository_ajax.php?action=upload`, { method: 'POST', body: fd });
    return r.json();
  }, { itemid, repo: m[1], name: path.basename(ruta), b64 });
  if (res.error) throw new Error('Subida: ' + res.error);
  return res;
}

/**
 * Abre el formulario de una actividad nueva, aplica `valores` sobre los campos del propio formulario
 * y lo envía. `ficheros` = { campoFilepicker: ruta }. Devuelve el cmid creado.
 */
async function crearActividad(page, { courseid, seccion, modulo, nombre, valores, ficheros = {}, preparar }) {
  const base = page.url().split('/').slice(0, 3).join('/');
  const { actividades } = await estado(page, courseid);
  if (actividades.some(a => a.name === nombre)) throw new Error(`Ya existe «${nombre}» en el curso ${courseid}.`);
  await page.goto(`${base}/course/modedit.php?add=${modulo}&course=${courseid}&section=${seccion}&return=0`);
  if (!(await page.locator('form.mform #id_name').count())) throw new Error(`No se abre el formulario de ${modulo}.`);
  for (const [campo, ruta] of Object.entries(ficheros)) {
    const itemid = await page.inputValue(`form.mform input[name="${campo}"]`);
    await subirBorrador(page, itemid, ruta);
  }
  // `preparar(page)` actúa sobre el formulario ya abierto y devuelve valores extra (p. ej. un HTML
  // que enlaza una imagen subida a su área de borrador).
  if (preparar) valores = { ...valores, ...(await preparar(page)) };
  const resultado = await page.evaluate(async ({ nombre, valores }) => {
    if (window.tinymce) window.tinymce.triggerSave();
    const form = document.querySelector('#region-main form.mform');
    const fd = new FormData(form);
    for (const k of ['submitbutton', 'cancel']) fd.delete(k);
    fd.set('submitbutton2', '1');
    fd.set('name', nombre);
    fd.set('visible', '0');
    for (const [k, v] of Object.entries(valores)) {
      if (v === null) fd.delete(k); else fd.set(k, String(v));
    }
    const r = await fetch(form.action, { method: 'POST', body: fd });
    const text = await r.text();
    const doc = new DOMParser().parseFromString(text, 'text/html');
    const errores = [...doc.querySelectorAll('.form-control-feedback.invalid-feedback, .error')]
      .map(e => e.textContent.trim()).filter(Boolean);
    return { url: r.url, errores, sigueEnFormulario: !!doc.querySelector('form.mform #id_name') };
  }, { nombre, valores });
  if (resultado.sigueEnFormulario || resultado.errores.length) {
    throw new Error(`Moodle rechazó el formulario de «${nombre}»: ${resultado.errores.join(' | ') || resultado.url}`);
  }
  const despues = await estado(page, courseid);
  const cm = despues.actividades.find(a => a.name === nombre);
  if (!cm) throw new Error(`No aparece «${nombre}» tras guardarlo.`);
  return Number(cm.id);
}

// --- Ajustes de las actividades del Tema 1 (plantilla) ------------------------------------------

const REVISION = (() => {
  const v = {};
  const fases = { during: false, immediately: true, open: true, closed: false };
  for (const item of ['attempt', 'correctness', 'maxmarks', 'marks', 'specificfeedback', 'generalfeedback', 'rightanswer', 'overallfeedback']) {
    for (const [fase, on] of Object.entries(fases)) {
      const activo = on || (fase === 'during' && (item === 'attempt' || item === 'maxmarks'));
      v[`${item}${fase}`] = activo ? 1 : null;
    }
  }
  return v;
})();

const AJUSTES = {
  scorm: { popup: 0, width: 100, height: 500, skipview: 0, hidebrowse: 0, hidetoc: 0, nav: 1, displaycoursestructure: 0,
    displayattemptstatus: 1, grademethod: 1, maxgrade: 100, maxattempt: 0, whatgrade: 0, forcenewattempt: 0,
    lastattemptlock: 0, forcecompleted: 0, auto: 0, autocommit: 0, masteryoverride: 0, updatefreq: 0,
    completion: 2, completionview: null, 'completionstatusrequired[2]': 1, 'completionstatusrequired[4]': 1,
    completionstatusallscos: null, completionscoreenabled: null, completionusegrade: null },
  quiz: { gradepass: 5, attempts: 3, grademethod: 1, questionsperpage: 1, navmethod: 'free', shuffleanswers: 1,
    preferredbehaviour: 'deferredfeedback', canredoquestions: 0, attemptonlast: 0, overduehandling: 'autosubmit',
    'graceperiod[enabled]': null, decimalpoints: 2, questiondecimalpoints: -1, showblocks: 0, showuserpicture: 0,
    ...REVISION, completion: 2, completionview: null, completionusegrade: 1, completionpassgrade: 1,
    completionminattemptsenabled: null },
  assign: { 'allowsubmissionsfromdate[enabled]': null, 'duedate[enabled]': null, 'cutoffdate[enabled]': null,
    'gradingduedate[enabled]': null, alwaysshowdescription: 1, assignsubmission_onlinetext_enabled: 1,
    assignsubmission_file_enabled: 1, assignsubmission_file_maxfiles: 1, assignsubmission_file_maxsizebytes: 52428800,
    assignfeedback_comments_enabled: 1, submissiondrafts: 0, requiresubmissionstatement: 0, maxattempts: 1,
    attemptreopenmethod: 'untilpass', sendnotifications: 0, sendlatenotifications: 0, sendstudentnotifications: 1,
    'grade[modgrade_type]': 'point', 'grade[modgrade_point]': 100, completion: 2, completionsubmit: 1 },
  forum: { type: 'general', forcesubscribe: 2, trackingtype: 1, maxbytes: 512000, maxattachments: 9, displaywordcount: 0,
    'grade_forum[modgrade_type]': 'none', assessed: 0, completion: 2, completionpostsenabled: 1, completionposts: 1,
    completiondiscussionsenabled: null, completionrepliesenabled: null, completionusegrade: null,
    completiongradeitemnumber: null },
};

/** Restricción «completar la actividad anterior» (cm -1): sobrevive a cambios de ids. */
const TRAS_ANTERIOR = JSON.stringify({ op: '&', showc: [true], c: [{ type: 'completion', cm: -1, e: 1 }] });

/** Importa un GIFT en el banco propio del cuestionario y añade las preguntas, una por página. */
async function idsDelBanco(page, base, cmid) {
  await page.goto(`${base}/question/edit.php?cmid=${cmid}`);
  const aviso = await page.locator('#region-main').innerText();
  if (/adhoc|transfer_question|no se han completado|not yet complete/i.test(aviso)) {
    throw new Error('El banco de preguntas aún no está disponible (tareas pendientes de Moodle). Reintentar más tarde.');
  }
  return (await page.$$eval('input[type=checkbox][name^="q"]', els =>
    els.map(e => e.name).filter(n => /^q\d+$/.test(n)).map(n => Number(n.slice(1)))))
    .sort((a, b) => a - b);
}

async function preguntasCuestionario(page, cmid, giftRuta) {
  const base = page.url().split('/').slice(0, 3).join('/');
  // Si el banco ya tiene preguntas (una ejecución anterior se cortó), no se importan otra vez.
  let ids = await idsDelBanco(page, base, cmid);
  if (!ids.length) ids = await importarGift(page, base, cmid, giftRuta);
  const sesskey = await page.evaluate(() => M.cfg.sesskey);
  let pagina = 0;
  for (const qid of ids) {
    await page.goto(`${base}/mod/quiz/edit.php?cmid=${cmid}&addquestion=${qid}&addonpage=${++pagina}&sesskey=${sesskey}`);
  }
  return { añadidas: ids.length };
}

async function importarGift(page, base, cmid, giftRuta) {
  await page.goto(`${base}/question/bank/importquestions/import.php?cmid=${cmid}`);
  const itemid = await page.inputValue('form.mform input[name="newfile"]');
  await subirBorrador(page, itemid, giftRuta);
  await page.check('input[name="format"][value="gift"]');
  await Promise.all([page.waitForLoadState('load'), page.click('form.mform #id_submitbutton')]);
  const texto = await page.locator('#region-main').innerText();
  if (!/Importando|Importing|Importar/i.test(texto)) {
    throw new Error('La importación GIFT no se completó: ' + texto.slice(0, 300));
  }
  const ids = await idsDelBanco(page, base, cmid);
  if (!ids.length) throw new Error('No encuentro las preguntas importadas en el banco.');
  return ids;
}

/** Edita una actividad existente: abre su formulario, aplica `valores` y lo guarda. */
async function editarActividad(page, cmid, valores) {
  // Si alguien ya completó la actividad, Moodle bloquea los ajustes de finalización (y la nota de
  // aprobado) hasta pulsar «Desbloquear»; al guardar recalcula las finalizaciones existentes.
  // Solo se desbloquea cuando la edición toca la finalización.
  if (Object.keys(valores).some(k => k.startsWith('completion') || k === 'gradepass')) valores = { completionunlocked: 1, ...valores };
  const base = page.url().split('/').slice(0, 3).join('/');
  await page.goto(`${base}/course/modedit.php?update=${cmid}&return=0`);
  if (!(await page.locator('form.mform #id_name').count())) throw new Error(`No se abre la edición de cm ${cmid}.`);
  const r = await page.evaluate(async (valores) => {
    if (window.tinymce) window.tinymce.triggerSave();
    const form = document.querySelector('#region-main form.mform');
    const fd = new FormData(form);
    for (const k of ['submitbutton', 'cancel']) fd.delete(k);
    fd.set('submitbutton2', '1');
    for (const [k, v] of Object.entries(valores)) { if (v === null) fd.delete(k); else fd.set(k, String(v)); }
    const res = await fetch(form.action, { method: 'POST', body: fd });
    const doc = new DOMParser().parseFromString(await res.text(), 'text/html');
    return { errores: [...doc.querySelectorAll('.form-control-feedback.invalid-feedback, .error')].map(e => e.textContent.trim()).filter(Boolean),
      sigue: !!doc.querySelector('form.mform #id_name') };
  }, valores);
  if (r.sigue || r.errores.length) throw new Error(`Moodle rechazó la edición de cm ${cmid}: ${r.errores.join(' | ')}`);
}

/** Criterios de finalización acordados con Mario (14/10/2026) para las actividades de cada tema. */
const FINALIZACION = {
  // El paquete marca «completed» al ver la última diapositiva y envía una puntuación de 100 con
  // masteryscore 100: con «masteryoverride» Moodle lo convierte en «passed» (o «failed» si se sale a
  // medias) y un requisito de solo «completed» no se cumpliría nunca. Se acepta cualquiera de los dos
  // y se desactiva la conversión.
  scorm: { completion: 2, completionview: null, 'completionstatusrequired[2]': 1, 'completionstatusrequired[4]': 1,
    masteryoverride: 0, completionscoreenabled: null, completionusegrade: null },
  quiz: { attempts: 3, completion: 2, completionview: null, gradepass: 5, completionusegrade: 1, completionpassgrade: 1,
    completionminattemptsenabled: null, completionattemptsexhausted: null },
  assign: { completion: 2, completionview: null, completionsubmit: 1, completionusegrade: null },
  forum: { completion: 2, completionview: null, completionpostsenabled: 1, completionposts: 1,
    completiondiscussionsenabled: null, completionrepliesenabled: null, completionusegrade: null,
    completiongradeitemnumber: null },
};

/** Finalización del curso: completar TODAS las actividades indicadas (y solo esas). */
async function finalizacionCurso(page, courseid, cmids) {
  const base = page.url().split('/').slice(0, 3).join('/');
  await page.goto(`${base}/course/completion.php?id=${courseid}`);
  // Si alguien ya cumplió algún criterio, la página está bloqueada. Desbloquear borra los datos de
  // finalización del curso (no los de las actividades): solo se permite mientras no haya alumnos reales.
  if (await page.locator('input[name="settingsunlock"]').count()) {
    if (!process.env.DESBLOQUEAR_FINALIZACION_CURSO) {
      throw new Error('La finalización del curso está bloqueada. Para desbloquearla (borra los datos de finalización del curso) lanza con DESBLOQUEAR_FINALIZACION_CURSO=1.');
    }
    // El botón pide confirmación en un diálogo: se envía el formulario con el botón ya «pulsado».
    await page.evaluate(async () => {
      const form = document.querySelector('#region-main form.mform');
      const fd = new FormData(form);
      const b = form.querySelector('input[name="settingsunlock"]');
      fd.set('settingsunlock', b.value);
      await fetch(form.action, { method: 'POST', body: fd });
    });
    await page.goto(`${base}/course/completion.php?id=${courseid}`);
    if (await page.locator('input[name="settingsunlock"]').count()) throw new Error('No se pudo desbloquear la finalización del curso.');
  }
  const r = await page.evaluate(async (cmids) => {
    const form = document.querySelector('#region-main form.mform');
    if (!form) return { error: 'No se abre la página de finalización del curso.' };
    const fd = new FormData(form);
    fd.delete('cancel');
    const disponibles = [...form.querySelectorAll('input[type=checkbox][name^="criteria_activity["]')].map(e => Number(e.name.match(/\d+/)[0]));
    const faltan = cmids.filter(id => !disponibles.includes(id));
    if (faltan.length) return { error: `Actividades sin finalización activada: ${faltan.join(', ')}` };
    for (const id of disponibles) fd.set(`criteria_activity[${id}]`, cmids.includes(id) ? '1' : '0');
    fd.set('activity_aggregation', '1');
    fd.set('overall_aggregation', '1');
    const res = await fetch(form.action, { method: 'POST', body: fd });
    const doc = new DOMParser().parseFromString(await res.text(), 'text/html');
    const marcadas = [...doc.querySelectorAll('input[type=checkbox][name^="criteria_activity["]:checked')].length;
    return { marcadas, errores: [...doc.querySelectorAll('.error, .alert-danger')].map(e => e.textContent.trim()).filter(Boolean) };
  }, cmids);
  if (r.error || (r.errores && r.errores.length)) throw new Error(r.error || r.errores.join(' | '));
  return r;
}

module.exports = { finalizacionCurso, editarActividad, FINALIZACION, ajax, estado, crearSeccion, subirBorrador, crearActividad, preguntasCuestionario, AJUSTES, TRAS_ANTERIOR };
