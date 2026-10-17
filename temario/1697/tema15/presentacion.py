"""MF2518_2 · UF1 · Tema 15 — presentación SCORM. Texto base: redacción de Mario (17/10/2026).

Contrastado con el BOE (RD 656/2017, ITC MIE APQ-10):
- Capacidad de retención ≥ al mayor de: 100 % del recipiente mayor o 10 % de la capacidad total
  almacenada (APQ-10, art. 10.2). Correcto en el texto base.
- Corrosivos incompatibles (ácidos y alcalinos/hipocloritos): al menos cubetos de retención separados
  (APQ-10, tabla de almacenamiento conjunto, nota A).
- Resistencia al fuego «EI 60/90» y separación «> 3 m» no figuran así en la ITC: se presentan como lo que
  fije el proyecto o la memoria. Instalación ATEX solo si hay productos inflamables.
- El proyecto puede sustituirse por una memoria en determinados casos (APQ-10, art. 3.2); la inscripción
  se hace ante el órgano competente de industria de la comunidad autónoma.
- Productos químicos, dosis y compatibilidades concretas: según el fabricante y la FDS.

    python3 -I temario/1697/tema15/presentacion.py   ->  entregas/MF2518_2-UF1-T15-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2518_2 · UF1 · Tema 15", ident="MF2518_2_UF1_T15",
            title="Reglamentación de almacenamiento de productos químicos (RD 656/2017 · ITC MIE APQ-10): almacenes, ventilación, cubetos e incompatibilidades",
            item_title="Tema 15 - Almacenamiento de productos quimicos APQ")

deck.add(
    portada("MF2518_2 · UF1 · Tema 15",
            "Almacenamiento de productos químicos",
            "Cómo debe ser el almacén de productos de la piscina según el RD 656/2017: local, ventilación, cubetos de retención y qué productos no pueden estar juntos.",
            "8 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 656/2017 · ITC MIE APQ-10",
            notes="Primer tema del módulo MF2518_2."),
    ficha("8 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el almacén de prácticas del centro.",
          "Aplicar los requisitos del RD 656/2017 y de sus instrucciones técnicas (APQ-10 para recipientes móviles) en el "
          "almacén de productos de una piscina: cubetos de retención, ventilación e incompatibilidades."),
    tarjetas("Qué se almacena", "1 · El marco normativo", "Productos que no pueden guardarse de cualquier manera", [
        ("Los productos", "Hipocloritos y cloros sólidos, reductores e incrementadores de pH, floculantes, alguicidas y desincrustantes."),
        ("La norma", "RD 656/2017, Reglamento de almacenamiento de productos químicos (APQ), y sus instrucciones técnicas complementarias."),
        ("Recipientes móviles", "Garrafas, bidones y contenedores GRG/IBC: ITC MIE APQ-10. Los depósitos fijos de corrosivos, ITC MIE APQ-6."),
    ], cols=3),
    tabla("El almacén", "A · Requisitos del almacén", "Lo que debe cumplir el local",
          ["Requisito", "Qué significa"], [
              ("Acceso restringido", "Cerrado y señalizado; solo entra personal formado."),
              ("Resistencia al fuego", "La que fije el proyecto o la memoria del almacenamiento."),
              ("Ventilación", "Natural o forzada, suficiente para que no se acumulen vapores."),
              ("Contención de derrames", "Cubetos o suelo de retención estancos y resistentes a los productos."),
              ("Instalación eléctrica", "Adecuada al local; protección ATEX solo si hay productos inflamables."),
              ("Medios de emergencia", "Lavaojos y ducha o agua abundante, absorbente y FDS a mano."),
          ]),
    tarjetas("Cubetos", "B · Cubetos de retención", "Que un derrame no salga del cubeto", [
        ("Capacidad mínima", "**La mayor de dos cifras**: el 100 % del recipiente mayor o el 10 % de todo lo que vierte en el cubeto (APQ-10, art. 10)."),
        ("Material", "Estanco y resistente al producto: polietileno de alta densidad para ácidos y álcalis, o metal tratado."),
        ("Uno por familia", "Cada cubeto se calcula solo con los recipientes que vierten en él."),
    ], cols=3),
    tarjetas("Ejemplo", "B · Calcular un cubeto", "Ocho garrafas de 25 L de ácido", [
        ("Recipiente mayor", "25 L → 100 % = 25 L."),
        ("Total", "8 × 25 L = 200 L → 10 % = 20 L."),
        ("Resultado", "El cubeto debe retener **al menos 25 L**, la mayor de las dos cifras."),
    ], cols=3, footer="Con un GRG de 1 000 L, el cubeto tendría que retener 1 000 L aunque solo hubiera ese recipiente."),
    tabla("Incompatibilidades", "2 · Almacenamiento conjunto", "Lo que no puede compartir cubeto",
          ["Familia", "No junto a", "Qué pasa"], [
              ("Ácidos (reductores de pH)", "Hipocloritos y cloros", "Desprenden gas cloro de forma inmediata."),
              ("Ácidos", "Bases (incrementadores de pH)", "Reacción que desprende calor y puede proyectar líquido."),
              ("Cloros sólidos (oxidantes)", "Combustibles: aceites, papel, madera", "Pueden avivar o provocar un incendio."),
          ], nota="APQ-10: los corrosivos incompatibles, como mínimo en cubetos de retención separados. Compatibilidades concretas: sección 10 de la FDS."),
    apoyo_visual("El almacén ordenado", [
        ("15.1 · Plano del almacén", "Imagen 15.1 · Plano de un almacén con la zona de ácidos y la de cloros y bases separadas, cada una con su cubeto"),
        ("15.2 · Cubeto de retención", "Imagen 15.2 · Garrafas de 25 L sobre un cubeto de polietileno con su capacidad indicada"),
    ], label="Infografía · almacén"),
    pasos("Ordenar el almacén", "C · Cómo se organiza", "Paso a paso", [
        ("Clasificar", "Cada envase por su familia, con la etiqueta y la FDS."),
        ("Separar", "Una zona y un cubeto por familia incompatible."),
        ("Calcular", "Capacidad de cada cubeto con sus recipientes."),
        ("Señalizar", "Peligros, EPI obligatorios y prohibiciones en la puerta."),
        ("Equipar", "Lavaojos, absorbente y extintor accesibles."),
        ("Revisar", "Fugas, caducidades y orden, con registro."),
    ]),
    alerta("Alerta de seguridad · PRL", "Ácido e hipoclorito, nunca en el mismo cubeto",
           "Si fugan a la vez una garrafa de reductor de pH y otra de hipoclorito en el mismo cubeto, la mezcla libera gas cloro a alta concentración dentro del almacén. Cada familia, con su cubeto; y en el almacén, nunca se trasvasa de un producto a otro.",
           [("Cubetos", "Uno por familia."),
            ("Colores", "Identificar cada zona."),
            ("Fugas", "Revisar y registrar."),
            ("Gas cloro", "Salir y ventilar desde fuera.")]),
    normativa("Proyecto e inscripción", [
        ("RD 656/2017", "Los almacenamientos que superan las cantidades de la ITC se inscriben ante el órgano de industria de la comunidad autónoma."),
        ("APQ-10 · art. 3", "En algunos casos el proyecto se sustituye por una memoria firmada por el titular."),
        ("Revisiones", "Inspecciones periódicas y registro de las revisiones del almacenamiento."),
    ], destacado=("100 % · 10 %", "Capacidad de retención: el mayor de los dos valores.")),
    preguntas([
        "¿Qué capacidad mínima debe tener un cubeto con varios recipientes?",
        "¿Qué gas se forma si se mezclan un ácido y un hipoclorito?",
        "¿Cómo se guardan los ácidos y los cloros en el mismo almacén?",
    ]),
    respuestas([
        ("B", "El mayor de: 100 % del recipiente mayor o 10 % del total."),
        ("B", "Gas cloro (Cl₂), muy tóxico por inhalación."),
        ("B", "En cubetos de retención separados y en zonas distintas."),
    ]),
    taller("5.1", "Auditoría y organización de un almacén", "4 horas · almacén de prácticas", [
        "Cubetos de retención y garrafas simuladas",
        "Carteles de señalización",
        "FDS de los productos del almacén",
        "EPI: guantes químicos, gafas y calzado de seguridad",
    ], [
        "Clasificar los envases por familia química",
        "Calcular la capacidad de un cubeto para garrafas de 25 L",
        "Reorganizar el almacén según las incompatibilidades",
        "Colocar la señalización y los equipos de emergencia",
    ]),
    cierre("Tema 15", [
        ("APQ-10", "Recipientes móviles: garrafas, bidones y GRG."),
        ("100 % o 10 %", "El cubeto, según el mayor de los dos."),
        ("Familias separadas", "Ácidos lejos de cloros y de bases."),
        ("Almacén preparado", "Ventilado, señalizado y con lavaojos."),
    ], "Siguiente · Tema 16 · Fichas de datos de seguridad y EPI"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2518_2-UF1-T15-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T15")
    print(deck.build(out, html_preview=preview))
