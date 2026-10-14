"""1732 · Tema 4 — Primeros auxilios (5 h). Redacción propia de VERAQUA.

RD 1157/2024, Anexo VIII, RA5 (criterios a–f): RCP, maniobra de Heimlich, grados de quemaduras,
protocolos de emergencia, clasificación de heridos y hemorragias. Contenido mínimo: RD 39/1997,
Anexo IV, bloque V. Técnicas según las recomendaciones del Consejo Europeo de Resucitación (ERC 2021)
y el método de triaje START. Orden inspirado en la unidad 6 del índice público de Paraninfo «MP1732».

    python3 -I temario/1732/tema04/presentacion.py   ->  entregas/1732-T4-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="1732 · Nivel básico de PRL · Tema 4", ident="1732_T4",
            title="Primeros auxilios",
            item_title="Tema 4 - Primeros auxilios")

deck.add(
    portada("1732 · Nivel básico de PRL · Tema 4",
            "Primeros auxilios",
            "Qué hacer en los primeros minutos: proteger, avisar y socorrer. RCP, atragantamiento, hemorragias, quemaduras y varios heridos a la vez.",
            "5 HORAS · TELEFORMACIÓN · RD 39/1997 · RD 1157/2024 · ERC 2021",
            notes="Bloque V del Anexo IV del RD 39/1997. Recomendaciones del Consejo Europeo de Resucitación."),
    ficha("5 h", "Teleformación",
          "Contenido autoinstruccional, tarea práctica y foro en el aula virtual.",
          "Aplicar técnicas básicas de primeros auxilios: RCP, maniobra de Heimlich, control de hemorragias y actuación "
          "ante quemaduras, siguiendo los protocolos de emergencia y la clasificación de heridos."),
    tarjetas("PAS", "Protocolo de emergencia", "Siempre en el mismo orden: P, A, S", [
        ("Proteger", "A ti, a la víctima y a los demás. Si el lugar no es seguro (corriente, gas, agua), primero se elimina el peligro."),
        ("Avisar", "Al 112: qué ha pasado, dónde, cuántas víctimas y en qué estado. No cuelgues hasta que te lo digan."),
        ("Socorrer", "Valorar a la víctima y aplicar los primeros auxilios que sepas hacer."),
    ], cols=3, footer="Primeros auxilios es lo que se hace **hasta que llega la ayuda sanitaria**: no sustituye al médico."),
    pasos("Valoración", "Socorrer · Valoración primaria", "¿Responde? ¿Respira?", [
        ("Consciencia", "Háblale y sacúdele suavemente los hombros."),
        ("Si no responde", "Pide ayuda en voz alta y que traigan un desfibrilador."),
        ("Abrir la vía aérea", "Frente hacia atrás y elevar el mentón."),
        ("Ver, oír y sentir", "Comprueba si respira normalmente, no más de 10 segundos."),
        ("Si respira", "Posición lateral de seguridad y vigilarla."),
        ("Si no respira", "112 y empezar la RCP de inmediato."),
    ]),
    tarjetas("RCP", "RCP · Reanimación cardiopulmonar", "Las compresiones mantienen la sangre llegando al cerebro", [
        ("Dónde", "En el centro del pecho, con los brazos rectos y una mano sobre la otra."),
        ("Cómo", "Hundir 5–6 cm, a un ritmo de 100–120 por minuto, dejando que el pecho vuelva a su sitio."),
        ("30 : 2", "30 compresiones y 2 ventilaciones. Si no sabes o no puedes ventilar, solo compresiones continuas."),
        ("DEA", "En cuanto llegue el desfibrilador, enciéndelo y sigue sus instrucciones de voz."),
    ], cols=2, footer="En un **ahogamiento**, como en una piscina, se empieza con **5 ventilaciones de rescate** antes de las compresiones: el problema es la falta de oxígeno."),
    apoyo_visual("RCP y desfibrilador", [
        ("4.1 · Posición de las manos", "Imagen 4.1 · Manos entrelazadas en el centro del pecho y brazos rectos"),
        ("4.2 · DEA", "Imagen 4.2 · Colocación de los parches del desfibrilador externo automático"),
        ("4.3 · Posición lateral de seguridad", "Imagen 4.3 · Víctima en posición lateral de seguridad"),
    ], label="Imágenes · RCP"),
    tarjetas("Atragantamiento", "Maniobra de Heimlich", "Cuando algo bloquea la vía aérea", [
        ("Obstrucción leve", "Tose y puede hablar: anímale a toser, sin golpearle."),
        ("Obstrucción grave", "No puede toser, hablar ni respirar: 5 golpes entre los omóplatos y, si no sale, 5 compresiones abdominales (Heimlich). Alternar."),
        ("Si pierde la consciencia", "Al suelo con cuidado, 112 y empezar la RCP."),
    ], cols=3, footer="Heimlich: por detrás, puño cerrado entre el ombligo y el esternón, la otra mano encima, y tirar **hacia dentro y hacia arriba**."),
    tarjetas("Hemorragias", "Hemorragias", "Parar la sangre", [
        ("Externa", "La sangre sale por una herida. Presión directa y firme sobre la herida con gasas o un paño limpio, sin levantarlas."),
        ("Interna", "No se ve: palidez, sudor frío, pulso rápido, mareo. Tumbar a la víctima, abrigarla y 112."),
        ("Exteriorizada", "Sale por un orificio natural. Nariz: cabeza hacia delante y presionar la aleta 10 minutos."),
    ], cols=3, footer="El **torniquete** solo en una hemorragia masiva de una extremidad que no se detiene con presión directa, anotando la hora de colocación."),
    tabla("Quemaduras", "Quemaduras", "Los grados de las quemaduras",
          ["Grado", "Cómo se ve", "Qué afecta"], [
              ("Primer grado", "Piel roja, dolorosa, sin ampollas, como una quemadura solar", "Epidermis"),
              ("Segundo grado", "Ampollas, piel roja y húmeda, mucho dolor", "Epidermis y dermis"),
              ("Tercer grado", "Piel blanquecina, acartonada o negruzca; puede no doler", "Todas las capas de la piel"),
          ], nota="La extensión importa tanto como el grado: cuanto mayor es la superficie quemada, más grave."),
    tarjetas("Actuar ante una quemadura", "Quemaduras", "Qué hacer y qué no hacer", [
        ("Enfriar", "Agua templada o fresca sobre la quemadura durante unos 20 minutos."),
        ("Quemadura química", "Quitar la ropa contaminada y lavar con agua abundante durante mucho tiempo, sin frotar."),
        ("Cubrir", "Con gasa estéril o un paño limpio y húmedo. Quitar anillos y relojes."),
        ("No hacer", "No romper ampollas, no aplicar pomadas, aceites ni remedios caseros, no despegar la ropa pegada."),
    ], cols=2, light=True),
    apoyo_visual("Hemorragias y quemaduras", [
        ("4.4 · Presión directa", "Imagen 4.4 · Presión directa sobre una herida del antebrazo con gasas"),
        ("4.5 · Enfriar una quemadura", "Imagen 4.5 · Quemadura en la mano bajo un chorro de agua"),
    ], label="Imágenes · lesiones"),
    tabla("Clasificación de heridos", "Triaje · Método START", "Varias víctimas: a quién atender primero",
          ["Color", "Situación", "Prioridad"], [
              ("Verde", "Puede caminar", "Puede esperar"),
              ("Rojo", "No camina y respira más de 30 veces por minuto, o sin pulso radial, o no obedece órdenes sencillas", "Atención inmediata"),
              ("Amarillo", "No camina, pero respira, tiene pulso y obedece órdenes", "Atención urgente, puede esperar un poco"),
              ("Negro", "No respira tras abrirle la vía aérea", "Fallecido o sin posibilidades"),
          ], nota="El triaje se hace rápido, menos de un minuto por víctima. Solo se abre la vía aérea y se controlan hemorragias graves."),
    tarjetas("Botiquín", "Medios", "El botiquín del centro de trabajo", [
        ("Qué lleva", "Desinfectante, gasas estériles, vendas, esparadrapo, tiritas, guantes desechables y tijeras."),
        ("Dónde", "Accesible, señalizado y revisado: se repone lo usado y lo caducado."),
        ("En el sector", "Junto a la sala técnica: lavaojos y agua abundante. Y la FDS de los productos a mano."),
    ], cols=3),
    alerta("Alerta de seguridad · PRL", "Rescate en el agua",
           "Si ves a alguien inconsciente en el vaso, avisa al socorrista y al 112. No te tires al agua si no sabes rescatar: usa un aro, una pértiga o cualquier objeto flotante. Ya fuera del agua, si no respira, empieza con 5 ventilaciones y sigue con la RCP.",
           [("Avisa", "Socorrista y 112."),
            ("Desde fuera", "Aro, pértiga, objeto que flote."),
            ("Fuera del agua", "Valorar consciencia y respiración."),
            ("No respira", "5 ventilaciones y RCP 30:2.")]),
    normativa("Primeros auxilios en la empresa", [
        ("Ley 31/1995 · art. 20", "La empresa organiza los primeros auxilios, designa al personal y comprueba que funcionan."),
        ("RD 486/1997", "Material de primeros auxilios adecuado y señalizado en los lugares de trabajo."),
        ("ERC 2021", "Recomendaciones europeas de reanimación que siguen los protocolos de este tema."),
    ], destacado=("112", "El número de emergencias en toda la Unión Europea, gratuito y desde cualquier teléfono.")),
    preguntas([
        "¿Qué ritmo y profundidad tienen las compresiones de una RCP en un adulto?",
        "Una persona se atraganta, no puede toser ni hablar. ¿Qué haces?",
        "¿Cómo reconoces una quemadura de segundo grado?",
    ]),
    respuestas([
        ("B", "Entre 100 y 120 por minuto y 5–6 cm de profundidad, en el centro del pecho."),
        ("C", "5 golpes entre los omóplatos y, si no se resuelve, 5 compresiones abdominales; alternar."),
        ("A", "Por las ampollas y el dolor intenso: afecta a la epidermis y a la dermis."),
    ]),
    taller("4.1", "Plan de actuación ante un accidente", "entrega en el aula", [
        "Este tema completo y sus diapositivas",
        "El caso de la tarea",
        "El protocolo de actuación del Tema 3",
    ], [
        "Aplicar la conducta PAS al caso",
        "Clasificar a los heridos con el método START",
        "Describir los primeros auxilios de cada herido",
        "Redactar la llamada al 112",
        "Indicar qué material de emergencia se usaría",
    ], tipo="Tarea", modalidad="Práctica en el aula virtual", etiqueta_equipo="Qué necesitas",
        notes="Tarea individual: se entrega en el aula como archivo o texto."),
    cierre("Tema 4", [
        ("PAS", "Proteger, avisar y socorrer, en ese orden."),
        ("30 : 2", "A 100–120 por minuto y 5–6 cm. Y el DEA."),
        ("Golpes y Heimlich", "5 y 5 ante una obstrucción grave."),
        ("Agua y gasa", "Enfriar la quemadura y cubrirla."),
    ], "Fin del módulo 1732 · Nivel básico de prevención de riesgos laborales"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "1732-T4-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-1732-T4")
    print(deck.build(out, html_preview=preview))
