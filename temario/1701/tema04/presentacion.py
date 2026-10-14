"""MF2522_2 · UF1 · Tema 4 — presentación SCORM. Texto base: redacción de Mario (14/10/2026).

Criterios acordados en el Tema 3: normativa andaluza (Decreto 485/2019, art. 11) sobre la base
estatal del RD 742/2013; productos químicos con la dosis y la pauta del fabricante; huecos de
imagen en cada bloque.

    python3 -I temario/1701/tema04/presentacion.py   ->  entregas/MF2522_2-UF1-T4-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF1 · Tema 4", ident="MF2522_2_UF1_T4",
            title="Comprobación de estanqueidad, revisión de circuitos y protocolo de hibernación o parada invernal",
            item_title="Tema 4 - Estanqueidad, circuitos y parada invernal")

deck.add(
    portada("MF2522_2 · UF1 · Tema 4",
            "Estanqueidad, revisión de circuitos y parada invernal",
            "Comprobar que el circuito no pierde agua y dejar vaso, conducciones y sala técnica protegidos durante el cierre.",
            "8 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019",
            notes="Último tema de la UF1. Cierra el ciclo: parada segura, vaciado, limpieza y ahora conservación."),
    ficha("8 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial en el banco de ensayo de depuración.",
          "Verificar la estanqueidad de los circuitos de alimentación y retorno, revisar contadores y filtros, y ejecutar "
          "la preparación completa para la hibernación, protegiendo vaso y conducciones frente a heladas y degradación."),
    tarjetas("Por qué importa", "Relevancia operativa", "Una fuga que no se ve sale cara", [
        ("Pérdida de agua", "Volumen que se escapa de forma constante y hay que reponer con agua de aporte."),
        ("Dosificación desajustada", "El agua nueva diluye el tratamiento y los equipos dosifican a ciegas."),
        ("Daño estructural", "El agua que escapa asienta el terreno junto al vaso y lo deteriora."),
    ], cols=3, intro="Antes de dar por terminada la puesta a punto, o antes de un periodo de inactividad, se comprueba la integridad hidráulica del vaso y de las conducciones."),
    tarjetas("Puntos de revisión", "Qué se revisa", "Cuatro puntos del circuito", [
        ("1 · Alimentación y retorno", "Impulsión, aspiración, skimmers y toma de limpiafondos."),
        ("2 · Elementos de medida", "Contadores de agua depurada y de agua renovada: que marquen paso."),
        ("3 · Filtros y prefiltros", "Juntas, tapas, mirillas y purgadores de aire."),
        ("4 · Bombas y motores", "Giro manual del eje y estanqueidad del sello mecánico."),
    ], cols=2),
    tarjetas("Pruebas de estanqueidad", "A · Pruebas de estanqueidad", "Presión, goteos y contadores", [
        ("Prueba de presión", "Se aísla el tramo de PVC o polietileno con tapones neumáticos, se presuriza y se vigila el manómetro al menos 30 minutos. Si la presión cae, hay fisura o una unión encolada o embridada que falla."),
        ("Sala técnica", "Sello mecánico de las bombas centrífugas y autoaspirantes: sin goteos por la carcasa ni por el prensaestopas."),
        ("Contadores", "Se anotan las lecturas del contador de agua renovada (aporte) y del de recirculación. Un consumo de aporte anómalo delata fugas ocultas en el vaso."),
    ], cols=3),
    apoyo_visual("Comprobar la estanqueidad", [
        ("4.1 · Prueba de presión", "Imagen 4.1 · Tramo de PVC aislado con tapón neumático y manómetro durante la prueba"),
        ("4.2 · Sello mecánico", "Imagen 4.2 · Bomba con el sello mecánico a la vista: zona donde se buscan goteos"),
        ("4.3 · Contadores", "Imagen 4.3 · Contadores de agua renovada y de recirculación en la sala técnica"),
    ], label="Imágenes · estanqueidad"),
    tarjetas("Giro y filtros", "B · Motores y filtros", "Antes del llenado definitivo", [
        ("Marcha y paro", "Arranque y parada instantáneos desde el cuadro: el ventilador y el eje giran en el sentido correcto y los rodamientos no hacen ruidos anómalos."),
        ("Filtro lleno de agua", "Se comprueba que el filtro está lleno, sin cámaras de aire que reduzcan la superficie filtrante o provoquen cavitación."),
    ], cols=2, light=True),
    tarjetas("Por qué invernar", "Parada invernal", "Cerrar sin tratar estropea la piscina", [
        ("Agua podrida", "Sin tratamiento, la materia orgánica se descompone en el vaso."),
        ("Algas", "Proliferación masiva durante los meses de cierre."),
        ("Heladas", "El agua que se congela en las tuberías las revienta y daña el vaso."),
    ], cols=3, intro="En las piscinas descubiertas de temporada, el cierre de los meses fríos exige un protocolo de hibernación.",
        footer="El invernaje no es vaciar el vaso: el agua se conserva tratada y protegida hasta la siguiente temporada."),
    pasos("Protocolo de invernaje", "Fase a fase", "Protocolo de hibernación", [
        ("Limpieza previa", "Vaso limpio y filtro lavado a contracorriente."),
        ("pH y cloración de choque", "pH entre 7,2 y 7,6 y choque inicial."),
        ("Producto invernador", "Conservador de invierno con la dosis del fabricante."),
        ("Bajada de nivel", "Por debajo de tuberías de playa y skimmers."),
        ("Vaciado y purgas", "Bombas, prefiltros, dosificadores y tramos expuestos."),
        ("Flotadores y cubierta", "Elementos antidilatación y lona de invierno."),
    ]),
    tarjetas("Química del invernaje", "Paso 1 · Acondicionar el agua", "El agua se deja tratada", [
        ("pH y choque", "pH ajustado entre 7,2 y 7,6 y cloración de choque para eliminar la materia orgánica en suspensión."),
        ("Producto invernador", "Con la depuradora en recirculación se añade el conservador de invierno: alguicida, floculante y antical que no mancha el revestimiento."),
    ], cols=2, footer="**Dosis y repeticiones: las que indique el fabricante** en la etiqueta. Muchos productos piden una segunda dosis a mitad del invierno."),
    tarjetas("Nivel y tuberías", "Paso 2 · Nivel y conducciones", "Que no quede agua donde pueda helarse", [
        ("Bajar el nivel", "Por debajo de las tuberías de playa, los skimmers y las boquillas de impulsión, por gravedad o con motobomba."),
        ("Por qué", "El agua retenida en las conducciones se congela, se dilata y revienta los tubos de PVC."),
        ("Tapones de skimmer", "Tapones o gizzmos en la embocadura de skimmers y tomas de aspiración para que no entre agua de lluvia."),
    ], cols=3),
    tarjetas("Hielo y cubierta", "Pasos 3 y 4 · Hielo y cubierta", "Proteger la lámina de agua y el vaso", [
        ("Flotadores antidilatación", "Boyas de invernaje, o bidones de plástico con algo de arena o agua, en diagonal o en el perímetro. El hielo los comprime en lugar de empujar las paredes."),
        ("Cubierta opaca", "Lona de invierno opaca y tensada con anclajes escamotables de acero inoxidable. Sin luz no hay fotosíntesis y las algas no crecen."),
    ], cols=2, light=True),
    apoyo_visual("La piscina en invernaje", [
        ("4.4 · Vaso en invernaje (corte)", "Imagen 4.4 · Corte del vaso: nivel por debajo de skimmers y tuberías de playa, flotador antidilatación y lona tensada"),
        ("4.5 · Flotadores", "Imagen 4.5 · Boyas de invernaje colocadas en diagonal sobre la lámina de agua"),
        ("4.6 · Cubierta de invierno", "Imagen 4.6 · Lona opaca tensada con anclajes escamotables de acero inoxidable"),
    ], label="Imágenes · invernaje"),
    tarjetas("Sala técnica en invierno", "Conservación de la maquinaria", "La sala técnica también hiberna", [
        ("Vaciar bombas y filtros", "Se abren los tapones de purga de aire y agua del prefiltro y de las botellas del filtro. Sin agua dentro, el hielo no rompe el cuerpo de la bomba ni el filtro."),
        ("Sondas de pH y REDOX", "Nunca secas al aire. Se desmontan del bypass y se guardan con su capuchón en solución de almacenamiento (KCl o la que indique el fabricante), lejos de las heladas."),
        ("Corte y bloqueo eléctrico", "Interruptor general en OFF, etiquetado y cubierto, para que no entren polvo ni roedores que muerdan el cableado."),
    ], cols=3),
    apoyo_visual("La sala técnica preparada", [
        ("4.7 · Purgas abiertas", "Imagen 4.7 · Tapones de purga abiertos en el prefiltro de la bomba y en la botella del filtro"),
        ("4.8 · Sonda conservada", "Imagen 4.8 · Sonda de pH guardada en su capuchón con solución de KCl"),
        ("4.9 · Cuadro consignado", "Imagen 4.9 · Interruptor general en OFF, con etiqueta y protegido del polvo"),
    ], label="Imágenes · sala técnica"),
    alerta("Alerta de seguridad · PRL", "Productos de invernaje",
           "Los conservadores de invierno llevan biocidas y antical concentrados. Se dosifican siempre con el EPI puesto, siguiendo la etiqueta, y con la sala técnica bien ventilada durante las purgas y los vaciados.",
           [("Guantes", "Protección química EN 374."),
            ("Ojos y cara", "Gafas o pantalla facial EN 166."),
            ("Ventilación", "Sala técnica ventilada en purgas y vaciados."),
            ("Etiqueta", "Dosis, plazo de seguridad y pictogramas del fabricante.")]),
    apoyo_visual("Dosificar con seguridad", [
        ("4.10 · Dosificación del invernador", "Imagen 4.10 · Operario con guantes y gafas añadiendo el conservador de invierno con la depuradora en marcha"),
        ("4.11 · Registro del cierre", "Imagen 4.11 · Protocolo de cierre y conservación cumplimentado, con lecturas de contadores"),
    ], label="Imágenes · dosificación"),
    normativa("Qué exige la normativa en Andalucía", [
        ("D 485/2019 · art. 11", "El vaso con agua durante el cierre no puede criar larvas de mosquito: agua tratada y cubierta. Los biocidas se aplican respetando los plazos de seguridad del envase."),
        ("RD 742/2013", "El cierre, el tratamiento aplicado y las lecturas de contadores quedan en el protocolo de autocontrol."),
        ("Criterio CR1.7", "Preparar la parada invernal: nivel bajo tuberías de playa, prefiltros limpios, conducciones purgadas y la instalación cerrada o cubierta."),
    ], destacado=("Cierre", "Fecha, producto, dosis y lecturas de contadores anotados el día del cierre: son la referencia para la reapertura."),
       notes="Marco andaluz: RD 742/2013 como base estatal y Decreto 485/2019 para lo higiénico-sanitario."),
    preguntas([
        "¿Por qué hay que bajar el nivel del agua por debajo de las tuberías de playa y los skimmers en la parada invernal?",
        "¿Qué cuidado necesitan las sondas de pH y REDOX durante la hibernación?",
        "¿Para qué sirven los flotadores antidilatación sobre la lámina de agua en invierno?",
    ]),
    respuestas([
        ("B", "Para que el agua retenida en skimmers y tuberías no se congele: al dilatarse, el hielo rompe los tubos de PVC."),
        ("C", "Se desmontan y se guardan sumergidas en su capuchón con solución de almacenamiento. Si el bulbo de vidrio se seca, la sonda queda inservible."),
        ("B", "Se comprimen con el empuje del hielo y alivian la presión sobre las paredes del vaso, evitando grietas."),
    ]),
    taller("1.4", "Hibernación y pruebas de estanqueidad", "4 horas · banco de ensayo", [
        "Circuito de pruebas con manómetros, contadores y tapones neumáticos",
        "Bombas de recirculación y filtros de arena con tapones de purga",
        "Kit de desmontaje y solución de conservación para sondas de pH y REDOX",
        "Muestra de cubierta opaca con tensores y boyas antidilatación",
        "EPI: guantes EN 374, gafas EN 166 y calzado de seguridad",
    ], [
        "Prueba de presión y estanqueidad en un tramo de PVC",
        "Simular la bajada de nivel y vaciar por los tapones de purga",
        "Desmontar una sonda y guardarla en su capuchón con solución de conservación",
        "Colocar las boyas y presentar el anclaje de la cubierta",
        "Cumplimentar el protocolo de cierre y conservación de la instalación",
    ]),
    cierre("Tema 4", [
        ("La presión no miente", "Si el manómetro baja en 30 minutos, hay una fuga."),
        ("Nada de agua en tubos", "Nivel bajo skimmers y playa; bombas y filtros purgados."),
        ("Sondas mojadas", "Siempre en su capuchón con solución de conservación."),
        ("Agua tratada y cubierta", "Invernador según fabricante y lona opaca."),
    ], "UF1 completada · Siguiente · UF2 · Tema 5 · Parámetros de calidad del agua"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF1-T4-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T4")
    print(deck.build(out, html_preview=preview))
