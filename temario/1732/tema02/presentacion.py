"""1732 · Tema 2 — Riesgos generales y su prevención (25 h). Redacción propia de VERAQUA.

RD 1157/2024, Anexo VIII, RA2 (criterios a–g). Contenido mínimo: RD 39/1997, Anexo IV, bloque II.
Referencias: RD 486/1997 (lugares de trabajo), RD 614/2001 (riesgo eléctrico), RD 1215/1997 (equipos),
RD 374/2001 y Reglamento (CE) 1272/2008 (químicos, CLP), RD 664/1997 (biológicos), RD 286/2006
(ruido), RD 487/1997 (cargas), RD 773/1997 (EPI), RD 485/1997 (señalización), Ley 31/1995 arts. 20 y
22, RD 393/2007 (autoprotección) y método de evaluación general del INSST. Orden inspirado en las
unidades 2 y 3 del índice público de Paraninfo «MP1732».

    python3 -I temario/1732/tema02/presentacion.py   ->  entregas/1732-T2-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="1732 · Nivel básico de PRL · Tema 2", ident="1732_T2",
            title="Riesgos generales y su prevención",
            item_title="Tema 2 - Riesgos generales y su prevencion")

deck.add(
    portada("1732 · Nivel básico de PRL · Tema 2",
            "Riesgos generales y su prevención",
            "Seguridad, ambiente de trabajo y carga de trabajo: cómo se evalúan los riesgos y con qué medidas se controlan.",
            "25 HORAS · TELEFORMACIÓN · LEY 31/1995 · RD 39/1997 · RD 1157/2024",
            notes="Tema central del módulo: el bloque II del Anexo IV del RD 39/1997."),
    ficha("25 h", "Teleformación",
          "Contenido autoinstruccional, tarea práctica y foro en el aula virtual.",
          "Identificar los riesgos ligados a la seguridad, al ambiente y a la carga de trabajo, evaluarlos de forma "
          "elemental y aplicar medidas de protección colectiva e individual, de emergencia y de vigilancia de la salud."),
    tarjetas("Mapa del tema", "Cómo se organiza", "Tres grupos de riesgos y cómo se controlan", [
        ("Seguridad", "Accidentes: caídas, golpes, cortes, electricidad, incendios, máquinas. Técnica: seguridad en el trabajo."),
        ("Ambiente de trabajo", "Enfermedades: agentes químicos, biológicos y físicos. Técnica: higiene industrial."),
        ("Carga de trabajo", "Fatiga e insatisfacción: esfuerzos, posturas, organización. Técnicas: ergonomía y psicosociología."),
    ], cols=3, footer="Y para todos: **evaluar** el riesgo, **proteger** (primero lo colectivo), **prepararse** para emergencias y **vigilar** la salud."),
    # --- Bloque A · Condiciones de seguridad ---
    tarjetas("Lugares de trabajo", "A · Condiciones de seguridad · RD 486/1997", "El lugar de trabajo también es un riesgo", [
        ("Suelos", "Fijos, estables y no resbaladizos, sin irregularidades. Playas y salas técnicas mojadas: el primer riesgo de caída."),
        ("Desniveles y aberturas", "Protegidos con barandillas cuando hay riesgo de caída de altura, como en fosos y depósitos."),
        ("Orden y limpieza", "Pasillos libres, productos en su sitio y derrames recogidos al momento."),
        ("Ambiente", "Temperatura, humedad, ventilación e iluminación adecuadas a la tarea."),
    ], cols=2),
    tarjetas("Riesgo eléctrico", "A · Riesgo eléctrico · RD 614/2001", "Agua y electricidad: la combinación más peligrosa", [
        ("Contacto directo", "Con partes en tensión: bornes, cables pelados, cuadros abiertos."),
        ("Contacto indirecto", "Con masas que se han puesto en tensión por un fallo: carcasa de una bomba, una escalera."),
        ("Protección", "Diferenciales, toma de tierra, aislamiento, grado de protección frente al agua y trabajos sin tensión."),
    ], cols=3, footer="Las **cinco reglas de oro** para trabajar sin tensión: desconectar, impedir la reconexión, comprobar la ausencia de tensión, poner a tierra y en cortocircuito, y señalizar la zona."),
    tarjetas("Incendios", "A · Incendios", "El fuego necesita cuatro cosas", [
        ("Combustible", "Lo que arde: papel, plásticos, gasóleo, gases."),
        ("Comburente", "El oxígeno del aire. Ojo: algunos productos de piscina son oxidantes y avivan el fuego."),
        ("Energía de activación", "Una chispa, una llama o un calentamiento."),
        ("Reacción en cadena", "Mantiene el fuego vivo. Quitando cualquiera de los cuatro, se apaga."),
    ], cols=4, intro="Clases de fuego: **A** sólidos, **B** líquidos, **C** gases, **D** metales, **F** aceites de cocina. Cada extintor indica en su etiqueta para qué clases sirve."),
    tarjetas("Máquinas y herramientas", "A · Equipos de trabajo · RD 1215/1997", "Máquinas, herramientas y equipos", [
        ("Riesgos", "Atrapamientos, cortes, golpes y proyecciones con bombas, hidrolimpiadoras o herramientas."),
        ("Equipos seguros", "Con marcado CE, resguardos colocados y manual de instrucciones."),
        ("Uso", "Solo personal formado, sin anular protecciones y con la máquina parada y consignada para mantenimiento."),
    ], cols=3, light=True),
    apoyo_visual("Riesgos de seguridad en la instalación", [
        ("2.1 · Suelo mojado", "Imagen 2.1 · Playa o sala técnica con suelo mojado y señal de advertencia de caída"),
        ("2.2 · Cuadro eléctrico", "Imagen 2.2 · Cuadro eléctrico de sala técnica con diferencial y protección frente al agua"),
        ("2.3 · Extintor", "Imagen 2.3 · Extintor señalizado junto a la puerta de la sala técnica"),
    ], label="Imágenes · seguridad"),
    # --- Bloque B · Medio ambiente de trabajo ---
    tarjetas("Agentes químicos", "B · Agentes químicos · RD 374/2001", "Los productos químicos: el riesgo diario del sector", [
        ("Vías de entrada", "Inhalatoria (la más frecuente), dérmica, digestiva y parenteral, a través de una herida."),
        ("Efectos", "Corrosivos, irritantes, tóxicos, sensibilizantes. Pueden ser inmediatos o aparecer con los años."),
        ("Información", "Etiqueta con pictogramas y frases de peligro (Reglamento CLP) y ficha de datos de seguridad, de 16 secciones."),
    ], cols=3, footer="Antes de usar un producto: **lee la etiqueta y la FDS**. Ahí están los EPI, la incompatibilidad con otros productos y qué hacer si hay un accidente."),
    tabla("Pictogramas CLP", "Reglamento (CE) 1272/2008", "Los pictogramas que más vas a ver",
          ["Pictograma", "Significa", "Ejemplo del sector"], [
              ("Corrosión", "Quemaduras graves en piel y ojos; ataca metales", "Ácidos reductores de pH, hipoclorito"),
              ("Signo de exclamación", "Irritante, nocivo, sensibilizante", "Muchos alguicidas y floculantes"),
              ("Llama sobre círculo", "Comburente: aviva el fuego", "Hipoclorito cálcico, tricloro"),
              ("Medio ambiente", "Tóxico para los organismos acuáticos", "Biocidas, hipoclorito"),
              ("Calavera", "Toxicidad aguda grave", "Algunos rodenticidas e insecticidas"),
          ], nota="Los pictogramas CLP son rombos con borde rojo y fondo blanco. Son nueve en total."),
    tarjetas("Agentes biológicos", "B · Agentes biológicos · RD 664/1997", "Lo que no se ve también enferma", [
        ("Qué son", "Bacterias, virus, hongos y parásitos que pueden causar infecciones, alergias o intoxicaciones."),
        ("Cuatro grupos", "Del 1 (poco probable que cause enfermedad) al 4 (enfermedad grave, sin tratamiento eficaz). Legionella está en el grupo 2."),
        ("En el sector", "Legionella en torres y aguas templadas, hongos en playas y duchas, roedores e insectos en control de plagas."),
    ], cols=3),
    tabla("Agentes físicos", "B · Agentes físicos", "Ruido, calor y otros agentes físicos",
          ["Agente", "Riesgo", "Referencia"], [
              ("Ruido", "Pérdida de audición. Protectores a disposición desde 80 dB(A) y obligatorios desde 85 dB(A)", "RD 286/2006"),
              ("Ambiente térmico", "Estrés térmico por calor y humedad, en piscinas cubiertas y en verano", "RD 486/1997"),
              ("Vibraciones", "Lesiones en manos, brazos y espalda con máquinas vibratorias", "RD 1311/2005"),
              ("Radiaciones", "Radiación ultravioleta solar y de equipos UV de desinfección", "Normativa específica"),
          ]),
    apoyo_visual("El ambiente de trabajo", [
        ("2.4 · Etiqueta CLP", "Imagen 2.4 · Etiqueta de un producto de piscina con sus pictogramas y frases de peligro"),
        ("2.5 · Ficha de datos de seguridad", "Imagen 2.5 · Primeras páginas de una FDS con la sección 8 (EPI) señalada"),
        ("2.6 · Sala ruidosa", "Imagen 2.6 · Operario con protectores auditivos junto a las bombas"),
    ], label="Imágenes · ambiente"),
    # --- Bloque C · Carga de trabajo ---
    tarjetas("Carga física", "C · Carga física · RD 487/1997", "Garrafas, sacos y posturas", [
        ("Manipulación de cargas", "Cuenta a partir de 3 kg. En condiciones ideales, 25 kg como máximo; 15 kg para proteger a más personas."),
        ("Cómo levantar", "Pies separados, flexionar las piernas, espalda recta, carga pegada al cuerpo y sin girar el tronco."),
        ("Posturas y movimientos", "Trabajo agachado en el vaso, brazos por encima de los hombros y movimientos repetidos."),
    ], cols=3),
    tarjetas("Carga mental y organización", "C · Carga mental y factores psicosociales", "Cuando el cansancio no es solo físico", [
        ("Carga mental", "Atención continua, decisiones rápidas y responsabilidad sobre la seguridad de los bañistas."),
        ("Factores psicosociales", "Ritmo, turnos, trabajo en solitario, falta de autonomía o de apoyo, conflictos."),
        ("Daños", "Fatiga física y mental, estrés, insatisfacción laboral y desgaste profesional."),
    ], cols=3, footer="Se previene **organizando el trabajo**: pausas, rotación de tareas, información clara, apoyo y participación."),
    apoyo_visual("Carga de trabajo", [
        ("2.7 · Levantar una garrafa", "Imagen 2.7 · Secuencia correcta para levantar una garrafa de 25 kg"),
        ("2.8 · Ayudas mecánicas", "Imagen 2.8 · Carretilla para mover sacos y garrafas en la sala técnica"),
    ], label="Imágenes · carga"),
    # --- Evaluación ---
    tabla("Evaluación de riesgos", "D · Evaluación de riesgos · RD 39/1997", "Cuánto importa cada riesgo",
          ["Probabilidad", "Ligeramente dañino / Dañino", "Extremadamente dañino"], [
              ("Baja", "Trivial / Tolerable", "Moderado"),
              ("Media", "Tolerable / Moderado", "Importante"),
              ("Alta", "Moderado / Importante", "Intolerable"),
          ], nota="Método general del INSST: el nivel de riesgo combina la probabilidad del daño y su gravedad. Cuanto más alto, antes hay que actuar."),
    pasos("Proceso de evaluación", "D · Evaluación", "La evaluación paso a paso", [
        ("Identificar el peligro", "Qué puede causar daño en cada tarea."),
        ("Quién está expuesto", "Puestos, personas y personas especialmente sensibles."),
        ("Estimar el riesgo", "Probabilidad y gravedad."),
        ("Valorar", "Decidir si es tolerable o hay que actuar."),
        ("Planificar medidas", "Qué, quién, cuándo y con qué medios."),
        ("Revisar", "Tras un daño, un cambio o periódicamente."),
    ]),
    # --- Protección ---
    tarjetas("Protección colectiva", "E · Protección colectiva", "Primero, proteger a todos", [
        ("Qué es", "La que protege a varias personas a la vez, sin que tengan que hacer nada."),
        ("Ejemplos", "Barandillas, resguardos de máquinas, ventilación de la sala técnica, diferenciales, cubetos de retención."),
        ("Prioridad", "Va antes que la individual (Ley 31/1995, art. 15)."),
    ], cols=3),
    tarjetas("EPI", "E · Equipos de protección individual · RD 773/1997", "El EPI: la última barrera", [
        ("Cuándo", "Si el riesgo no se puede evitar ni limitar lo suficiente con medidas colectivas."),
        ("Elección", "Según el riesgo y la FDS; con marcado CE y folleto informativo del fabricante."),
        ("Uso", "Personal, bien ajustado, revisado antes de usarlo, limpio, guardado y repuesto cuando se deteriora."),
        ("Categorías", "I riesgo mínimo, II riesgo intermedio, III riesgo muy grave o mortal: protección respiratoria o química."),
    ], cols=2, light=True),
    tabla("Señalización", "RD 485/1997", "Colores y formas de la señalización",
          ["Tipo de señal", "Color y forma", "Ejemplo"], [
              ("Prohibición", "Círculo rojo con banda diagonal", "Prohibido fumar en la sala técnica"),
              ("Advertencia", "Triángulo amarillo con borde negro", "Riesgo eléctrico, suelo resbaladizo"),
              ("Obligación", "Círculo azul", "Uso obligatorio de guantes y gafas"),
              ("Salvamento", "Rectángulo o cuadrado verde", "Salida de emergencia, lavaojos, botiquín"),
              ("Lucha contra incendios", "Rectángulo o cuadrado rojo", "Extintor, pulsador de alarma"),
          ]),
    # --- Emergencias y salud ---
    tarjetas("Emergencias", "F · Emergencias · Ley 31/1995 art. 20 · RD 393/2007", "Saber qué hacer antes de que pase", [
        ("Plan de emergencia", "Qué hacer ante incendio, fuga química, accidente o evacuación, y quién lo hace."),
        ("Equipos", "Alarma y evacuación, primera intervención, segunda intervención y primeros auxilios, con un jefe de emergencia."),
        ("Simulacros", "Para comprobar que el plan funciona y que todos saben su papel."),
    ], cols=3, footer="Ante una fuga de cloro: **alejarse en contra del viento**, avisar, evacuar a los bañistas y no volver a entrar sin la protección adecuada."),
    tarjetas("Vigilancia de la salud", "G · Vigilancia de la salud · Ley 31/1995 art. 22", "Controlar la salud de quien trabaja", [
        ("Voluntaria", "Con excepciones: cuando sea imprescindible para valorar los efectos del trabajo, cuando haya riesgo para otras personas o lo exija una norma."),
        ("Específica", "Según los riesgos del puesto: piel, respiración, audición."),
        ("Confidencial", "Los datos médicos no se usan contra la persona trabajadora; la empresa solo conoce si es apta."),
    ], cols=3),
    alerta("Alerta de seguridad · PRL", "Nunca mezcles productos",
           "Mezclar un producto clorado con un ácido desprende gas cloro de forma inmediata. Cada producto en su envase original, etiquetado, y almacenado separado de los incompatibles según su ficha de datos de seguridad.",
           [("Etiqueta", "Nunca trasvasar a envases sin etiquetar."),
            ("Separación", "Ácidos y clorados, en zonas distintas."),
            ("Ventilación", "Sala técnica ventilada."),
            ("Derrames", "Material absorbente a mano.")]),
    normativa("Las normas de este tema", [
        ("Seguridad", "RD 486/1997 lugares · RD 614/2001 electricidad · RD 1215/1997 equipos."),
        ("Ambiente", "RD 374/2001 químicos · CLP 1272/2008 · RD 664/1997 biológicos · RD 286/2006 ruido."),
        ("Protección", "RD 487/1997 cargas · RD 773/1997 EPI · RD 485/1997 señalización."),
    ], destacado=("Art. 15", "Combatir el riesgo en su origen y anteponer la protección colectiva a la individual (Ley 31/1995).")),
    preguntas([
        "¿Qué forma y color tiene una señal de obligación?",
        "¿A partir de qué exposición diaria al ruido debe la empresa poner protectores auditivos a disposición?",
        "En la sala técnica hay vapores de un producto. ¿Qué medida va primero?",
    ]),
    respuestas([
        ("C", "Un círculo azul con el pictograma en blanco, como «uso obligatorio de guantes» (RD 485/1997)."),
        ("B", "A partir de 80 dB(A); desde 85 dB(A) su uso es obligatorio (RD 286/2006)."),
        ("A", "La ventilación de la sala, porque es protección colectiva y va antes que la mascarilla (Ley 31/1995, art. 15)."),
    ]),
    taller("2.1", "Evaluación elemental de una sala técnica", "entrega en el aula", [
        "Este tema completo y sus diapositivas",
        "La matriz de evaluación del INSST de este tema",
        "La descripción de la sala técnica de la tarea",
    ], [
        "Identificar seis riesgos de la sala técnica",
        "Clasificarlos: seguridad, ambiente o carga",
        "Estimar el nivel de cada riesgo con la matriz",
        "Proponer una medida para cada uno, colectiva primero",
        "Indicar la señalización y los EPI necesarios",
    ], tipo="Tarea", modalidad="Práctica en el aula virtual", etiqueta_equipo="Qué necesitas",
        notes="Tarea individual: se entrega en el aula como archivo o texto."),
    cierre("Tema 2", [
        ("Tres grupos", "Seguridad, ambiente y carga de trabajo."),
        ("Evaluar", "Probabilidad por gravedad: decide la prioridad."),
        ("Colectiva primero", "El EPI es la última barrera."),
        ("Preparados", "Plan de emergencia y vigilancia de la salud."),
    ], "Siguiente · Tema 3 · Riesgos específicos: piscinas y biocidas"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "1732-T2-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-1732-T2")
    print(deck.build(out, html_preview=preview))
