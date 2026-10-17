"""MF2519_2 · UF1 · Tema 19 — presentación SCORM. Texto base: redacción de Mario (17/10/2026).

Correcciones:
- REBT ITC-BT-31: volumen 0 = interior del vaso; volumen 1 = hasta 2 m en horizontal desde el borde y
  2,5 m de altura; volumen 2 = 1,5 m más allá del volumen 1. En los volúmenes 0 y 1 solo MBTS de 12 V en
  alterna (30 V en continua) con la fuente de seguridad fuera de esos volúmenes.
- Oxígeno: el 19,5 % es el criterio de entrada habitual (aire normal 20,9 %).
- Recurso preventivo (art. 32 bis Ley 31/1995 y RD 39/1997), arnés EN 361.

    python3 -I temario/1732/tema19/presentacion.py   ->  entregas/MF2519_2-UF1-T19-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2519_2 · UF1 · Tema 19", ident="MF2519_2_UF1_T19",
            title="Marco normativo de PRL y riesgos específicos en piscinas: eléctrico, espacios confinados, caídas y sobreesfuerzos",
            item_title="Tema 19 - Marco de PRL y riesgos especificos")

deck.add(
    portada("MF2519_2 · UF1 · Tema 19",
            "Marco de PRL y riesgos específicos",
            "Derechos y deberes en prevención, electricidad junto al agua, depósitos de compensación, caídas y cargas.",
            "8 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · LEY 31/1995 · RD 39/1997 · REBT ITC-BT-31",
            notes="Primer tema del módulo MF2519_2."),
    ficha("8 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el depósito de prácticas y el banco eléctrico del centro.",
          "Conocer los derechos y deberes en prevención (Ley 31/1995), identificar los riesgos propios del mantenimiento de "
          "piscinas —eléctrico en locales mojados, espacios confinados, caídas y sobreesfuerzos— y aplicar sus medidas preventivas."),
    tarjetas("Marco normativo", "1 · Ley 31/1995 y RD 39/1997", "Prevenir es organizar el trabajo", [
        ("Principios de la acción preventiva", "Evitar los riesgos, evaluar los que no se pueden evitar y combatirlos en su origen (art. 15)."),
        ("Deberes de la empresa", "Evaluar, planificar, formar e informar, dar los EPI y vigilar la salud."),
        ("Deberes del trabajador", "Usar bien equipos y EPI, no anular dispositivos de seguridad e informar de los riesgos (art. 29)."),
        ("RD 39/1997", "Reglamento de los Servicios de Prevención: evaluación de riesgos, planificación y recurso preventivo."),
    ], cols=2),
    tabla("REBT ITC-BT-31", "2 · Electricidad junto al agua", "Los volúmenes del vaso",
          ["Volumen", "Dónde", "Qué se admite"], [
              ("0", "Interior del vaso y de sus huecos", "Solo MBTS: 12 V en alterna (30 V en continua)."),
              ("1", "Hasta 2 m en horizontal desde el borde y 2,5 m de altura", "Solo MBTS de 12 V, con la fuente de seguridad fuera de los volúmenes 0 y 1."),
              ("2", "1,5 m más allá del volumen 1", "Equipos protegidos por diferencial de 30 mA o MBTS, con el grado de protección exigido."),
          ], nota="La sala técnica es un local mojado. Todas las masas metálicas (escaleras, rejillas, bombas) se unen con la conexión equipotencial."),
    tarjetas("Protecciones", "A · Protección frente a contactos", "Lo que salva la vida", [
        ("Diferencial de 30 mA", "Corta la corriente si hay una fuga a tierra. Se prueba con su botón de test."),
        ("Equipotencialidad", "Todas las masas al mismo potencial: no hay diferencia de tensión al tocarlas."),
        ("Nunca con las manos mojadas", "Ni sobre suelo encharcado. Consignar antes de intervenir (Tema 1)."),
    ], cols=3),
    tarjetas("Espacios confinados", "3 · Depósitos de compensación y arquetas", "Un espacio que no está hecho para trabajar dentro", [
        ("Por qué son peligrosos", "Abertura pequeña, ventilación natural escasa y posible falta de oxígeno o gases tóxicos."),
        ("Oxígeno", "El aire tiene un 20,9 %. Por debajo del **19,5 %** no se entra."),
        ("Gases", "Sulfuro de hidrógeno (H₂S), monóxido de carbono (CO), cloro o atmósferas inflamables (LEL)."),
    ], cols=3),
    pasos("Protocolo de entrada", "A · Antes de entrar", "Cinco pasos que no se saltan", [
        ("Permiso de trabajo", "Firmado por quien autoriza la entrada."),
        ("Medición", "Detector multigas: O₂, H₂S, CO y LEL, antes y durante el trabajo."),
        ("Ventilación", "Forzada y continua con insuflador."),
        ("Vigilante exterior", "Recurso preventivo presente todo el tiempo."),
        ("Rescate", "Trípode con torno y arnés EN 361 puesto."),
    ]),
    tarjetas("Otros riesgos", "4 · Caídas y sobreesfuerzos", "Los accidentes más frecuentes", [
        ("Caídas al mismo nivel", "Suelos mojados o con producto: calzado antideslizante, orden y limpieza."),
        ("Caídas a distinto nivel", "Vaso vacío, fosos y escaleras: barandillas, tapas y señalización."),
        ("Sobreesfuerzos", "Garrafas de 25 kg y sacos: carretilla, bomba de trasvase y técnica correcta (RD 487/1997)."),
    ], cols=3),
    apoyo_visual("Riesgo eléctrico y confinados", [
        ("19.1 · Volúmenes del vaso", "Imagen 19.1 · Esquema de los volúmenes 0, 1 y 2 alrededor del vaso (ITC-BT-31)"),
        ("19.2 · Trípode de rescate", "Imagen 19.2 · Trípode con torno sobre la boca del depósito de compensación y operario con arnés"),
    ], label="Imágenes · REBT y confinados"),
    alerta("Alerta de seguridad · PRL", "Nunca se entra solo en un espacio confinado",
           "Está prohibido entrar solo en un depósito de compensación o una arqueta profunda. Siempre queda un compañero fuera, vigilando y preparado para activar el rescate con el trípode. Quien vigila no entra a rescatar sin equipo: así se producen la mayoría de las muertes.",
           [("Fuera", "Un vigilante siempre."),
            ("Medir", "Antes y durante."),
            ("Ventilar", "Todo el tiempo."),
            ("Rescatar", "Con trípode, no entrando.")]),
    normativa("Formación e información", [
        ("Art. 19 Ley 31/1995", "Formación teórica y práctica, suficiente y adecuada, específica del puesto."),
        ("Art. 18 Ley 31/1995", "Información sobre los riesgos del puesto y sus medidas."),
        ("Recurso preventivo", "Obligatorio, entre otros casos, en trabajos en espacios confinados (art. 32 bis y RD 39/1997)."),
    ], destacado=("30 mA", "Sensibilidad del diferencial que protege a las personas.")),
    preguntas([
        "¿Qué tensión máxima se admite en los proyectores del interior del vaso (volumen 0)?",
        "¿Con qué porcentaje de oxígeno mínimo se puede entrar en un depósito de compensación?",
        "¿Qué protección corta la corriente ante una fuga a tierra?",
    ]),
    respuestas([
        ("B", "Muy baja tensión de seguridad: 12 V en alterna."),
        ("B", "Al menos un 19,5 % (el aire normal tiene un 20,9 %)."),
        ("B", "Un interruptor diferencial de alta sensibilidad, de 30 mA."),
    ]),
    taller("6.1", "Espacios confinados y seguridad eléctrica", "4 horas · depósito de prácticas y banco eléctrico", [
        "Detector multigas y trípode de rescate",
        "Arnés EN 361",
        "Cuadro con diferencial de 30 mA",
    ], [
        "Medir la atmósfera en la boca de un depósito",
        "Montar el trípode con torno y colocarse el arnés",
        "Comprobar el disparo del diferencial con el botón de test",
    ]),
    cierre("Tema 19", [
        ("Ley 31/1995", "Evitar, evaluar y combatir en origen."),
        ("12 V", "MBTS en los volúmenes 0 y 1."),
        ("19,5 % de O₂", "Por debajo, no se entra."),
        ("Nunca solo", "Vigilante y trípode."),
    ], "Siguiente · Tema 20 · Riesgo químico y biológico"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2519_2-UF1-T19-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T19")
    print(deck.build(out, html_preview=preview))
