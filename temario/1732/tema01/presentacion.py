"""1732 · Tema 1 — Fundamentos y gestión de la prevención (15 h). Redacción propia de VERAQUA.

Resultados de aprendizaje del RD 1157/2024, Anexo VIII: RA1 (conceptos básicos y normativa) y RA4
(gestión de la prevención). Contenido mínimo: RD 39/1997, Anexo IV, bloques I y IV. Referencias:
Ley 31/1995 (arts. 4, 14–23, 29, 33–39), RD 39/1997 (arts. 10–21, 35), LGSS (RDL 8/2015, art. 156),
RD 1299/2006. Orden inspirado en las unidades 1 y 5 del índice público de Paraninfo «MP1732».

    python3 -I temario/1732/tema01/presentacion.py   ->  entregas/1732-T1-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="1732 · Nivel básico de PRL · Tema 1", ident="1732_T1",
            title="Fundamentos y gestión de la prevención de riesgos laborales",
            item_title="Tema 1 - Fundamentos y gestion de la prevencion")

deck.add(
    portada("1732 · Nivel básico de PRL · Tema 1",
            "Fundamentos y gestión de la prevención",
            "Qué es un riesgo laboral, qué dice la ley, qué derechos y deberes tienes y quién se ocupa de la prevención en la empresa.",
            "15 HORAS · TELEFORMACIÓN · LEY 31/1995 · RD 39/1997 · RD 1157/2024",
            notes="Primer tema del módulo 1732, común a todos los certificados de Sanidad Ambiental."),
    ficha("15 h", "Teleformación",
          "Contenido autoinstruccional, tarea práctica y foro en el aula virtual.",
          "Identificar los conceptos básicos de la prevención y la normativa que la regula, los derechos y deberes "
          "de las personas trabajadoras, y cómo se organiza y documenta la prevención en la empresa."),
    tarjetas("Cultura preventiva", "Por qué empezar aquí", "La prevención es parte del trabajo, no un añadido", [
        ("Antes que reparar", "Se actúa sobre las causas antes de que haya un daño, no después del accidente."),
        ("En toda la empresa", "La prevención se integra en cada decisión y en cada nivel, desde la dirección hasta el operario."),
        ("Responsabilidad compartida", "La empresa organiza y protege; cada persona trabajadora cumple y avisa."),
    ], cols=3, intro="En una piscina o en un tratamiento con biocidas conviven agua, electricidad, productos químicos y esfuerzo físico. Trabajar seguro es una competencia profesional más."),
    tarjetas("Trabajo y salud", "Trabajo y salud", "Las condiciones de trabajo influyen en la salud", [
        ("Salud", "No es solo la ausencia de enfermedad: es un estado de bienestar físico, mental y social."),
        ("Condición de trabajo", "Cualquier característica del trabajo que pueda influir de forma significativa en la aparición de riesgos: locales, equipos, productos, organización (Ley 31/1995, art. 4)."),
    ], cols=2, footer="Cuando las condiciones de trabajo son malas, la salud se resiente: lesiones, enfermedades, fatiga o malestar."),
    tarjetas("Conceptos clave", "Ley 31/1995 · art. 4", "Las palabras que vas a usar siempre", [
        ("Peligro", "Lo que puede causar daño: un producto corrosivo, una superficie mojada, un cuadro eléctrico."),
        ("Riesgo laboral", "La posibilidad de que una persona trabajadora sufra un daño concreto derivado del trabajo."),
        ("Daño derivado del trabajo", "Enfermedad, patología o lesión sufrida con motivo u ocasión del trabajo."),
        ("Riesgo grave e inminente", "El que es probable que se materialice pronto y puede causar un daño grave para la salud."),
    ], cols=2, footer="**Prevenir** es evitar o reducir el riesgo; **proteger** es limitar el daño si el riesgo llega a materializarse. Primero se previene."),
    tabla("Factores de riesgo", "Clasificación", "Cinco familias de factores de riesgo",
          ["Factor", "Qué incluye", "Ejemplo en piscinas y biocidas"], [
              ("Condiciones de seguridad", "Lugares, máquinas, herramientas, electricidad, incendios", "Playa mojada, bomba sin protección, cuadro eléctrico"),
              ("Ambiente físico", "Ruido, vibraciones, temperatura, iluminación, radiaciones", "Sala técnica ruidosa, calor y humedad en piscina cubierta"),
              ("Contaminantes", "Agentes químicos y biológicos", "Hipoclorito, ácidos, biocidas, legionela"),
              ("Carga de trabajo", "Esfuerzo físico y mental, posturas", "Garrafas de 25 kg, trabajo agachado en el vaso"),
              ("Organización", "Horarios, ritmo, comunicación, autonomía", "Turnos partidos, trabajo en solitario, prisas"),
          ]),
    tarjetas("Daños derivados", "Daños derivados del trabajo", "Qué puede pasar si el riesgo se materializa", [
        ("Accidente de trabajo", "Toda lesión corporal que se sufre con ocasión o por consecuencia del trabajo por cuenta ajena (LGSS, art. 156). Incluye el accidente in itinere, al ir o volver del trabajo."),
        ("Enfermedad profesional", "La contraída a consecuencia del trabajo en las actividades del cuadro oficial (RD 1299/2006) y provocada por los agentes que este indica."),
        ("Otros daños", "Enfermedades relacionadas con el trabajo, fatiga, estrés e insatisfacción laboral."),
    ], cols=3),
    apoyo_visual("Reconocer peligros y riesgos", [
        ("1.1 · Peligro y riesgo", "Imagen 1.1 · Sala técnica: garrafas de producto químico (peligro) y operario trasvasando sin guantes (riesgo)"),
        ("1.2 · Factores de riesgo", "Imagen 1.2 · Vista de una piscina con los cinco factores de riesgo señalados"),
    ], label="Imágenes · conceptos"),
    tabla("Marco normativo", "Marco normativo", "Las normas básicas de la prevención",
          ["Norma", "Qué regula", "Para ti"], [
              ("Constitución, art. 40.2", "Los poderes públicos velan por la seguridad e higiene en el trabajo", "Es el origen de todo"),
              ("Directiva 89/391/CEE", "Directiva marco europea de seguridad y salud", "La base de la ley española"),
              ("Ley 31/1995", "Ley de Prevención de Riesgos Laborales", "Derechos, deberes y obligaciones"),
              ("RD 39/1997", "Reglamento de los Servicios de Prevención", "Evaluación, organización, nivel básico"),
              ("Reales decretos específicos", "Lugares de trabajo, EPI, agentes químicos y biológicos, cargas", "Se ven en los Temas 2 y 3"),
          ]),
    tarjetas("Derechos", "Ley 31/1995 · arts. 14–22", "Tus derechos en prevención", [
        ("Protección eficaz", "A que la empresa garantice tu seguridad y salud en todos los aspectos del trabajo."),
        ("Información y formación", "Sobre los riesgos de tu puesto y las medidas; formación teórica y práctica, en horario de trabajo y sin coste."),
        ("Consulta y participación", "Directamente o a través de tus representantes."),
        ("Interrumpir la actividad", "Ante un riesgo grave e inminente, puedes parar y abandonar el lugar de trabajo."),
        ("Vigilancia de la salud", "Periódica y en función de los riesgos, con confidencialidad."),
        ("EPI adecuados", "Facilitados por la empresa, gratuitos y en buen estado."),
    ], cols=3, light=True),
    tarjetas("Deberes", "Ley 31/1995 · art. 29", "Tus deberes en prevención", [
        ("Usar bien", "Máquinas, herramientas, sustancias peligrosas y equipos de trabajo, según su uso previsto."),
        ("EPI", "Utilizar correctamente los equipos de protección que te faciliten."),
        ("Dispositivos de seguridad", "No anularlos ni ponerlos fuera de funcionamiento."),
        ("Informar", "Avisar de inmediato a tu superior o al servicio de prevención de cualquier situación de riesgo."),
        ("Cooperar", "Contribuir al cumplimiento de las obligaciones de seguridad y colaborar con la empresa."),
    ], cols=3, footer="Incumplir estos deberes se considera un incumplimiento laboral (Ley 31/1995, art. 29.3)."),
    pasos("Principios preventivos", "Ley 31/1995 · art. 15", "Cómo debe actuar la empresa", [
        ("Evitar los riesgos", "Si se puede eliminar el peligro, se elimina."),
        ("Evaluar los que quedan", "Los que no se pueden evitar se evalúan."),
        ("Combatir en el origen", "Actuar sobre la fuente, no sobre la persona."),
        ("Adaptar el trabajo", "A la persona, a la técnica y a su evolución."),
        ("Sustituir lo peligroso", "Por lo que entrañe poco o ningún peligro."),
        ("Colectiva antes que individual", "Y dar las instrucciones debidas."),
    ]),
    tabla("Modalidades", "RD 39/1997 · arts. 10–21", "Cómo se organiza la prevención en la empresa",
          ["Modalidad", "Cuándo", "Quién la hace"], [
              ("Asunción por el empresario", "Hasta 10 trabajadores, o 25 con un solo centro; nunca en actividades del Anexo I", "La propia persona empresaria, con formación"),
              ("Trabajadores designados", "Para parte o toda la actividad preventiva", "Personas de la plantilla con formación"),
              ("Servicio de prevención propio", "Más de 500 trabajadores, o de 250 a 500 en actividades del Anexo I", "Unidad específica de la empresa"),
              ("Servicio de prevención ajeno", "Lo que la empresa no asume con medios propios", "Entidad acreditada externa"),
              ("Servicio mancomunado", "Empresas de un mismo centro, polígono o sector", "Servicio compartido"),
          ], nota="El Anexo I del RD 39/1997 incluye, entre otras, las actividades con exposición a agentes tóxicos como los plaguicidas y biocidas."),
    tarjetas("Representación", "Ley 31/1995 · arts. 35–38", "Quién te representa en prevención", [
        ("Delegados de prevención", "Representantes de la plantilla con funciones específicas en prevención. Hasta 30 trabajadores, lo es el delegado de personal; de 31 a 49, uno elegido por y entre los delegados de personal; desde 50, según una escala."),
        ("Comité de Seguridad y Salud", "Órgano paritario (empresa y delegados) de consulta regular. Obligatorio en empresas o centros con 50 o más trabajadores."),
    ], cols=2),
    tarjetas("Organismos públicos", "Organismos públicos", "Quién vigila y asesora", [
        ("INSST", "Instituto Nacional de Seguridad y Salud en el Trabajo: órgano científico-técnico estatal. Publica guías y notas técnicas."),
        ("Inspección de Trabajo", "Vigila el cumplimiento de la normativa y puede proponer sanciones o paralizar trabajos."),
        ("Junta de Andalucía", "Instituto Andaluz de Prevención de Riesgos Laborales y Centros de Prevención de Riesgos Laborales en cada provincia."),
        ("Mutuas", "Mutuas colaboradoras con la Seguridad Social: gestionan contingencias profesionales."),
    ], cols=2, light=True),
    tarjetas("Documentación", "Ley 31/1995 · art. 23", "Lo que la empresa tiene que tener por escrito", [
        ("Plan de prevención", "Cómo integra la prevención en su gestión."),
        ("Evaluación de riesgos", "Y el resultado de los controles periódicos."),
        ("Planificación preventiva", "Medidas, plazos, responsables y medios."),
        ("Medidas y EPI", "Las medidas de protección y prevención que se aplican."),
        ("Vigilancia de la salud", "Resultado de los controles, con su confidencialidad."),
        ("Daños", "Relación de accidentes y enfermedades profesionales con baja de más de un día."),
    ], cols=3, footer="Tu papel en el nivel básico: **recoger, elaborar y archivar** la documentación preventiva que te corresponda (RD 1157/2024, RA4)."),
    apoyo_visual("Quién es quién en prevención", [
        ("1.3 · Organización preventiva", "Imagen 1.3 · Esquema: empresa, servicio de prevención, delegados, comité y organismos públicos"),
        ("1.4 · Documentación", "Imagen 1.4 · Archivo de prevención: evaluación de riesgos, planificación y registros"),
    ], label="Imágenes · gestión"),
    alerta("Alerta de seguridad · PRL", "Riesgo grave e inminente",
           "Si detectas un riesgo grave e inminente para tu vida o tu salud, tienes derecho a interrumpir la actividad y abandonar el lugar de trabajo (Ley 31/1995, art. 21). Hacerlo no puede perjudicarte, salvo mala fe o negligencia grave.",
           [("Para", "Detén la tarea en condiciones seguras."),
            ("Aléjate", "Sal de la zona de peligro."),
            ("Avisa", "Informa de inmediato a tu responsable."),
            ("No vuelvas", "Hasta que el riesgo esté controlado.")]),
    normativa("Tu papel en el nivel básico", [
        ("RD 39/1997 · art. 35", "El nivel básico promueve comportamientos seguros, realiza evaluaciones elementales de riesgos y colabora con la empresa."),
        ("RD 1157/2024", "Este módulo de 50 horas da la formación de nivel básico a quien cursa el certificado."),
        ("Andalucía", "En Andalucía se imparte antes de las prácticas en empresa (Resolución de 2 de abril de 2025)."),
    ], destacado=("50 h", "Las horas mínimas del nivel básico en actividades del Anexo I, como las que usan biocidas.")),
    preguntas([
        "¿Qué es un riesgo laboral según la Ley 31/1995?",
        "¿Cuál de estas acciones es un deber de la persona trabajadora?",
        "¿Qué puedes hacer ante un riesgo grave e inminente?",
    ]),
    respuestas([
        ("B", "La posibilidad de que una persona trabajadora sufra un daño concreto derivado del trabajo (art. 4)."),
        ("C", "Usar correctamente los EPI que te facilita la empresa (art. 29)."),
        ("A", "Interrumpir la actividad y abandonar el lugar de trabajo (art. 21), avisando de inmediato."),
    ]),
    taller("1.1", "Ficha de prevención de un puesto", "entrega en el aula", [
        "Este tema completo y sus diapositivas",
        "La Ley 31/1995 (arts. 14 a 29)",
        "Una piscina o instalación que conozcas, o la del caso del foro",
    ], [
        "Describir el puesto y las tareas principales",
        "Identificar cinco factores de riesgo y clasificarlos",
        "Indicar el daño que podría causar cada uno",
        "Señalar dos derechos y dos deberes aplicables",
        "Indicar quién gestiona la prevención y qué documentos debe haber",
    ], tipo="Tarea", modalidad="Práctica en el aula virtual", etiqueta_equipo="Qué necesitas",
        notes="Tarea individual: se entrega en el aula como archivo o texto."),
    cierre("Tema 1", [
        ("Riesgo no es peligro", "El peligro está; el riesgo es la posibilidad de daño."),
        ("Ley 31/1995", "Derechos, deberes y obligaciones de todos."),
        ("Puedes parar", "Ante un riesgo grave e inminente."),
        ("Todo por escrito", "Evaluación, planificación y registros."),
    ], "Siguiente · Tema 2 · Riesgos generales y su prevención"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "1732-T1-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-1732-T1")
    print(deck.build(out, html_preview=preview))
