// Muestra cada tema en su propia página; la portada del curso enseña en cada tema «Progreso: X / N».
// Es la única indicación de progreso por tema que da Moodle sin plugins (15/10/2026).
//
//   node tools/aula/una_seccion_por_pagina.js [--deshacer] [--courseid=4]
const { abrir } = require('./sesion');

const args = Object.fromEntries(process.argv.slice(2).map(a => { const [k, v = true] = a.replace(/^--/, '').split('='); return [k, v]; }));
const cursos = args.courseid ? [Number(args.courseid)] : [4, 3, 2];
const valor = args.deshacer ? '0' : '1';

(async () => {
  const { browser, page } = await abrir();
  try {
    const base = page.url().split('/').slice(0, 3).join('/');
    for (const id of cursos) {
      await page.goto(`${base}/course/edit.php?id=${id}`);
      if (!(await page.locator('form.mform [name="coursedisplay"]').count())) { console.log(`Curso ${id}: no puedo cambiar la presentación`); continue; }
      const r = await page.evaluate(async (valor) => {
        if (window.tinymce) window.tinymce.triggerSave();
        const form = document.querySelector('#region-main form.mform');
        const fd = new FormData(form);
        fd.delete('cancel'); fd.set('saveanddisplay', '1'); fd.set('coursedisplay', valor);
        const res = await fetch(form.action, { method: 'POST', body: fd });
        const doc = new DOMParser().parseFromString(await res.text(), 'text/html');
        return { errores: [...doc.querySelectorAll('.form-control-feedback.invalid-feedback, .error')].map(e => e.textContent.trim()).filter(Boolean),
          sigue: !!doc.querySelector('form.mform [name="coursedisplay"]') };
      }, valor);
      await page.goto(`${base}/course/edit.php?id=${id}`);
      const ahora = await page.inputValue('form.mform [name="coursedisplay"]');
      console.log(`Curso ${id}: ${r.sigue || r.errores.length ? 'RECHAZADO ' + r.errores.join(' | ') : 'guardado'} · coursedisplay=${ahora}`);
    }
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
