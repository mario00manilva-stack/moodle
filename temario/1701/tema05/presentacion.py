"""MF2522_2 · UF2 · Tema 5 — presentación SCORM. Texto base: redacción de Mario (14/10/2026).

Valores comprobados contra el RD 742/2013 consolidado y su corrección de errores (BOE-A-2013-11796):
Anexo I (valores paramétricos y cierre), art. 12 (incumplimientos) y art. 13 (incidencias). Doble
control diario de Andalucía: Decreto 485/2019, Anexo III. El potencial REDOX no tiene valor de cierre.

    python3 -I temario/1701/tema05/presentacion.py   ->  entregas/MF2522_2-UF2-T5-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF2 · Tema 5", ident="MF2522_2_UF2_T5",
            title="Parámetros indicadores de la calidad del agua de baño según el RD 742/2013 y el Decreto 485/2019",
            item_title="Tema 5 - Parametros de calidad del agua")

deck.add(
    portada("MF2522_2 · UF2 · Tema 5",
            "Parámetros de calidad del agua de baño",
            "pH, cloro libre y combinado, turbidez, transparencia, ácido isocianúrico y REDOX: qué se mide, cuánto se tolera y cuándo se cierra el vaso.",
            "10 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019",
            notes="Abre la UF2. Es el tema de referencia para el control diario del agua."),
    ficha("10 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el laboratorio de análisis.",
          "Identificar, medir e interpretar pH, cloro libre y combinado, turbidez, ácido isocianúrico y REDOX, aplicando "
          "las tolerancias y los criterios de cierre del RD 742/2013 y del Decreto 485/2019."),
    tarjetas("Por qué se controla", "Relevancia operativa", "El agua del vaso recibe contaminación sin parar", [
        ("Eficacia desinfectante", "Que el desinfectante elimine bacterias y virus en segundos."),
        ("Confort del bañista", "Sin irritación de piel, mucosas ni ojos."),
        ("Protección de la instalación", "Sin corrosión de metales ni incrustación en bombas y tuberías."),
    ], cols=3, intro="Los bañistas aportan sudor, cremas solares y restos de piel; el entorno, polvo, hojas y radiación solar. Mantener los parámetros en rango persigue tres objetivos:"),
    tarjetas("Marco normativo", "Marco normativo", "Dos normas, una sobre otra", [
        ("RD 742/2013 · estatal", "Criterios técnico-sanitarios básicos: los parámetros del agua y sus valores (Anexo I), los incumplimientos (art. 12) y las incidencias (art. 13)."),
        ("D 485/2019 · Andalucía", "Reglamento Técnico-Sanitario de las Piscinas en Andalucía: desarrolla y endurece la norma estatal, por ejemplo con el doble control diario."),
    ], cols=2, footer="La norma estatal es el mínimo. Cuando la andaluza la endurece, en Andalucía se cumple la andaluza."),
    tabla("Tabla de parámetros", "RD 742/2013 · Anexo I", "Valores del agua del vaso y cierre",
          ["Parámetro", "Valor paramétrico", "Cierre del vaso"], [
              ("pH", "7,2 – 8,0", "Por debajo de 6,0 o por encima de 9,0"),
              ("Cloro libre residual", "0,5 – 2,0 mg/L Cl₂", "Ausencia o más de 5 mg/L"),
              ("Cloro combinado residual", "≤ 0,6 mg/L Cl₂", "Más de 3 mg/L"),
              ("Turbidez", "≤ 5 UNF", "Más de 20 UNF"),
              ("Transparencia", "Desagüe de fondo bien visible", "No se ve el desagüe de fondo"),
              ("Ácido isocianúrico", "≤ 75 mg/L, si se usan derivados del ácido tricloroisocianúrico", "Más de 150 mg/L"),
              ("Potencial REDOX", "250 – 900 mV, si el desinfectante no es cloro ni bromo", "Sin valor de cierre propio"),
          ], nota="En todos los casos de cierre, el vaso permanece cerrado hasta que el valor se normaliza."),
    tarjetas("pH", "A · Potencial de hidrógeno", "pH: el que manda sobre los demás", [
        ("Qué mide", "La acidez o basicidad del agua, en una escala de 0 a 14."),
        ("Rango legal", "7,2 a 8,0. Si sale de ese rango, se calcula el índice de Langelier, que debe quedar entre −0,5 y +0,5."),
        ("Efecto", "Por encima de 8,0 el cloro pierde eficacia; por debajo de 7,2 el agua se vuelve agresiva y corrosiva."),
    ], cols=3, footer="**Cierre** con pH por debajo de 6,0 o por encima de 9,0, hasta que el valor se normalice."),
    tarjetas("Cloro libre y combinado", "B y C · Cloro libre y cloro combinado", "El cloro que desinfecta y el que irrita", [
        ("Cloro libre residual", "Ácido hipocloroso e hipoclorito: el desinfectante activo. Rango 0,5 a 2,0 mg/L. Cierre si falta por completo o supera 5 mg/L."),
        ("Cloro combinado residual", "Cloraminas: el cloro que ha reaccionado con sudor y orina. Da el olor a piscina e irrita los ojos. Hasta 0,6 mg/L. Cierre por encima de 3 mg/L y, en cubiertas, más renovación de aire."),
    ], cols=2, footer="**Combinado = total − libre.** Con el DPD1 se lee el cloro libre y con el DPD3 el total; el combinado sale de la resta."),
    tarjetas("Turbidez y transparencia", "D · Turbidez y transparencia", "Ver el fondo es una cuestión de seguridad", [
        ("Turbidez", "Partículas en suspensión. Hasta 5 UNF. Cierre por encima de 20 UNF."),
        ("Transparencia", "Desde la playa debe verse con claridad el desagüe de fondo. Si no se ve, el vaso se cierra: un bañista en apuros en el fondo no se vería."),
    ], cols=2, light=True),
    tarjetas("Ácido isocianúrico", "E · Ácido isocianúrico", "El estabilizante que puede bloquear el cloro", [
        ("Qué es", "Lo aportan los cloros estabilizados (dicloro y tricloro) para proteger el cloro de la radiación solar."),
        ("Límite", "Hasta 75 mg/L. Se controla cuando se usan derivados del ácido tricloroisocianúrico."),
        ("Cierre", "Por encima de 150 mg/L el cloro queda bloqueado: el vaso se cierra y se renueva agua para diluirlo."),
    ], cols=3, footer="El ácido isocianúrico no se consume: se acumula con cada dosis de cloro estabilizado. Solo baja renovando agua."),
    apoyo_visual("Leer los parámetros", [
        ("5.1 · Fotómetro y DPD", "Imagen 5.1 · Fotómetro de campo con la cubeta de lectura de cloro libre (DPD1) teñida de rosa"),
        ("5.2 · Transparencia", "Imagen 5.2 · Desagüe de fondo visto desde la playa: agua transparente frente a agua turbia"),
        ("5.3 · pH con rojo de fenol", "Imagen 5.3 · Comparador de pH con rojo de fenol y su escala de color"),
    ], label="Imágenes · lectura"),
    tarjetas("Frecuencias", "Frecuencias de control", "Cada cuánto se mide", [
        ("Rutina · RD 742/2013", "Al menos una vez al día, antes de abrir: pH, desinfectante residual, turbidez, transparencia, temperatura y tiempo de recirculación."),
        ("Rutina · Andalucía", "En piscinas públicas y de chapoteo, dos veces al día y al menos una en horas de máxima afluencia (D 485/2019, Anexo III)."),
        ("Periódico · mensual", "Laboratorio: todos los parámetros del Anexo I, también Escherichia coli y Pseudomonas aeruginosa."),
    ], cols=3, footer="Además, **control inicial** antes de abrir la temporada o tras un cierre prolongado."),
    tarjetas("Puntos de muestreo", "Dónde se toma la muestra", "El agua que toca el bañista", [
        ("Profundidad", "Entre 20 y 30 cm bajo la superficie: ni el film superficial ni el fondo."),
        ("Posición", "En la zona de baño de más uso, lejos de las boquillas de impulsión y de skimmers o rebosadero."),
        ("Vasos grandes", "Varios puntos: esquinas y centro de los laterales."),
    ], cols=3, footer="Muestrear en el circuito sirve para diagnosticar la instalación, pero el dato que exige la norma es el del vaso."),
    apoyo_visual("Tomar la muestra", [
        ("5.4 · Puntos de muestreo", "Imagen 5.4 · Planta del vaso con los puntos de muestra: esquinas y centro de los laterales, lejos de impulsión y skimmers"),
        ("5.5 · Toma a 20–30 cm", "Imagen 5.5 · Operario tomando la muestra con el brazo sumergido a 20–30 cm de profundidad"),
        ("5.6 · Envase microbiológico", "Imagen 5.6 · Envase estéril con neutralizante para la muestra de laboratorio"),
    ], label="Imágenes · muestreo"),
    pasos("Fuera de rango", "Si un valor se sale", "Actuar y dejarlo escrito", [
        ("Valorar el riesgo", "¿Hay criterio de cierre o riesgo para la salud?"),
        ("Cerrar si procede", "Hasta normalizar; también con heces o vómito en el agua."),
        ("Investigar la causa", "Dosificación, filtración, carga de bañistas, aporte."),
        ("Corregir", "pH, cloro, floculación, contralavado o renovación."),
        ("Volver a medir", "Confirmar el valor antes de reabrir."),
        ("Registrar", "Valor, hora, medida aplicada, cierre y reapertura."),
    ]),
    alerta("Alerta de seguridad · PRL", "Reactivos de análisis in situ",
           "Las pastillas DPD1, DPD3 y rojo de fenol no se tocan con los dedos: la grasa de la piel altera el resultado. Usa tubos y cubetas limpios, enjuagados antes con la propia agua del vaso.",
           [("Guantes", "Nitrilo durante el análisis."),
            ("Ojos", "Gafas de seguridad."),
            ("Reactivos", "En fecha y bien cerrados."),
            ("Cubetas", "Limpias y enjuagadas con agua del vaso.")]),
    apoyo_visual("Reactivos bien usados", [
        ("5.7 · Pastilla sin tocar", "Imagen 5.7 · Pastilla DPD dejada caer desde el blíster directamente en la cubeta"),
        ("5.8 · Cubeta enjuagada", "Imagen 5.8 · Enjuague de la cubeta con agua del vaso antes de la lectura"),
    ], label="Imágenes · reactivos"),
    normativa("Qué exige la normativa en Andalucía", [
        ("D 485/2019 · Anexo III", "Dos controles diarios en piscinas públicas y de chapoteo, uno en horas de máxima afluencia, con la hora anotada."),
        ("RD 742/2013 · art. 12", "Ante un incumplimiento: investigar la causa, corregir, informar a la autoridad sanitaria si lo dispone y dejarlo registrado."),
        ("SILOÉ", "Los datos del autocontrol se vuelcan en SILOÉ. Las incidencias (ahogamientos, lesiones, intoxicaciones) se comunican a la autoridad sanitaria."),
    ], destacado=("2 / día", "En Andalucía, una lectura antes de abrir no basta: la segunda, en la hora de más bañistas."),
       notes="El volcado en SILOÉ se trata a fondo en el Tema 14."),
    preguntas([
        "¿Cuál es el rango legal del pH del agua del vaso?",
        "En el control de la mañana mides 0,0 mg/L de cloro libre. ¿Qué exige la norma?",
        "¿A partir de qué valor de ácido isocianúrico hay que cerrar el vaso?",
    ]),
    respuestas([
        ("B", "Entre 7,2 y 8,0 (RD 742/2013, Anexo I). Fuera de ese rango se calcula el índice de Langelier."),
        ("B", "Cierre inmediato hasta recuperar el cloro libre entre 0,5 y 2,0 mg/L. La ausencia de cloro, o más de 5 mg/L, obliga a cerrar."),
        ("C", "Por encima de 150 mg/L. El valor paramétrico es de hasta 75 mg/L, pero el cierre llega al superar 150."),
    ]),
    taller("2.1", "Analítica físico-química in situ", "4 horas · laboratorio", [
        "Fotómetros de campo y comparadores DPD (UNE-ISO 17381)",
        "Reactivos DPD1, DPD3 y rojo de fenol",
        "Turbidímetro portátil, medidor REDOX y pH-metro de electrodo",
        "Muestras de agua con parámetros alterados",
        "EPI: guantes de nitrilo, gafas de seguridad y bata",
    ], [
        "Tomar la muestra en el vaso a 20–30 cm de profundidad",
        "Medir pH, cloro libre y cloro combinado con fotómetro calibrado",
        "Determinar la turbidez y comprobar la transparencia del fondo",
        "Comparar los resultados con la tabla de valores y de cierre",
        "Cumplimentar la hoja de control diario del libro de registro",
    ]),
    cierre("Tema 5", [
        ("pH primero", "7,2–8,0. Cierre por debajo de 6,0 o por encima de 9,0."),
        ("Libre y combinado", "Libre 0,5–2,0; combinado hasta 0,6. Sin cloro, se cierra."),
        ("Ver el fondo", "Si no se ve el desagüe, el vaso se cierra."),
        ("Dos veces al día", "En Andalucía, una en la hora de más bañistas."),
    ], "Siguiente · Tema 6 · Sistemas de desinfección y corrección química"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF2-T5-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T5")
    print(deck.build(out, html_preview=preview))
