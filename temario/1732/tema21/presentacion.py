"""MF2519_2 · UF2 · Tema 21 — presentación SCORM. Texto base: redacción de Mario (17/10/2026).

Correcciones:
- Categorías del Reglamento (UE) 2016/425: la categoría III no lleva una «revisión anual obligatoria»
  general; la revisión y caducidad las marca el fabricante en su folleto. La categoría III exige el marcado
  CE con el número de cuatro cifras del organismo notificado.
- Folleto informativo en castellano: Reglamento (UE) 2016/425. Entrega registrada: buena práctica para
  acreditar la obligación de proporcionar los EPI (RD 773/1997).
- Señalización: RD 485/1997.

    python3 -I temario/1732/tema21/presentacion.py   ->  entregas/MF2519_2-UF2-T21-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2519_2 · UF2 · Tema 21", ident="MF2519_2_UF2_T21",
            title="Selección, uso, mantenimiento y certificación de los EPI y señalización de seguridad en salas técnicas",
            item_title="Tema 21 - EPI y senalizacion")

deck.add(
    portada("MF2519_2 · UF2 · Tema 21",
            "EPI y señalización",
            "Elegir el EPI adecuado, comprobar su marcado y su caducidad, cuidarlo y entender las señales de la sala técnica.",
            "8 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 773/1997 · REGLAMENTO (UE) 2016/425 · RD 485/1997",
            notes="Primer tema de la UF2 del módulo MF2519_2."),
    ficha("8 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el taller de equipamiento de seguridad del centro.",
          "Seleccionar, mantener y verificar el marcado CE de los equipos de protección individual (RD 773/1997 y Reglamento (UE) "
          "2016/425) e interpretar la señalización de seguridad de las salas técnicas (RD 485/1997)."),
    tarjetas("El EPI", "1 · Qué es un EPI", "La última barrera, no la primera", [
        ("Definición", "Equipo que lleva el trabajador para protegerse de uno o varios riesgos."),
        ("Cuándo", "Cuando los riesgos no se pueden evitar o limitar con medidas colectivas u organizativas."),
        ("Quién", "La empresa los proporciona gratis; el trabajador los usa y cuida (RD 773/1997)."),
    ], cols=3),
    tabla("Categorías", "A · Reglamento (UE) 2016/425", "Tres categorías según el riesgo",
          ["Categoría", "Riesgo", "Ejemplos en piscinas"], [
              ("I", "Riesgos mínimos", "Guantes de limpieza para productos suaves, gafas de sol."),
              ("II", "Riesgos intermedios", "Calzado de seguridad antideslizante, gafas de montura integral."),
              ("III", "Riesgos que pueden causar la muerte o daños irreversibles", "Máscara con filtros ABEK, guantes de protección química EN ISO 374-1, arnés anticaídas."),
          ], nota="Categoría III: marcado CE seguido del número de cuatro cifras del organismo notificado."),
    tarjetas("Uso y mantenimiento", "B · Cuidar el EPI", "Un EPI en mal estado no protege", [
        ("Folleto del fabricante", "En castellano: uso, limpieza, almacenamiento, revisión y caducidad."),
        ("Antes de usar", "Revisar grietas, cortes, filtros caducados o mal ajuste."),
        ("Después", "Limpiar, secar y guardar en su sitio, lejos de los productos."),
        ("Registro", "Ficha de entrega firmada: qué EPI, cuándo y la información recibida."),
    ], cols=2),
    tabla("Señalización", "2 · RD 485/1997", "Forma y color de las señales",
          ["Forma y color", "Significado", "Ejemplo en la sala técnica"], [
              ("Redonda, borde y banda roja", "Prohibición", "Prohibido el paso a personas no autorizadas."),
              ("Triangular amarilla, borde negro", "Advertencia", "Riesgo eléctrico, materias corrosivas."),
              ("Redonda azul", "Obligación", "Uso obligatorio de gafas y guantes."),
              ("Rectangular o cuadrada verde", "Salvamento o socorro", "Ducha de seguridad y lavaojos."),
              ("Rectangular o cuadrada roja", "Equipos contra incendios", "Extintor."),
          ]),
    apoyo_visual("EPI y señales", [
        ("21.1 · Marcado CE", "Imagen 21.1 · Guante químico con marcado CE, número del organismo notificado y pictograma EN ISO 374-1"),
        ("21.2 · Puerta de la sala", "Imagen 21.2 · Puerta de la sala técnica con señales de prohibición, advertencia y obligación"),
    ], label="Imágenes · EPI y señalización"),
    alerta("Alerta de seguridad · PRL", "Filtros y guantes también caducan",
           "Los filtros para gases tienen fecha de caducidad y, una vez abiertos, su duración la limita el uso y lo que indique el fabricante. Si notas olor o sabor a producto con la máscara puesta, sal y cambia el filtro. Los guantes químicos se revisan antes de cada uso.",
           [("Fecha", "En el filtro y el folleto."),
            ("Olor", "Salir y cambiar el filtro."),
            ("Guantes", "Revisar antes de usar."),
            ("Guardar", "Limpio y en su bolsa.")]),
    normativa("Obligaciones con los EPI", [
        ("RD 773/1997", "La empresa elige, proporciona y repone los EPI e informa y forma sobre su uso."),
        ("Reglamento (UE) 2016/425", "Marcado CE, declaración UE de conformidad y folleto en la lengua del país."),
        ("RD 485/1997", "Señalización de seguridad y salud en el trabajo."),
    ], destacado=("CE 0000", "Categoría III: CE más el número del organismo notificado.")),
    preguntas([
        "¿A qué categoría pertenecen los EPI frente a riesgos mortales?",
        "¿Cómo es la señal que obliga a usar gafas?",
        "¿Qué marcado llevan los guantes químicos de categoría III?",
    ]),
    respuestas([
        ("B", "Categoría III."),
        ("B", "Redonda, azul, con pictograma blanco."),
        ("A", "Marcado CE seguido del número del organismo notificado."),
    ]),
    taller("6.3", "Inspección de EPI y señalización", "3 horas · taller de equipamiento de seguridad", [
        "Lote de EPI de categorías I, II y III",
        "Señales de seguridad",
        "Fichas de entrega de EPI",
    ], [
        "Clasificar diez EPI por categoría y revisar caducidades",
        "Colocar la señalización en el acceso a la sala técnica",
        "Cumplimentar una ficha de entrega de EPI",
    ]),
    cierre("Tema 21", [
        ("Última barrera", "Primero las medidas colectivas."),
        ("Categoría III", "CE + organismo notificado."),
        ("Azul redonda", "Obligación."),
        ("Folleto", "Manda el fabricante."),
    ], "Siguiente · Tema 22 · Emergencias y primeros auxilios"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2519_2-UF2-T21-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T21")
    print(deck.build(out, html_preview=preview))
