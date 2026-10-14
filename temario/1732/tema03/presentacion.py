"""1732 · Tema 3 — Riesgos específicos: piscinas y biocidas (5 h). Redacción propia de VERAQUA.

RD 1157/2024, Anexo VIII, RA3 (criterios a–e). Contenido mínimo: RD 39/1997, Anexo IV, bloque III.
Referencias: RD 374/2001, Reglamento (CE) 1272/2008, RD 656/2017 (almacenamiento de productos químicos),
RD 830/2010 (capacitación para tratamientos con biocidas), RD 487/2022 (legionelosis), Ley 31/1995
art. 32 bis y RD 604/2006 (recurso preventivo). Orden inspirado en la unidad 4 del índice público de
Paraninfo «MP1732».

    python3 -I temario/1732/tema03/presentacion.py   ->  entregas/1732-T3-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="1732 · Nivel básico de PRL · Tema 3", ident="1732_T3",
            title="Riesgos específicos del puesto: piscinas y biocidas",
            item_title="Tema 3 - Riesgos especificos piscinas y biocidas")

deck.add(
    portada("1732 · Nivel básico de PRL · Tema 3",
            "Riesgos del puesto: piscinas y biocidas",
            "Los riesgos propios del mantenimiento de instalaciones acuáticas y de la aplicación de biocidas, sus medidas y qué hacer si algo sale mal.",
            "5 HORAS · TELEFORMACIÓN · RD 374/2001 · RD 830/2010 · RD 487/2022",
            notes="Bloque III del Anexo IV del RD 39/1997: riesgos específicos del sector."),
    ficha("5 h", "Teleformación",
          "Contenido autoinstruccional, tarea práctica y foro en el aula virtual.",
          "Identificar los riesgos y las condiciones de trabajo del puesto, los daños que pueden causar, las medidas "
          "preventivas específicas y los protocolos de actuación cuando se produce un daño."),
    tarjetas("Los puestos", "Condiciones de trabajo del puesto", "Dos puestos, muchos riesgos en común", [
        ("Mantenimiento de piscinas", "Sala técnica, vaso, playas y duchas. Productos de tratamiento del agua, bombas y cuadros eléctricos, a menudo en solitario."),
        ("Aplicación de biocidas", "Desinfección, control de plagas y prevención de legionela. Productos concentrados, pulverizadores y espacios cerrados."),
    ], cols=2, footer="En los dos: **productos químicos** a diario, **agua junto a la electricidad**, **esfuerzos** con garrafas y sacos y trabajo en **espacios poco ventilados**."),
    tabla("Riesgos del puesto", "Riesgos específicos", "Riesgo, situación y daño",
          ["Riesgo", "Situación típica", "Daño posible"], [
              ("Químico", "Trasvases, mezclas, fugas de cloro, pulverización", "Quemaduras, intoxicación, lesiones respiratorias"),
              ("Eléctrico", "Cuadros y bombas en sala técnica húmeda", "Electrocución, quemaduras"),
              ("Caídas", "Playas mojadas, escaleras del vaso, vaso vacío", "Golpes, fracturas"),
              ("Sobreesfuerzos", "Garrafas de 25 kg, sacos de sal, posturas en el vaso", "Lesiones de espalda"),
              ("Espacios confinados", "Depósitos de compensación, arquetas, galerías", "Asfixia, intoxicación"),
              ("Biológico", "Aerosoles de duchas y torres, roedores e insectos", "Legionelosis, infecciones"),
          ]),
    tarjetas("Riesgo químico", "Medidas específicas · Riesgo químico", "El producto: conocerlo antes de tocarlo", [
        ("Antes", "Leer la etiqueta y la FDS. Comprobar los EPI de la sección 8 y las incompatibilidades."),
        ("Durante", "Trasvasar con bomba o dosificador, nunca a envases sin etiquetar ni de alimentos. Un producto cada vez."),
        ("Después", "Cerrar envases, recoger derrames, lavar los EPI reutilizables y lavarse las manos."),
    ], cols=3, footer="**Nunca mezcles** cloro con ácido: desprende gas cloro de forma inmediata."),
    tarjetas("Almacenamiento", "Medidas específicas · RD 656/2017", "Dónde y cómo se guardan los productos", [
        ("Separados", "Ácidos lejos de clorados y de oxidantes, en zonas o armarios distintos."),
        ("Contenidos", "Sobre cubetos de retención, que recogen un derrame."),
        ("Ventilados y señalizados", "Local ventilado, señalizado, con acceso restringido y lejos de fuentes de calor."),
        ("Preparados", "Material absorbente, lavaojos y ducha o agua abundante cerca."),
    ], cols=2, light=True),
    tarjetas("Espacios confinados", "Medidas específicas · Espacios confinados", "Entrar en un depósito no es entrar en una habitación", [
        ("El peligro", "Poco oxígeno o gases tóxicos (cloro, sulfhídrico en arquetas) que no se ven ni siempre se huelen."),
        ("Antes de entrar", "Permiso de trabajo, medir la atmósfera (oxígeno y gases), ventilar y consignar bombas y válvulas."),
        ("Durante", "Nunca solo: una persona fuera vigilando, con comunicación y medios de rescate. Presencia de recurso preventivo."),
    ], cols=3, footer="Si alguien se desploma dentro, **no entres a rescatarle sin protección respiratoria**: la mayoría de las víctimas son los rescatadores."),
    tarjetas("Biocidas y legionela", "Medidas específicas · RD 830/2010 · RD 487/2022", "Aplicar biocidas y trabajar con legionela", [
        ("Capacitación", "Los tratamientos con biocidas exigen la formación que regula el RD 830/2010."),
        ("Plazo de seguridad", "Respetar el de la etiqueta: nadie entra en la zona tratada hasta que pasa. Señalizarla."),
        ("Legionela", "Limpieza y desinfección de instalaciones de riesgo con protección respiratoria y sin generar aerosoles innecesarios."),
    ], cols=3),
    apoyo_visual("El puesto en imágenes", [
        ("3.1 · Almacén de productos", "Imagen 3.1 · Almacén con ácidos y clorados separados, sobre cubetos de retención"),
        ("3.2 · Espacio confinado", "Imagen 3.2 · Medición de la atmósfera antes de entrar en un depósito de compensación"),
        ("3.3 · Aplicación de biocida", "Imagen 3.3 · Aplicador con EPI completo y zona tratada señalizada"),
    ], label="Imágenes · puesto"),
    pasos("Si hay un daño", "Protocolos de actuación", "Qué hacer en los accidentes más probables", [
        ("Salpicadura en los ojos", "Lavaojos o agua abundante, al menos 15 minutos, y al médico."),
        ("Contacto con la piel", "Quitar la ropa contaminada y lavar con mucha agua."),
        ("Inhalación de cloro", "Sacar a la víctima al aire libre sin exponerte, 112."),
        ("Ingestión", "No provocar el vómito; llamar a Información Toxicológica."),
        ("Derrame", "Ventilar, contener con absorbente y no mezclar con otros productos."),
        ("Descarga eléctrica", "Cortar la corriente antes de tocar a la víctima."),
    ]),
    tarjetas("Teléfonos", "Protocolos de actuación", "Los números que tienen que estar a la vista", [
        ("112", "Emergencias: ambulancia, bomberos, policía."),
        ("91 562 04 20", "Servicio de Información Toxicológica, las 24 horas."),
        ("Responsable", "El teléfono del responsable de la instalación y del servicio de prevención."),
    ], cols=3, footer="Ten a mano la **FDS** o la etiqueta del producto: es lo primero que te pedirán por teléfono."),
    apoyo_visual("Equipos de emergencia", [
        ("3.4 · Lavaojos", "Imagen 3.4 · Lavaojos de emergencia en la sala técnica, con su señal verde"),
        ("3.5 · Cartel de teléfonos", "Imagen 3.5 · Cartel con el 112, el Servicio de Información Toxicológica y el responsable"),
    ], label="Imágenes · emergencia"),
    alerta("Alerta de seguridad · PRL", "El trabajo en solitario",
           "Muchas tareas de mantenimiento se hacen sin nadie cerca. Antes de empezar, alguien debe saber dónde estás y cuánto vas a tardar, y debes tener forma de pedir ayuda. Hay tareas que nunca se hacen en solitario: entrar en un espacio confinado es la principal.",
           [("Avisa", "Dónde vas y cuánto tardarás."),
            ("Comunica", "Teléfono o radio con cobertura."),
            ("Revisa", "Llamadas de control acordadas."),
            ("Nunca solo", "En espacios confinados.")]),
    normativa("Normas específicas del sector", [
        ("RD 830/2010", "Capacitación para realizar tratamientos con biocidas."),
        ("RD 487/2022", "Prevención y control de la legionelosis."),
        ("RD 656/2017", "Almacenamiento de productos químicos."),
    ], destacado=("15 min", "El tiempo mínimo de lavado de los ojos tras una salpicadura de un producto corrosivo.")),
    preguntas([
        "¿Qué hay que hacer antes de entrar en un depósito de compensación?",
        "¿Qué haces si te salpica un producto corrosivo en los ojos?",
        "¿Cuál es el teléfono del Servicio de Información Toxicológica?",
    ]),
    respuestas([
        ("B", "Medir la atmósfera, ventilar, consignar bombas y válvulas y no entrar nunca solo."),
        ("A", "Lavar con agua abundante o lavaojos durante al menos 15 minutos y acudir al médico."),
        ("C", "91 562 04 20, disponible las 24 horas. Para emergencias, el 112."),
    ]),
    taller("3.1", "Protocolo de actuación del puesto", "entrega en el aula", [
        "Este tema completo y sus diapositivas",
        "La FDS de un hipoclorito y la de un reductor de pH",
        "El plano o la descripción de una sala técnica",
    ], [
        "Elegir tres situaciones de daño del puesto",
        "Escribir los pasos de actuación de cada una",
        "Indicar los EPI y el material de emergencia",
        "Incluir los teléfonos y a quién se avisa",
        "Presentarlo como un cartel de una página",
    ], tipo="Tarea", modalidad="Práctica en el aula virtual", etiqueta_equipo="Qué necesitas",
        notes="Tarea individual: se entrega en el aula como archivo o texto."),
    cierre("Tema 3", [
        ("Conoce el producto", "Etiqueta y FDS antes de usarlo."),
        ("Separados", "Ácidos y clorados nunca juntos."),
        ("Nunca solo", "En espacios confinados, medir y vigilar."),
        ("Protocolo a mano", "Lavaojos, 112 y 91 562 04 20."),
    ], "Siguiente · Tema 4 · Primeros auxilios"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "1732-T3-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-1732-T3")
    print(deck.build(out, html_preview=preview))
