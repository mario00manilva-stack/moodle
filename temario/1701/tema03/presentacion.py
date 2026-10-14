"""MF2522_2 · UF1 · Tema 3 — presentación SCORM. Texto base: redacción de Mario (14/10/2026).

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
        ("Antialgas de superficie", "Con el vaso limpio y aclarado, se pulveriza o se aplica con rodillo sobre paredes y fondo para que el biocida se fije en los poros del revestimiento."),
    ], cols=2, footer="**Al menos 6 horas de reposo** antes de empezar el llenado: así el antialgas se adhiere y evita que las esporas se fijen en el vaso nuevo."),
    tarjetas("Maquinaria y útiles", "Maquinaria y útiles", "Química más fuerza mecánica", [
        ("Hidrolimpiadora", "Agua a 100–150 bar para esquinas, rincones y juntas. Lanza a 45° de la superficie: en perpendicular salta el gresite y el rejuntado."),
        ("Cepillos y rasquetas", "Cerdas duras para frotar las incrustaciones rebeldes. Nunca púas metálicas sobre liner."),
        ("Limpiafondos", "Durante el llenado, con 30–40 cm de agua, se pasa el limpiafondos para retirar los finos depositados en la solera."),
    ], cols=3),
    pasos("Aclarado y residuos", "Procedimiento", "Del rascado al vaso listo", [
        ("Mojar", "Humedecer paramentos con agua limpia."),
        ("Aplicar y frotar", "Producto según FDS; cepillo de cerdas duras."),
        ("Aclarar", "Hidrolimpiadora a 45° y manguera abundante."),
        ("Arrastrar al punto bajo", "Lodos ácidos y restos hacia la zona más profunda."),
        ("Retirar residuos", "Por el desagüe de fondo o como residuo químico, nunca al circuito de filtración."),
        ("Antialgas y reposo", "Pulverizar y esperar al menos 6 h antes de llenar."),
    ]),
    tarjetas("Elementos complementarios", "Más allá del vaso", "Revisión e higienización de los anexos", [
        ("Playas y andenes", "Pavimento antideslizante, con pendiente hacia los imbornales y sin encharcamientos."),
        ("Escaleras", "Anclaje firme, peldaños antideslizantes, sin óxido ni aristas."),
        ("Rejillas y skimmers", "Sin deformaciones, piezas rotas ni holguras peligrosas."),
        ("Duchas y pediluvios", "Desinfección diaria de rociadores, platos y canaletas."),
    ], cols=4),
    tarjetas("Anexos en detalle", "Mantenimiento de los anexos", "Lo que se revisa en cada uno", [
        ("Playas perimetrales", "Impermeables y con pendiente hacia los imbornales para que el agua de lavado no vuelva al vaso. Se baldean y desinfectan a diario con productos bactericidas y fungicidas: evitan las micosis entre bañistas."),
        ("Escaleras y agarres", "Acero inoxidable con anclaje sólido y sin aristas cortantes. Los puntos de óxido se tratan con pasivantes específicos para inoxidable."),
        ("Duchas y pediluvios", "Limpieza y desinfección al menos una vez al día. En el pediluvio, renovación continua del agua desinfectada para que no sea foco de contaminación cruzada."),
    ], cols=3, light=True),
    alerta("Alerta de seguridad · PRL", "Corrosivos y mezclas prohibidas",
           "Con ácidos y desincrustantes el EPI es obligatorio. Y nunca mezcles un producto clorado con un ácido (salfumán o desincrustante): se libera gas cloro al instante, altamente tóxico y potencialmente mortal por inhalación.",
           [("Guantes", "Nitrilo o PVC de manga larga (EN 374)."),
            ("Ojos y cara", "Gafas de montura integral (EN 166) y pantalla facial."),
            ("Respiración", "Mascarilla con filtro para gases y vapores (EN 14387)."),
            ("Pies", "Botas de agua antideslizantes.")],
           notes="Insistir en la mezcla cloro + ácido: es el accidente más grave y más evitable del tema."),
    normativa("Inspección de elementos cortantes", [
        ("Criterio CR1.5", "La cualificación exige inspeccionar las instalaciones complementarias para comprobar que no hay elementos agresivos o cortantes."),
        ("Qué se busca", "Aristas, esquinas oxidadas y azulejos desprendidos que puedan causar heridas o atrapamientos."),
        ("RD 742/2013", "Lo revisado y corregido se documenta en el protocolo de autocontrol de la instalación."),
    ], destacado=("0 aristas", "Ningún elemento agresivo o cortante en playas, escaleras, rejillas ni vaso antes de abrir al baño.")),
    apoyo_visual("Imágenes que debes reconocer", [
        ("3.1 · Desincrustado con EPI completo", "Imagen 3.1 · Operario con traje impermeable, pantalla facial y guantes químicos frotando el gresite con cepillo de cerdas duras"),
        ("3.2 · Aclarado con hidrolimpiadora a 45°", "Imagen 3.2 · Aclarado del paramento con hidrolimpiadora a presión, lanza a 45° de la superficie"),
    ]),
    preguntas([
        "Al desincrustar las paredes con un limpiador ácido, ¿qué haces antes para no dañar el rejuntado?",
        "Tras limpiar y aclarar el vaso, ¿cuánto debe reposar el antialgas antes de empezar el llenado?",
        "¿Qué ocurre si mezclas por accidente un producto clorado con un desincrustante ácido?",
    ]),
    respuestas([
        ("B", "Humedecer antes los paramentos con agua limpia. El agua evita que el ácido penetre en la masa de las juntas y lo limita a la cal superficial."),
        ("B", "Al menos 6 horas, para que el biocida se fije al revestimiento antes de introducir agua nueva."),
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
        "Pulverizar el antialgas sobre los paramentos respetando la dosis",
        "Registrar los residuos generados y cumplimentar el parte de trabajo",
    ]),
    cierre("Tema 3", [
        ("Primero mojar", "El ácido siempre sobre superficie húmeda: protege las juntas."),
        ("Cloro y ácido, nunca", "Mezclarlos libera gas cloro. Un producto cada vez y aclarado entre ambos."),
        ("Lanza a 45°", "La presión limpia; en perpendicular arranca gresite y rejuntado."),
        ("Antialgas y 6 h", "La última capa antes de llenar, y el reposo no se acorta."),
    ], "Siguiente · Tema 4 · Estanqueidad, revisión de circuitos y parada invernal"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF1-T3-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T3")
    print(deck.build(out, html_preview=preview))
