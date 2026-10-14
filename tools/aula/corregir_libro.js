// Corrige capítulos del libro base de un curso aplicando sustituciones exactas sobre el texto
// ACTUAL del aula (el aula manda: se lee del formulario de edición, no de la instantánea).
// Si alguna sustitución no encuentra su texto, no se guarda nada de ese capítulo.
//   node tools/aula/corregir_libro.js --courseid=4 --correcciones=temario/1701/correcciones-libro.json
const fs = require('fs');
const path = require('path');
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => a.replace(/^--/, '').split('=')));
const correcciones = JSON.parse(fs.readFileSync(path.resolve(__dirname, '..', '..', args.correcciones), 'utf8'));

(async () => {
  const { browser, page, URL } = await abrir();
  try {
    const { actividades } = await A.estado(page, Number(args.courseid));
    const libro = actividades.find(a => a.module === 'book');
    await page.goto(`${URL}/mod/book/view.php?id=${libro.id}`);
    const capitulos = await page.$$eval('.book_toc a, .book_toc strong', els => els.map(e => ({
      titulo: e.textContent.trim(), id: (e.href || '').match(/chapterid=(\d+)/)?.[1] })));
    for (const c of correcciones) {
      let id = capitulos.find(x => x.titulo.startsWith(c.capitulo) && x.id)?.id;
      if (!id) { // el capítulo abierto aparece sin enlace
        await page.goto(`${URL}/mod/book/view.php?id=${libro.id}`);
        throw new Error(`No encuentro el capítulo «${c.capitulo}»`);
      }
      await page.goto(`${URL}/mod/book/edit.php?cmid=${libro.id}&id=${id}`);
      const r = await page.evaluate(async (subs) => {
        const form = document.querySelector('#region-main form.mform');
        const ta = form.querySelector('textarea[name="content_editor[text]"]');
        const ed = window.tinymce && window.tinymce.get(ta.id);
        let html = ed ? ed.getContent() : ta.value;
        const faltan = subs.filter(([a]) => !html.includes(a)).map(([a]) => a.slice(0, 60));
        if (faltan.length) return { faltan };
        for (const [a, b] of subs) html = html.replace(a, b);
        const fd = new FormData(form);
        fd.delete('cancel');
        fd.set('content_editor[text]', html);
        const res = await fetch(form.action, { method: 'POST', body: fd });
        const doc = new DOMParser().parseFromString(await res.text(), 'text/html');
        return { ok: !doc.querySelector('form.mform textarea[name="content_editor[text]"]'), url: res.url };
      }, c.sustituciones);
      if (r.faltan) throw new Error(`«${c.capitulo}»: el texto del aula ya no coincide en: ${r.faltan.join(' | ')}`);
      if (!r.ok) throw new Error(`«${c.capitulo}»: Moodle no guardó el capítulo`);
      console.log(`Corregido: «${c.capitulo}» (${c.sustituciones.length} cambios)`);
    }
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
