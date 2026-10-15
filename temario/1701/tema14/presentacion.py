"""MF2522_2 · UF4 · Tema 14 — presentación SCORM. Texto base: redacción de Mario (15/10/2026).

Contrastado con el BOE (RD 742/2013 consolidado) y el BOJA núm. 108 de 2019 (Decreto 485/2019):
- Control de rutina: RD 742/2013, al menos 1 vez al día, por la mañana antes de abrir; D 485/2019
  (anexo III): en piscinas públicas y de chapoteo, 2 veces al día, una en horas de máxima afluencia.
- Incumplimientos (RD 742 art. 12: fuera de los anexos I a III) e incidencias (art. 13 y anexo V:
  ahogamientos, lesiones medulares, traumatismos, quemaduras graves, electrocución, intoxicación…) son
  cosas distintas. Las incidencias se comunican a la Delegación con el anexo VII del D 485/2019, «a la
  mayor brevedad posible y en todo caso antes de cinco días» (art. 17.9), no «hábiles».
- SILOÉ: RD 742/2013 art. 15 (redacción del RD 3/2023): piscinas de uso público, datos del anexo IV
  antes del 30 de abril; partes A y B, al menos cada 5 años si no cambian. El RD 3/2023 no la «hace
  obligatoria»: ya lo era. Anexo IV: A instalación, B tratamiento, C muestreos por vasos.
- Registros: modelos de los anexos V (rutina), VI (periódico) y VII (incidencias) del D 485/2019.
- Falsear registros: alterar el protocolo es infracción grave (D 485/2019 art. 22).

    python3 -I temario/1701/tema14/presentacion.py   ->  entregas/MF2522_2-UF4-T14-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF4 · Tema 14", ident="MF2522_2_UF4_T14",
            title="Cumplimentación del libro de registro diario y procedimiento de alta, notificación y vuelco de datos en SILOÉ",
            item_title="Tema 14 - Libro de registro y SILOE")

deck.add(
    portada("MF2522_2 · UF4 · Tema 14",
            "Libro de registro y SILOÉ",
            "Qué se anota cada día, qué se comunica a Sanidad cuando algo va mal y cómo se envían los datos anuales de la piscina al sistema SILOÉ.",
            "7 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019",
            notes="Último tema del módulo MF2522_2."),
    ficha("7 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el aula de informática.",
          "Cumplimentar el registro diario y periódico de la piscina, comunicar las incidencias con el anexo VII del "
          "Decreto 485/2019 en menos de cinco días y notificar los datos anuales en SILOÉ conforme al anexo IV del RD 742/2013."),
    tabla("Registros", "1 · El registro de la piscina", "Qué se anota y cada cuánto",
          ["Control", "Frecuencia mínima", "Qué se anota"], [
              ("Rutina", "Diario, por la mañana antes de abrir. En Andalucía, en piscinas públicas y de chapoteo, 2 veces al día (una en máxima afluencia)", "pH, desinfectante residual, turbidez, transparencia, temperatura, tiempo de recirculación; en cubiertas, aire."),
              ("Periódico", "Mensual, en laboratorio", "Todos los parámetros de los anexos I y II."),
              ("Inicial", "Antes de abrir y tras más de 2 semanas cerrado", "Todos los parámetros, en laboratorio."),
              ("Contadores", "Con el control de rutina", "Lecturas de agua de aporte y de recirculación."),
              ("Incumplimientos e incidencias", "En el momento", "Qué pasó, causa y medidas correctoras y preventivas."),
          ], nota="RD 742/2013 y D 485/2019, anexo III. Modelos: anexo V (rutina) y anexo VI (periódico) del D 485/2019. Una hoja por vaso."),
    apoyo_visual("La hoja de registro", [
        ("14.1 · Hoja de control de rutina", "Imagen 14.1 · Hoja de registro con fecha, hora, pH, cloro libre, turbidez, contadores, firma y observaciones"),
    ], label="Imagen · registro"),
    tarjetas("Incumplimiento o incidencia", "2 · Incumplimiento e incidencia", "No son lo mismo", [
        ("Incumplimiento", "Un parámetro fuera de los valores de los anexos I a III (pH, cloro, turbidez, E. coli…). Se investiga la causa, se corrige y se registra; se cierra el vaso si lo indica la norma."),
        ("Incidencia", "Un daño a personas: ahogamientos, lesiones medulares, traumatismos craneoencefálicos, quemaduras graves, electrocución o intoxicación química."),
        ("Comunicación", "Las incidencias se comunican a la Delegación Territorial de Salud con el anexo VII, lo antes posible y siempre antes de cinco días."),
    ], cols=3, footer="RD 742/2013 arts. 12 y 13 y **D 485/2019 art. 17.9**. Las dos cosas se anotan en el protocolo con sus medidas."),
    pasos("Ante una incidencia", "A · Qué hacer ante una incidencia", "Paso a paso", [
        ("Atender", "Socorrista, primeros auxilios y 112."),
        ("Proteger", "Cerrar el vaso o la zona si hay riesgo para otros."),
        ("Investigar", "Causas: instalación, agua, productos, uso."),
        ("Corregir", "Medidas correctoras y preventivas."),
        ("Comunicar", "Anexo VII a la Delegación, antes de 5 días."),
        ("Registrar", "Todo, en el protocolo de autocontrol."),
    ]),
    tarjetas("SILOÉ", "3 · SILOÉ", "El sistema de información de piscinas del Ministerio de Sanidad", [
        ("Quién", "Las piscinas de uso público: tipo 1 (el agua es la actividad principal) y tipo 2 (servicio complementario, como hoteles o campings)."),
        ("Cuándo", "Los datos del año anterior, **antes del 30 de abril** de cada año."),
        ("Partes A y B", "Si no cambian, al menos cada 5 años."),
    ], cols=3, footer="RD 742/2013, art. 15 (redacción del RD 3/2023). Dirección: siloe.sanidad.gob.es. En Andalucía, el D 485/2019 (art. 17.8) permite llevar en SILOÉ los datos del anexo IV."),
    tabla("Anexo IV", "A · Qué se notifica", "Las tres partes del anexo IV",
          ["Parte", "Contenido"], [
              ("A · Instalación", "Localización, denominación, tipo de piscina, origen del agua y vasos: clase, volumen, superficie, cubierto o descubierto."),
              ("B · Tratamiento", "Filtración y velocidad máxima, desinfección, floculantes y otros tratamientos de cada vaso."),
              ("C · Muestreos por vasos", "Por temporada y parámetro: muestreos realizados y conformes, valores medio, máximo y mínimo, y días con incumplimiento."),
          ]),
    apoyo_visual("SILOÉ", [
        ("14.2 · Partes de SILOÉ", "Imagen 14.2 · Esquema de la aplicación SILOÉ con las partes A (instalación), B (tratamiento) y C (muestreos)"),
    ], label="Infografía · SILOÉ"),
    pasos("Notificar en SILOÉ", "B · La notificación anual", "Paso a paso", [
        ("Reunir datos", "Registros diarios, análisis mensuales y contadores del año."),
        ("Acceder", "A siloe.sanidad.gob.es con el usuario de la piscina."),
        ("Parte A", "Comprobar o dar de alta la instalación y sus vasos."),
        ("Parte B", "Tratamiento de cada vaso."),
        ("Parte C", "Resumen de muestreos por vaso y parámetro."),
        ("Enviar y guardar", "Antes del 30 de abril, con copia en el protocolo."),
    ]),
    alerta("Alerta · ética profesional", "Los registros no se maquillan",
           "Anotar valores correctos cuando el agua está fuera de rango oculta riesgos reales para los bañistas, como infecciones por E. coli o Pseudomonas. Alterar el protocolo de autocontrol es una infracción grave y puede acarrear responsabilidades al técnico y al titular.",
           [("Real", "Anotar lo que se mide."),
            ("Corregir", "Y anotar la medida tomada."),
            ("Firmar", "Cada registro."),
            ("Guardar", "Las hojas y los boletines.")]),
    normativa("Notificaciones y plazos", [
        ("D 485/2019 · art. 17.9", "Incidencias a la Delegación con el anexo VII, antes de cinco días."),
        ("RD 742/2013 · art. 15", "Datos del anexo IV en SILOÉ antes del 30 de abril."),
        ("D 485/2019 · art. 22", "Alterar u ocultar el protocolo es una infracción grave."),
    ], destacado=("30 de abril", "Fecha límite para notificar en SILOÉ los datos del año anterior.")),
    preguntas([
        "En Andalucía, ¿cuántas veces al día se hace el control de rutina en una piscina pública?",
        "¿Cuál es la fecha límite para notificar los datos anuales en SILOÉ?",
        "¿Cuál es el plazo para comunicar una incidencia con el anexo VII?",
    ]),
    respuestas([
        ("B", "Dos veces al día, una de ellas en horas de máxima afluencia."),
        ("B", "El 30 de abril de cada año, con los datos del año anterior."),
        ("B", "Lo antes posible y siempre antes de cinco días."),
    ]),
    taller("4.2", "Registro diario y notificación en SILOÉ", "4 horas · aula de informática", [
        "Modelos de los anexos V, VI y VII del Decreto 485/2019",
        "Entorno simulado de SILOÉ",
        "Casos prácticos con boletines de laboratorio",
        "Ordenador con hoja de cálculo",
    ], [
        "Cumplimentar un mes de registros de rutina",
        "Simular el alta de una piscina tipo 2 y sus vasos (parte A)",
        "Configurar el tratamiento de cada vaso (parte B)",
        "Redactar la comunicación de una incidencia (anexo VII)",
        "Simular la notificación anual de muestreos (parte C)",
    ]),
    cierre("Tema 14", [
        ("Cada día", "Rutina antes de abrir; en Andalucía, dos veces en piscinas públicas."),
        ("Incidencia ≠ incumplimiento", "Daño a personas: anexo VII antes de 5 días."),
        ("30 de abril", "Datos del año anterior en SILOÉ."),
        ("Registros reales", "Lo que se mide, lo que se hace y quién lo firma."),
    ], "Fin del módulo MF2522_2 · Control de organismos nocivos en piscinas"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF4-T14-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T14")
    print(deck.build(out, html_preview=preview))
