"""MF2518_2 · UF2 · Tema 18 — presentación SCORM. Texto base: redacción de Mario (17/10/2026).

Correcciones:
- SIGFITO es el sistema de envases agrarios (fitosanitarios): no se aplica a los productos de piscina. Los
  envases y residuos peligrosos se entregan a un gestor autorizado.
- Productos químicos desechados: el código lo asigna el gestor según el producto (por ejemplo, 16 05 07*,
  productos químicos inorgánicos desechados con sustancias peligrosas). Lodos: según su caracterización.
- Triple lavado: buena práctica para aprovechar el producto y reducir restos; el envase se sigue
  gestionando como indiquen el fabricante y el gestor.
- Ley 7/2022: residuos peligrosos almacenados como máximo 6 meses en la instalación del productor; archivo
  cronológico de los residuos. Vaciados y lavados de filtros: según la autorización de vertido.

    python3 -I temario/1697/tema18/presentacion.py   ->  entregas/MF2518_2-UF2-T18-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2518_2 · UF2 · Tema 18", ident="MF2518_2_UF2_T18",
            title="Gestión de residuos químicos, envases vacíos de biocidas y aguas residuales en instalaciones acuáticas",
            item_title="Tema 18 - Gestion de residuos")

deck.add(
    portada("MF2518_2 · UF2 · Tema 18",
            "Gestión de residuos",
            "Envases vacíos, productos caducados, absorbentes y lodos: cómo se clasifican, dónde se guardan y a quién se entregan.",
            "7 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · LEY 7/2022 · LISTA EUROPEA DE RESIDUOS",
            notes="Último tema del módulo MF2518_2."),
    ficha("7 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en la zona de residuos del centro.",
          "Clasificar, etiquetar, almacenar y entregar a gestor autorizado los residuos peligrosos del mantenimiento de piscinas, "
          "conforme a la Ley 7/2022 de residuos y suelos contaminados."),
    tarjetas("Residuos", "1 · Qué residuos genera una piscina", "Ni al contenedor ni al desagüe", [
        ("Envases vacíos", "Garrafas y sacos de biocidas, ácidos y otros productos."),
        ("Productos desechados", "Caducados, rechazados o sin identificar."),
        ("Absorbentes y trapos", "Contaminados con producto o con aceite de las bombas."),
        ("Lodos y aguas", "Del vaciado del vaso, del lavado de filtros o de la limpieza."),
    ], cols=2),
    tabla("Código LER", "A · La lista europea de residuos", "Cada residuo, con su código",
          ["Residuo", "Código LER", "Tipo"], [
              ("Envases con restos de sustancias peligrosas", "15 01 10*", "Peligroso"),
              ("Absorbentes y trapos contaminados", "15 02 02*", "Peligroso"),
              ("Productos químicos inorgánicos desechados (p. ej., ácidos, hipocloritos)", "16 05 07*", "Peligroso"),
              ("Lodos de decantación o del lavado de filtros", "Según su análisis", "Peligroso o no peligroso"),
          ], nota="El asterisco (*) marca los residuos peligrosos. El código definitivo lo confirma el gestor autorizado."),
    pasos("Triple lavado", "2 · Envases vacíos", "Aprovechar el producto y reducir restos", [
        ("Escurrir", "Vaciar la garrafa del todo en el depósito de preparación."),
        ("Agua", "Llenar con agua limpia una cuarta parte del envase."),
        ("Agitar", "Tapón puesto, agitar unos 30 segundos y verter al depósito."),
        ("Tres veces", "Repetir el enjuague tres veces seguidas."),
        ("Inutilizar", "Perforar el fondo para que nadie lo reutilice."),
        ("Zona de residuos", "Etiquetado, hasta su entrega al gestor."),
    ], notes="El triple lavado es una buena práctica. El envase se gestiona como indiquen el fabricante y el gestor autorizado."),
    tarjetas("Almacenamiento", "A · La zona de residuos", "Hasta que llegue el gestor", [
        ("Separada", "Lejos del producto en uso, con cubeto y protegida de la lluvia."),
        ("Etiquetada", "Código LER, descripción, pictogramas de peligro, fecha de inicio del almacenamiento y productor."),
        ("Plazo", "Los residuos peligrosos, como máximo **6 meses** antes de entregarlos (Ley 7/2022)."),
    ], cols=3),
    tarjetas("Aguas residuales", "B · Aguas del vaso y de los filtros", "Tampoco van a cualquier sitio", [
        ("Vaciado", "A la red de saneamiento o según la autorización de vertido, sin cloro residual (Tema 2)."),
        ("Lavado de filtros", "Por la línea de desagüe prevista; nunca al terreno ni a la pluvial sin autorización."),
        ("Derrames", "Se recogen con absorbente: el absorbente usado es un residuo peligroso."),
    ], cols=3),
    apoyo_visual("La zona de residuos", [
        ("18.1 · Etiqueta de residuo", "Imagen 18.1 · Etiqueta de residuo peligroso con código LER 15 01 10*, pictogramas y fecha"),
        ("18.2 · Zona de residuos", "Imagen 18.2 · Garrafas vacías perforadas y bidón de absorbentes usados en la zona de residuos"),
    ], label="Imágenes · residuos"),
    alerta("Alerta de seguridad · PRL", "Una garrafa de producto nunca vuelve a usarse",
           "Está prohibido reutilizar envases vacíos de biocidas o ácidos para agua de beber, bebidas o para trasvasar otros productos. Los restos que quedan en el plástico pueden provocar intoxicaciones graves.",
           [("Inutilizar", "Perforar el envase vacío."),
            ("Etiquetar", "Como residuo peligroso."),
            ("Separar", "En la zona de residuos."),
            ("Entregar", "Solo a gestor autorizado.")]),
    normativa("Ley 7/2022 de residuos", [
        ("Almacenamiento", "Residuos peligrosos en la instalación como máximo 6 meses."),
        ("Gestor autorizado", "La entrega se documenta con su documento de identificación."),
        ("Archivo cronológico", "El productor registra cantidades, códigos, fechas y destino de sus residuos."),
    ], destacado=("15 01 10*", "Envases con restos de sustancias peligrosas: residuo peligroso.")),
    preguntas([
        "¿Qué código LER corresponde a los envases vacíos de biocidas?",
        "¿En qué consiste el triple lavado?",
        "¿Cuánto tiempo se pueden guardar los residuos peligrosos antes de entregarlos?",
    ]),
    respuestas([
        ("B", "LER 15 01 10*, residuo peligroso."),
        ("B", "Enjuagar el envase tres veces con agua limpia y verter el agua al depósito de preparación."),
        ("B", "Como máximo 6 meses."),
    ]),
    taller("5.4", "Triple lavado y gestión de residuos", "3 horas · zona de residuos", [
        "Garrafas de simulación y etiquetas de residuo",
        "Bidón de recogida de absorbentes",
        "EPI: guantes químicos y gafas",
    ], [
        "Hacer el triple lavado e inutilizar las garrafas",
        "Cumplimentar y colocar las etiquetas de residuo peligroso",
        "Anotar una retirada en el archivo cronológico",
    ]),
    cierre("Tema 18", [
        ("Con asterisco", "Residuo peligroso: gestor autorizado."),
        ("Triple lavado", "Y envase inutilizado."),
        ("6 meses", "Máximo en la instalación."),
        ("Nunca reutilizar", "Una garrafa de producto."),
    ], "Fin del módulo MF2518_2 · Preparación y traslado de materiales"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2518_2-UF2-T18-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T18")
    print(deck.build(out, html_preview=preview))
