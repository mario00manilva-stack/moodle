"""MF2522_2 · UF2 · Tema 6 — presentación SCORM. Texto base: redacción de Mario (14/10/2026).

Correcciones sobre el texto base: punto de inyección del corrector de pH (aguas abajo de la toma de
las sondas, no antes), efecto Venturi (por velocidad, no por presión hidrostática), ozono (el residual
del agua se elimina con carbón activo y el gas de escape con un destructor), la electrólisis sube el
pH, y definición vigente del TP2 del Reglamento (UE) 528/2012. Sin tratamientos químicos en el vaso:
RD 742/2013; dosificación automática o semiautomática al circuito: D 485/2019, art. 7.
Concentraciones de sal en la electrólisis: según fabricante.

    python3 -I temario/1701/tema06/presentacion.py   ->  entregas/MF2522_2-UF2-T6-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF2 · Tema 6", ident="MF2522_2_UF2_T6",
            title="Sistemas de desinfección y corrección química del agua: hipoclorito, cloración salina, ozono, radiación UV e inyección de reactivos",
            item_title="Tema 6 - Desinfeccion y correccion quimica")

deck.add(
    portada("MF2522_2 · UF2 · Tema 6",
            "Desinfección y corrección química del agua",
            "Cloro y sus derivados, cloración salina, ozono y radiación UV, y los equipos que inyectan los reactivos en el circuito.",
            "10 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019",
            notes="Sigue al Tema 5: allí se mide el agua; aquí se ve cómo se corrige."),
    ficha("10 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el banco de tratamiento químico.",
          "Identificar, seleccionar y supervisar los sistemas de desinfección química, electroquímica y física, y operar y "
          "mantener los equipos de dosificación de correctores de pH y biocidas en el circuito de tratamiento."),
    tarjetas("Objetivo", "1 · Desinfección química", "Desinfectar ahora y dejar reserva", [
        ("Acción inmediata", "Destruir bacterias, virus, hongos y esporas de algas en segundos."),
        ("Reserva residual", "Mantener desinfectante activo en el vaso para el agua que contaminan los bañistas."),
    ], cols=2, footer="Por eso el cloro sigue siendo la base: es el desinfectante que deja **residual** en el vaso."),
    tabla("Productos clorados", "Productos clorados", "Cuatro formas de aportar cloro",
          ["Producto", "Presentación", "A tener en cuenta"], [
              ("Hipoclorito sódico", "Líquido · ≈ 150 g/L de cloro activo", "El más usado en piscina pública. Sube el pH y pierde riqueza con el tiempo y el calor."),
              ("Hipoclorito cálcico", "Granulado o pastillas · 65–70 %", "No aporta ácido isocianúrico. Aumenta la dureza cálcica."),
              ("Tricloro", "Pastillas · ≈ 90 %", "Cloro lento o estabilizado. Aporta ácido isocianúrico y baja el pH."),
              ("Dicloro", "Granulado · 55–62 %", "Cloro rápido o de choque, muy soluble. Aporta ácido isocianúrico."),
          ], nota="Con tricloro o dicloro el ácido isocianúrico se acumula: hasta 75 mg/L y cierre por encima de 150 mg/L (Tema 5)."),
    tarjetas("Química del cloro", "A · Reacción del cloro en el agua", "El que desinfecta es el ácido hipocloroso", [
        ("La reacción", "Cl₂ + H₂O ⇌ HClO + HCl. Con hipoclorito sódico: NaClO + H₂O ⇌ HClO + NaOH. En ambos casos el producto útil es el ácido hipocloroso (HClO)."),
        ("Ácido hipocloroso", "La forma activa: unas 80 veces más eficaz que el ión hipoclorito (ClO⁻)."),
        ("Depende del pH", "A pH 7,2 algo más de la mitad del cloro libre es ácido hipocloroso; a pH 8,0, apenas una cuarta parte."),
    ], cols=3, footer="Con el pH alto el cloro se mide en el análisis, pero desinfecta poco. **Mantener el pH entre 7,2 y 8,0, mejor en la parte baja.**"),
    tarjetas("Cloraminas", "B · Cloro combinado", "Las cloraminas: el olor a piscina", [
        ("Cómo se forman", "El cloro reacciona con el nitrógeno que aportan los bañistas (sudor, orina): monocloramina, dicloramina y tricloramina."),
        ("Qué provocan", "El olor a piscina, irritación de ojos y mucosas y menos confort. Desinfectan muy poco."),
        ("Cómo se eliminan", "Cloración de choque con el vaso cerrado, renovación de agua y tratamientos complementarios como la radiación UV."),
    ], cols=3, footer="El olor fuerte a cloro no indica exceso de cloro: indica **cloraminas**. Hasta 0,6 mg/L de cloro combinado; cierre por encima de 3 mg/L."),
    tarjetas("Tecnologías avanzadas", "2 · Tecnologías avanzadas", "Menos producto concentrado, mejor agua", [
        ("Electrólisis salina", "Genera el cloro en la instalación a partir de sal disuelta en el agua."),
        ("Radiación UV", "Desinfección física en una cámara. Destruye cloraminas. Sin residual."),
        ("Ozono", "Oxidante muy potente en una cámara de contacto. Sin residual en el vaso."),
    ], cols=3, footer="Ninguna sustituye al desinfectante residual: UV y ozono **siempre** se combinan con cloro en el vaso."),
    apoyo_visual("Tres equipos en la sala técnica", [
        ("6.1 · Electrólisis salina", "Imagen 6.1 · Esquema de célula electrolítica en la impulsión con su fuente de alimentación y el control de pH"),
        ("6.2 · Reactor UV", "Imagen 6.2 · Reactor UV de baja o media presión instalado en la tubería de impulsión, tras el filtro"),
        ("6.3 · Ozono", "Imagen 6.3 · Generador de ozono con cámara de contacto, filtro de carbón activo y destructor del gas de escape"),
    ], label="Imágenes · equipos"),
    tarjetas("Cloración salina", "A · Cloración salina", "Cloro fabricado con sal", [
        ("Principio", "Se disuelve sal (NaCl) en el vaso, en la concentración que indique el fabricante (habitualmente de 3 a 6 g/L). La corriente continua de la célula genera cloro, que forma ácido hipocloroso."),
        ("Ciclo", "Cuando el cloro actúa, vuelve a cloruro y la célula lo reutiliza. La sal solo se repone por lavados, salpicaduras y renovación de agua."),
        ("Lo que exige", "Sube el pH: necesita regulación automática con reductor de pH. Los electrodos se incrustan: limpieza e inversión de polaridad según el fabricante."),
    ], cols=3, footer="El cloro producido por electrólisis es un **biocida**: el equipo debe estar autorizado como tal (Reglamento (UE) 528/2012)."),
    tarjetas("Radiación UV", "B · Radiación ultravioleta", "Luz que desinfecta y rompe cloraminas", [
        ("Principio", "El agua pasa por una cámara con lámparas en vainas de cuarzo. Las de baja presión emiten a 254 nm; las de media presión, en un espectro más amplio."),
        ("Ventajas", "Altera el ADN de bacterias y virus y elimina las cloraminas por fotólisis."),
        ("Limitación", "Tratamiento físico sin efecto residual: necesita siempre un desinfectante de amparo, como el hipoclorito a baja dosis."),
    ], cols=3, footer="Las vainas de cuarzo se ensucian y las lámparas pierden potencia con las horas: **limpieza y cambio según el fabricante.**"),
    tarjetas("Ozono", "C · Ozono (O₃)", "El oxidante más potente, y el más peligroso", [
        ("Principio", "Se genera por descarga eléctrica en aire seco u oxígeno y se inyecta en una cámara de contacto."),
        ("En el agua", "El ozono que no ha reaccionado se elimina con un filtro de carbón activo antes de que el agua vuelva al vaso."),
        ("En el aire", "El gas sobrante de la cámara va a un destructor de ozono. Es tóxico por inhalación: la sala técnica se ventila y se vigila."),
    ], cols=3, footer="El ozono no deja residual: el vaso **siempre** lleva cloro."),
    tarjetas("Equipos de dosificación", "3 · Inyección de reactivos", "Nunca en el vaso con bañistas", [
        ("Bombas peristálticas", "Rodillos que aprietan un tubo flexible. Caudales bajos y medios; el tubo es la pieza de desgaste."),
        ("Bombas de membrana", "Electromagnéticas, con membrana de PTFE. Alta precisión y presión de inyección."),
        ("Dosificadores de pastillas", "Las pastillas se disuelven por erosión en un bypass. Con bromo se llaman bromadores."),
        ("Inyectores Venturi", "Aspiran el producto por la caída de presión que crea el estrechamiento de la tubería."),
    ], cols=4, footer="Los tratamientos químicos no se hacen en el vaso (RD 742/2013). En Andalucía, el vertido al circuito es con sistemas automáticos o semiautomáticos (D 485/2019, art. 7)."),
    pasos("Puntos de inyección", "A · Puntos de inyección", "Cada reactivo en su sitio", [
        ("Toma de las sondas", "Agua que viene del vaso, antes de cualquier inyección."),
        ("Filtro", "El filtro recibe el agua sin reactivos concentrados."),
        ("Calentamiento", "El intercambiador tampoco debe recibir producto concentrado."),
        ("Corrector de pH", "Tras filtro y calentamiento, aguas abajo de las sondas."),
        ("Desinfectante", "Lo último, separado del pH, justo antes de la impulsión."),
        ("Impulsión al vaso", "El agua vuelve filtrada, corregida y desinfectada."),
    ], notes="Error frecuente: inyectar el pH antes de la toma de las sondas. La sonda mide el producto recién inyectado, no el agua del vaso."),
    tarjetas("Mantenimiento", "B · Mantenimiento preventivo", "Una bomba que no dosifica no avisa", [
        ("Cada semana", "Tubo de la peristáltica, o válvulas de aspiración e impulsión de la bomba de membrana."),
        ("Purga de aire", "El hipoclorito desprende gas en la cabeza de la bomba y la desceba. Se purga a mano."),
        ("Calibración", "Ajustar la dosis al volumen del vaso y a las lecturas de las sondas, y comprobarla con el análisis manual."),
    ], cols=3, footer="Lanza de aspiración con su filtro y su detector de nivel: **sin producto, la bomba aspira aire y deja de dosificar.**"),
    apoyo_visual("Dosificación en la sala técnica", [
        ("6.4 · Bomba peristáltica", "Imagen 6.4 · Bomba peristáltica abierta con los rodillos y el tubo de apriete"),
        ("6.5 · Bomba de membrana", "Imagen 6.5 · Cabeza de bomba de membrana con la válvula de purga"),
        ("6.6 · Depósitos", "Imagen 6.6 · Depósitos de ácido y de hipoclorito en cubetos separados, con colores distintos"),
    ], label="Imágenes · dosificación"),
    alerta("Alerta de seguridad · PRL", "Ácido y cloro: incompatibilidad absoluta",
           "Nunca se conecta la aspiración de la bomba de pH a un depósito de cloro, ni al revés. La mezcla de reductor de pH (ácido) e hipoclorito desprende de forma violenta e inmediata gas cloro, tóxico y corrosivo, que puede ser mortal.",
           [("Colores", "Cada línea y depósito, con su color."),
            ("Conexiones", "Que no se puedan intercambiar."),
            ("Almacén", "Ácidos y cloros en cubetos separados."),
            ("EPI", "Guantes EN 374, pantalla facial y delantal.")]),
    normativa("Biocidas autorizados", [
        ("RD 742/2013", "Los desinfectantes del agua del vaso deben ser biocidas autorizados para ese uso."),
        ("Reglamento (UE) 528/2012", "Tipo de producto 2 (TP2): desinfectantes y alguicidas no destinados a aplicarse directamente a personas o animales. Incluye el agua de piscina."),
        ("Comprobación", "La etiqueta lleva el número de registro o de autorización. Se comprueba en el registro de biocidas del Ministerio de Sanidad."),
    ], destacado=("TP2", "Sin número de registro o autorización en la etiqueta, el producto no entra en la piscina."),
       notes="Incluye el cloro generado por electrólisis: el equipo también debe estar autorizado."),
    preguntas([
        "¿Qué forma del cloro en el agua tiene el verdadero poder desinfectante?",
        "¿Para qué sirve un reactor UV como tratamiento complementario?",
        "¿Dónde se inyecta el hipoclorito sódico en el circuito?",
    ]),
    respuestas([
        ("B", "El ácido hipocloroso (HClO): la especie con mayor eficacia germicida del equilibrio del cloro en agua."),
        ("B", "Desinfecta el agua que pasa por la cámara y destruye las cloraminas, aunque necesita un desinfectante residual de amparo."),
        ("C", "Al final del circuito, tras filtración y calentamiento, antes de la impulsión: así protege los equipos de la corrosión."),
    ]),
    taller("2.2", "Dosificación y equipos avanzados", "4 horas · banco de tratamiento", [
        "Bombas dosificadoras peristálticas y de membrana",
        "Célula de electrólisis de pruebas y reactor UV de demostración",
        "Válvulas de inyección con retención y racores de PTFE",
        "Depósitos de reactivos con cubetos de colores",
        "EPI: guantes EN 374, pantalla facial y delantal impermeable",
    ], [
        "Identificar las piezas de una peristáltica y cambiar el tubo",
        "Cebar y purgar el aire de una bomba de membrana",
        "Desmontar e inspeccionar los electrodos de una célula de electrólisis",
        "Instalar una válvula de inyección en una impulsión de PVC",
        "Cumplimentar la ficha de mantenimiento de equipos de dosificación",
    ]),
    cierre("Tema 6", [
        ("Manda el HClO", "Y depende del pH: con pH alto el cloro desinfecta poco."),
        ("Siempre residual", "UV y ozono ayudan, pero el vaso siempre lleva cloro."),
        ("Cada cosa en su sitio", "Sondas, filtro, calentamiento, pH y, al final, cloro."),
        ("Ácido y cloro, nunca juntos", "Colores y conexiones que no se puedan intercambiar."),
    ], "Siguiente · Tema 7 · Determinaciones analíticas y control microbiológico"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF2-T6-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T6")
    print(deck.build(out, html_preview=preview))
