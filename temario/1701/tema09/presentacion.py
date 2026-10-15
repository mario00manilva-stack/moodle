"""MF2522_2 · UF3 · Tema 9 — presentación SCORM. Texto base: redacción de Mario (15/10/2026).

Correcciones sobre el texto base:
- Se quitan las marcas de cita del texto (12, 45, [5]…).
- Maniobra marcha/paro: con el pulsador o el contactor de la bomba en el cuadro, no con el IGA.
- Giro invertido en trifásica: la bomba sigue impulsando en el mismo sentido, pero con mucho menos
  caudal y presión (no «por fricción»); se corrige intercambiando dos fases, trabajo de un electricista.
- Cavitación: por restricción en la aspiración (baja presión en el ojo del rodete). La entrada de aire
  es otra avería (pérdida de cebado), aunque también hace ruido.
- Guardamotor (sobrecarga o bloqueo) y diferencial (derivación a tierra) disparan por causas distintas.
- Ausencia de tensión: con comprobador o multímetro, no con la pinza amperimétrica (mide intensidad).
  Consignación: RD 614/2001 (cinco reglas de oro), no el REBT. Girar el eje a mano, siempre consignado.
- Registro: RD 742/2013, art. 11.5 c), mantenimiento en el protocolo de autocontrol. Se quitan las
  referencias a criterios de realización y al RD 46/2022 que no se han podido contrastar.
- Altura de aspiración de las autoaspirantes y paso de sólidos de las de achique: según fabricante.

    python3 -I temario/1701/tema09/presentacion.py   ->  entregas/MF2522_2-UF3-T9-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF3 · Tema 9", ident="MF2522_2_UF3_T9",
            title="Bombas de filtración (autoaspirantes y centrífugas) y de achique: componentes, funcionamiento, diagnóstico de averías y ruidos anómalos",
            item_title="Tema 9 - Bombas de filtracion y de achique")

deck.add(
    portada("MF2522_2 · UF3 · Tema 9",
            "Bombas de filtración y de achique",
            "Cómo funcionan, de qué piezas están hechas, cómo se ponen en marcha y cómo se reconoce una avería por su ruido antes de que la bomba se rompa.",
            "10 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · RD 614/2001",
            notes="Primer tema de la UF3, mantenimiento electromecánico e hidráulico."),
    ficha("10 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el taller de electromecánica y el banco de pruebas.",
          "Identificar los componentes de las bombas de filtración y de achique, comprobar su sentido de giro, interpretar "
          "la placa de características y diagnosticar cavitación, desgaste de rodamientos, fugas del sello mecánico y disparos "
          "eléctricos, aplicando el mantenimiento preventivo y la prevención de riesgos laborales."),
    tabla("Tipos de bombas", "1 · Tipos de bombas", "Tres bombas, tres trabajos",
          ["Tipo", "Dónde se usa", "Lo que la distingue"], [
              ("Autoaspirante", "Piscinas privadas y colectivas medianas, por encima o por debajo de la lámina", "Expulsa por sí misma el aire de la aspiración, hasta la altura que indique el fabricante."),
              ("Centrífuga", "Piscinas públicas grandes y parques acuáticos", "Necesita trabajar en carga (por debajo de la lámina) o con válvula de pie. Grandes caudales."),
              ("Sumergible de achique", "Vaciado de vasos, arquetas y sumideros de sala técnica", "Motor estanco sumergido. Para aguas limpias o, con rodete vórtex, aguas sucias con sólidos."),
          ], nota="El paso de sólidos y la altura de aspiración dependen del modelo: siempre según la ficha del fabricante."),
    tarjetas("Principio", "A · Cómo mueve el agua el rodete", "Fuerza centrífuga y presión atmosférica", [
        ("El giro", "El motor hace girar el rodete, habitualmente a unas 2 900 r.p.m. con motores de 2 polos a 50 Hz."),
        ("La impulsión", "Los álabes lanzan el agua hacia la periferia y la voluta la conduce a la impulsión con presión."),
        ("La aspiración", "En el ojo del rodete queda una zona de baja presión; la presión atmosférica empuja el agua del vaso hacia la bomba."),
    ], cols=3, footer="La bomba es el **corazón del circuito**: aspira del vaso, empuja el agua por el filtro y la devuelve tratada."),
    tarjetas("Despiece", "2 · Componentes de la bomba", "Parte hidráulica y parte motor", [
        ("Prefiltro", "Cestillo y tapa con junta: retiene hojas y sólidos gruesos antes del rodete."),
        ("Tapón de vaciado", "Drena el cuerpo de la bomba en la parada invernal o el mantenimiento."),
        ("Difusor y rodete", "Los canales que dirigen el agua y la pieza que la impulsa."),
        ("Sello mecánico", "Dos caras pulidas sobre el eje que impiden que el agua pase al motor."),
        ("Eje, rotor y estator", "Eje de acero inoxidable con el rotor; el estator bobinado crea el campo que lo hace girar."),
        ("Rodamientos", "Delantero y trasero: sostienen el giro del eje."),
        ("Caja de bornes", "Conexión eléctrica y, en los motores monofásicos, condensador de arranque."),
        ("Ventilador", "En la parte trasera, con su tapa: refrigera el motor."),
    ], cols=4, light=True),
    apoyo_visual("La bomba por dentro", [
        ("9.1 · Despiece", "Imagen 9.1 · Despiece de una bomba autoaspirante con flechas numeradas: prefiltro, difusor, rodete, sello mecánico, rodamiento delantero, rotor y estator, caja de bornes y ventilador"),
    ], label="Infografía · despiece"),
    tarjetas("Sello mecánico", "A · El sello mecánico", "La pieza más delicada de la bomba", [
        ("Cómo es", "Una cara fija en el cuerpo y otra que gira con el eje, apretadas por un muelle. Suelen ser de grafito y cerámica."),
        ("Para qué sirve", "Impide que el agua a presión de la voluta salga a lo largo del eje hacia el motor."),
        ("Por qué se rompe", "Por trabajar **en seco**: sin agua que la lubrique y refrigere, se calienta en segundos y la cerámica se agrieta."),
    ], cols=3, footer="Un sello que gotea acaba mojando el **rodamiento delantero**: una avería pequeña se convierte en una grande."),
    apoyo_visual("Piezas de desgaste", [
        ("9.2 · Sello mecánico", "Imagen 9.2 · Sello mecánico nuevo junto a uno con la cara cerámica agrietada"),
        ("9.3 · Rodete y difusor", "Imagen 9.3 · Rodete desmontado con el difusor y la junta tórica"),
        ("9.4 · Placa de características", "Imagen 9.4 · Placa de un motor: potencia, tensión, intensidad, r.p.m., frecuencia e IP"),
    ], label="Imágenes · piezas"),
    pasos("Puesta en marcha", "3 · Puesta en marcha", "Antes de arrancar una bomba parada o nueva", [
        ("Cebar", "Llenar el prefiltro de agua limpia: nunca arrancar en seco."),
        ("Revisar la junta", "La de la tapa del prefiltro; si está dura o cortada, se cambia."),
        ("Abrir válvulas", "Aspiración e impulsión abiertas del todo, y selectora del filtro en «filtración»."),
        ("Marcha y paro", "Un impulso de un segundo con el pulsador o el contactor de la bomba en el cuadro."),
        ("Sentido de giro", "El ventilador debe girar como indica la flecha de la carcasa."),
        ("Purgar el filtro", "Abrir la purga hasta que salga agua de forma continua."),
    ], notes="El impulso no se da con el IGA: el interruptor general deja sin servicio toda la instalación."),
    alerta("Atención · motores trifásicos (400 V)", "Giro invertido",
           "Si se cruzan las fases, el motor gira al revés. La bomba sigue impulsando hacia el mismo lado, pero con mucho menos caudal y presión, se calienta y, en algunos modelos, el rodete roscado puede aflojarse del eje.",
           [("Detectar", "Marcha/paro y mirar el ventilador."),
            ("Corregir", "Intercambiar dos fases."),
            ("Quién", "Un electricista cualificado."),
            ("Comprobar", "Otra vez el giro tras la corrección.")]),
    tabla("Diagnóstico", "4 · Diagnóstico de averías", "Ruidos y síntomas: qué significan",
          ["Síntoma", "Causa probable", "Qué hacer"], [
              ("Ruido de grava en la voluta", "Cavitación: aspiración restringida (cestillo sucio, válvula medio cerrada)", "Limpiar el cestillo y abrir del todo la aspiración."),
              ("Burbujas, pérdida de caudal o de cebado", "Entrada de aire: junta de la tapa, racores de aspiración", "Cambiar la junta y apretar o sellar racores."),
              ("Chirrido continuo en el motor", "Rodamientos desgastados", "Cambiar rodamientos y revisar el sello."),
              ("Zumbido sin que gire el eje", "Condensador averiado (monofásico) o rodete bloqueado", "Con la bomba consignada, girar el eje a mano y cambiar el condensador si procede."),
              ("Goteo bajo el cuerpo de la bomba", "Sello mecánico roto o rayado", "Cambiar el sello completo."),
              ("Salta el guardamotor", "Sobreconsumo: rodete frenado, rodamientos, tensión baja", "Medir la intensidad con pinza y compararla con la placa."),
              ("Salta el diferencial", "Derivación a tierra en el motor o el cable", "Consignar y avisar al electricista: medida de aislamiento."),
          ]),
    tarjetas("Cavitación", "A · Cavitación", "El ruido de la grava", [
        ("Qué es", "Con la aspiración estrangulada, la presión en el ojo del rodete baja tanto que el agua forma burbujas de vapor."),
        ("Por qué daña", "Las burbujas colapsan al llegar a zonas de más presión y arrancan material del rodete."),
        ("Cómo se evita", "Cestillos limpios, válvulas de aspiración abiertas y tuberías de aspiración bien dimensionadas."),
    ], cols=3, footer="Los ruidos se oyen **antes** de que la bomba se rompa: escucharla en cada ronda forma parte del mantenimiento."),
    apoyo_visual("Diagnóstico en la sala técnica", [
        ("9.5 · Pinza amperimétrica", "Imagen 9.5 · Medida de la intensidad de una fase del motor con pinza amperimétrica"),
        ("9.6 · Rodete con cavitación", "Imagen 9.6 · Rodete con la superficie picada por la cavitación"),
    ], label="Imágenes · diagnóstico"),
    alerta("Alerta de seguridad · PRL", "Consignación antes de tocar la bomba",
           "Antes de abrir la tapa del prefiltro o de tocar los bornes o el eje, la bomba se consigna: desconectar el guardamotor en el cuadro, bloquearlo con candado y tarjeta, y comprobar la ausencia de tensión con un comprobador o multímetro. La pinza amperimétrica mide intensidad, no sirve para comprobar que no hay tensión.",
           [("Cortar", "Guardamotor de la bomba."),
            ("Bloquear", "Candado y tarjeta personal."),
            ("Comprobar", "0 V con comprobador o multímetro."),
            ("Bornes", "Solo personal cualificado.")]),
    normativa("Seguridad y registro", [
        ("RD 614/2001", "Trabajos con riesgo eléctrico: las cinco reglas de oro para trabajar sin tensión."),
        ("RD 742/2013 · art. 11.5", "El protocolo de autocontrol de la piscina incluye el mantenimiento de la instalación."),
        ("Registro", "Cada cambio de sello, rodamientos, condensador o ajuste se anota con fecha, pieza y responsable."),
    ], destacado=("0 V", "Hasta comprobar la ausencia de tensión, la bomba se trata como si estuviera en marcha.")),
    preguntas([
        "¿Qué le pasa al sello mecánico si la bomba funciona en seco?",
        "¿Qué fenómeno produce un ruido de grava dentro de la bomba?",
        "Tras cambiar un motor trifásico, ¿qué se comprueba con la maniobra marcha/paro?",
    ]),
    respuestas([
        ("B", "Se calienta sin agua que lo lubrique, sus caras se agrietan y empieza a perder agua."),
        ("B", "Cavitación: la aspiración está restringida y se forman burbujas de vapor que erosionan el rodete."),
        ("B", "Que el ventilador gire en el sentido de la flecha de la carcasa: depende del orden de las fases."),
    ]),
    taller("3.1", "Despiece y mantenimiento de bombas", "4 horas · taller de electromecánica", [
        "Bombas autoaspirantes de prueba, extractor de rodamientos y llaves de vaso",
        "Repuestos: sellos mecánicos, juntas tóricas, rodamientos y condensadores",
        "Pinza amperimétrica, multímetro y kit de consignación con candados y tarjetas",
        "EPI: calzado de seguridad, guantes de protección mecánica y gafas",
    ], [
        "Consignar la bomba y comprobar la ausencia de tensión",
        "Desmontar la parte hidráulica y extraer el rodete",
        "Cambiar el sello mecánico limpiando bien su asiento",
        "Comprobar el sentido de giro con marcha/paro",
        "Medir la intensidad y compararla con la placa",
        "Cumplimentar el parte de mantenimiento",
    ]),
    cierre("Tema 9", [
        ("Nunca en seco", "Prefiltro cebado antes de arrancar: el sello lo agradece."),
        ("Mira el ventilador", "Marcha/paro y flecha de la carcasa en cada motor trifásico."),
        ("Escucha la bomba", "Grava, chirrido o zumbido: cada ruido tiene su causa."),
        ("Consigna siempre", "Candado, tarjeta y 0 V antes de tocarla."),
    ], "Siguiente · Tema 10 · Sistemas y medios de filtración"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF3-T9-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T9")
    print(deck.build(out, html_preview=preview))
