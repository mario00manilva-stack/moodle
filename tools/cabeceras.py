"""Cabeceras ilustradas de los módulos (diseño propio de VERAQUA, sin fotos de terceros).

Genera, por módulo, un HTML con la cabecera para la página del curso (1600×450) y la imagen de la
tarjeta del curso (1200×675). Se rasterizan a PNG con Playwright (tools/aula/cabeceras_png.js).

    python3 -I tools/cabeceras.py   ->  entregas/cabeceras/<modulo>-{cabecera,tarjeta}.html
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "entregas", "cabeceras")
NAVY, INK, CYAN, MINT, AMBER, PAPER = "#0B1F3A", "#07131F", "#00C2CB", "#4ECFA0", "#E8A838", "#F4F7F8"

PISCINA = f"""
<svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg">
  <rect x="40" y="110" width="560" height="210" rx="18" fill="#0E2E4A" stroke="{CYAN}" stroke-width="4"/>
  <rect x="58" y="128" width="524" height="174" rx="10" fill="#0F4C6B"/>
  <g stroke="{CYAN}" stroke-width="3" stroke-dasharray="14 10" opacity=".55">
    <line x1="58" y1="171" x2="582" y2="171"/><line x1="58" y1="214" x2="582" y2="214"/><line x1="58" y1="257" x2="582" y2="257"/>
  </g>
  <g fill="none" stroke="{MINT}" stroke-width="4" stroke-linecap="round" opacity=".9">
    <path d="M78 150 q20 -12 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0"/>
    <path d="M78 236 q20 -12 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0" opacity=".5"/>
  </g>
  <g fill="none" stroke="{PAPER}" stroke-width="7" stroke-linecap="round">
    <path d="M536 70 v120"/><path d="M572 70 v120"/><path d="M536 70 q18 -26 36 0"/>
    <line x1="536" y1="140" x2="572" y2="140"/><line x1="536" y1="170" x2="572" y2="170"/>
  </g>
  <g transform="translate(92 36)">
    <rect x="0" y="0" width="34" height="96" rx="8" fill="{PAPER}"/><rect x="5" y="44" width="24" height="46" rx="5" fill="{CYAN}"/>
    <rect x="48" y="14" width="34" height="82" rx="8" fill="{PAPER}"/><rect x="53" y="52" width="24" height="38" rx="5" fill="{MINT}"/>
    <text x="17" y="30" font-family="DM Mono, monospace" font-size="14" text-anchor="middle" fill="{NAVY}">pH</text>
    <text x="65" y="40" font-family="DM Mono, monospace" font-size="14" text-anchor="middle" fill="{NAVY}">Cl</text>
  </g>
  <path d="M330 22 c22 30 36 50 36 70 a36 36 0 0 1 -72 0 c0 -20 14 -40 36 -70z" fill="{CYAN}"/>
  <path d="M318 96 a14 14 0 0 0 14 14" stroke="{PAPER}" stroke-width="5" fill="none" stroke-linecap="round"/>
</svg>"""

MATERIALES = f"""
<svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg">
  <rect x="40" y="300" width="560" height="22" rx="6" fill="#1B3348"/>
  <g>
    <path d="M80 130 h120 a14 14 0 0 1 14 14 v156 h-148 v-156 a14 14 0 0 1 14 -14z" fill="#E9EEF1"/>
    <rect x="150" y="110" width="40" height="24" rx="5" fill="{CYAN}"/><rect x="92" y="112" width="44" height="14" rx="7" fill="none" stroke="#9FB3C0" stroke-width="6"/>
    <rect x="86" y="190" width="108" height="70" rx="6" fill="#FFFFFF" stroke="#C8D4DC" stroke-width="2"/>
  </g>
  <g>
    <path d="M250 160 h96 a12 12 0 0 1 12 12 v128 h-120 v-128 a12 12 0 0 1 12 -12z" fill="#DDE6EB"/>
    <rect x="306" y="142" width="34" height="22" rx="5" fill="{AMBER}"/>
    <rect x="252" y="206" width="96" height="60" rx="6" fill="#FFFFFF" stroke="#C8D4DC" stroke-width="2"/>
  </g>
  <g transform="translate(140 225) rotate(45)"><rect x="-20" y="-20" width="40" height="40" fill="#FFFFFF" stroke="#D93A3A" stroke-width="6"/></g>
  <text x="140" y="233" font-family="Arial, sans-serif" font-weight="700" font-size="22" text-anchor="middle" fill="{NAVY}">!</text>
  <g transform="translate(300 236) rotate(45)"><rect x="-18" y="-18" width="36" height="36" fill="#FFFFFF" stroke="#D93A3A" stroke-width="5"/></g>
  <path d="M290 240 q10 -14 20 0" stroke="{NAVY}" stroke-width="4" fill="none"/>
  <g transform="translate(400 150)">
    <path d="M0 0 h110 l-14 150 h-82z" fill="none" stroke="{PAPER}" stroke-width="6" stroke-linejoin="round"/>
    <path d="M10 70 h90 l-8 80 h-74z" fill="{CYAN}" opacity=".85"/>
    <g stroke="{PAPER}" stroke-width="3"><line x1="88" y1="30" x2="104" y2="30"/><line x1="88" y1="60" x2="104" y2="60"/><line x1="88" y1="90" x2="104" y2="90"/><line x1="88" y1="120" x2="104" y2="120"/></g>
  </g>
  <g transform="translate(452 36)" stroke="{MINT}" stroke-width="5" stroke-linejoin="round">
    <rect x="0" y="10" width="104" height="58" rx="8" fill="#123A3A"/>
    <path d="M104 26 h30 l22 24 v18 h-52z" fill="#123A3A"/>
    <path d="M112 32 h20 l12 14 h-32z" fill="{MINT}" opacity=".5" stroke="none"/>
    <circle cx="30" cy="74" r="12" fill="{INK}"/><circle cx="128" cy="74" r="12" fill="{INK}"/>
  </g>
</svg>"""

PRL = f"""
<svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg">
  <path d="M210 40 l130 46 v86 c0 82 -58 132 -130 160 c-72 -28 -130 -78 -130 -160 v-86z" fill="#0F4C6B" stroke="{CYAN}" stroke-width="6"/>
  <path d="M160 186 l38 38 l78 -86" fill="none" stroke="{MINT}" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
  <g transform="translate(380 70)">
    <path d="M20 110 a90 90 0 0 1 180 0z" fill="{AMBER}"/>
    <rect x="0" y="106" width="220" height="22" rx="11" fill="#C98A20"/>
    <rect x="100" y="24" width="20" height="86" rx="10" fill="#F2C063"/>
  </g>
  <g transform="translate(430 220)">
    <rect x="0" y="0" width="110" height="110" rx="18" fill="#FFFFFF"/>
    <rect x="42" y="18" width="26" height="74" rx="4" fill="#2E9D78"/><rect x="18" y="42" width="74" height="26" rx="4" fill="#2E9D78"/>
  </g>
  <g transform="translate(590 182)" fill="none" stroke="{PAPER}" stroke-width="6">
    <rect x="-60" y="0" width="44" height="34" rx="14"/><rect x="0" y="0" width="44" height="34" rx="14"/><path d="M-16 14 h16"/>
  </g>
</svg>"""

MODULOS = {
    "1701": ("SEA_C_006_4B · Módulo 1701", "Control de organismos nocivos en piscinas e instalaciones acuáticas",
             "Vaciado, limpieza, tratamiento del agua y mantenimiento de la instalación.", PISCINA),
    "1697": ("SEA_C_006_4B · Módulo 1697", "Preparación y traslado de materiales",
             "Productos, fichas de seguridad, dosificación, transporte y almacenamiento seguro.", MATERIALES),
    "1732": ("SEA_C_006_4B · Módulo 1732", "Nivel básico de prevención de riesgos laborales",
             "Riesgos del trabajo, protección, gestión de la prevención y primeros auxilios.", PRL),
}

HEAD = """<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800&family=DM+Sans:wght@400;500&family=DM+Mono:wght@500&display=swap" rel="stylesheet">
<style>html,body{margin:0}#c{position:relative;overflow:hidden;background:linear-gradient(160deg,#0B1F3A 0%,#07131F 100%);color:#F4F7F8;font-family:'DM Sans',system-ui,sans-serif}
.k{font-family:'DM Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:#00C2CB;margin:0}
h1{font-family:'Barlow Condensed',sans-serif;font-weight:800;text-transform:uppercase;line-height:.95;letter-spacing:-.01em;margin:0}
p.s{color:#B8C8D2;margin:0;line-height:1.4}.bar{height:4px;background:linear-gradient(90deg,#00C2CB,#4ECFA0)}</style></head><body>"""


def cabecera(kicker, titulo, sub, svg):
    return (HEAD + f"""<div id="c" style="width:1600px;height:450px;display:grid;grid-template-columns:1fr 640px;align-items:center">
<div style="padding:0 0 0 90px;display:flex;flex-direction:column;gap:18px">
<img src="logo-light.svg" style="width:210px" alt="">
<div class="bar" style="width:160px"></div>
<p class="k" style="font-size:22px">{kicker}</p>
<h1 style="font-size:{58 if len(titulo) > 50 else 66}px;max-width:860px">{titulo}</h1>
<p class="s" style="font-size:24px;max-width:780px">{sub}</p></div>
<div style="height:360px">{svg}</div></div></body></html>""")


def tarjeta(kicker, titulo, svg):
    return (HEAD + f"""<div id="c" style="width:1200px;height:675px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:18px">
<div style="width:720px;height:405px">{svg}</div>
<p class="k" style="font-size:24px">{kicker}</p>
<h1 style="font-size:44px;max-width:1000px;text-align:center">{titulo}</h1></div></body></html>""")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    logo = os.path.join(ROOT, "instantaneas", "plantilla-scorm", "ds", "assets", "logo-light.svg")
    with open(logo, "rb") as src, open(os.path.join(OUT, "logo-light.svg"), "wb") as dst:
        dst.write(src.read())
    for m, (k, t, s, svg) in MODULOS.items():
        open(os.path.join(OUT, f"{m}-cabecera.html"), "w", encoding="utf-8").write(cabecera(k, t, s, svg))
        open(os.path.join(OUT, f"{m}-tarjeta.html"), "w", encoding="utf-8").write(tarjeta(k, t, svg))
    print(OUT)
