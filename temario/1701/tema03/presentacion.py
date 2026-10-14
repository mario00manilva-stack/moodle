"""MF2522_2 · UF1 · Tema 3 — presentación SCORM. Texto base: redacción de Mario (14/10/2026).

Normativa: RD 742/2013 (estatal), Decreto 485/2019 (Reglamento Técnico-Sanitario de las Piscinas en
Andalucía, art. 11 DDD y biocidas) y CTE DB-SUA 6 (andenes y escaleras). Antialgas: según fabricante.

    python3 -I temario/1701/tema03/presentacion.py   ->  entregas/MF2522_2-UF1-T3-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF1 · Tema 3", ident="MF2522_2_UF1_T3",
            title="Técnicas de limpieza, desincrustado e higienización de revestimientos, paramentos y elementos complementarios",
            item_title="Tema 3 - Limpieza, desincrustado e higienizacion")

deck.add(
    portada("MF2522_2 · UF1 · Tema 3",
            "Limpieza, desincrustado e higienización del vaso y sus anexos",
            "Revestimientos, paramentos y elementos complementarios: el vaso vacío se deja limpio, sano y listo para el llenado.",
            "8 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019",
            notes="Tema 3 de la UF1. Continúa donde terminó el Tema 2: el vaso ya está vacío."),
    ficha("8 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el vaso didáctico.",
          "Seleccionar y aplicar detergentes, desincrustantes y biocidas; usar la maquinaria y los útiles de limpieza; "
          "higienizar el vaso, playas, escaleras, duchas y rejillas, y aplicar el antialgas preventivo con las medidas de PRL."),
    tarjetas("Limpiar y desinfectar", "Punto de partida", "Tras el vaciado: qué hay en las paredes", [
        ("Biofilm", "Película de microorganismos adherida a paredes y solera."),
        ("Incrustación calcárea", "Sarro y carbonatos fijados al revestimiento."),
        ("Suciedad orgánica", "Grasas, cremas y restos en la línea de flotación."),
        ("Moho y algas", "Manchas en juntas, esquinas y zonas de sombra."),
    ], cols=4, intro="El objetivo es eliminarlo sin dañar el revestimiento: gresite, liner, lámina armada o poliéster.",
        footer="**Limpiar** es retirar la suciedad (acción física y química). **Desinfectar** es eliminar los microorganismos patógenos. Son dos operaciones distintas y van en ese orden.",
        light=True),
    apoyo_visual("El vaso antes de limpiar", [
        ("3.1 · Vaso vacío antes de la limpieza", "Imagen 3.1 · Paredes del vaso vacío con biofilm, cal y franja de suciedad en la línea de flotación"),
        ("3.2 · Tipos de revestimiento", "Imagen 3.2 · Muestras de gresite, liner, lámina armada y poliéster"),
    ], label="Imágenes · el vaso"),
    tarjetas("Clasificación de productos", "Química de la limpieza", "Cuatro familias de productos", [
        ("1 · Desincrustantes ácidos", "Eliminan los depósitos calcáreos y el sarro acumulado."),
        ("2 · Detergentes alcalinos", "Disuelven grasas, cremas y biofilm."),
        ("3 · Limpiadores clorados", "Blanqueante para el moho de las juntas del gresite y las baldosas."),
        ("4 · Antialgas de superficie", "Impregnación preventiva antes del llenado del vaso."),
    ], cols=2),
    tarjetas("Desincrustantes ácidos", "A · Limpiadores y desincrustantes ácidos", "Contra la cal: ácido, pero con cabeza", [
        ("Función", "Reaccionan con los carbonatos cálcicos insolubles fijados a las paredes del vaso."),
        ("Producto", "Antes, salfumán (ácido clorhídrico comercial). Hoy se recomiendan desincrustantes específicos para piscinas, con tensioactivos e inhibidores de corrosión que protegen juntas y tuberías."),
    ], cols=2, footer="**Siempre sobre superficie mojada.** Humedecer antes con agua limpia evita que el ácido penetre en el rejuntado: actúa solo sobre la cal superficial."),
    tarjetas("Alcalinos y antialgas", "B y C · Detergentes alcalinos y antialgas preventivo", "La línea de flotación y la última capa", [
        ("Detergentes alcalinos", "Eliminan la franja de grasa de la línea de flotación (aceites solares, sudor, secreciones). Con esponja o cepillo no abrasivo: dejar actuar unos minutos, frotar y aclarar."),
        ("Antialgas de superficie", "Con el vaso limpio y aclarado, se pulveriza o se aplica con rodillo sobre paredes y fondo, con la dosis y el modo de aplicación que indique el fabricante, para que el biocida se fije en los poros del revestimiento."),
    ], cols=2, footer="**Reposo antes del llenado: el que indique el fabricante** en la etiqueta o la ficha técnica. Durante ese plazo de seguridad nadie accede al vaso tratado (Decreto 485/2019, art. 11)."),
    tarjetas("Maquinaria y útiles", "Maquinaria y útiles", "Química más fuerza mecánica", [
        ("Hidrolimpiadora", "Agua a 100–150 bar para esquinas, rincones y juntas. Lanza a 45° de la superficie: en perpendicular salta el gresite y el rejuntado."),
        ("Cepillos y rasquetas", "Cerdas duras para frotar las incrustaciones rebeldes. Nunca púas metálicas sobre liner."),
        ("Limpiafondos", "Durante el llenado, con 30–40 cm de agua, se pasa el limpiafondos para retirar los finos depositados en la solera."),
    ], cols=3),
    apoyo_visual("La maquinaria en uso", [
        ("3.3 · Desincrustado con EPI", "Imagen 3.3 · Operario con traje impermeable, pantalla facial y guantes químicos frotando el gresite con cepillo de cerdas duras"),
        ("3.4 · Hidrolimpiadora a 45°", "Imagen 3.4 · Aclarado del paramento con hidrolimpiadora, lanza a 45° de la superficie"),
        ("3.5 · Limpiafondos en el llenado", "Imagen 3.5 · Limpiafondos sobre la solera con 30–40 cm de agua"),
    ], label="Imágenes · maquinaria"),
    pasos("Aclarado y residuos", "Procedimiento", "Del rascado al vaso listo", [
        ("Mojar", "Humedecer paramentos con agua limpia."),
        ("Aplicar y frotar", "Producto según FDS; cepillo de cerdas duras."),
        ("Aclarar", "Hidrolimpiadora a 45° y manguera abundante."),
        ("Arrastrar al punto bajo", "Lodos ácidos y restos hacia la zona más profunda."),
        ("Retirar residuos", "Por el desagüe de fondo o como residuo químico, nunca al circuito de filtración. Sin charcos: el agua estancada cría larvas de mosquito."),
        ("Antialgas y reposo", "Dosis y plazo de reposo del fabricante antes de llenar."),
    ]),
    tarjetas("Elementos complementarios", "Más allá del vaso", "Revisión e higienización de los anexos", [
        ("Playas y andenes", "Al menos 1,20 m de ancho, suelo antideslizante de clase 3 y sin encharcamientos (CTE DB-SUA 6)."),
        ("Escaleras", "Anclaje firme, peldaños antideslizantes, sin óxido ni aristas. Como máximo 15 m entre ellas."),
        ("Rejillas y skimmers", "Sin deformaciones, piezas rotas ni holguras peligrosas."),
        ("Duchas y pediluvios", "Desinfección diaria de rociadores, platos y canaletas."),
    ], cols=4),
    tarjetas("Anexos en detalle", "Mantenimiento de los anexos", "Lo que se revisa en cada uno", [
        ("Playas perimetrales", "Mínimo 1,20 m, suelo de clase 3 e impermeable, con pendiente hacia los imbornales para que el agua de lavado no vuelva al vaso. Se baldean y desinfectan a diario con bactericidas y fungicidas contra las micosis."),
        ("Escaleras y agarres", "Llegan a 1 m bajo el agua, o hasta 30 cm del fondo; cerca de los ángulos y de los cambios de pendiente, a 15 m como máximo (CTE DB-SUA 6). Anclaje sólido, sin aristas; el óxido se trata con pasivantes para inoxidable."),
        ("Duchas y pediluvios", "Limpieza y desinfección al menos una vez al día. En el pediluvio, renovación continua del agua desinfectada para que no sea foco de contaminación cruzada."),
    ], cols=3, light=True),
    apoyo_visual("Los anexos que se revisan", [
        ("3.6 · Playa con imbornal", "Imagen 3.6 · Playa perimetral con pendiente hacia el imbornal y pavimento antideslizante"),
        ("3.7 · Escalera de acceso", "Imagen 3.7 · Escalera de acero inoxidable con anclajes y peldaños antideslizantes"),
        ("3.8 · Duchas y pediluvio", "Imagen 3.8 · Duchas de playa y pediluvio con renovación continua de agua"),
    ], label="Imágenes · anexos"),
    alerta("Alerta de seguridad · PRL", "Corrosivos y mezclas prohibidas",
           "Con ácidos y desincrustantes el EPI es obligatorio. Y nunca mezcles un producto clorado con un ácido (salfumán o desincrustante): se libera gas cloro al instante, altamente tóxico y potencialmente mortal por inhalación.",
           [("Guantes", "Nitrilo o PVC de manga larga (EN 374)."),
            ("Ojos y cara", "Gafas de montura integral (EN 166) y pantalla facial."),
            ("Respiración", "Mascarilla con filtro para gases y vapores (EN 14387)."),
            ("Pies", "Botas de agua antideslizantes.")],
           notes="Insistir en la mezcla cloro + ácido: es el accidente más grave y más evitable del tema."),
    apoyo_visual("Protección y etiquetado", [
        ("3.9 · EPI de protección química", "Imagen 3.9 · Guantes EN 374, gafas EN 166, pantalla facial, mascarilla EN 14387 y botas"),
        ("3.10 · Etiquetas de ácido y de clorado", "Imagen 3.10 · Etiquetas de un desincrustante ácido y de un hipoclorito con sus pictogramas de peligro"),
    ], label="Imágenes · EPI"),
    normativa("Qué exige la normativa en Andalucía", [
        ("D 485/2019 · art. 11", "Biocidas aplicados respetando los plazos de seguridad del envase: nadie accede al recinto tratado hasta que pasan. Plan DDD integrado en el autocontrol."),
        ("CTE DB-SUA 6", "Andenes de 1,20 m como mínimo con suelo de clase 3; escaleras a 15 m como máximo entre sí, hasta 1 m bajo el agua o 30 cm del fondo."),
        ("Criterio CR1.5", "Inspeccionar las instalaciones complementarias: sin aristas, esquinas oxidadas ni azulejos desprendidos que causen heridas o atrapamientos."),
    ], destacado=("RD 742/2013", "Todo lo revisado y corregido se anota en el protocolo de autocontrol de la instalación."),
       notes="Marco andaluz: RD 742/2013 como base estatal, Decreto 485/2019 para lo higiénico-sanitario y el CTE para lo constructivo."),
    preguntas([
        "Al desincrustar las paredes con un limpiador ácido, ¿qué haces antes para no dañar el rejuntado?",
        "Tras limpiar y aclarar el vaso, ¿cuánto debe reposar el antialgas antes de empezar el llenado?",
        "¿Qué ocurre si mezclas por accidente un producto clorado con un desincrustante ácido?",
    ]),
    respuestas([
        ("B", "Humedecer antes los paramentos con agua limpia. El agua evita que el ácido penetre en la masa de las juntas y lo limita a la cal superficial."),
        ("B", "El que indique el fabricante en la etiqueta o la ficha técnica: es el plazo para que el biocida se fije y el plazo de seguridad sin acceso al vaso."),
        ("C", "Se libera gas cloro de forma inmediata: tóxico y corrosivo por inhalación, con lesiones respiratorias graves."),
    ]),
    taller("1.3", "Limpieza y tratamiento de un vaso", "4 horas · vaso didáctico", [
        "Hidrolimpiadora con boquilla regulable y lanza de seguridad",
        "Cepillos de cerdas duras, rasquetas de goma y pulverizador de mochila",
        "Desincrustante ácido para piscinas y antialgas de superficie",
        "EPI completo: traje impermeable, guantes EN 374, pantalla facial y botas",
    ], [
        "Equiparte con el EPI de protección química e inspeccionar su estado",
        "Preparar la dilución del desincrustante según la FDS del fabricante",
        "Mojar la pared de prueba, aplicar el producto y frotar con cepillo",
        "Aclarar con la hidrolimpiadora con la lanza a 45°",
        "Pulverizar el antialgas con la dosis y el reposo que marca el fabricante",
        "Registrar los residuos generados y cumplimentar el parte de trabajo",
    ]),
    cierre("Tema 3", [
        ("Primero mojar", "El ácido siempre sobre superficie húmeda: protege las juntas."),
        ("Cloro y ácido, nunca", "Mezclarlos libera gas cloro. Un producto cada vez y aclarado entre ambos."),
        ("Lanza a 45°", "La presión limpia; en perpendicular arranca gresite y rejuntado."),
        ("Antialgas y fabricante", "Dosis y reposo de la etiqueta. El plazo de seguridad no se acorta."),
    ], "Siguiente · Tema 4 · Estanqueidad, revisión de circuitos y parada invernal"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF1-T3-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T3")
    print(deck.build(out, html_preview=preview))
