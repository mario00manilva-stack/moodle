"""MF2522_2 · UF2 · Tema 8 — presentación SCORM. Texto base: redacción de Mario (15/10/2026).

Correcciones sobre el texto base, contrastadas con el BOE (RD 742/2013 anexos II y III; RITE
consolidado, RD 1027/2007):
- Temperatura del aire: 1–2 ºC por encima del agua, con un máximo de 30 ºC (RITE IT 1.1.4.1.2); no se
  aplica a hidromasaje ni a vasos terapéuticos (RD 742/2013). HR < 65 % (RD 742 y RITE); el 55–60 % y
  el mínimo del 50 % son recomendaciones de confort, no límites legales.
- Tricloramina en el aire: 0,5 mg/m³ es un valor de referencia de la OMS; ni el RD 742/2013 ni el RITE
  fijan un límite.
- Depresión: el recinto del vaso (no la sala técnica) a 20–40 Pa por debajo de los locales contiguos, y
  ventilación mínima de 2,5 dm³/s por m² de lámina y playa (RITE IT 1.1.4.2.3).
- Barreras térmicas: obligatorias sobre la lámina fuera de servicio (RITE IT 1.2.4.5.5), no solo
  recomendables. Recuperación de energía del aire expulsado obligatoria (RITE IT 1.2.4.5.2).
- Control diario: temperatura, HR y CO₂ (RD 742/2013, anexo III, control de rutina en aire).
- Mohos de paredes y techos: Aspergillus, Penicillium… (Candida es una levadura, no un moho de paramentos).

    python3 -I temario/1701/tema08/presentacion.py   ->  entregas/MF2522_2-UF2-T8-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF2 · Tema 8", ident="MF2522_2_UF2_T8",
            title="Calidad del aire en piscinas climatizadas y cubiertas: parámetros ambientales, deshumectación y ventilación",
            item_title="Tema 8 - Calidad del aire en piscinas cubiertas")

deck.add(
    portada("MF2522_2 · UF2 · Tema 8",
            "Calidad del aire en piscinas cubiertas",
            "Temperatura, humedad, CO₂ y cloraminas en el aire del recinto, y los equipos que los controlan: deshumectadoras, UTA, ventilación y mantas térmicas.",
            "10 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019 · RITE",
            notes="Último tema de la UF2. En una piscina cubierta, el agua y el aire se controlan juntos."),
    ficha("10 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en la sala técnica de climatización.",
          "Controlar y corregir la temperatura, la humedad relativa, el CO₂ y las cloraminas del aire en recintos acuáticos "
          "cubiertos, operando los equipos de deshumectación, climatización y renovación de aire conforme al RD 742/2013, "
          "el Decreto 485/2019 y el RITE."),
    tarjetas("Agua y aire", "1 · El aire del recinto", "En una piscina cubierta, el agua se nota en el aire", [
        ("Evaporación", "La lámina de agua cede vapor sin parar: sube la humedad y se pierde calor del vaso."),
        ("Cloraminas", "El cloro combinado del agua pasa al aire como tricloramina: el olor a «piscina»."),
        ("Consecuencias", "Molestias respiratorias, condensaciones en paramentos, mohos y corrosión de estructuras metálicas."),
    ], cols=3, footer="Un agua con mucho **cloro combinado** acaba siendo un **aire irritante**: el Tema 5 y este tema van juntos."),
    tabla("Parámetros del aire", "A · Parámetros del aire", "Los valores del aire del recinto",
          ["Parámetro", "Valor", "Si se desvía"], [
              ("Temperatura del aire", "1–2 ºC por encima del agua, máx. 30 ºC", "Aire más frío: más evaporación. Más caliente: sensación de bochorno."),
              ("Humedad relativa", "< 65 %", "Por encima: condensaciones, mohos y corrosión. Muy baja: sequedad de piel y mucosas."),
              ("CO₂", "No más de 500 ppm sobre el aire exterior", "Aire cargado y somnolencia: la ventilación no basta."),
              ("Tricloramina", "Referencia OMS: 0,5 mg/m³", "Irritación de ojos, tos y asma. No es un límite legal."),
          ], nota="RD 742/2013, anexo II, y RITE IT 1.1.4.1.2. La regla de temperatura no se aplica a vasos de hidromasaje ni terapéuticos."),
    tarjetas("Aire y agua", "A · Relación térmica aire–agua", "El aire, un poco más caliente que el agua", [
        ("La regla", "Agua a 27 ºC: aire entre 28 y 29 ºC. Agua a 28 ºC: aire entre 29 y 30 ºC, que es el máximo."),
        ("Por qué", "El aire más frío admite menos vapor: crece la diferencia de presión de vapor con la lámina y el agua se evapora más."),
        ("Resultado", "Más evaporación, más humedad, más trabajo de la deshumectadora y más gasto en calentar el vaso."),
    ], cols=3, footer="El agua de una piscina climatizada está entre **24 y 30 ºC** según su uso (RITE IT 1.1.4.3.2)."),
    tarjetas("Humedad y CO₂", "B · Humedad relativa y CO₂", "Dos números que delatan una mala ventilación", [
        ("Humedad relativa", "Siempre por debajo del 65 %. Lo cómodo suele estar entre el 55 y el 60 %."),
        ("Punto de rocío", "Si una superficie fría baja del punto de rocío, el vapor condensa: mohos (Aspergillus, Penicillium) y corrosión de vigas y carpinterías."),
        ("CO₂", "Lo producen los bañistas al respirar. Si supera en más de 500 ppm al aire exterior, falta renovación."),
        ("Tricloramina", "Gas más pesado que el aire que se queda sobre la lámina. La ventilación debe barrer esa capa."),
    ], cols=2, light=True),
    apoyo_visual("El recinto del vaso", [
        ("8.1 · Condensaciones", "Imagen 8.1 · Cristalera de piscina cubierta con condensación y moho en la carpintería"),
        ("8.2 · Termohigrómetro", "Imagen 8.2 · Termohigrómetro y medidor de CO₂ en el recinto del vaso"),
    ], label="Imágenes · recinto"),
    tarjetas("Deshumectación", "2 · Deshumectación y ventilación", "Tres formas de quitar el vapor", [
        ("Deshumectadora frigorífica", "El vapor condensa en la batería fría del evaporador; el calor recuperado vuelve al aire o al agua del vaso."),
        ("Aire exterior", "Se renueva el aire con aire exterior más seco, pasando por un recuperador de calor."),
        ("UTA de piscina", "Combina las dos y regula el aire exterior con las sondas de humedad y CO₂."),
    ], cols=3, footer="El RITE obliga a **recuperar la energía del aire expulsado** en las piscinas climatizadas."),
    apoyo_visual("La UTA de una piscina cubierta", [
        ("8.3 · Esquema de la UTA", "Imagen 8.3 · Diagrama de flujo: extracción de aire húmedo, recuperador de calor, circuito frigorífico deshumectador y aporte de aire exterior filtrado"),
    ], label="Infografía · UTA"),
    tarjetas("Ventilación", "A · Ventilación y depresión", "Lo que exige el RITE", [
        ("Aire exterior", "Al menos 2,5 dm³/s por m² de lámina de agua y playa, más el necesario para controlar la humedad."),
        ("Depresión", "El recinto del vaso, entre 20 y 40 Pa por debajo de vestuarios y pasillos: la humedad y el olor no salen."),
        ("Calidad del aire", "Las piscinas son locales IDA 2: aire interior de buena calidad."),
    ], cols=3, footer="RITE, IT 1.1.4.2.3. Si al abrir una puerta el aire **sale** del recinto, la depresión no funciona."),
    tarjetas("Mantenimiento de la UTA", "B · Mantenimiento preventivo", "Una UTA sucia es un recinto húmedo", [
        ("Filtros", "Revisión mensual del prefiltro y del filtro fino (G4 y F7, hoy clasificados según UNE-EN ISO 16890). Un filtro saturado baja el caudal y sube la humedad."),
        ("Bandeja de condensados", "Limpieza y desinfección periódicas y desagüe libre: agua estancada y tibia favorece Legionella y hongos."),
        ("Ventiladores y compuertas", "Tensión y desgaste de correas, rodamientos y funcionamiento de las compuertas motorizadas de aire exterior."),
    ], cols=3),
    pasos("Menos evaporación", "3 · Reducir la evaporación", "Ahorro de energía al cerrar", [
        ("Cerrar la instalación", "Comprobar que no queda nadie en el vaso."),
        ("Parar la agitación", "Cascadas, chorros, hidromasaje y juegos de agua apagados."),
        ("Desplegar la manta", "Manta térmica flotante sobre toda la lámina, sin huecos."),
        ("Ajustar la UTA", "Modo nocturno según el fabricante: menos deshumectación con la manta puesta."),
        ("Recoger la manta", "Antes de abrir, enrollarla y revisar que no quede agua sobre ella."),
        ("Registrar", "Temperatura, humedad y CO₂ al abrir, en el libro de registro."),
    ], notes="La manta puede reducir la evaporación en torno al 90 % según el modelo. En piscinas climatizadas es obligatoria fuera de servicio (RITE IT 1.2.4.5.5)."),
    apoyo_visual("Ahorro energético", [
        ("8.4 · Manta térmica", "Imagen 8.4 · Enrollador con manta térmica desplegada sobre el vaso al cierre"),
        ("8.5 · Filtros de la UTA", "Imagen 8.5 · Filtro de la UTA saturado junto a uno nuevo"),
    ], label="Imágenes · mantenimiento"),
    alerta("Alerta de seguridad · PRL", "Cloraminas acumuladas en el aire",
           "Sin una ventilación adecuada, la tricloramina se acumula justo sobre la lámina, en la zona donde respiran los nadadores y los socorristas. Provoca tos irritativa, picor de ojos y puede desencadenar crisis de asma. Si al entrar notas un olor picante intenso a «cloro», aumenta de inmediato el aire exterior y revisa el cloro combinado del agua.",
           [("Ventilar", "Más aire exterior, ya."),
            ("Medir el agua", "Cloro combinado ≤ 0,6 mg/L."),
            ("Avisar", "Si hay bañistas con tos o picor de ojos."),
            ("Registrar", "La incidencia y lo que se hizo.")]),
    normativa("Qué exige la norma", [
        ("RD 742/2013 · anexos II y III", "Temperatura, humedad y CO₂ del aire: medición y registro al menos una vez al día en piscinas cubiertas."),
        ("RITE · IT 1.1.4", "Temperatura del aire (máx. 30 ºC), HR < 65 %, aire exterior y depresión de 20–40 Pa."),
        ("RITE · IT 1.2.4.5.5", "Barreras térmicas sobre la lámina cuando la piscina está fuera de servicio."),
    ], destacado=("< 65 %", "Humedad relativa máxima del aire del recinto: el mismo límite en el RD 742/2013 y en el RITE.")),
    preguntas([
        "Con el agua a 28 ºC, ¿a qué temperatura debe estar el aire del recinto?",
        "¿Cuál es el límite de humedad relativa del aire en una piscina cubierta?",
        "¿Qué aporta la manta térmica al cerrar una piscina climatizada?",
    ]),
    respuestas([
        ("B", "Entre 29 y 30 ºC: de 1 a 2 ºC por encima del agua y sin pasar de 30 ºC."),
        ("B", "Por debajo del 65 %, para evitar condensaciones, mohos y corrosión."),
        ("B", "Reduce mucho la evaporación (en torno al 90 %) y el gasto en deshumectación y calentamiento. Fuera de servicio es obligatoria."),
    ]),
    taller("2.4", "Climatización y deshumectación", "4 horas · sala de climatización y recinto del vaso", [
        "Termohigrómetro digital calibrado y anemómetro",
        "Medidor de CO₂ de pared y medidor portátil",
        "UTA de demostración con prefiltro y filtro fino",
        "Enrollador con manta térmica",
        "EPI: calzado de seguridad, guantes y ropa de trabajo",
    ], [
        "Medir la temperatura del agua y la temperatura y humedad del aire",
        "Medir el CO₂ dentro y fuera y comparar",
        "Inspeccionar y cambiar los filtros de la UTA",
        "Desplegar y ajustar la manta térmica en el vaso didáctico",
        "Cumplimentar el registro de parámetros ambientales",
    ]),
    cierre("Tema 8", [
        ("1–2 ºC más", "El aire, por encima del agua y como máximo a 30 ºC."),
        ("Menos de 65 %", "Humedad relativa: si no, condensación y moho."),
        ("+500 ppm", "El CO₂ delata la falta de renovación."),
        ("Manta al cerrar", "Menos evaporación y menos gasto, y lo exige el RITE."),
    ], "Siguiente · UF3 · Tema 9 · Bombas de filtración y de achique"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF2-T8-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T8")
    print(deck.build(out, html_preview=preview))
