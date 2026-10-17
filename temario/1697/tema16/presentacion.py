"""MF2518_2 · UF1 · Tema 16 — presentación SCORM. Texto base: redacción de Mario (17/10/2026).

Correcciones: protección ocular frente a salpicaduras químicas, UNE-EN 166 (la EN 170 es para filtros
ultravioleta). Filtros UNE-EN 14387: A orgánicos, B inorgánicos (incluido el cloro), E ácidos (SO₂, HCl),
K amoníaco. FDS en la lengua oficial (Reglamento REACH, art. 31). El EPI concreto: sección 8 de la FDS.

    python3 -I temario/1697/tema16/presentacion.py   ->  entregas/MF2518_2-UF1-T16-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2518_2 · UF1 · Tema 16", ident="MF2518_2_UF1_T16",
            title="Interpretación de fichas de datos de seguridad (REACH y CLP), pictogramas, frases H y P y equipos de protección individual",
            item_title="Tema 16 - Fichas de datos de seguridad y EPI")

deck.add(
    portada("MF2518_2 · UF1 · Tema 16",
            "Fichas de datos de seguridad y EPI",
            "Leer una FDS, entender los pictogramas y las frases H y P de la etiqueta, y elegir el EPI que pide cada producto.",
            "7 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · REACH · CLP · RD 773/1997",
            notes="Sigue al Tema 15: después de guardar bien el producto, hay que saber manejarlo."),
    ficha("7 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el taller de prevención.",
          "Interpretar las 16 secciones de la FDS según REACH y CLP, reconocer los pictogramas y las frases H y P, y "
          "seleccionar los EPI adecuados para cada producto químico."),
    tarjetas("La FDS", "1 · La ficha de datos de seguridad", "El documento que acompaña a cada producto", [
        ("Quién la da", "El proveedor está obligado a entregarla, en castellano y actualizada (Reglamento REACH)."),
        ("Dónde está", "Accesible donde se manipula el producto: en el almacén o la sala técnica."),
        ("Para qué", "Para saber los peligros, cómo manipular y guardar, qué EPI usar y qué hacer si algo sale mal."),
    ], cols=3),
    tabla("16 secciones", "A · Las 16 secciones", "Qué hay en cada una",
          ["Secciones", "Contenido"], [
              ("1 · 2 · 3", "Identificación del producto y del proveedor, peligros (clasificación CLP) y composición."),
              ("4 · 5 · 6", "Primeros auxilios, lucha contra incendios y qué hacer ante un vertido."),
              ("7 · 8", "Manipulación y almacenamiento; controles de exposición y EPI."),
              ("9 · 10 · 11", "Propiedades, estabilidad y reactividad (incompatibilidades), toxicología."),
              ("12 · 13 · 14", "Ecología, eliminación de residuos y transporte."),
              ("15 · 16", "Información reglamentaria y otra información."),
          ], nota="Las que más usarás en el día a día: 2 (peligros), 4 (primeros auxilios), 6 (vertidos), 7 (manipulación), 8 (EPI) y 10 (incompatibilidades)."),
    tarjetas("Pictogramas", "B · Pictogramas CLP", "Rombo de borde rojo y fondo blanco", [
        ("Corrosión", "Quema piel y ojos. Hipocloritos, ácidos y bases."),
        ("Comburente", "Llama sobre un círculo: aviva el fuego. Cloro sólido."),
        ("Toxicidad aguda", "Calavera: daño grave por ingestión, contacto o inhalación."),
        ("Medio ambiente", "Árbol y pez: tóxico para la vida acuática. No al desagüe."),
    ], cols=2, footer="La palabra de advertencia indica la gravedad: **«Peligro»** es más grave que **«Atención»**."),
    tarjetas("Frases H y P", "C · Frases H y P", "Peligro y precaución, en código", [
        ("Frases H", "Describen el peligro. H314: provoca quemaduras graves en la piel y lesiones oculares graves."),
        ("Frases P", "Consejos de prudencia. P280: llevar guantes, prendas, gafas o máscara de protección."),
        ("En la etiqueta", "Pictogramas, palabra de advertencia, frases H y P, proveedor, cantidad y, en los biocidas, número de registro."),
    ], cols=3),
    apoyo_visual("Etiqueta y FDS", [
        ("16.1 · Etiqueta CLP", "Imagen 16.1 · Etiqueta de un reductor de pH con pictograma de corrosión, palabra «Peligro» y frases H314 y P280"),
        ("16.2 · Sección 8 de la FDS", "Imagen 16.2 · Sección 8 de una FDS con el tipo de guante, gafas y filtro respiratorio"),
    ], label="Imágenes · etiquetado"),
    tabla("EPI", "2 · Elegir el EPI", "Lo que pide la sección 8, con su norma",
          ["Protección", "Norma", "Uso en piscinas"], [
              ("Respiratoria", "UNE-EN 14387 (filtros)", "Filtros B (cloro y gases inorgánicos), E (ácidos), K (amoníaco) o combinados ABEK."),
              ("Ojos y cara", "UNE-EN 166", "Gafas de montura integral o pantalla facial contra salpicaduras."),
              ("Manos", "UNE-EN ISO 374-1", "Guantes químicos (nitrilo, neopreno, PVC) del material que indique la FDS."),
              ("Cuerpo", "UNE-EN 13034 / UNE-EN 14605", "Delantal o traje contra salpicaduras o líquidos."),
          ], nota="El guante no es genérico: el material y el espesor dependen del producto. Mira siempre la sección 8."),
    pasos("Antes de abrir", "A · Antes de abrir un envase", "Paso a paso", [
        ("Etiqueta", "Pictogramas, palabra de advertencia y frases H."),
        ("FDS sección 8", "Qué guante, qué gafas y qué filtro."),
        ("Revisar el EPI", "Guante sin poros, filtro en fecha, gafas limpias."),
        ("Ponérselo", "Antes de abrir, no a mitad de la tarea."),
        ("Ajuste", "Comprobar el ajuste de la máscara (presión positiva y negativa)."),
        ("Después", "Quitarse el EPI sin contaminarse y lavarse las manos."),
    ]),
    alerta("Alerta de seguridad · PRL", "La sección 8 antes del trasvase",
           "Antes de abrir o trasvasar cualquier producto de la piscina, consulta la sección 8 de su FDS y ponte exactamente el guante, las gafas y el filtro que indica. El EPI «de siempre» del almacén puede no servir para ese producto.",
           [("Sección 8", "EPI del producto concreto."),
            ("Guante", "Material y espesor."),
            ("Filtro", "Tipo y caducidad."),
            ("Gafas", "Montura integral.")]),
    normativa("Obligaciones", [
        ("Ley 31/1995 · art. 17", "La empresa proporciona los EPI adecuados, con marcado CE, y vela por su uso."),
        ("Ley 31/1995 · art. 29", "El trabajador los usa correctamente según la formación recibida."),
        ("RD 773/1997", "Uso de los EPI en el trabajo. Reglamento REACH: FDS en castellano."),
    ], destacado=("Sección 8", "Controles de exposición y protección individual: el EPI de cada producto.")),
    preguntas([
        "¿En qué sección de la FDS están los EPI necesarios?",
        "¿Qué significa la frase H314?",
        "¿Qué norma cumplen los guantes de protección química?",
    ]),
    respuestas([
        ("B", "En la sección 8, controles de exposición y protección individual."),
        ("B", "Provoca quemaduras graves en la piel y lesiones oculares graves."),
        ("B", "UNE-EN ISO 374."),
    ]),
    taller("5.2", "Lectura de FDS y selección de EPI", "3 horas · taller de prevención", [
        "FDS de un hipoclorito, un ácido clorhídrico y un floculante",
        "Kit de EPI: gafas, guantes y máscaras con distintos filtros",
    ], [
        "Interpretar tres FDS: pictogramas, frases H y P y EPI",
        "Elegir el filtro y el guante adecuados para cada producto",
        "Hacer la comprobación de ajuste de una máscara",
    ]),
    cierre("Tema 16", [
        ("16 secciones", "Y las clave: 2, 4, 6, 7, 8 y 10."),
        ("Rombo rojo", "Pictograma de peligro; «Peligro» > «Atención»."),
        ("H y P", "Peligro y precaución."),
        ("Sección 8", "El EPI exacto de cada producto."),
    ], "Siguiente · UF2 · Tema 17 · Preparación, trasvase y transporte ADR"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2518_2-UF1-T16-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T16")
    print(deck.build(out, html_preview=preview))
