// Dentro de cada unidad formativa, mete cada tema en una subsección plegable: «TEMA N · título», con su
// cabecera (etiqueta «TEMA N») y sus cuatro actividades. Acordado con Mario el 15/10/2026.
//
//   node tools/aula/subsecciones_uf.js --courseid=4 [--aplicar]
//
// Requiere el curso organizado por UF (reorganizar_uf.js). Mismos ids de actividad. Se puede repetir.
const { abrir } = require('./sesion');
const A = require('./acciones');

const args = Object.fromEntries(process.argv.slice(2).map(a => { const [k, v = true] = a.replace(/^--/, '').split('='); return [k, v]; }));
const courseid = Number(args.courseid);
const num = s => Number(s.number ?? s.section);
const ufs = secciones => secciones.filter(s => !s.component && /^UF\d/.test(s.title ?? s.name ?? ''));

(async () => {
  const { browser, page } = await abrir();
  try {
    let { secciones, actividades } = await A.estado(page, courseid);
    for (const uf of ufs(secciones)) {
      // Cada tema empieza en su etiqueta «TEMA N» y acaba antes de la siguiente.
      const cms = (uf.cmlist || []).map(id => actividades.find(a => String(a.id) === String(id))).filter(Boolean);
      const temas = [];
      for (const cm of cms) {
        const m = cm.module === 'label' && cm.name.match(/^TEMA (\d+)$/);
        if (m) temas.push({ n: Number(m[1]), cms: [cm] });
        else if (cm.module !== 'subsection' && temas.length) temas[temas.length - 1].cms.push(cm);
      }
      console.log(`${uf.title ?? uf.name}: ${temas.length} temas por agrupar`);
      for (const t of temas) {
        const scorm = t.cms.find(c => c.module === 'scorm');
        const nombre = `TEMA ${t.n}${scorm ? " · " + scorm.name.replace(/^Tema \d+ · /, "") : ""}`;
        console.log(`  ${nombre}: ${t.cms.length} elementos`);
        if (!args.aplicar) continue;
        ({ secciones, actividades } = await A.estado(page, courseid));
        let sub = secciones.find(s => s.component === 'mod_subsection' && (s.title ?? s.name) === nombre);
        if (!sub) {
          const ufAhora = secciones.find(s => String(s.id) === String(uf.id));
          const cmid = await A.crearActividad(page, { courseid, seccion: num(ufAhora), modulo: 'subsection', nombre, valores: {} });
          ({ secciones, actividades } = await A.estado(page, courseid));
          sub = secciones.find(s => s.component === 'mod_subsection' && (s.title ?? s.name) === nombre);
          if (!sub) throw new Error(`No encuentro la subsección «${nombre}» tras crearla.`);
        }
        // Recién creada, la subsección puede tardar un momento en aceptar actividades: se reintenta.
        for (const cm of t.cms) {
          for (let intento = 1; ; intento++) {
            try {
              await A.ajax(page, 'core_courseformat_update_course', { action: 'cm_move', courseid, ids: [Number(cm.id)], targetsectionid: Number(sub.id) });
              break;
            } catch (e) {
              if (intento >= 4) throw e;
              await page.waitForTimeout(2000);
              await page.reload();
            }
          }
        }
      }
    }
    if (args.aplicar) {
      // Las subsecciones se crean ocultas: se muestran al final, ya con su contenido.
      ({ secciones, actividades } = await A.estado(page, courseid));
      const ocultas = actividades.filter(a => a.module === 'subsection' && !a.visible).map(a => Number(a.id));
      for (const id of ocultas) {
        for (let intento = 1; ; intento++) {
          try { await A.ajax(page, 'core_courseformat_update_course', { action: 'cm_show', courseid, ids: [id] }); break; }
          catch (e) { if (intento >= 3) { console.log(`  no pude mostrar la subsección ${id}: ${e.message.slice(0, 120)}`); break; } await page.waitForTimeout(2000); await page.reload(); }
        }
      }
      ({ secciones, actividades } = await A.estado(page, courseid));
      for (const s of secciones) {
        const n = (s.cmlist || []).length;
        console.log(`${s.component ? '    ↳' : num(s) + ' ·'} ${s.title ?? s.name} · visible=${s.visible} · ${n} elementos`);
      }
    } else console.log('(sin --aplicar: no se ha cambiado nada)');
  } finally { await browser.close(); }
})().catch(e => { console.error('ERROR:', e.message); process.exit(1); });
