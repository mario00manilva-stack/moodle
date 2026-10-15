// Rasteriza las cabeceras de entregas/cabeceras/*.html a PNG (tools/cabeceras.py).
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const dir = path.resolve(__dirname, '..', '..', 'entregas', 'cabeceras');
(async () => {
  const b = await chromium.launch();
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
    const p = await b.newPage({ deviceScaleFactor: 1.5 });
    await p.goto('file://' + path.join(dir, f)); await p.waitForTimeout(1500);
    await p.locator('#c').screenshot({ path: path.join(dir, f.replace('.html', '.png')) });
    console.log(f.replace('.html', '.png'));
  }
  await b.close();
})();
