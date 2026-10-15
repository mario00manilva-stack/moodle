"""MF2522_2 · UF2 · Tema 7 — presentación SCORM. Texto base: redacción de Mario (15/10/2026).

Correcciones sobre el texto base, contrastadas con el BOE:
- RD 742/2013, anexo I: el indicador es Legionella spp. (no solo L. pneumophila), < 100 UFC/L y solo en
  vasos climatizados con aerosolización. Ante E. coli o P. aeruginosa: cierre del vaso y medidas
  correctoras; la dosis de la cloración de choque la fija el protocolo de autocontrol y el fabricante.
- RD 487/2022, art. 7: el titular elige entre un PPCL (el punto de partida) o un PSL (opcional, basado
  en la evaluación del riesgo); ninguno de los dos es «exigible» frente al otro.
- RD 487/2022, anexo I.7: aplica a sistemas de agua a 24 ºC o más con aerosolización (hidromasaje,
  spas, vasos con dispositivos de juego, setas, cortinas, cascadas) y a las redes de agua sanitaria.
- Frecuencia de Legionella: mensual en spas e hidromasajes y trimestral en agua sanitaria (anexo V,
  tabla 3). Medidas por recuento (tablas 8 y 9): de 100 a < 1 000 UFC/L, revisión, limpieza y
  desinfección; desde 1 000 UFC/L, parada, vaciado, limpieza y desinfección; en ambos casos nueva
  muestra a los 15–30 días. Choque en spas: recirculación con el biocida al menos 10 h (anexo IV, C).
  ACS: 70 ºC durante 2 h en los acumuladores (anexo IV, A). Registros: al menos 5 años (art. 8.5).

    python3 -I temario/1701/tema07/presentacion.py   ->  entregas/MF2522_2-UF2-T7-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF2 · Tema 7", ident="MF2522_2_UF2_T7",
            title="Determinaciones analíticas in situ, control microbiológico y criterios de aplicación del RD 487/2022 para Legionella",
            item_title="Tema 7 - Analitica in situ y control microbiologico")

deck.add(
    portada("MF2522_2 · UF2 · Tema 7",
            "Analítica in situ y control microbiológico",
            "Medir el agua con fotómetro, sondas y turbidímetro, interpretar los análisis de laboratorio y saber cuándo entra en juego el RD 487/2022 frente a Legionella.",
            "10 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019 · RD 487/2022",
            notes="Sigue a los Temas 5 y 6: allí se vieron los parámetros y cómo se corrigen; aquí, cómo se miden y se verifican."),
    ficha("10 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el laboratorio y el vaso de hidromasaje didáctico.",
          "Realizar determinaciones analíticas in situ con fotómetro y reactivos, interpretar los resultados microbiológicos "
          "(E. coli, Pseudomonas aeruginosa, Legionella spp.) y aplicar los criterios del RD 487/2022 para saber en qué "
          "instalaciones hay que implantar un plan frente a Legionella."),
    tabla("Equipos de medida", "1 · Métodos de análisis in situ", "Qué mide cada equipo",
          ["Método o equipo", "Parámetros", "Cómo funciona"], [
              ("Fotómetro digital", "Cloro libre y combinado, pH, ácido isocianúrico", "Mide cuánta luz absorbe la muestra coloreada con el reactivo."),
              ("Comparador de disco", "Cloro y pH básicos", "Se compara a simple vista el color con una escala patrón."),
              ("Sondas (electrometría)", "pH, potencial REDOX (mV), conductividad (µS/cm)", "Electrodos de vidrio o platino calibrados."),
              ("Turbidímetro portátil", "Turbidez (UNF)", "Mide la luz que dispersan las partículas en suspensión."),
          ], nota="Los kits y reactivos listos para usar se eligen y aplican según la norma UNE-ISO 17381 y las instrucciones del fabricante."),
    pasos("Medición fotométrica", "A · Protocolo de medición con DPD", "Cloro libre y cloro combinado, paso a paso", [
        ("Toma de muestra", "A 20–30 cm de profundidad y al menos a 1 m de las boquillas de impulsión."),
        ("Puesta a cero", "Cubeta con la muestra, cristal limpio con microfibra y «cero» en el equipo."),
        ("Cloro libre", "Pastilla DPD 1 triturada hasta disolverse y lectura inmediata."),
        ("Cloro total", "En la misma cubeta, DPD 3. Esperar el tiempo del fabricante (habitualmente 2 min) y leer."),
        ("Cloro combinado", "Cloro total menos cloro libre."),
        ("Registro", "Anotar valores, hora y punto de muestreo en el libro de registro."),
    ], notes="Si se lee el cloro libre tarde, las cloraminas empiezan a reaccionar con el DPD 1 y el valor sale más alto de lo real."),
    tarjetas("Cálculo", "A · Cloro combinado", "Una resta que hay que saber hacer", [
        ("Fórmula", "**Cloro combinado = cloro total (DPD 1 + DPD 3) − cloro libre (DPD 1).**"),
        ("Ejemplo", "DPD 1: 1,2 mg/L. Total tras DPD 3: 1,6 mg/L. Cloro combinado: 0,4 mg/L, dentro del límite."),
        ("Límite", "Hasta 0,6 mg/L de cloro combinado; cierre del vaso por encima de 3 mg/L (Tema 5)."),
    ], cols=3),
    apoyo_visual("La medición in situ", [
        ("7.1 · Toma de muestra", "Imagen 7.1 · Operario con guantes tomando agua del vaso a 20–30 cm de profundidad, lejos de las boquillas"),
        ("7.2 · Fotómetro", "Imagen 7.2 · Fotómetro digital con la cubeta y las pastillas DPD 1 y DPD 3"),
        ("7.3 · Sondas y turbidímetro", "Imagen 7.3 · Sonda de pH / REDOX y turbidímetro portátil en la sala técnica"),
    ], label="Imágenes · medición"),
    tabla("Control microbiológico", "2 · Control microbiológico", "Los indicadores del laboratorio",
          ["Indicador", "Valor paramétrico", "Qué indica"], [
              ("Escherichia coli", "0 UFC o NMP en 100 mL", "Contaminación fecal reciente."),
              ("Pseudomonas aeruginosa", "0 UFC o NMP en 100 mL", "Infecciones de oído y de piel."),
              ("Legionella spp.", "< 100 UFC/L", "Solo en vasos climatizados con aerosolización. Neumonía por inhalación de aerosoles."),
          ], nota="RD 742/2013, anexo I. El control periódico es **mensual**, en laboratorio, aunque los parámetros físico-químicos sean correctos."),
    pasos("Incidencia microbiológica", "B · Si aparece E. coli o Pseudomonas", "Actuación ante un resultado positivo", [
        ("Cerrar el vaso", "Sin bañistas desde que se conoce el resultado (RD 742/2013)."),
        ("Investigar la causa", "Revisar registros de cloro, pH, filtración y aforo de los últimos días."),
        ("Cloración de choque", "Con el vaso cerrado y recirculando, según el protocolo de autocontrol y el fabricante del producto."),
        ("Filtros", "Lavado a contracorriente y enjuague de los lechos filtrantes."),
        ("Nuevo análisis", "Con el desinfectante de nuevo en sus valores, nueva muestra. No se reabre hasta que dé 0 UFC."),
        ("Registrar y comunicar", "Incidencia, medidas y resultados. Informar a la autoridad sanitaria si así lo dispone."),
    ]),
    tarjetas("RD 487/2022", "3 · ¿Cuándo aplica el RD 487/2022?", "No todas las piscinas necesitan plan de Legionella", [
        ("No aplica al vaso", "Piscinas descubiertas de agua fría, sin chorros, juegos de agua ni aerosoles. El agua del vaso se controla con el RD 742/2013 y el D 485/2019."),
        ("Sí aplica", "Agua a 24 ºC o más con aerosolización: hidromasajes, spas, jacuzzis, bañeras terapéuticas, vasos con chorros, setas, cortinas o cascadas."),
        ("Y también", "La red de agua sanitaria de la instalación: agua caliente (ACS) y fría de vestuarios y duchas."),
    ], cols=3, footer="Una piscina descubierta y fría queda fuera, pero **sus duchas sí entran**: la red de ACS se controla siempre."),
    apoyo_visual("Dónde aplica el RD 487/2022", [
        ("7.4 · Piscina descubierta", "Imagen 7.4 · Piscina al aire libre de agua fría sin chorros: «RD 742/2013 · sin plan de Legionella para el vaso»"),
        ("7.5 · Spa climatizado", "Imagen 7.5 · Spa con chorros de aire y agua en vaso climatizado: «RD 487/2022 · PPCL o PSL»"),
    ], label="Infografía · aplicabilidad"),
    tarjetas("PPCL y PSL", "A · Los planes frente a Legionella", "El titular elige uno de los dos", [
        ("PPCL", "Plan de Prevención y Control de Legionella. Es el punto de partida y cumple, como mínimo, los anexos del real decreto."),
        ("PSL", "Plan Sanitario frente a Legionella. Opcional: se basa en una evaluación del riesgo con puntos críticos, medidas de control y correctoras."),
        ("Quién responde", "El titular de la instalación, aunque contrate el mantenimiento con una empresa externa."),
    ], cols=3),
    tabla("Muestreo de Legionella", "B · Frecuencia mínima de muestreo", "Cada cuánto se analiza Legionella spp.",
          ["Instalación", "Legionella spp.", "pH, temperatura, turbidez y biocida"], [
              ("Spas, hidromasajes y vasos con aerosolización (≥ 24 ºC)", "Mensual", "Diario"),
              ("Agua sanitaria (ACS y agua fría)", "Trimestral", "pH diario · temperatura diaria y rotatoria"),
          ], nota="RD 487/2022, anexo V, tabla 3. Tras una limpieza y desinfección, nueva determinación a los 15–30 días."),
    tabla("Actuación según recuento", "C · Qué hacer según el recuento", "Spas e hidromasajes: tres escalones",
          ["Legionella spp. (UFC/L)", "Medidas"], [
              ("No detectado o < 100", "Mantener los programas de mantenimiento y tratamiento."),
              ("≥ 100 y < 1 000", "Revisar los programas, limpieza y desinfección, y nueva muestra a los 15–30 días."),
              ("≥ 1 000", "Parar la instalación y vaciarla, limpiar y desinfectar antes de reabrir, y nueva muestra a los 15–30 días."),
          ], nota="RD 487/2022, anexo V, tabla 9. La autoridad sanitaria puede dictar otras medidas."),
    tarjetas("Tratamiento de choque", "D · Tratamiento de choque", "Cómo se desinfecta tras un positivo", [
        ("Spa o hidromasaje", "Prohibir el uso, vaciar, frotar paredes y depósitos, limpiar filtros y boquillas, llenar y recircular con el biocida al menos **10 horas**, controlando biocida y pH cada hora."),
        ("Acumuladores de ACS", "Choque térmico: subir el agua a **70 ºC y mantenerla 2 horas**. Si la instalación no lo permite, desinfección con biocida."),
        ("Biocidas", "Dosis, tiempo de contacto y neutralización según el fabricante y el PPCL."),
    ], cols=3, light=True),
    alerta("Alerta de seguridad · PRL", "Bioaerosoles al muestrear spas y redes de ACS",
           "Al tomar muestras o trabajar en la sala técnica de un spa, un hidromasaje o una red de ACS con sospecha de Legionella, se respiran los aerosoles que transmiten la enfermedad. Protección respiratoria con mascarilla FFP3 (UNE-EN 149) en todo momento.",
           [("FFP3", "Mascarilla autofiltrante UNE-EN 149."),
            ("Chorros parados", "Sin aerosoles mientras se muestrea."),
            ("Guantes de nitrilo", "Y frascos estériles."),
            ("RD 664/1997", "Exposición a agentes biológicos.")]),
    normativa("Responsabilidad y registros", [
        ("RD 487/2022 · art. 5", "El titular es el responsable del cumplimiento, aunque contrate el servicio con una empresa externa."),
        ("RD 487/2022 · art. 7", "El titular elige entre implantar un PPCL o un PSL."),
        ("RD 742/2013 y D 485/2019", "Control del agua del vaso y registro de los resultados en la instalación y en SILOÉ."),
    ], destacado=("5 años", "Tiempo mínimo de conservación de los registros y resultados analíticos del plan frente a Legionella.")),
    preguntas([
        "¿Cómo se calcula el cloro combinado con los reactivos DPD?",
        "¿Cuál es el valor paramétrico de Escherichia coli en el agua del vaso?",
        "¿Aplica el RD 487/2022 al vaso de una piscina descubierta de agua fría sin chorros ni aerosoles?",
    ]),
    respuestas([
        ("B", "Cloro total (DPD 1 + DPD 3) menos cloro libre (DPD 1)."),
        ("C", "0 UFC en 100 mL: ausencia total, igual que Pseudomonas aeruginosa."),
        ("B", "No: el vaso se rige por el RD 742/2013. Las redes de ACS y agua fría de sus duchas sí entran en el RD 487/2022."),
    ]),
    taller("2.3", "Analítica avanzada y muestreo", "4 horas · laboratorio y vaso de hidromasaje", [
        "Fotómetros multiparamétricos con DPD 1, DPD 3, rojo fenol y ácido cianúrico",
        "Frascos estériles con tiosulfato sódico para muestras microbiológicas",
        "Nevera portátil para el transporte de muestras",
        "Mascarillas FFP3 y guantes de nitrilo",
        "PPCL de ejemplo para cumplimentar",
    ], [
        "Medir cloro libre y total y calcular el cloro combinado",
        "Simular la toma estéril de una muestra para laboratorio",
        "Localizar los puntos críticos de Legionella del hidromasaje",
        "Cumplimentar la hoja de registro analítico",
        "Valorar qué medidas del plan frente a Legionella aplicar",
    ]),
    cierre("Tema 7", [
        ("Total menos libre", "El cloro combinado sale de una resta: DPD 1 y DPD 3."),
        ("Cero es cero", "E. coli y Pseudomonas: 0 UFC/100 mL o se cierra el vaso."),
        ("24 ºC y aerosoles", "Ahí entra el RD 487/2022, y en las redes de ACS siempre."),
        ("PPCL o PSL", "El titular elige, responde y guarda los registros 5 años."),
    ], "Siguiente · Tema 8 · Calidad del aire en piscinas cubiertas"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF2-T7-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T7")
    print(deck.build(out, html_preview=preview))
