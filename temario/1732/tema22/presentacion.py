"""MF2519_2 · UF2 · Tema 22 — presentación SCORM. Texto base: redacción de Mario (17/10/2026).

Correcciones:
- RD 393/2007 (Norma Básica de Autoprotección) y, en Andalucía, Decreto 195/2007: plan de autoprotección
  para las actividades incluidas en su ámbito. En cualquier caso, la empresa debe adoptar medidas de
  emergencia (art. 20 Ley 31/1995).
- DEA: obligación según la normativa autonómica y el tipo de establecimiento; en Andalucía la regula el
  Decreto 22/2012. Se redacta con prudencia: comprobar si la instalación está obligada.
- Ahogamiento (ERC): 5 ventilaciones de rescate iniciales y después 30:2.
- Fuga de cloro: el cloro es más denso que el aire; evacuar hacia donde viene el viento (o en
  perpendicular a la nube) y hacia zonas altas.

    python3 -I temario/1732/tema22/presentacion.py   ->  entregas/MF2519_2-UF2-T22-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2519_2 · UF2 · Tema 22", ident="MF2519_2_UF2_T22",
            title="Plan de emergencia y evacuación, actuación ante fugas químicas, primeros auxilios, soporte vital básico y DEA",
            item_title="Tema 22 - Emergencias y primeros auxilios")

deck.add(
    portada("MF2519_2 · UF2 · Tema 22",
            "Emergencias y primeros auxilios",
            "Qué hacer ante una fuga de cloro o un conato de incendio y cómo actuar ante un ahogamiento: SVB y desfibrilador.",
            "7 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · LEY 31/1995 ART. 20 · RD 393/2007 · ERC",
            notes="Último tema del módulo MF2519_2."),
    ficha("7 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el recinto acuático y el aula de primeros auxilios del centro.",
          "Actuar según el plan de emergencia ante fugas de cloro o conatos de incendio, contener y neutralizar vertidos y aplicar "
          "primeros auxilios, soporte vital básico (SVB) y desfibrilador externo automatizado (DEA) ante un ahogamiento o una parada cardiorrespiratoria."),
    tarjetas("Planificar", "1 · El plan de emergencia", "Saber qué hacer antes de que pase", [
        ("Ley 31/1995, art. 20", "Toda empresa analiza las posibles emergencias y adopta medidas de primeros auxilios, lucha contra incendios y evacuación."),
        ("Plan de autoprotección", "Obligatorio para las actividades del anexo del RD 393/2007; en Andalucía, también el Decreto 195/2007."),
        ("Simulacros", "Se practican para que cada persona sepa su papel."),
    ], cols=3),
    tabla("Niveles", "A · Niveles de emergencia", "Según la gravedad",
          ["Nivel", "Ejemplo", "Actuación"], [
              ("Conato", "Goteo en un racor de la dosificación", "Equipo de primera intervención con EPI y kit de derrames."),
              ("Emergencia parcial", "Fuga en el almacén de productos", "Equipo de segunda intervención y evacuación de la zona."),
              ("Emergencia general", "Nube de cloro fuera de control", "Evacuación total y llamada inmediata al 112."),
          ]),
    alerta("Alerta de seguridad · PRL", "Nube de cloro: arriba y con el viento de cara",
           "El cloro es más denso que el aire y se acumula en sótanos, fosos y zonas bajas. Se evacúa hacia donde viene el viento o en perpendicular a la nube, buscando zonas altas y al aire libre. Nadie entra a la zona sin equipo de respiración: se espera a los bomberos.",
           [("Arriba", "El cloro baja."),
            ("Viento de cara", "La nube se aleja."),
            ("112", "Lo antes posible."),
            ("No entrar", "Sin equipo autónomo.")]),
    pasos("SVB en ahogamiento", "2 · Soporte vital básico (ERC)", "La secuencia ante un ahogado", [
        ("Seguridad", "Sacar a la víctima del agua sin ponerse en peligro."),
        ("Consciencia y ayuda", "Si no responde: llamar al 112 y pedir el DEA."),
        ("Vía aérea", "Maniobra frente-mentón; ver, oír y sentir hasta 10 s."),
        ("5 ventilaciones", "De rescate iniciales: el ahogado tiene falta de oxígeno."),
        ("30:2", "Si no hay signos de vida: 30 compresiones y 2 ventilaciones."),
        ("DEA", "Conectarlo en cuanto llegue y seguir sus instrucciones."),
    ]),
    tarjetas("DEA", "A · El desfibrilador", "Cualquiera puede usarlo", [
        ("Cómo funciona", "Analiza el ritmo del corazón y solo descarga si es necesario."),
        ("Parches", "Sobre el pecho secado; parches pediátricos o modo infantil en niños pequeños."),
        ("Nadie toca", "Durante el análisis y la descarga."),
        ("Obligación", "Depende de la comunidad y del establecimiento; en Andalucía lo regula el Decreto 22/2012. Comprueba si tu instalación está obligada."),
    ], cols=2),
    apoyo_visual("Emergencias", [
        ("22.1 · Plano de evacuación", "Imagen 22.1 · Plano «usted está aquí» con recorridos de evacuación y punto de reunión"),
        ("22.2 · SVB", "Imagen 22.2 · Compresiones torácicas sobre maniquí junto al vaso y DEA abierto"),
    ], label="Imágenes · emergencias y SVB"),
    normativa("Emergencias y primeros auxilios", [
        ("Art. 20 Ley 31/1995", "Medidas de emergencia en toda empresa."),
        ("RD 393/2007 · Decreto 195/2007", "Plan de autoprotección para las actividades de su ámbito."),
        ("Decreto 22/2012 (Andalucía)", "Uso de desfibriladores fuera del ámbito sanitario."),
    ], destacado=("30:2", "30 compresiones y 2 ventilaciones, tras las 5 de rescate en el ahogado.")),
    preguntas([
        "¿Qué se hace antes de las compresiones en un ahogado?",
        "¿Hacia dónde se evacúa en una fuga de cloro?",
        "¿Cuál es la relación compresiones-ventilaciones en adultos?",
    ]),
    respuestas([
        ("A", "Dar 5 ventilaciones de rescate iniciales."),
        ("B", "A zonas altas y al aire libre, con el viento de cara o en perpendicular a la nube."),
        ("B", "30 compresiones y 2 ventilaciones."),
    ]),
    taller("6.4", "Simulacro de evacuación y SVB con DEA", "4 horas · recinto acuático y aula de primeros auxilios", [
        "Maniquí de RCP de adulto y pediátrico",
        "DEA de entrenamiento",
        "Material de simulación de fuga",
    ], [
        "SVB completo en maniquí: 5 ventilaciones y 30:2",
        "Colocar los parches del DEA y seguir sus instrucciones",
        "Simulacro de evacuación por fuga con aviso al 112",
    ]),
    cierre("Tema 22", [
        ("Plan", "Cada uno sabe su papel."),
        ("Cloro", "Arriba y con el viento de cara."),
        ("5 + 30:2", "En el ahogado."),
        ("DEA", "En cuanto llegue."),
    ], "Fin del módulo MF2519_2 · Prevención de riesgos laborales"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2519_2-UF2-T22-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T22")
    print(deck.build(out, html_preview=preview))
