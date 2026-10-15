// Pone la imagen de cabecera de cada tema (recursos/cabeceras/temas/<módulo>-temaNN.jpg) como
// descripción de su sección en el aula. Imágenes de Mario (15/10/2026).
//
//   node tools/aula/cabeceras_temas.js [--modulo=1701] [--tema=7]
//
// Se puede repetir: sustituye la cabecera anterior y conserva el resto de la descripción. Los temas
// que aún no tienen sección en el aula se saltan.
const fs = require('fs');
const path = require('path');
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => { const [k, v = true] = a.replace(/^--/, '').split('='); return [k, v]; }));
const DIR = path.resolve(__dirname, '..', '..', 'recursos', 'cabeceras', 'temas');
const CURSOS = { 1701: 4, 1697: 3, 1732: 2 };
const MARCA = 'veraqua-cabecera-tema';

(async () => {
  const { browser, page } = await abrir();
  try {
    const base = page.url().split('/').slice(0, 3).join('/');
    const imagenes = fs.readdirSync(DIR).map(f => f.match(/^(\d{4})-tema(\d+)\.jpg$/)).filter(Boolean)
      .filter(([, m, t]) => (!args.modulo || args.modulo === m) && (!args.tema || Number(args.tema) === Number(t)));
    const porCurso = {};
    for (const [f, m, t] of imagenes) (porCurso[m] = porCurso[m] || []).push({ f, tema: Number(t) });
    for (const [modulo, lista] of Object.entries(porCurso)) {
      const courseid = CURSOS[modulo];
      const { secciones } = await A.estado(page, courseid);
      for (const { f, tema } of lista.sort((a, b) => a.tema - b.tema)) {
        const s = secciones.find(x => !x.component && Number(x.number ?? x.section) === tema);
        if (!s) { console.log(`${modulo} · Tema ${tema}: sin sección en el aula todavía (se salta)`); continue; }
        await page.goto(`${base}/course/editsection.php?id=${s.id}&sr=0`);
        const itemid = await page.inputValue('form.mform [name="summary_editor[itemid]"]');
        const sub = await A.subirBorrador(page, itemid, path.join(DIR, f));
        const r = await page.evaluate(async ({ url, alt, marca }) => {
          if (window.tinymce) window.tinymce.triggerSave();
          const form = document.querySelector('#region-main form.mform');
          const fd = new FormData(form);
          const resto = (fd.get('summary_editor[text]') || '').replace(new RegExp(`<p class="${marca}">[\\s\\S]*?</p>`), '').trim();
          fd.set('summary_editor[text]', `<p class="${marca}"><img src="${url}" alt="${alt}" class="img-fluid" style="width:100%;height:auto;border-radius:12px"></p>${resto}`);
          fd.set('summary_editor[format]', '1');
          fd.delete('cancel');
          const res = await fetch(form.action, { method: 'POST', body: fd });
          const doc = new DOMParser().parseFromString(await res.text(), 'text/html');
          return { errores: [...doc.querySelectorAll('.form-control-feedback.invalid-feedback, .error')].map(e => e.textContent.trim()).filter(Boolean),
            sigue: !!doc.querySelector('form.mform [name="summary_editor[itemid]"]') };
        }, { url: sub.url, alt: `${s.title ?? s.name ?? 'Tema ' + tema}`, marca: MARCA });
        if (r.sigue || r.errores.length) throw new Error(`${modulo} · Tema ${tema}: Moodle rechazó la sección: ${r.errores.join(' | ')}`);
        console.log(`${modulo} · Tema ${tema}: cabecera puesta`);
      }
    }
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
