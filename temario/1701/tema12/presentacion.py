"""MF2522_2 · UF3 · Tema 12 — presentación SCORM. Texto base: redacción de Mario (15/10/2026).

Correcciones sobre el texto base:
- La dosificación automática o semiautomática al circuito la exige el Decreto 485/2019 (art. 7) en
  Andalucía; el RD 742/2013 prohíbe tratar en el vaso (art. 6.3), pero no exige equipos automáticos.
- Toma de muestra de las sondas: agua representativa del vaso, antes de cualquier punto de inyección
  (coherente con el Tema 6), no «de la impulsión».
- REDOX: depende sobre todo del HClO, de forma logarítmica, no proporcional. El ácido isocianúrico
  retiene parte del cloro y baja el REDOX; se quitan las cifras ilustrativas sin fuente.
- Temperatura: cambia la pendiente del electrodo de pH (compensación ATC), no «la conductividad».
- Limpiezas, concentración del desincrustante, pendiente mínima y consignas: según el fabricante.
- Conservación: la sonda nunca se deja secar (solución de conservación de KCl).
- Electrólisis: el cloro generado se disuelve formando HClO; óxido de rutenio (no «rutinio»).
- Verificación diaria frente al análisis manual: buena práctica del autocontrol; los márgenes de
  0,2 pH y 0,3 mg/L quedan como criterio orientativo. Sin CR4.1 / SEA757_2, no contrastados.

    python3 -I temario/1701/tema12/presentacion.py   ->  entregas/MF2522_2-UF3-T12-scorm.zip
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from veraqua_deck import (Deck, alerta, apoyo_visual, cierre, ficha, normativa, pasos, portada,  # noqa: E402
                          preguntas, respuestas, tabla, taller, tarjetas)

deck = Deck(code="MF2522_2 · UF3 · Tema 12", ident="MF2522_2_UF3_T12",
            title="Dosificación automática y semiautomática, mantenimiento y calibración de sondas (pH, REDOX, cloro) y equipos de electrólisis salina",
            item_title="Tema 12 - Dosificacion automatica, sondas y electrolisis")

deck.add(
    portada("MF2522_2 · UF3 · Tema 12",
            "Dosificación automática, sondas y electrólisis",
            "Cómo funciona un panel de regulación, cómo se limpian y calibran las sondas de pH, REDOX y cloro, y cómo se mantiene una célula de electrólisis salina.",
            "10 HORAS · TELEFORMACIÓN + TALLER PRESENCIAL · RD 742/2013 · D 485/2019",
            notes="Enlaza con los Temas 5 (parámetros), 6 (dosificación) y 7 (análisis in situ)."),
    ficha("10 h", "Teleformación + taller",
          "Contenido autoinstruccional y práctica presencial con el panel automático didáctico.",
          "Operar y mantener los sistemas automáticos de regulación química, limpiar, conservar y calibrar las sondas de pH, "
          "REDOX y cloro con soluciones patrón, entender cómo se influyen temperatura, pH, REDOX y ácido isocianúrico, y "
          "limpiar y desincrustar las células de cloración salina."),
    tarjetas("Por qué automatizar", "1 · Dosificación automática", "Dosis pequeñas y continuas, no golpes de producto", [
        ("A mano", "Añadir producto de golpe provoca subidas y bajadas: falta de desinfección o exceso que irrita a los bañistas."),
        ("Automático", "El equipo mide en continuo y dosifica solo lo necesario para mantener la consigna."),
        ("La norma", "Nunca en el vaso (RD 742/2013, art. 6.3). En Andalucía, al circuito con sistemas automáticos o semiautomáticos (D 485/2019, art. 7)."),
    ], cols=3),
    pasos("El panel", "A · Partes de un panel de regulación", "De la muestra a la bomba dosificadora", [
        ("Toma de muestra", "Bypass con agua representativa del vaso, antes de cualquier punto de inyección."),
        ("Portasondas", "Sondas de pH, REDOX, cloro libre y temperatura."),
        ("Controlador", "Compara cada lectura con su consigna (set-point)."),
        ("Actuadores", "Bombas de reductor de pH y de cloro, o la célula de electrólisis."),
        ("Detector de flujo", "Sin caudal en el portasondas, corta la dosificación."),
        ("Niveles y alarmas", "Avisa y para la bomba cuando el depósito se vacía."),
    ]),
    apoyo_visual("El panel de regulación", [
        ("12.1 · Esquema del panel", "Imagen 12.1 · Bypass desde la tubería principal, portasondas transparente con detector de flujo, sondas conectadas al controlador y salidas a las bombas de reductor de pH e hipoclorito"),
    ], label="Infografía · panel"),
    tarjetas("Seguridades", "B · Seguridades del panel", "Que nunca se dosifique en agua parada", [
        ("Detector de flujo", "Si se para la recirculación o se cierra el bypass, bloquea las bombas: evita inyectar ácido o cloro concentrado en agua estancada."),
        ("Sondas de nivel", "Paran la bomba y dan alarma cuando la garrafa o el depósito se agota."),
        ("Comprobación", "Probar el corte simulando la falta de caudal, con la frecuencia que fije el protocolo."),
    ], cols=3),
    tabla("Tipos de sonda", "2 · Sondas y electrodos", "Qué mide cada sonda y cómo",
          ["Sonda", "Qué mide", "Cómo funciona"], [
              ("Electrodo de pH", "pH (0–14)", "Electrodo combinado de vidrio con referencia de KCl. A pH 7 da 0 mV; unos 59 mV por unidad de pH a 25 ºC."),
              ("Electrodo de REDOX (ORP)", "Potencial de oxidación, en mV", "Anillo o punta de platino (o de oro). Indica la capacidad oxidante del agua, que depende sobre todo del HClO."),
              ("Sonda amperométrica", "Cloro libre, en mg/L", "Célula abierta o de membrana: mide la corriente que produce el cloro al reaccionar en el electrodo."),
          ], nota="Consignas y márgenes de cada sonda: según el fabricante del equipo."),
    tarjetas("Mantenimiento", "A · Mantenimiento de las sondas", "Una sonda sucia mide mal y el equipo dosifica mal", [
        ("Inspección", "Cada 15 días o cada mes: biopelícula, grasa, algas o cal sobre el bulbo de vidrio o el platino."),
        ("Nunca seca", "Fuera del portasondas, siempre con su capuchón de solución de conservación (KCl). Nunca en agua destilada."),
        ("Vida útil", "Las sondas envejecen aunque estén limpias: la calibración dice cuándo hay que cambiarlas."),
    ], cols=3),
    pasos("Limpieza", "B · Limpieza de una sonda", "Paso a paso", [
        ("Cerrar el bypass", "Cerrar las llaves de corte antes de sacar la sonda."),
        ("Cal", "Bulbo en el limpiador ácido suave que indique el fabricante, unos minutos."),
        ("Grasa y cremas", "Limpiador o detergente neutro, según el fabricante."),
        ("Enjuagar", "Con agua destilada abundante."),
        ("No frotar", "El vidrio no se frota con papel ni paños: se raya y se carga."),
        ("Calibrar", "Tras limpiar, siempre se comprueba o se calibra."),
    ]),
    apoyo_visual("Las sondas", [
        ("12.2 · Portasondas", "Imagen 12.2 · Portasondas transparente con las sondas de pH, REDOX y cloro y el detector de flujo"),
        ("12.3 · Sonda sucia", "Imagen 12.3 · Bulbo de vidrio de un electrodo de pH con depósitos de cal junto a uno limpio"),
    ], label="Imágenes · sondas"),
    pasos("Calibración de pH", "3 · Calibración del pH en dos puntos", "Con soluciones patrón certificadas y en vigor", [
        ("Preparar", "Sonda limpia y enjuagada; patrones sin caducar y sin reutilizar."),
        ("Menú", "Entrar en «Calibración» en el controlador."),
        ("Punto 1 · pH 7,00", "Sonda en el patrón, esperar a que la lectura sea estable y confirmar."),
        ("Enjuagar", "Agua destilada entre patrón y patrón."),
        ("Punto 2 · pH 4,01", "O pH 9,21 / 10,01, según el equipo. Confirmar."),
        ("Pendiente", "El equipo indica la pendiente (%). Fuera del rango del fabricante: cambiar la sonda."),
    ], notes="Muchos fabricantes fijan la pendiente mínima entre el 80 y el 90 %."),
    tarjetas("REDOX y cloro", "A · REDOX y sonda de cloro", "Se comprueban de otra forma", [
        ("REDOX", "No se calibra en dos puntos: se comprueba con una solución patrón (p. ej., 468 mV) y se acepta o se limpia/cambia la sonda."),
        ("Cloro amperométrico", "Se ajusta con el análisis manual: medir el cloro libre con DPD y fotómetro (Tema 7) e introducir ese valor."),
        ("Registro", "Fecha, patrones (lote y caducidad), lecturas, pendiente y responsable."),
    ], cols=3),
    tarjetas("Interdependencia", "B · Los parámetros se influyen entre sí", "Por qué un número solo no basta", [
        ("pH y REDOX", "Si el pH sube por encima de 8,0, hay menos HClO y el REDOX baja, aunque el cloro libre medido sea correcto."),
        ("Isocianúrico y REDOX", "El ácido isocianúrico retiene parte del cloro: el fotómetro marca cloro libre, pero el REDOX sale bajo. Límite de 75 mg/L (Tema 5)."),
        ("Temperatura", "Cambia la respuesta del electrodo de pH. Los equipos la compensan con una sonda Pt100/Pt1000 (ATC)."),
    ], cols=3, footer="Si el REDOX baja con el cloro correcto, revisa **pH** e **isocianúrico** antes de subir la dosis."),
    tarjetas("Electrólisis", "4 · Electrólisis salina", "Mantenimiento de la célula", [
        ("Cómo funciona", "La corriente entre las placas de titanio genera cloro a partir de la sal, que se disuelve al instante como HClO (Tema 6)."),
        ("Inversión de polaridad", "Los equipos invierten la polaridad cada cierto tiempo para desprender la cal de las placas."),
        ("Cuando no basta", "Con agua dura, las placas se cubren de carbonato cálcico blanco y baja la corriente (A): hay que limpiarla."),
    ], cols=3),
    pasos("Desincrustar la célula", "A · Limpieza química de la célula", "Paso a paso", [
        ("Desconectar", "Equipo apagado en el cuadro y consignado."),
        ("Aislar", "Cerrar las válvulas de la célula y vaciarla."),
        ("Desmontar", "Sacar el cuerpo de la célula con las placas."),
        ("Sumergir", "En el desincrustante diluido que indique el fabricante, hasta que deje de burbujear."),
        ("Nunca rascar", "Ni herramientas ni cepillos metálicos: se destruye el recubrimiento de óxidos de rutenio e iridio."),
        ("Enjuagar y montar", "Agua abundante, montar, comprobar fugas y la corriente de la célula."),
    ]),
    apoyo_visual("La célula de electrólisis", [
        ("12.4 · Célula incrustada", "Imagen 12.4 · Placas de titanio con incrustación blanca de cal"),
        ("12.5 · Limpieza por inmersión", "Imagen 12.5 · Placas sumergidas en el desincrustante en un cubeto, con guantes y gafas"),
    ], label="Imágenes · electrólisis"),
    alerta("Alerta de seguridad · PRL", "Hidrógeno en la célula de electrólisis",
           "La electrólisis produce también hidrógeno, un gas muy inflamable. Si se para la recirculación y la célula sigue funcionando porque falla el detector de flujo, el gas se acumula en la célula y puede reventarla. Comprueba con regularidad que la célula se para sin caudal.",
           [("Detector de flujo", "Comprobar que corta."),
            ("Sin caudal", "La célula nunca funciona."),
            ("Ácidos", "Guantes EN 374 y gafas."),
            ("Ventilar", "La sala técnica.")]),
    normativa("Comprobar el automático", [
        ("RD 742/2013 · anexo III", "Control de rutina diario del pH y del desinfectante en el agua del vaso."),
        ("Protocolo de autocontrol", "Comparar cada día la pantalla del equipo con el análisis manual (fotómetro, UNE-ISO 17381)."),
        ("Criterio orientativo", "Si la diferencia supera unas 0,2 unidades de pH o 0,3 mg/L de cloro, limpiar y recalibrar."),
    ], destacado=("Pantalla = análisis", "El equipo automático no sustituye al análisis manual: lo verifica.")),
    preguntas([
        "¿Qué dispositivo bloquea las bombas dosificadoras si se para la recirculación?",
        "¿Cómo se limpian las placas incrustadas de una célula de electrólisis?",
        "Con el pH en 8,2, ¿qué le pasa a la lectura de REDOX?",
    ]),
    respuestas([
        ("B", "El detector o interruptor de flujo del portasondas."),
        ("C", "Sumergidas en el desincrustante diluido, sin rascar el recubrimiento de óxidos."),
        ("B", "Baja: hay menos ácido hipocloroso y el agua desinfecta menos de lo que parece."),
    ]),
    taller("3.4", "Calibración de sondas y electrólisis", "4 horas · panel automático didáctico", [
        "Panel multiparamétrico con controlador, detector de flujo y bombas peristálticas",
        "Patrones certificados de pH 7,00 y 4,01, REDOX 468 mV y agua destilada",
        "Célula de electrólisis con incrustación de cal",
        "Desincrustante y cubeto de inmersión",
        "EPI: guantes EN 374, gafas y bata",
    ], [
        "Desmontar, limpiar y enjuagar las sondas de pH y REDOX",
        "Calibrar el pH en dos puntos y anotar la pendiente",
        "Comprobar el corte del detector de flujo",
        "Desincrustar la célula sin rascar las placas",
        "Cumplimentar la ficha de calibración",
    ]),
    cierre("Tema 12", [
        ("Sin caudal, sin dosis", "El detector de flujo protege el agua y al operario."),
        ("Sonda limpia y húmeda", "Y calibrada con patrones en vigor."),
        ("Mira el pH", "Si el REDOX baja, revisa pH e isocianúrico."),
        ("No rascar", "La célula se limpia con ácido diluido."),
    ], "Siguiente · UF4 · Tema 13 · Protocolo de autocontrol"),
)

if __name__ == "__main__":
    out = os.path.join(ROOT, "entregas", "MF2522_2-UF3-T12-scorm.zip")
    preview = os.path.join(ROOT, "entregas", "preview-T12")
    print(deck.build(out, html_preview=preview))
