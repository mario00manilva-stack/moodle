"""MF2519_2 · UF1 · Tema 20 — presentación SCORM. Texto base: redacción de Mario (17/10/2026).

Correcciones:
- VLA (INSST): cloro VLA-EC 0,5 ppm; cloruro de hidrógeno VLA-ED 5 ppm y VLA-EC 10 ppm; dióxido de carbono
  VLA-ED 5 000 ppm (el INSST no le fija VLA-EC). Valores a comprobar cada año en la publicación del INSST.
- RD 664/1997: Legionella pneumophila y Pseudomonas aeruginosa, grupo 2.
- Lavaojos y ducha de emergencia (EN 15154) cerca del punto de manipulación; se quita la distancia de
  «menos de 10 m», que no es un requisito de la normativa española.
- Trajes de protección química: tipos de la norma europea (3, 4…), no «nivel C».

    python3 -I temario/1732/tema20/presentacion.py   ->  entregas/MF2519_2-UF1-T20-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2519_2 · UF1 · Tema 20", ident="MF2519_2_UF1_T20",
            title="Riesgo químico y biológico en instalaciones acuáticas: cloro, biocidas, vapores y bioaerosoles",
            item_title="Tema 20 - Riesgo quimico y biologico")

deck.add(
    portada("MF2519_2 · UF1 · Tema 20",
            "Riesgo químico y biológico",
            "Vapores de cloro y cloraminas, ácidos, Legionella, Pseudomonas y hongos: cómo entran en el cuerpo y cómo se controlan.",
            "7 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 374/2001 · RD 664/1997 · VLA DEL INSST",
            notes="Segundo tema de la UF1 del módulo MF2519_2."),
    ficha("7 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el taller de seguridad e higiene del centro.",
          "Evaluar y controlar la exposición a agentes químicos (cloro, cloraminas, ácidos) y biológicos (Legionella, Pseudomonas, "
          "hongos y virus) en salas técnicas y vasos, con los valores límite ambientales del INSST y las medidas de higiene."),
    tarjetas("Vías de entrada", "1 · Riesgo químico", "Cómo entra el contaminante", [
        ("Inhalatoria", "Vapores de cloro, cloraminas y ácidos en la sala técnica y el almacén. La más frecuente."),
        ("Dérmica", "Salpicaduras de hipoclorito o ácido en piel y ojos."),
        ("Digestiva", "Comer, beber o fumar con las manos contaminadas, o confundir envases."),
    ], cols=3, footer="Norma de referencia: **RD 374/2001**, de agentes químicos."),
    tabla("VLA", "A · Valores límite ambientales (INSST)", "Cuánto se puede respirar",
          ["Contaminante", "VLA-ED (8 h)", "VLA-EC (15 min)"], [
              ("Cloro (Cl₂)", "—", "0,5 ppm"),
              ("Cloruro de hidrógeno (HCl)", "5 ppm", "10 ppm"),
              ("Dióxido de carbono (CO₂)", "5 000 ppm", "—"),
          ], nota="VLA-ED: exposición diaria de 8 horas. VLA-EC: exposición de corta duración, 15 minutos. Los valores se revisan cada año en «Límites de exposición profesional» del INSST."),
    tarjetas("Riesgo biológico", "2 · RD 664/1997", "Agentes del grupo 2", [
        ("Legionella pneumophila", "Neumonía por inhalación de aerosoles de jacuzzis, cascadas y duchas."),
        ("Pseudomonas aeruginosa", "Otitis del nadador e infecciones de piel."),
        ("Hongos dermatofitos", "Pie de atleta por contacto con suelos húmedos."),
        ("Medidas", "Desinfección, higiene personal, guantes y protección respiratoria al limpiar o desinfectar equipos con aerosoles."),
    ], cols=2, footer="Grupo 2: pueden causar enfermedad en las personas, pero es poco probable que se propaguen y suele haber tratamiento."),
    tarjetas("Protección respiratoria", "A · Filtros", "El filtro adecuado al contaminante", [
        ("Tipo B (gris)", "Gases inorgánicos, como el cloro."),
        ("Tipo E (amarillo)", "Gases ácidos, como el cloruro de hidrógeno."),
        ("ABEK", "Combinado: orgánicos, inorgánicos, ácidos y amoniaco. Cubre lo habitual en una piscina."),
    ], cols=3, footer="Los filtros se cambian según el fabricante y siempre que se note olor o dificultad para respirar."),
    apoyo_visual("Higiene y emergencia", [
        ("20.1 · Lavaojos", "Imagen 20.1 · Ducha de emergencia y lavaojos junto al almacén de productos"),
        ("20.2 · Máscara ABEK", "Imagen 20.2 · Máscara buconasal con filtros ABEK y su código de colores"),
    ], label="Imágenes · riesgo químico"),
    alerta("Alerta de seguridad · PRL", "Ducha de emergencia y lavaojos junto a los químicos",
           "Debe haber ducha de emergencia y lavaojos (EN 15154) cerca del punto donde se manipulan los productos, accesibles y probados. Si salpica ácido o cloro a los ojos: lavar con agua de forma ininterrumpida al menos 15 minutos, con los párpados abiertos, y acudir al médico con la FDS.",
           [("Cerca", "Del punto de manipulación."),
            ("15 minutos", "De lavado sin parar."),
            ("Párpados abiertos", "Sin frotar."),
            ("Al médico", "Con la FDS.")]),
    normativa("Vigilancia de la salud", [
        ("Art. 22 Ley 31/1995", "La empresa garantiza la vigilancia periódica de la salud según los riesgos del puesto."),
        ("Protocolos específicos", "Pruebas respiratorias (espirometría) y dermatológicas para expuestos a agentes químicos."),
        ("Confidencial", "Los resultados solo se comunican al trabajador; la empresa conoce si es apto."),
    ], destacado=("Grupo 2", "Legionella pneumophila en el RD 664/1997.")),
    preguntas([
        "¿Qué filtro protege frente a vapores ácidos y cloro?",
        "¿Cuánto tiempo se lavan los ojos tras una salpicadura?",
        "¿A qué grupo de riesgo pertenece Legionella pneumophila?",
    ]),
    respuestas([
        ("B", "Un filtro combinado ABEK."),
        ("B", "Al menos 15 minutos con abundante agua corriente."),
        ("B", "Al grupo 2: puede causar enfermedad en las personas."),
    ]),
    taller("6.2", "Emergencia química y lavaojos", "3 horas · taller de seguridad e higiene", [
        "Ducha de emergencia y lavaojos",
        "Kit de derrames con absorbente inerte",
        "Traje de protección química, máscara con filtros ABEK y guantes",
    ], [
        "Accionar el lavaojos y comprobar caudal y presión",
        "Recoger un derrame simulado de 5 L de ácido con absorbente",
        "Ponerse el traje y la máscara y comprobar el ajuste facial",
    ]),
    cierre("Tema 20", [
        ("Inhalación", "La vía más frecuente."),
        ("0,5 ppm", "VLA-EC del cloro."),
        ("ABEK", "Filtro combinado para piscinas."),
        ("15 minutos", "De lavado de ojos."),
    ], "Siguiente · Tema 21 · EPI y señalización"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2519_2-UF1-T20-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T20")
    print(deck.build(out, html_preview=preview))
