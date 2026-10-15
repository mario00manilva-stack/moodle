"""MF2522_2 · UF3 · Tema 11 — presentación SCORM. Texto base: redacción de Mario (15/10/2026).

Correcciones sobre el texto base, contrastadas con el BOE (RD 742/2013) y el BOJA núm. 108 de 2019
(Decreto 485/2019):
- Tiempo de recirculación: el D 485/2019 (anexo I) no fija horas: «según las especificaciones y
  necesidades de la piscina para cumplir con los parámetros de calidad», y se controla a diario
  (control de rutina, anexo III). Las horas por tipo de vaso quedan como valores orientativos de diseño.
- Contadores: el art. 7 del RD 742/2013 trata de los productos químicos, no de contadores. Las dos normas
  sitúan los controles «en los contadores de la piscina» (anexo III): sus lecturas forman parte del
  autocontrol.
- Skimmers por superficie, volumen del depósito de compensación y velocidades en tuberías:
  recomendaciones de diseño, no límites legales.
- Válvula de retención: habitual en la impulsión, no «obligatoria» por norma. Se sustituye la «reductora de
  presión en colectores de reactivos» por las válvulas de inyección con retención (Tema 6).

    python3 -I temario/1701/tema11/presentacion.py   ->  entregas/MF2522_2-UF3-T11-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF3 · Tema 11", ident="MF2522_2_UF3_T11",
            title="El circuito hidráulico de depuración: canal desbordante, depósito de compensación, conducciones de PVC/PE, valvulería y contadores de agua",
            item_title="Tema 11 - Circuito hidraulico de depuracion")

deck.add(
    portada("MF2522_2 · UF3 · Tema 11",
            "El circuito hidráulico de depuración",
            "Por dónde viaja el agua desde el vaso hasta la sala técnica y de vuelta: skimmers y canal desbordante, depósito de compensación, tuberías, válvulas y contadores.",
            "10 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019",
            notes="Une los Temas 9 (bombas) y 10 (filtros) con el vaso."),
    ficha("10 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en la maqueta de recirculación del centro.",
          "Identificar y mantener los elementos del circuito hidráulico (rebosaderos, depósito de compensación, tuberías "
          "de PVC y PE, válvulas e instrumentos de caudal y presión), calcular el tiempo de recirculación y las velocidades "
          "en tuberías y evitar golpes de ariete y contaminaciones cruzadas."),
    tarjetas("Captación", "1 · Captar el agua del vaso", "La suciedad flota: se capta por arriba", [
        ("La capa superficial", "Grasas, cremas, pelos y la mayor parte de la suciedad orgánica se acumulan en la superficie del agua."),
        ("Skimmers", "Bocas de aspiración en la pared con compuerta flotante. Para vasos pequeños o de poco aforo."),
        ("Canal desbordante", "El agua rebosa de forma continua por todo el perímetro hacia una canaleta con rejilla. El habitual en piscinas públicas."),
    ], cols=3, footer="Como orientación de diseño, se suele prever **un skimmer por cada 25–50 m²** de lámina de agua."),
    apoyo_visual("Dos formas de captar el agua", [
        ("11.1 · Skimmers", "Imagen 11.1 · Circuito con skimmers conectados directamente a la aspiración de la bomba"),
        ("11.2 · Canal desbordante", "Imagen 11.2 · Canal desbordante que vierte por gravedad al depósito de compensación con sondas de nivel y válvula de llenado"),
    ], label="Infografía · captación"),
    tarjetas("Depósito de compensación", "A · El depósito de compensación", "El pulmón de una piscina desbordante", [
        ("Absorbe a los bañistas", "Recoge el agua que desplazan los bañistas al entrar, sin que se pierda por el rebosadero."),
        ("Reserva para lavados", "Guarda el agua necesaria para lavar los filtros (Tema 10)."),
        ("Protege las bombas", "Mantiene siempre agua en la aspiración: las bombas no trabajan en seco."),
    ], cols=3, footer="Su volumen se calcula en el proyecto: desplazamiento de bañistas, lámina sobre el rebosadero y lavados. Como orientación, un **5–10 % del volumen del vaso**."),
    tarjetas("Niveles", "B · Control de niveles", "Las sondas del depósito", [
        ("Nivel mínimo", "Abre la electroválvula de agua de aporte y, si sigue bajando, protege las bombas."),
        ("Nivel de trabajo", "Rango normal de funcionamiento de la recirculación."),
        ("Nivel máximo", "Alarma de rebose: cierra el aporte y avisa."),
    ], cols=3, footer="Sondas conductivas o de boya. Se limpian y se comprueban: una sonda sucia puede dejar el depósito sin agua o hacerlo rebosar."),
    tarjetas("Tuberías", "2 · Conducciones", "PVC en la sala, PE enterrado", [
        ("PVC-U PN10 / PN16", "Rígido, en la sala técnica. Se une con limpiador y adhesivo. PN indica la presión nominal en bar."),
        ("PE100", "Polietileno flexible para tramos enterrados: soporta mejor los asentamientos del terreno."),
        ("Identificación", "Colores o etiquetas por circuito (aspiración, impulsión, desagüe, reactivos) y sentido del flujo."),
    ], cols=3),
    tabla("Válvulas", "A · Valvulería", "Qué hace cada válvula",
          ["Válvula", "Función y ubicación"], [
              ("De bola", "Apertura y cierre en ramales: skimmers, fondo, limpiafondos."),
              ("De mariposa", "Grandes diámetros (desde unos DN75). Cierre y regulación con palanca o reductor de volante."),
              ("De retención", "Impide el retorno del agua: evita que la bomba se desceba o el filtro se vacíe al parar. Habitual en la impulsión."),
              ("De pie", "Retención con filtro en la aspiración de bombas que no trabajan en carga."),
              ("De inyección", "Entrada de reactivos al circuito, con retención para que el agua no vuelva a la línea de producto (Tema 6)."),
          ]),
    tarjetas("Velocidades", "B · Velocidad del agua y pérdidas de carga", "Tuberías bien dimensionadas, bombas que no sufren", [
        ("Pérdida de carga", "El rozamiento del agua con tuberías, codos y válvulas resta presión. A más velocidad, más pérdidas y más ruido."),
        ("Aspiración", "Recomendado hasta unos 1,2–1,5 m/s: con más velocidad aparece la cavitación (Tema 9)."),
        ("Impulsión", "Recomendado hasta unos 2–2,5 m/s."),
    ], cols=3, footer="Son **recomendaciones de diseño**, no límites legales. Velocidad (m/s) = caudal (m³/s) ÷ sección interior de la tubería (m²)."),
    tabla("Instrumentos", "3 · Instrumentos de control", "Lo que mide el circuito",
          ["Instrumento", "Dónde", "Para qué"], [
              ("Contador de agua de aporte", "Entrada de agua de red al vaso o al depósito", "Agua nueva que entra: renovación diaria en m³."),
              ("Contador de recirculación", "Tubería general tras los filtros", "Volumen que pasa por la depuración."),
              ("Caudalímetro o rotámetro", "Tramo recto de la impulsión", "Caudal instantáneo en m³/h."),
              ("Manómetros", "Entrada y salida de bombas y filtros", "Presión de trabajo y colmatación del filtro."),
          ], nota="El RD 742/2013 y el D 485/2019 sitúan los controles «en los contadores de la piscina» (anexo III): sus lecturas se anotan en el registro."),
    tarjetas("Recirculación", "A · Tiempo de recirculación", "Cuánto tarda en pasar todo el vaso por el filtro", [
        ("La fórmula", "**Tiempo (h) = volumen del vaso (m³) ÷ caudal de recirculación (m³/h)**."),
        ("Ejemplo", "Vaso de 600 m³ con 150 m³/h de recirculación: 600 ÷ 150 = 4 horas."),
        ("Qué dice la norma", "El D 485/2019 no fija horas: el tiempo debe ser el que necesite la piscina para cumplir los parámetros de calidad, y se controla a diario."),
    ], cols=3, footer="Como orientación de diseño: vasos infantiles en torno a 1 h, vasos recreativos y de enseñanza de 2 a 4 h, y vasos grandes y profundos más tiempo."),
    apoyo_visual("La sala técnica", [
        ("11.3 · Depósito de compensación", "Imagen 11.3 · Depósito de compensación con sondas de nivel y electroválvula de aporte"),
        ("11.4 · Colector y válvulas", "Imagen 11.4 · Colector de PVC con válvulas de mariposa, de bola y de retención identificadas"),
        ("11.5 · Contador y caudalímetro", "Imagen 11.5 · Contador de agua de aporte y rotámetro en la impulsión"),
    ], label="Imágenes · circuito"),
    alerta("Alerta de seguridad · PRL", "Golpe de ariete",
           "Cerrar de golpe una válvula de mariposa o de bola con la bomba a pleno caudal crea una onda de sobrepresión que puede reventar tuberías de PVC o romper la carcasa de un filtro. Las válvulas se abren y se cierran siempre de forma suave y progresiva.",
           [("Despacio", "Abrir y cerrar sin golpes."),
            ("Bomba parada", "Para maniobras grandes."),
            ("Retención", "Revisar que cierra bien."),
            ("PVC", "Encolar con ventilación y guantes.")]),
    tarjetas("Contaminación cruzada", "B · Evitar contaminaciones cruzadas", "El agua sucia nunca vuelve a la red", [
        ("Agua de red", "El llenado se hace con separación (vertido libre sobre el depósito o dispositivo antirretorno), nunca con la red conectada directamente al circuito."),
        ("Desagües", "Lavados y vaciados, a la red de saneamiento con su arqueta, sin conexiones con el agua limpia."),
        ("Reactivos", "Cada línea de producto, con su válvula de inyección y retención."),
    ], cols=3),
    normativa("Registro del circuito", [
        ("RD 742/2013 · art. 6.2", "El agua de recirculación se filtra y desinfecta antes de volver al vaso."),
        ("D 485/2019 · anexos I y III", "Tiempo de recirculación según las necesidades de la piscina y control diario de rutina."),
        ("Registro", "Lecturas diarias de los contadores de aporte y de recirculación y tiempo de recirculación."),
    ], destacado=("V ÷ Q", "Volumen del vaso entre caudal: el tiempo de recirculación, en horas.")),
    preguntas([
        "¿Para qué sirve el depósito de compensación de una piscina desbordante?",
        "¿Qué velocidad se recomienda en las tuberías de aspiración?",
        "¿Qué dice el D 485/2019 sobre el tiempo de recirculación?",
    ]),
    respuestas([
        ("B", "Absorbe el agua que desplazan los bañistas y guarda la reserva para lavar los filtros."),
        ("A", "Hasta unos 1,2–1,5 m/s, para limitar las pérdidas de carga y evitar la cavitación."),
        ("C", "Que sea el necesario para cumplir los parámetros de calidad, y que se controle a diario."),
    ]),
    taller("3.3", "Montaje y maniobra de circuitos", "4 horas · maqueta de recirculación", [
        "Tubo de PVC PN10/PN16, manguitos, codos de 90° y 45°, limpiador y adhesivo",
        "Válvulas de bola, de mariposa y de retención",
        "Rotámetros, contadores de agua y cortatubos",
        "EPI: guantes, gafas y mascarilla para vapores; ventilación al encolar",
    ], [
        "Cortar, biselar, limpiar y encolar un tramo de PVC",
        "Instalar una válvula de retención y una de mariposa",
        "Leer un contador y calcular el caudal en m³/h",
        "Equilibrar caudales entre fondo y skimmers",
        "Cumplimentar la hoja de recirculación y contadores",
    ]),
    cierre("Tema 11", [
        ("Arriba está la suciedad", "Skimmers o canal desbordante."),
        ("El depósito, pulmón", "Bañistas, lavados y bombas protegidas."),
        ("Despacio con las válvulas", "Sin golpes de ariete."),
        ("V ÷ Q", "Y lecturas de contadores en el registro cada día."),
    ], "Siguiente · Tema 12 · Dosificación automática, sondas y electrólisis"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF3-T11-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T11")
    print(deck.build(out, html_preview=preview))
