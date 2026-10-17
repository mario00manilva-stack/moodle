"""MF2518_2 · UF2 · Tema 17 — presentación SCORM. Texto base: redacción de Mario (17/10/2026).

Correcciones (ADR 2025):
- El documento que se lleva a bordo es la «carta de porte» (documento de transporte, ADR 5.4.1), no
  «carta de pago».
- Exención 1.1.3.6: la suma de cantidades por el factor de su categoría de transporte (categoría 2 × 3,
  categoría 3 × 1) no supera 1 000. El hipoclorito UN 1791 es clase 8: categoría 2 (grupo II) o 3 (grupo
  III) según el producto. Con la exención: carta de porte, extintor de polvo de 2 kg, bultos homologados y
  etiquetados; sin paneles naranja ni certificado ADR del conductor.
- Cantidades limitadas (LQ, capítulo 3.4): envases interiores pequeños (en clase 8, 1 L en grupo II y 5 L
  en grupo III) en bultos de hasta 30 kg brutos; marca en rombo con los vértices superior e inferior negros.
- Panel naranja del hipoclorito: 80 / 1791. Dosis y diluciones: según el fabricante.

    python3 -I temario/1697/tema17/presentacion.py   ->  entregas/MF2518_2-UF2-T17-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2518_2 · UF2 · Tema 17", ident="MF2518_2_UF2_T17",
            title="Preparación de disoluciones, trasvase seguro de biocidas y transporte por carretera (ADR) con sus exenciones",
            item_title="Tema 17 - Disoluciones, trasvase y transporte ADR")

deck.add(
    portada("MF2518_2 · UF2 · Tema 17",
            "Disoluciones, trasvase y transporte ADR",
            "Cómo se diluye un producto sin que salte a la cara, cómo se trasvasa sin cargar garrafas a pulso y qué exige el ADR para llevar productos en la furgoneta.",
            "8 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · ADR · RD 97/2014",
            notes="Primer tema de la UF2 del módulo MF2518_2."),
    ficha("8 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el taller y la zona de carga del centro.",
          "Preparar disoluciones con seguridad, trasvasar con bombas o embudos adecuados e identificar lo que exige el ADR "
          "para transportar productos peligrosos por carretera, incluidas las exenciones 1.1.3.6 y de cantidades limitadas."),
    alerta("Regla de oro", "El ácido sobre el agua, nunca el agua sobre el ácido",
           "Para diluir un producto concentrado, sobre todo un ácido, se pone primero el agua y se vierte encima el producto, despacio. Si se echa agua sobre el ácido concentrado, la reacción desprende calor de golpe y proyecta líquido corrosivo hirviendo hacia la cara y el cuerpo.",
           [("Primero", "Agua en el recipiente."),
            ("Después", "El producto, despacio."),
            ("Un producto", "Nunca mezclar dos."),
            ("EPI puesto", "Antes de abrir.")]),
    pasos("Preparar una disolución", "1 · Preparación", "Paso a paso", [
        ("Calcular", "Cantidad de producto según el fabricante y el volumen."),
        ("EPI", "El de la sección 8 de la FDS."),
        ("Agua primero", "Recipiente con el agua limpia."),
        ("Producto encima", "Despacio, removiendo con utensilio de plástico."),
        ("Etiquetar", "Producto, dilución, fecha y quién la preparó."),
        ("Registrar", "Cantidad usada y lote."),
    ]),
    tarjetas("Trasvase", "A · Trasvase seguro", "Sin cargar garrafas a pulso", [
        ("Bombas de trasvase", "Manuales o eléctricas, de polipropileno o PVDF, resistentes a corrosivos. Evitan volcar garrafas de 25–30 kg."),
        ("Embudos de seguridad", "Con tapa, aireación y control de llenado: no salpican ni generan sobrepresión."),
        ("Recipiente de destino", "Compatible, etiquetado y de uso exclusivo para ese producto."),
    ], cols=3, footer="Un trasvase a pulso suma dos riesgos: **salpicadura** y **lesión de espalda**."),
    tarjetas("ADR", "2 · El ADR", "Llevar productos de piscina por la vía pública", [
        ("Qué es", "El acuerdo europeo para el transporte de mercancías peligrosas por carretera; en España, junto con el RD 97/2014."),
        ("A quién afecta", "A llevar hipocloritos, ácidos y otros productos peligrosos del almacén a las piscinas."),
        ("Clave", "Cada producto tiene un número ONU, una clase y un grupo de embalaje. El hipoclorito en solución es el UN 1791, clase 8."),
    ], cols=3),
    tabla("Modalidades", "A · Exenciones y requisitos", "Cuánto se lleva y qué exige",
          ["Modalidad", "Condición", "Qué hace falta"], [
              ("Exención 1.1.3.6", "Cantidades × factor de su categoría ≤ 1 000 «puntos»", "Carta de porte, extintor de polvo de 2 kg, bultos homologados y etiquetados. Sin paneles naranja."),
              ("Cantidades limitadas (LQ)", "Envases interiores pequeños en bultos de hasta 30 kg", "Bulto con la marca LQ (rombo con vértices negros). Sin paneles."),
              ("ADR completo", "Por encima de la exención", "Conductor con certificado ADR, vehículo equipado y paneles naranja delante y detrás."),
          ], nota="Factor de la categoría de transporte: categoría 2 × 3 · categoría 3 × 1. Los límites exactos de cada producto, en su FDS (sección 14) y en el ADR."),
    tarjetas("Ejemplo", "B · Calcular la exención 1.1.3.6", "La carga de una mañana", [
        ("Hipoclorito", "8 garrafas de 25 L = 200 L. Si es categoría 3: 200 × 1 = 200 puntos."),
        ("Reductor de pH", "4 garrafas de 25 L = 100 L de un corrosivo de categoría 2: 100 × 3 = 300 puntos."),
        ("Total", "500 puntos ≤ 1 000: se puede ir con la exención, con carta de porte y extintor."),
    ], cols=3),
    apoyo_visual("Señalización ADR", [
        ("17.1 · Panel naranja", "Imagen 17.1 · Furgoneta con panel naranja 80 / 1791 (hipoclorito en solución)"),
        ("17.2 · Marca LQ", "Imagen 17.2 · Caja con la marca de cantidad limitada: rombo con los vértices negros"),
        ("17.3 · Bomba de trasvase", "Imagen 17.3 · Bomba manual de trasvase sobre garrafa de 25 L"),
    ], label="Imágenes · ADR y trasvase"),
    alerta("Alerta de seguridad · PRL", "Estiba de garrafas en el vehículo",
           "Los envases viajan de pie, con los tapones bien cerrados, sobre bandeja y sujetos con cinchas de trinquete. Los incompatibles, separados. Nunca en la cabina con el conductor.",
           [("Vertical", "Tapón arriba y cerrado."),
            ("Amarrado", "Cinchas de trinquete."),
            ("Separados", "Ácidos lejos de cloros."),
            ("Fuera de la cabina", "Siempre.")]),
    normativa("A bordo del vehículo", [
        ("Carta de porte", "Número ONU, designación oficial, clase, grupo de embalaje y cantidad de cada producto. Obligatoria también con la exención 1.1.3.6."),
        ("Extintor", "Al menos uno de polvo de 2 kg."),
        ("FDS y emergencias", "Fichas de seguridad, absorbente y agua para lavado de ojos."),
    ], destacado=("80 / 1791", "Panel naranja del hipoclorito en solución: 80 es «corrosivo» y 1791, el número ONU.")),
    preguntas([
        "¿Cuál es la regla de oro para diluir un ácido?",
        "¿Qué producto es el número ONU 1791?",
        "¿Qué extintor exige la exención 1.1.3.6?",
    ]),
    respuestas([
        ("B", "Verter el ácido despacio sobre el agua, nunca al revés."),
        ("B", "Hipoclorito en solución."),
        ("B", "Al menos un extintor de polvo de 2 kg."),
    ]),
    taller("5.3", "Trasvase seguro y señalización ADR", "4 horas · taller y zona de carga", [
        "Bombas de trasvase manual y eléctrica",
        "Garrafas homologadas y paneles naranja de prácticas",
        "EPI: guantes químicos, gafas o pantalla y delantal",
    ], [
        "Preparar una dilución vertiendo el producto sobre el agua",
        "Trasvasar con bomba a un depósito de dosificación",
        "Calcular los puntos de una carga según el 1.1.3.6",
        "Cumplimentar la carta de porte de la ruta",
    ]),
    cierre("Tema 17", [
        ("Ácido sobre agua", "Nunca al revés."),
        ("Bomba de trasvase", "Sin garrafas a pulso."),
        ("1 000 puntos", "Límite de la exención 1.1.3.6."),
        ("Carta de porte", "Y extintor de 2 kg, siempre."),
    ], "Siguiente · Tema 18 · Gestión de residuos"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2518_2-UF2-T17-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T17")
    print(deck.build(out, html_preview=preview))
