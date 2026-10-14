"""Generador de presentaciones SCORM 1.2 con el diseño de los temas de VERAQUA FORMACIÓN.

Reproduce la estructura del paquete del Tema 1 de MF2522_2 (deck-stage + envoltorio SCORM que da
el tema por completado al ver todas las diapositivas). El motor (deck-stage.js), los logotipos y la
cabecera se toman de la plantilla extraída del aula, que no se versiona: instantaneas/plantilla-scorm.

Uso desde el script de cada tema:
    deck = Deck(code="MF2522_2 · UF1 · Tema 3", ident="MF2522_2_UF1_T3", title="…")
    deck.add(portada(...), ficha(...), ...)
    deck.build("entregas/MF2522_2-UF1-T3-scorm.zip")
"""
import html
import os
import re
import unicodedata
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLA = os.path.join(ROOT, "instantaneas", "plantilla-scorm")

NAVY, INK, PAPER, MIST = "#0B1F3A", "#07131F", "#F4F7F8", "#EAF0F3"
CYAN, TEAL, MINT, AMBER = "#00C2CB", "#009199", "#4ECFA0", "#E8A838"
TEXT2, LINE, MUTED = "#3D5567", "#D8E2E8", "#6B8A9E"
MONO = "font-family:'DM Mono',monospace"
COND = "font-family:'Barlow Condensed',sans-serif;font-weight:800;text-transform:uppercase"
DARK_BG = f"background:linear-gradient(160deg,{NAVY} 0%,{INK} 100%);color:{PAPER}"


def e(text):
    """Escapa texto y permite **negrita** con el estilo de las diapositivas."""
    out = html.escape(text, quote=False)
    # Los títulos van en mayúsculas: «pH» se protege para que no salga «PH».
    out = re.sub(r"\bpH\b", '<span style="text-transform:none">pH</span>', out)
    return re.sub(r"\*\*(.+?)\*\*", r'<strong style="font-weight:700">\1</strong>', out)


def _section(label, notes, style, body, dark=False):
    base = ("height:100%;box-sizing:border-box;display:flex;flex-direction:column;"
            "font-family:'DM Sans',system-ui,sans-serif;overflow:hidden")
    look = f"{DARK_BG};position:relative;{style}" if dark else style
    return (f'<section data-label="{html.escape(label)}" data-speaker-notes="{html.escape(notes)}" '
            f'style="{base};{look}">\n{body}\n  </section>')


def _kicker(text, color=TEAL, dark=False):
    pos = ";position:relative" if dark else ""
    return (f'    <p style="{MONO};font-size:24px;letter-spacing:0.14em;text-transform:uppercase;'
            f'color:{color};margin:0{pos}">{e(text)}</p>')


def _h2(text, size=76, dark=False):
    pos = ";position:relative" if dark else ""
    return (f'    <h2 style="{COND};font-size:{size}px;line-height:0.95;letter-spacing:-0.02em;'
            f'margin:24px 0 0{pos}">{e(text)}</h2>')


def _card(title, text, top=None, dark=False, title_size=44):
    border = f"border-top:6px solid {top};" if top else ""
    if dark:
        box = f"background:{INK};border:1px solid #1B3348;{border}"
        tcol, xcol = PAPER, "#B8C8D2"
    else:
        box = f"background:#FFFFFF;border:1px solid {LINE};{border}"
        tcol, xcol = NAVY, TEXT2
    return (f'      <div style="{box}border-radius:12px;padding:40px;display:flex;flex-direction:column;gap:16px">'
            f'<span style="{COND};font-size:{title_size}px;line-height:1.05;color:{tcol}">{e(title)}</span>'
            f'<span style="font-size:30px;line-height:1.4;color:{xcol}">{e(text)}</span></div>')


def portada(code, title, subtitle, footer, notes=""):
    body = f"""    <img src="ds/assets/pattern/escudo-silueta.svg" alt="" style="position:absolute;right:-90px;top:80px;height:880px;opacity:0.05" />
    <img src="ds/assets/logo-light.svg" alt="VERAQUA FORMACIÓN" style="width:540px;height:auto;position:relative" />
    <div style="display:flex;flex-direction:column;gap:32px;position:relative">
      <div style="width:220px;height:3px;background:linear-gradient(90deg,{CYAN},{MINT})"></div>
      <p style="{MONO};font-size:28px;letter-spacing:0.14em;text-transform:uppercase;color:{CYAN};margin:0">{e(code)}</p>
      <h1 style="{COND};font-size:112px;line-height:0.92;letter-spacing:-0.03em;margin:0;max-width:1560px">{e(title)}</h1>
      <p style="font-size:38px;line-height:1.45;margin:0;color:#B8C8D2;max-width:1280px">{e(subtitle)}</p>
    </div>
    <p style="{MONO};font-size:26px;letter-spacing:0.1em;color:#8BA5B5;margin:0;position:relative">{e(footer)}</p>"""
    return _section("Portada", notes, "justify-content:space-between;padding:100px", body, dark=True)


def ficha(horas, modalidad, modalidad_txt, objetivo, notes=""):
    body = f"""{_kicker("Ficha técnica del tema")}
{_h2("Cómo se cursa este tema")}
    <div style="display:grid;grid-template-columns:1fr 1fr 1.4fr;gap:32px;margin-top:52px">
      <div style="background:#FFFFFF;border:1px solid {LINE};border-top:6px solid {CYAN};border-radius:12px;padding:44px;display:flex;flex-direction:column;gap:20px">
        <span style="{MONO};font-size:24px;letter-spacing:0.12em;text-transform:uppercase;color:{MUTED}">Dedicación</span>
        <span style="{MONO};font-size:96px;line-height:1;color:{NAVY}">{e(horas)}</span>
        <span style="font-size:30px;line-height:1.4;color:{TEXT2}">Lectura y trabajo individual en Moodle.</span>
      </div>
      <div style="background:#FFFFFF;border:1px solid {LINE};border-top:6px solid {MINT};border-radius:12px;padding:44px;display:flex;flex-direction:column;gap:20px">
        <span style="{MONO};font-size:24px;letter-spacing:0.12em;text-transform:uppercase;color:{MUTED}">Modalidad</span>
        <span style="{COND};font-size:52px;line-height:1">{e(modalidad)}</span>
        <span style="font-size:30px;line-height:1.4;color:{TEXT2}">{e(modalidad_txt)}</span>
      </div>
      <div style="background:{NAVY};border-radius:12px;padding:44px;display:flex;flex-direction:column;gap:20px">
        <span style="{MONO};font-size:24px;letter-spacing:0.12em;text-transform:uppercase;color:{CYAN}">Objetivo de aprendizaje</span>
        <span style="font-size:30px;line-height:1.45;color:{PAPER}">{e(objetivo)}</span>
      </div>
    </div>"""
    return _section("Ficha técnica", notes, f"padding:96px 100px 80px;background:{MIST};color:{NAVY}", body)


def tarjetas(label, kicker, title, cards, cols=2, intro=None, footer=None, notes="", light=False):
    """Diapositiva de contenido: título y rejilla de tarjetas (título, texto)."""
    bg = PAPER if light else MIST
    parts = [_kicker(kicker), _h2(title)]
    if intro:
        parts.append(f'    <p style="font-size:32px;line-height:1.45;margin:36px 0 0;color:{TEXT2};max-width:1600px">{e(intro)}</p>')
    tops = [CYAN, MINT]
    cells = "\n".join(_card(t, x, top=tops[i % 2] if cols > 2 else None, title_size=44 if cols < 4 else 38)
                      for i, (t, x) in enumerate(cards))
    parts.append(f'    <div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:28px;margin-top:44px">\n{cells}\n    </div>')
    if footer:
        parts.append(f'    <div style="margin-top:40px;background:#FFFFFF;border:1px solid {LINE};border-left:8px solid {AMBER};'
                     f'border-radius:12px;padding:36px 48px"><span style="font-size:32px;line-height:1.4;color:{NAVY}">{e(footer)}</span></div>')
    return _section(label, notes, f"padding:96px 100px 80px;background:{bg};color:{NAVY}", "\n".join(parts))


def pasos(label, kicker, title, rows, notes=""):
    """Lista numerada (número, título, texto)."""
    items = "\n".join(
        f'      <div style="background:#FFFFFF;border:1px solid {LINE};border-radius:8px;padding:22px 40px;display:grid;'
        f'grid-template-columns:80px 640px 1fr;gap:32px;align-items:center">'
        f'<span style="{MONO};font-size:32px;color:{CYAN}">{i:02d}</span>'
        f'<span style="{COND};font-size:42px">{e(t)}</span>'
        f'<span style="font-size:29px;line-height:1.4;color:{TEXT2}">{e(x)}</span></div>'
        for i, (t, x) in enumerate(rows, 1))
    body = f'{_kicker(kicker)}\n{_h2(title)}\n    <div style="display:flex;flex-direction:column;gap:12px;margin-top:40px">\n{items}\n    </div>'
    return _section(label, notes, f"padding:96px 100px 80px;background:{MIST};color:{NAVY}", body)


def alerta(kicker, title, text, cards, notes=""):
    cells = "\n".join(_card(t, x, top=AMBER, dark=True, title_size=40) for t, x in cards)
    body = f"""    <img src="ds/assets/pattern/escudo-silueta.svg" alt="" style="position:absolute;right:-140px;top:40px;height:900px;opacity:0.05" />
    <div style="position:relative">
      <p style="{MONO};font-size:26px;letter-spacing:0.14em;text-transform:uppercase;color:{AMBER};margin:0">{e(kicker)}</p>
      <h2 style="{COND};font-size:84px;line-height:0.95;letter-spacing:-0.02em;margin:24px 0 0;max-width:1560px">{e(title)}</h2>
    </div>
    <p style="font-size:34px;line-height:1.45;margin:0;color:{PAPER};max-width:1620px;position:relative">{e(text)}</p>
    <div style="display:grid;grid-template-columns:repeat({len(cards)},1fr);gap:24px;position:relative">
{cells}
    </div>"""
    return _section("Alerta PRL", notes, "justify-content:center;gap:44px;padding:90px 100px", body, dark=True)


def normativa(title, cards, destacado=None, notes=""):
    """Tarjetas (etiqueta, texto); la última va en oscuro. destacado = (cifra, texto)."""
    cells = []
    for i, (tag, text) in enumerate(cards):
        last = i == len(cards) - 1 and len(cards) > 1
        bg = f"background:{NAVY}" if last else f"background:#FFFFFF;border:1px solid {LINE}"
        cells.append(f'      <div style="{bg};border-radius:12px;padding:44px;display:flex;flex-direction:column;gap:18px">'
                     f'<span style="{MONO};font-size:28px;color:{CYAN if last else TEAL}">{e(tag)}</span>'
                     f'<span style="font-size:31px;line-height:1.45;color:{PAPER if last else TEXT2}">{e(text)}</span></div>')
    parts = [_kicker("Cumplimiento normativo"), _h2(title),
             f'    <div style="display:grid;grid-template-columns:repeat({len(cards)},1fr);gap:32px;margin-top:52px">\n'
             + "\n".join(cells) + "\n    </div>"]
    if destacado:
        parts.append(f'    <div style="margin-top:44px;background:#FFFFFF;border:1px solid {LINE};border-left:8px solid {AMBER};'
                     f'border-radius:12px;padding:44px 52px;display:flex;align-items:center;gap:40px">'
                     f'<span style="{MONO};font-size:52px;color:{NAVY};white-space:nowrap">{e(destacado[0])}</span>'
                     f'<span style="font-size:33px;line-height:1.4;color:{NAVY}">{e(destacado[1])}</span></div>')
    return _section("Cumplimiento normativo", notes, f"padding:96px 100px 80px;background:{PAPER};color:{NAVY}", "\n".join(parts))


def apoyo_visual(title, imagenes, label="Apoyo visual",
                 notes="Imágenes de apoyo para el aula virtual. Sustituir los huecos por fotos reales del taller."):
    cells = "\n".join(
        f'      <div style="display:flex;flex-direction:column;gap:20px;min-height:0">'
        f'<div style="flex:1;min-height:0;border:1px solid {LINE};border-radius:12px;overflow:hidden;background:#FFFFFF">'
        f'<div style="width:100%;height:100%;box-sizing:border-box;display:flex;align-items:center;justify-content:center;'
        f'padding:48px;background:{MIST};border:2px dashed #B8C8D2"><span style="{MONO};font-size:26px;line-height:1.5;'
        f'color:{MUTED};text-align:center;max-width:640px">{e(desc)}</span></div></div>'
        f'<span style="{MONO};font-size:26px;color:{TEXT2}">{e(cap)}</span></div>'
        for cap, desc in imagenes)
    body = (f'{_kicker("Apoyo visual · Moodle")}\n{_h2(title)}\n'
            f'    <div style="display:grid;grid-template-columns:repeat({len(imagenes)},1fr);gap:36px;margin-top:44px;flex:1;min-height:0">\n{cells}\n    </div>')
    return _section(label, notes, f"padding:96px 100px 80px;background:{MIST};color:{NAVY}", body)


def preguntas(qs, notes="Preguntas de autocomprobación. Dejar que el alumno responda antes de pasar a las respuestas razonadas."):
    items = "\n".join(
        f'      <div style="background:#FFFFFF;border:1px solid {LINE};border-radius:12px;padding:40px 48px;display:grid;'
        f'grid-template-columns:80px 1fr;gap:32px;align-items:start"><span style="{MONO};font-size:34px;color:{CYAN}">{i:02d}</span>'
        f'<span style="font-size:34px;line-height:1.4">{e(q)}</span></div>' for i, q in enumerate(qs, 1))
    n = {3: "Tres", 4: "Cuatro", 5: "Cinco"}.get(len(qs), str(len(qs)))
    body = f'{_kicker("Autocomprobación")}\n{_h2(f"{n} preguntas")}\n    <div style="display:flex;flex-direction:column;gap:28px;margin-top:52px">\n{items}\n    </div>'
    return _section("Autoevaluación", notes, f"padding:96px 100px 80px;background:{PAPER};color:{NAVY}", body)


def respuestas(rs, notes="Respuestas razonadas."):
    items = "\n".join(
        f'      <div style="background:#FFFFFF;border:1px solid {LINE};border-radius:12px;padding:36px 44px;display:grid;'
        f'grid-template-columns:120px 1fr;gap:36px;align-items:center"><span style="{MONO};font-size:32px;color:{NAVY};'
        f'background:{MINT};border-radius:8px;padding:12px 0;text-align:center">{i:02d} · {e(letra)}</span>'
        f'<span style="font-size:31px;line-height:1.4;color:{TEXT2}">{e(t)}</span></div>' for i, (letra, t) in enumerate(rs, 1))
    body = f'{_kicker("Autocomprobación")}\n{_h2("Respuestas razonadas")}\n    <div style="display:flex;flex-direction:column;gap:24px;margin-top:52px">\n{items}\n    </div>'
    return _section("Respuestas", notes, f"padding:96px 100px 80px;background:{MIST};color:{NAVY}", body)


def taller(numero, title, meta, equipamiento, tareas, notes="Ficha del taller presencial: equipamiento disponible y tareas del alumno."):
    eq = "\n".join(f'        <span style="font-size:28px;line-height:1.4;color:{PAPER}">{e(x)}</span>' for x in equipamiento)
    ta = "\n".join(
        f'        <div style="background:{INK};border:1px solid #1B3348;border-radius:8px;padding:14px 28px;display:grid;'
        f'grid-template-columns:64px 1fr;gap:24px;align-items:center"><span style="{MONO};font-size:26px;color:{CYAN}">{i}</span>'
        f'<span style="font-size:28px;line-height:1.35">{e(t)}</span></div>' for i, t in enumerate(tareas, 1))
    body = f"""    <img src="ds/assets/pattern/gota-silueta.svg" alt="" style="position:absolute;left:-80px;bottom:-120px;height:840px;opacity:0.05" />
{_kicker(f"Taller {numero} · Práctica presencial · {meta}", color=CYAN, dark=True)}
{_h2(title, dark=True)}
    <div style="display:grid;grid-template-columns:640px 1fr;gap:40px;margin-top:32px;position:relative">
      <div style="background:{INK};border:1px solid #1B3348;border-radius:12px;padding:36px;display:flex;flex-direction:column;gap:14px">
        <span style="{MONO};font-size:24px;letter-spacing:0.12em;text-transform:uppercase;color:#8BA5B5">Equipamiento</span>
{eq}
      </div>
      <div style="display:flex;flex-direction:column;gap:10px">
        <span style="{MONO};font-size:24px;letter-spacing:0.12em;text-transform:uppercase;color:#8BA5B5">Tareas del alumno</span>
{ta}
      </div>
    </div>"""
    return _section(f"Taller {numero}", notes, "padding:96px 100px 80px", body, dark=True)


def cierre(tema, ideas, siguiente, notes=""):
    tops = [CYAN, CYAN, MINT, MINT]
    cells = "\n".join(
        f'      <div style="background:#FFFFFF;border:1px solid {LINE};border-top:6px solid {tops[i % 4]};border-radius:12px;padding:40px;'
        f'display:flex;flex-direction:column;gap:16px"><span style="{MONO};font-size:26px;color:{TEAL}">{i + 1:02d}</span>'
        f'<span style="{COND};font-size:40px;line-height:1.05">{e(t)}</span>'
        f'<span style="font-size:28px;line-height:1.4;color:{TEXT2}">{e(x)}</span></div>' for i, (t, x) in enumerate(ideas))
    body = f"""    <div>
{_kicker("Para llevarte")}
{_h2(f"Cuatro ideas del {tema}", size=84)}
    </div>
    <div style="display:grid;grid-template-columns:repeat({len(ideas)},1fr);gap:28px">
{cells}
    </div>
    <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:60px">
      <p style="{MONO};font-size:28px;color:{MUTED};margin:0">{e(siguiente)}</p>
      <img src="ds/assets/logo-dark.svg" alt="VERAQUA FORMACIÓN" style="width:360px;height:auto" />
    </div>"""
    return _section("Cierre", notes, f"justify-content:space-between;padding:96px 100px 80px;background:{MIST};color:{NAVY}", body)


def _ascii(text):
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()


class Deck:
    def __init__(self, code, ident, title, item_title):
        self.code, self.ident, self.title, self.item_title = code, ident, title, item_title
        self.slides = []

    def add(self, *slides):
        self.slides.extend(slides)

    def html(self):
        head = open(os.path.join(PLANTILLA, "head-t1.html"), encoding="utf-8").read()
        head = re.sub(r"<title>.*?</title>", f"<title>{html.escape(self.code)} — {html.escape(self.title)}</title>", head)
        head = head.replace("MF2522_2 UF1 Tema 1", _ascii(self.code.replace(" · ", " ")))
        slides = []
        for i, s in enumerate(self.slides, 1):
            slides.append(s.replace("<section ", f'<section data-screen-label="{i:02d}" ', 1))
        return ('<!DOCTYPE html>\n<html lang="es">\n' + head + '\n<body>\n<deck-stage width="1920" height="1080">\n\n  '
                + "\n\n  ".join(slides) + "\n\n</deck-stage>\n</body>\n</html>\n")

    def manifest(self, files):
        res = "\n".join(f'      <file href="{f}"/>' for f in files)
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="VERAQUA_{self.ident}" version="1.2"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata><schema>ADL SCORM</schema><schemaversion>1.2</schemaversion></metadata>
  <organizations default="VERAQUA_ORG">
    <organization identifier="VERAQUA_ORG">
      <title>{html.escape(_ascii(self.code.replace(' · ', ' - ') + ' - ' + self.title))}</title>
      <item identifier="ITEM_{self.ident}" identifierref="RES_{self.ident}" isvisible="true">
        <title>{html.escape(_ascii(self.item_title))}</title>
        <adlcp:masteryscore>100</adlcp:masteryscore>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES_{self.ident}" type="webcontent" adlcp:scormtype="sco" href="index.html">
{res}
    </resource>
  </resources>
</manifest>
"""

    def build(self, zip_path, html_preview=None):
        assets = ["deck-stage.js", "ds/assets/logo-dark.svg", "ds/assets/logo-light.svg",
                  "ds/assets/pattern/escudo-silueta.svg", "ds/assets/pattern/gota-silueta.svg"]
        page = self.html()
        os.makedirs(os.path.dirname(os.path.abspath(zip_path)), exist_ok=True)
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("imsmanifest.xml", self.manifest(["index.html"] + assets))
            z.writestr("index.html", page)
            for a in assets:
                z.write(os.path.join(PLANTILLA, a), a)
        if html_preview:
            os.makedirs(html_preview, exist_ok=True)
            with zipfile.ZipFile(zip_path) as z:
                z.extractall(html_preview)
        return zip_path


def tabla(label, kicker, title, headers, rows, nota=None, notes=""):
    """Tabla de valores: cabeceras y filas de texto; la última columna se resalta en ámbar."""
    cols = "minmax(0,1.1fr) minmax(0,1.3fr) minmax(0,1fr)" if len(headers) == 3 else f"repeat({len(headers)},minmax(0,1fr))"
    head = "".join(f'<span style="{MONO};font-size:22px;letter-spacing:0.1em;text-transform:uppercase;color:{TEAL if i < len(headers) - 1 else AMBER}">{e(h)}</span>'
                   for i, h in enumerate(headers))
    body = []
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            if i == 0:
                cells.append(f'<span style="{COND};font-size:34px;line-height:1.1">{e(c)}</span>')
            elif i == len(r) - 1:
                cells.append(f'<span style="font-size:27px;line-height:1.3;color:{NAVY};font-weight:500">{e(c)}</span>')
            else:
                cells.append(f'<span style="font-size:27px;line-height:1.3;color:{TEXT2}">{e(c)}</span>')
        body.append(f'      <div style="background:#FFFFFF;border:1px solid {LINE};border-radius:8px;padding:14px 32px;display:grid;'
                    f'grid-template-columns:{cols};gap:32px;align-items:center">{"".join(cells)}</div>')
    parts = [_kicker(kicker), _h2(title),
             f'    <div style="display:grid;grid-template-columns:{cols};gap:32px;padding:28px 33px 8px">{head}</div>',
             '    <div style="display:flex;flex-direction:column;gap:8px">\n' + "\n".join(body) + "\n    </div>"]
    if nota:
        parts.append(f'    <p style="{MONO};font-size:22px;line-height:1.4;color:{MUTED};margin:20px 0 0">{e(nota)}</p>')
    return _section(label, notes, f"padding:84px 100px 60px;background:{MIST};color:{NAVY}", "\n".join(parts))
