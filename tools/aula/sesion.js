// Sesión de navegador en el aula con la cuenta de la herramienta.
// Credenciales: AULA_USER y AULA_PASS (o MOODLE_USER / MOODLE_PASSWORD). Nunca en el repositorio.
const { chromium } = require('playwright');

const URL = (process.env.MOODLE_URL || 'https://formacion.veraqua.es').replace(/\/$/, '');

async function abrir({ headless = true } = {}) {
  const user = process.env.AULA_USER || process.env.MOODLE_USER;
  const pass = process.env.AULA_PASS || process.env.MOODLE_PASSWORD;
  if (!user || !pass) throw new Error('Faltan AULA_USER/AULA_PASS');
  const browser = await chromium.launch({ headless });
  const context = await browser.newContext({ locale: 'es-ES', viewport: { width: 1400, height: 1000 } });
  const page = await context.newPage();
  await page.goto(`${URL}/login/index.php`);
  await page.fill('#username', user);
  await page.fill('#password', pass);
  await Promise.all([page.waitForLoadState('networkidle'), page.click('#loginbtn')]);
  if (page.url().includes('/login/')) {
    const err = await page.locator('.alert, #loginerrormessage').first().textContent().catch(() => '');
    await browser.close();
    throw new Error('No se pudo entrar: ' + (err || '').trim());
  }
  const sesskey = await page.evaluate(() => (window.M && M.cfg && M.cfg.sesskey) || null);
  return { browser, context, page, sesskey, URL };
}

module.exports = { abrir, URL };
