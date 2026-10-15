"""MF2522_2 · UF3 · Tema 10 — presentación SCORM. Texto base: redacción de Mario (15/10/2026).

Correcciones sobre el texto base:
- Se quitan las marcas de cita del texto («1more_horiz», 12, [9]…).
- RD 742/2013: turbidez ≤ 5 UNF y cierre del vaso por encima de 20 UNF (anexo I); el agua de
  recirculación siempre filtrada y desinfectada (art. 6.2).
- Capacidad de retención de cada medio: valores orientativos de fabricantes. Sin el «87,6 %» (no
  contrastado) ni marcas comerciales; ahorro de agua y vida útil del vidrio, según fabricante.
- Velocidades: recomendaciones técnicas, no límites del RD 742/2013 (que solo pide declarar la
  velocidad máxima en SILOÉ, anexo IV). Diatomeas y cartuchos: según fabricante.
- Floculantes y presión de lavado (0,3–0,5 bar sobre filtro limpio): según fabricante.
- Lavado: no se cierran los skimmers por norma; se cierra el limpiafondos y se asegura nivel en el
  vaso o en el depósito de compensación. Nunca la bomba en marcha con la selectora en CERRADO.
- Registro: RD 742/2013, art. 11.5; sin las referencias a CR y al RD 46/2022, no contrastadas.

    python3 -I temario/1701/tema10/presentacion.py   ->  entregas/MF2522_2-UF3-T10-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF3 · Tema 10", ident="MF2522_2_UF3_T10",
            title="Sistemas y medios de filtración (arena, vidrio, diatomeas, zeolitas), velocidades de filtración y protocolo de lavado y enjuague",
            item_title="Tema 10 - Sistemas y medios de filtracion")

deck.add(
    portada("MF2522_2 · UF3 · Tema 10",
            "Sistemas y medios de filtración",
            "Arena, vidrio, diatomeas, zeolitas y cartuchos; cómo se calcula la velocidad de filtración, cuándo hay que lavar el filtro y cómo se hace paso a paso.",
            "10 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019",
            notes="Sigue al Tema 9: la bomba empuja el agua; el filtro la limpia."),
    ficha("10 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el banco de filtración didáctico.",
          "Identificar los medios filtrantes de piscinas, calcular e interpretar la velocidad de filtración, detectar la "
          "colmatación con el manómetro y realizar el lavado a contracorriente y el enjuague con la válvula selectora de 6 vías."),
    tarjetas("Filtración", "1 · La filtración", "Sin agua clara, el desinfectante no funciona", [
        ("Dos pilares", "Tratamiento químico (desinfección) y tratamiento físico (retener partículas en un lecho poroso)."),
        ("Por qué filtrar", "La turbidez y la materia orgánica protegen a los microorganismos y consumen desinfectante."),
        ("Lo que exige la norma", "El agua de recirculación, siempre filtrada y desinfectada (RD 742/2013, art. 6.2). Turbidez ≤ 5 UNF; cierre por encima de 20 UNF."),
    ], cols=3),
    tabla("Medios filtrantes", "A · Medios filtrantes", "Qué retiene cada uno",
          ["Medio", "Retención orientativa", "Características"], [
              ("Arena de sílex (0,4–0,8 mm)", "20–40 µm", "El más extendido. Se renueva cada pocos años por apelmazamiento y desgaste."),
              ("Vidrio filtrante activado", "5–15 µm", "Resiste la formación de biopelícula y necesita menos agua de lavado. Vida útil según fabricante."),
              ("Diatomeas", "2–5 µm", "Filtración muy fina sobre un soporte. No admite floculantes."),
              ("Zeolitas", "3–5 µm", "Mineral volcánico que además retiene amonio por intercambio iónico."),
              ("Cartucho", "10–20 µm", "Para vasos pequeños y spas. Se limpia o se cambia el cartucho."),
          ], nota="Los micrajes son valores de fabricantes: dependen del producto, la granulometría y el estado del lecho."),
    tarjetas("Velocidad", "2 · Velocidad de filtración", "Cuánta agua pasa por cada m² de filtro", [
        ("La fórmula", "**Velocidad (m/h) = caudal (m³/h) ÷ superficie filtrante (m²)**."),
        ("Ejemplo", "Caudal de 60 m³/h y un filtro de 1,2 m de diámetro (1,13 m²): 60 ÷ 1,13 ≈ 53 m/h. Demasiado rápido para uso público."),
        ("Por qué importa", "Cuanto más despacio pasa el agua, más tiempo de contacto y más suciedad retiene el lecho."),
    ], cols=3, footer="Superficie de un filtro circular: **π × r²**. Con 1,2 m de diámetro, r = 0,6 m → 3,14 × 0,36 ≈ 1,13 m²."),
    tabla("Velocidades", "A · Velocidades recomendadas", "Rangos habituales por tipo de filtro",
          ["Filtro", "Velocidad recomendada", "Comentario"], [
              ("Arena o vidrio · uso público", "20–30 m/h", "Mejor retención. Por encima de 30 m/h se pierde calidad de filtrado."),
              ("Arena o vidrio · uso privado", "Hasta 40–50 m/h", "Según el fabricante del filtro."),
              ("Diatomeas", "Hasta unos 5 m/h", "Según el fabricante."),
              ("Cartucho", "Muy baja", "Según el caudal máximo por cartucho que indique el fabricante."),
          ], nota="Son recomendaciones técnicas. El RD 742/2013 no fija un valor, pero la velocidad máxima se declara en SILOÉ (anexo IV)."),
    apoyo_visual("El filtro por dentro", [
        ("10.1 · Velocidad de filtración", "Imagen 10.1 · Infografía con la fórmula de la velocidad de filtración"),
        ("10.2 · Filtro de poliéster", "Imagen 10.2 · Filtro laminado con mirilla: lecho de arena o vidrio y colectores de crepinas"),
    ], label="Infografía · filtración"),
    tarjetas("Floculación", "B · Coagulación y floculación", "Para las partículas que la arena no para", [
        ("El problema", "Las partículas coloidales muy finas atraviesan la arena y vuelven al vaso enturbiando el agua."),
        ("La solución", "Una bomba dosificadora inyecta coagulante o floculante (p. ej., policloruro de aluminio) antes del filtro. Los coloides se agrupan en flóculos que el lecho sí retiene."),
        ("Dónde no", "En filtros de diatomeas o de cartucho no se usan floculantes: colmatan el soporte."),
    ], cols=3, footer="Producto y dosis **según el fabricante**, como todos los reactivos del tratamiento."),
    tabla("Válvula selectora", "3 · La válvula selectora de 6 vías", "Por dónde va el agua en cada posición",
          ["Posición", "Recorrido del agua y uso"], [
              ("Filtración", "Entra por arriba, atraviesa el lecho hacia abajo, pasa por las crepinas y vuelve limpia al vaso."),
              ("Lavado", "Flujo invertido: entra por las crepinas, esponja el lecho y arrastra la suciedad al desagüe."),
              ("Enjuague", "Entra por arriba y sale al desagüe 30–60 s: asienta el lecho y expulsa los restos de suciedad."),
              ("Vaciado", "De la bomba al desagüe sin pasar por el filtro."),
              ("Recirculación", "De la bomba al vaso sin pasar por el filtro."),
              ("Cerrado", "Sin paso de agua. Nunca con la bomba en marcha."),
          ]),
    alerta("Regla de oro en la sala técnica", "Nunca girar la selectora con la bomba en marcha",
           "Antes de cambiar de posición, la bomba se para en el cuadro. Girar la palanca con presión rompe la junta en estrella interior y provoca golpes de ariete. Y nunca se arranca la bomba con la selectora en CERRADO.",
           [("Parar", "La bomba en el cuadro."),
            ("Girar", "Presionar la palanca y cambiar."),
            ("Arrancar", "Solo en una posición con paso."),
            ("Comprobar", "Presión y fugas.")]),
    tarjetas("Colmatación", "4 · Cuándo lavar el filtro", "El manómetro avisa", [
        ("Colmatación", "El lecho se llena de suciedad: sube la presión del filtro y baja el caudal que vuelve al vaso."),
        ("Presión de referencia", "Anotar la presión con el filtro recién lavado: es la «presión de filtro limpio»."),
        ("Criterio de lavado", "Cuando la presión sube unos 0,3–0,5 bar sobre la de filtro limpio, o lo que indique el fabricante."),
    ], cols=3),
    pasos("Lavado", "A · Lavado a contracorriente", "Paso a paso: lavado", [
        ("Parar la bomba", "En el cuadro de mando."),
        ("Preparar", "Cerrar el limpiafondos y comprobar nivel suficiente en el vaso o en el depósito de compensación."),
        ("Abrir el desagüe", "La llave de la línea de evacuación."),
        ("Posición LAVADO", "Presionar y girar la palanca de la selectora."),
        ("Arrancar la bomba", "El agua sale turbia por la mirilla."),
        ("Hasta agua clara", "Unos 2–3 minutos, hasta que la mirilla se vea limpia. Parar la bomba."),
    ]),
    pasos("Enjuague", "B · Enjuague y vuelta al servicio", "Paso a paso: enjuague", [
        ("Posición ENJUAGUE", "Con la bomba parada."),
        ("Arrancar", "Entre 30 y 60 segundos."),
        ("Parar la bomba", "En el cuadro."),
        ("Posición FILTRACIÓN", "Y cerrar la llave del desagüe."),
        ("Arrancar y purgar", "Purgar el aire del filtro y anotar la nueva presión de filtro limpio."),
        ("Reponer y registrar", "Agua de aporte, contadores y m³ de lavado en el registro."),
    ]),
    apoyo_visual("La maniobra de lavado", [
        ("10.3 · Válvula selectora", "Imagen 10.3 · Válvula selectora de 6 vías con sus posiciones y el manómetro"),
        ("10.4 · Mirilla de lavado", "Imagen 10.4 · Mirilla con agua turbia al empezar el lavado y clara al final"),
    ], label="Imágenes · lavado"),
    alerta("Alerta de seguridad · PRL", "Presión y aire en el filtro",
           "Los filtros trabajan a presión, con el máximo que indica su placa (a menudo en torno a 2,5 bar). Al arrancar tras un lavado acumulan aire en la parte superior. Abre la purga manual con un recipiente hasta que salga agua continua sin burbujas y no te coloques sobre la tapa durante la puesta en marcha.",
           [("Purgar", "Hasta agua sin burbujas."),
            ("Placa", "No superar la presión máxima."),
            ("Tapa", "Nunca encima al arrancar."),
            ("EPI", "Gafas y calzado antideslizante.")]),
    normativa("Registro de la filtración", [
        ("RD 742/2013 · art. 6.2", "El agua de recirculación se filtra y desinfecta antes de volver al vaso."),
        ("RD 742/2013 · art. 11.5", "El protocolo de autocontrol incluye el tratamiento del agua y el mantenimiento."),
        ("Registro", "Lavados, presiones antes y después, y lecturas de los contadores de agua depurada y de aporte."),
    ], destacado=("≤ 5 UNF", "Turbidez máxima del agua del vaso. Por encima de 20 UNF, cierre.")),
    preguntas([
        "¿Qué medio filtrante resiste la formación de biopelícula y necesita menos agua de lavado?",
        "El manómetro marca 0,5 bar más que con el filtro limpio. ¿Qué haces?",
        "¿Para qué sirve el enjuague después del lavado?",
    ]),
    respuestas([
        ("B", "El vidrio filtrante activado: su superficie dificulta que se fijen las bacterias."),
        ("B", "Parar la bomba, poner la selectora en LAVADO y lavar a contracorriente."),
        ("B", "Asentar el lecho y expulsar al desagüe los restos de suciedad, para que no vayan al vaso."),
    ]),
    taller("3.2", "Lavado y mantenimiento de filtros", "4 horas · banco de filtración", [
        "Filtro transparente con válvula selectora de 6 vías y mirilla",
        "Manómetros y purgadores de aire manuales",
        "Contador de agua de lavado y kit de turbidez",
        "EPI: calzado antideslizante, guantes y gafas",
    ], [
        "Leer la presión y calcular la velocidad de filtración",
        "Parar la bomba y cambiar la selectora correctamente",
        "Lavar a contracorriente observando la mirilla",
        "Enjuagar y volver a filtración",
        "Purgar el aire y comprobar la estanqueidad",
        "Registrar los m³ de lavado",
    ]),
    cierre("Tema 10", [
        ("Caudal ÷ superficie", "La velocidad de filtración, en m/h."),
        ("+0,3–0,5 bar", "Hora de lavar el filtro."),
        ("Bomba parada", "Antes de tocar la selectora, siempre."),
        ("Lavado y enjuague", "Y purga, nueva presión de referencia y registro."),
    ], "Siguiente · Tema 11 · Circuito hidráulico de depuración"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF3-T10-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T10")
    print(deck.build(out, html_preview=preview))
