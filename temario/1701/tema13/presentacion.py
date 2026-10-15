"""MF2522_2 · UF4 · Tema 13 — presentación SCORM. Texto base: redacción de Mario (15/10/2026).

Contrastado con el BOE (RD 742/2013 consolidado) y el BOJA núm. 108 de 2019 (Decreto 485/2019):
- Los 7 aspectos mínimos del protocolo son los del RD 742/2013 art. 11.5 y el D 485/2019 art. 17.6
  (tratamiento; control de calidad del agua y del aire; mantenimiento; limpieza y desinfección;
  seguridad y buenas prácticas; plagas; proveedores). La «revisión y mejora» no es uno de ellos: es la
  obligación de mantenerlo actualizado.
- El protocolo está en la piscina a disposición del personal de mantenimiento y de la autoridad
  sanitaria (no de los usuarios); el D 485/2019 art. 17.4 añade registrar incumplimientos e incidencias.
- La ocultación, alteración o ausencia del protocolo es infracción grave: D 485/2019 art. 22.b) 5.º
  (no el art. 17.4).
- Laboratorios: métodos acreditados UNE-EN ISO/IEC 17025 o, al menos, procedimientos validados
  (RD 742/2013 art. 9; D 485/2019 art. 9). No hay «inscripción del laboratorio en SILOÉ». Los kits in situ:
  UNE-ISO 17381.
- Personal: cualificación SEA757_2 (RD 46/2022), RD 742/2013 disp. adicional 3.ª (RD 3/2023).
- Plagas: evaluación al menos anual y antes de la temporada (D 485/2019 art. 11.2).

    python3 -I temario/1701/tema13/presentacion.py   ->  entregas/MF2522_2-UF4-T13-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF4 · Tema 13", ident="MF2522_2_UF4_T13",
            title="Elaboración y gestión del protocolo de autocontrol higiénico-sanitario de la piscina",
            item_title="Tema 13 - Protocolo de autocontrol")

deck.add(
    portada("MF2522_2 · UF4 · Tema 13",
            "El protocolo de autocontrol",
            "El documento donde la piscina organiza y deja por escrito cómo trata el agua, cómo la controla, cómo mantiene, limpia y protege la instalación, y con quién trabaja.",
            "8 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019",
            notes="Primer tema de la UF4. Recoge lo aprendido en las UF1, UF2 y UF3."),
    ficha("8 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el aula de informática.",
          "Diseñar, implantar y revisar el protocolo de autocontrol de una piscina, con los siete aspectos mínimos que fijan "
          "el RD 742/2013 (art. 11.5) y el Decreto 485/2019 de Andalucía (art. 17.6)."),
    tarjetas("Qué es", "1 · El protocolo de autocontrol", "El manual de funcionamiento sanitario de la piscina", [
        ("Específico", "Hecho a medida de cada piscina y de cada uno de sus vasos."),
        ("En la piscina", "Siempre en la propia instalación, a disposición del personal de mantenimiento y de la autoridad sanitaria."),
        ("Registro", "Recoge los controles, los incumplimientos y las incidencias con sus medidas, preferentemente en soporte informático."),
        ("Vivo", "Se actualiza con la frecuencia necesaria: cambios en la instalación, en la norma o problemas detectados."),
    ], cols=2, footer="Lo exige el **RD 742/2013 (art. 11.5)** y, en Andalucía, el **Decreto 485/2019 (art. 17.4 y 17.6)**. La Junta publica una guía para elaborarlo."),
    apoyo_visual("Los siete aspectos del protocolo", [
        ("13.1 · Mapa del protocolo", "Imagen 13.1 · Rueda con el protocolo de autocontrol en el centro y sus siete aspectos alrededor"),
    ], label="Infografía · protocolo"),
    tabla("Los 7 aspectos", "2 · Contenido mínimo", "Los siete aspectos que debe contemplar",
          ["Aspecto", "Qué recoge"], [
              ("a) Tratamiento del agua de cada vaso", "Esquema del circuito, productos (biocidas TP2, correctores, floculantes), dosificación y procedimientos de trabajo."),
              ("b) Control de la calidad del agua y del aire", "Controles inicial, de rutina y periódico, puntos de muestreo, métodos y laboratorio."),
              ("c) Mantenimiento", "Bombas, filtros, sondas, contadores, depósito de compensación, rejillas y sala técnica."),
              ("d) Limpieza y desinfección", "Vaso, playas, vestuarios y aseos: qué, cómo, con qué y cada cuánto."),
              ("e) Seguridad y buenas prácticas", "Prevención de accidentes, socorrismo, botiquín, información al público y emergencias."),
              ("f) Plan de control de plagas", "Evaluación, tratamientos y plazos de seguridad."),
              ("g) Proveedores y servicios", "Empresas, laboratorios, productos y personal, con su acreditación."),
          ], nota="RD 742/2013 art. 11.5 y D 485/2019 art. 17.6. La revisión periódica no es un apartado más: es la obligación de mantenerlo al día."),
    tarjetas("Tratamiento y control", "A · Tratamiento y control de calidad", "Aspectos a) y b)", [
        ("Tratamiento", "Esquema hidráulico de cada vaso y procedimientos normalizados de trabajo (PNT) de dosificación. Solo biocidas TP2 registrados."),
        ("Control del agua", "Rutina diaria in situ (Tema 14), periódico mensual en laboratorio y control inicial antes de abrir o tras más de dos semanas cerrado."),
        ("Laboratorio y kits", "Laboratorio con métodos acreditados UNE-EN ISO/IEC 17025 o, al menos, validados. Kits in situ conformes a UNE-ISO 17381."),
    ], cols=3),
    tarjetas("Mantenimiento y limpieza", "B · Mantenimiento y limpieza", "Aspectos c) y d)", [
        ("Mantenimiento", "Calendario de lavado de filtros, calibración de sondas, revisión de bombas, contadores, rejillas de fondo y almacén de productos (RD 656/2017)."),
        ("Limpieza y desinfección", "Vaso, playas, vestuarios, aseos y mobiliario: frecuencia (diaria, semanal, de choque), método y producto con su FDS."),
        ("Registro", "Quién lo hizo, cuándo y con qué: cada tarea firmada."),
    ], cols=3),
    tarjetas("Seguridad, plagas y proveedores", "C · Seguridad, plagas y proveedores", "Aspectos e), f) y g)", [
        ("Seguridad", "Reglamento de régimen interno a la vista, socorristas (desde 200 m² de lámina, D 485/2019 art. 17.10), botiquín, flotadores y plan de emergencia."),
        ("Plagas", "Evaluación al menos una vez al año y antes de la temporada, y tratamientos por empresa inscrita en el ROESB, respetando los plazos de seguridad."),
        ("Proveedores", "Productos con su registro, laboratorio acreditado y personal cualificado (SEA757_2 para el tratamiento)."),
    ], cols=3),
    tarjetas("Información al público", "D · Información al público", "Lo que el usuario debe poder ver (RD 742/2013, art. 14)", [
        ("Resultados", "Los últimos controles, con el vaso, la fecha y la hora."),
        ("Incumplimientos", "Qué no cumple, qué se ha hecho y recomendaciones sanitarias."),
        ("Prevención", "Material sobre ahogamientos, traumatismos y lesiones medulares; en exteriores, protección solar."),
        ("Contactos y normas", "Socorrista, centros sanitarios y emergencias más cercanos, productos químicos usados y normas de uso."),
    ], cols=2),
    apoyo_visual("El protocolo en la instalación", [
        ("13.2 · Carpeta del protocolo", "Imagen 13.2 · Carpeta del protocolo de autocontrol en la sala técnica con sus apartados identificados"),
        ("13.3 · Tablón de información", "Imagen 13.3 · Tablón a la entrada con resultados de análisis, normas de uso y teléfonos de emergencia"),
    ], label="Imágenes · protocolo"),
    pasos("Elaborar el protocolo", "3 · Cómo se elabora", "De la instalación al documento", [
        ("Inventario", "Vasos, volúmenes, circuitos, equipos y productos."),
        ("Guía", "Partir de la guía de la Junta de Andalucía para el protocolo."),
        ("Siete aspectos", "Redactar cada uno con sus procedimientos y fichas de registro."),
        ("Responsables", "Quién hace cada tarea y quién la supervisa."),
        ("Implantar", "Formar al personal y empezar a registrar."),
        ("Revisar", "Tras incidencias, cambios o cada temporada: actualizar."),
    ]),
    alerta("Alerta de seguridad · PRL", "Fichas de datos de seguridad a mano",
           "Las FDS de todos los productos químicos de la piscina deben estar archivadas y accesibles de inmediato, en papel o en formato digital. Antes de manipular cualquier producto, revisa sus pictogramas, sus indicaciones de peligro (H) y sus consejos de prudencia (P).",
           [("FDS", "Una por producto, en vigor."),
            ("Pictogramas", "Saber leerlos."),
            ("Frases H y P", "Peligros y precauciones."),
            ("Sección 8", "Los EPI necesarios.")]),
    normativa("El protocolo ante la inspección", [
        ("D 485/2019 · art. 17.4", "El protocolo está siempre en la propia piscina, a disposición de las autoridades sanitarias."),
        ("D 485/2019 · art. 22", "La ocultación, alteración o ausencia del protocolo es una infracción grave."),
        ("RD 742/2013 · disp. adicional 3.ª", "El personal del tratamiento debe tener la cualificación SEA757_2 (RD 46/2022)."),
    ], destacado=("7", "Aspectos mínimos del protocolo, iguales en el RD 742/2013 y en el Decreto 485/2019.")),
    preguntas([
        "¿Dónde debe estar el protocolo de autocontrol?",
        "¿Qué se exige al laboratorio que analiza el agua?",
        "¿Qué información debe estar a la vista de los usuarios?",
    ]),
    respuestas([
        ("B", "En la propia piscina, a disposición del personal de mantenimiento y de la autoridad sanitaria."),
        ("B", "Métodos acreditados según UNE-EN ISO/IEC 17025 o, al menos, procedimientos validados."),
        ("B", "Normas de uso, resultados de los controles, socorrismo, prevención de accidentes y teléfonos de emergencia."),
    ]),
    taller("4.1", "Diseño de un protocolo de autocontrol", "4 horas · aula de informática", [
        "Guía de la Junta de Andalucía para el protocolo de autocontrol",
        "FDS de productos químicos reales",
        "Modelos de procedimientos normalizados de trabajo (PNT)",
        "Ordenador con procesador de textos y hoja de cálculo",
    ], [
        "Redactar el aspecto de tratamiento del agua con sus PNT",
        "Diseñar la ficha de limpieza y desinfección de vestuarios",
        "Integrar las FDS y revisar el almacén de productos",
        "Simular una inspección revisando los siete aspectos",
        "Cumplimentar la hoja de evaluación del protocolo",
    ]),
    cierre("Tema 13", [
        ("Siete aspectos", "Tratamiento, control, mantenimiento, limpieza, seguridad, plagas y proveedores."),
        ("En la piscina", "Siempre, y a disposición de la inspección."),
        ("Registrado", "Controles, incumplimientos e incidencias."),
        ("Al día", "Se revisa tras cada cambio o incidencia."),
    ], "Siguiente · Tema 14 · Libro de registro y SILOÉ"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF4-T13-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T13")
    print(deck.build(out, html_preview=preview))
