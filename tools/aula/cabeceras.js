// Pone la cabecera ilustrada de cada módulo arriba del todo en la página del curso (etiqueta en la
// sección General) y, si la cuenta tiene permiso, la imagen del curso que se ve en «Mis cursos».
//
//   python3 -I tools/cabeceras.py && node tools/aula/cabeceras_png.js
//   node tools/aula/cabeceras.js [--curso=1701]
//
// Se puede repetir: si la etiqueta ya existe, le pone la imagen actual y la deja visible y la primera.
const path = require('path');
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => a.replace(/^--/, '').split('=')));
const fs = require('fs');
const ROOT = path.resolve(__dirname, '..', '..');
// Imágenes de Mario (recursos/cabeceras/<módulo>.jpg); si faltan, las ilustraciones generadas.
const imagen = (modulo, tipo) => {
  const propia = path.join(ROOT, 'recursos', 'cabeceras', `${modulo}.jpg`);
  return fs.existsSync(propia) ? propia : path.join(ROOT, 'entregas', 'cabeceras', `${modulo}-${tipo}.png`);
};
const CURSOS = {
  1701: { courseid: 4, alt: 'Módulo 1701 · Control de organismos nocivos en piscinas y otras instalaciones acuáticas' },
  1697: { courseid: 3, alt: 'Módulo 1697 · Preparación y traslado de materiales en el control de organismos nocivos' },
  1732: { courseid: 2, alt: 'Módulo 1732 · Nivel básico de Prevención de riesgos laborales' },
};
const NOMBRE = 'Cabecera del módulo';

const htmlImagen = (url, alt) => `<p><img src="${url}" alt="${alt}" class="img-fluid" style="width:100%;height:auto;border-radius:12px"></p>`;

async function etiqueta(page, modulo, { courseid, alt }) {
  let { secciones, actividades } = await A.estado(page, courseid);
  let cm = actividades.find(a => a.name === NOMBRE);
  if (!cm) {
    const cmid = await A.crearActividad(page, { courseid, seccion: 0, modulo: 'label', nombre: NOMBRE,
      valores: { 'introeditor[format]': 1, completion: 0 },
      preparar: async (p) => {
        const itemid = await p.inputValue('form.mform input[name="introeditor[itemid]"]');
        const sub = await A.subirBorrador(p, itemid, imagen(modulo, 'cabecera'));
        return { 'introeditor[text]': htmlImagen(sub.url, alt) };
      } });
    ({ secciones, actividades } = await A.estado(page, courseid));
    cm = actividades.find(a => Number(a.id) === cmid);
    console.log(`${modulo}: etiqueta creada (cm ${cmid})`);
  } else {
    await A.editarActividad(page, Number(cm.id), {}, async (p) => {
      const itemid = await p.inputValue('form.mform input[name="introeditor[itemid]"]');
      await vaciarBorrador(p, itemid);
      const sub = await A.subirBorrador(p, itemid, imagen(modulo, 'cabecera'));
      return { 'introeditor[text]': htmlImagen(sub.url, alt) };
    });
    console.log(`${modulo}: etiqueta actualizada con la imagen nueva (cm ${cm.id})`);
  }
  if (!cm.visible) await A.ajax(page, 'core_courseformat_update_course', { action: 'cm_show', courseid, ids: [Number(cm.id)] });
  const general = secciones.find(s => Number(s.number ?? s.section) === 0);
  const primero = (general.cmlist || [])[0];
  if (primero && Number(primero) !== Number(cm.id)) {
    await A.ajax(page, 'core_courseformat_update_course', { action: 'cm_move', courseid, ids: [Number(cm.id)],
      targetsectionid: Number(general.id), targetcmid: Number(primero) });
  }
}

async function imagenCurso(page, modulo, { courseid }) {
  const base = page.url().split('/').slice(0, 3).join('/');
  await page.goto(`${base}/course/edit.php?id=${courseid}`);
  const campo = page.locator('form.mform input[name="overviewfiles_filemanager"]');
  if (!(await campo.count())) { console.log(`${modulo}: la cuenta no puede cambiar la imagen del curso (se omite)`); return; }
  const itemid = await campo.inputValue();
  await vaciarBorrador(page, itemid);
  await A.subirBorrador(page, itemid, imagen(modulo, 'tarjeta'));
  const r = await page.evaluate(async () => {
    if (window.tinymce) window.tinymce.triggerSave();
    const form = document.querySelector('#region-main form.mform');
    const fd = new FormData(form);
    fd.delete('cancel'); fd.set('saveanddisplay', '1');
    const res = await fetch(form.action, { method: 'POST', body: fd });
    const doc = new DOMParser().parseFromString(await res.text(), 'text/html');
    return { errores: [...doc.querySelectorAll('.form-control-feedback.invalid-feedback, .error')].map(e => e.textContent.trim()).filter(Boolean),
      sigue: !!doc.querySelector('form.mform input[name="overviewfiles_filemanager"]') };
  });
  if (r.sigue || r.errores.length) console.log(`${modulo}: Moodle no aceptó la imagen del curso: ${r.errores.join(' | ') || 'formulario devuelto'}`);
  else console.log(`${modulo}: imagen del curso actualizada`);
}

/** Vacía un área de borrador (la imagen anterior) antes de subir la nueva. */
async function vaciarBorrador(page, itemid) {
  await page.evaluate(async (itemid) => {
    const fd = new FormData();
    for (const [k, v] of Object.entries({ sesskey: M.cfg.sesskey, itemid, filepath: '/', client_id: 'herramienta' })) fd.append(k, v);
    const r = await fetch(`${M.cfg.wwwroot}/repository/draftfiles_ajax.php?action=list`, { method: 'POST', body: fd });
    const lista = await r.json();
    for (const f of (lista.list || [])) {
      const d = new FormData();
      for (const [k, v] of Object.entries({ sesskey: M.cfg.sesskey, itemid, filepath: '/', filename: f.filename, client_id: 'herramienta' })) d.append(k, v);
      await fetch(`${M.cfg.wwwroot}/repository/draftfiles_ajax.php?action=delete`, { method: 'POST', body: d });
    }
  }, itemid);
}

(async () => {
  const { browser, page } = await abrir();
  try {
    for (const [modulo, c] of Object.entries(CURSOS)) {
      if (args.curso && args.curso !== modulo) continue;
      if (args.ids) c.courseid = Number(JSON.parse(args.ids)[modulo] ?? c.courseid);
      await etiqueta(page, modulo, c);
      await imagenCurso(page, modulo, c);
    }
  } finally { await browser.close(); }
})().catch(e => { console.error(e.message); process.exit(1); });
