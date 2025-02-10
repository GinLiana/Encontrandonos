# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define alex = Character("Alex")
define lily = Character("Lily")

# Variables para las elecciones
default afinidad = 0
default confianza = 0
default seguridad = 0

# El juego comienza aquí.

label start:

label acto1_cafe:
    scene cafe_universitario with fade
    
    # Alex entra al café
    alex "Qué día tan largo... Un café me vendría bien."

    # Lily está en la barra, distraída con su teléfono
    show lily normal at right
    lily "(Pensando) Ugh, otra notificación de mi ex... Qué fastidio."

    # Alex sin querer choca con Lily
    show lily molesta at right
    "Alex, distraído, da un paso atrás y choca con Lily, derramando un poco de café sobre la mesa."

    lily "¡Hey, cuidado! Casi me tiras el café encima."

    menu:
        "Disculparse rápidamente":
            $ afinidad += 1
            alex "Lo siento mucho, no fue mi intención."
            lily "Hmph, bueno... Supongo que a todos nos pasa."

        "Responder de forma indiferente":
            $ afinidad -= 1
            alex "No fue para tanto, no exageres."
            lily "¿Ah sí? Vaya, qué caballeroso."

    # Continúa la conversación según la afinidad
    if afinidad > 0:
        lily "Bueno, ya que estamos aquí... ¿Eres nuevo en este café?"
        alex "Más o menos. Prefiero lugares tranquilos."
        lily "Hmm, pues llegaste al lugar equivocado, a esta hora siempre está lleno."
    else:
        lily "En fin... mejor me cambio de mesa."
        alex "(Susurrando) Vaya, qué carácter..."
    

label acto2_biblioteca:
    scene biblioteca_con_luz suave with fade
    
    # Alex y Lily están sentados en una mesa de estudio
    alex "Creo que tengo todo claro para el examen, solo me falta repasar un par de conceptos."
    
    lily "¿De verdad? Yo he tenido que repasar todo el temario de nuevo, no sé si voy a llegar a tiempo."
    
    menu:
        "Ofrecerle ayuda":
            $ afinidad += 1
            alex "Si necesitas ayuda, puedo explicarte algunas cosas."
            lily "¿En serio? ¡Eso sería genial, gracias!"
            alex "(Sonriendo) No es nada, estamos en esto juntos."
            
        "Ignorar su estrés":
            $ afinidad -= 1
            alex "Bueno, yo ya terminé. Suerte con eso."
            lily "Ah... qué amable..."
            alex "(Pensando) Parece que no le importa mucho."
    
    # Después de la conversación, continúan estudiando
    lily "A veces siento que mi forma de estudiar no es la mejor..."
    alex "Cada quien tiene su propio ritmo. Lo importante es que te esfuerces."
    lily "Tienes razón. Aunque me cuesta mucho concentrarme con todo lo que pasa..."
    

label acto2_paseo:
    scene parque_tarde with fade
    
    # Alex y Lily caminando por el parque
    lily "A veces, solo salir a caminar me ayuda a despejar la cabeza. ¿Tú nunca lo haces?"
    alex "No mucho, la verdad. Siempre tengo que estar ocupado con algo."
    
    lily "Yo... cuando todo se complica, me gusta desconectarme de todo. Tal vez porque... siempre me siento como si estuviera corriendo de algo."
    alex "¿De qué hablas?"
    
    menu:
        "Preguntar más sobre lo que dijo":
            $ confianza += 1
            alex "¿De qué estás huyendo? Si te molesta hablar de eso..."
            lily "No es eso... es solo que mi pasado me persigue a veces. Pero ya no importa."
            
        "Cambiar de tema para evitar incomodarla":
            $ confianza -= 1
            alex "Supongo que todos tenemos algo que nos molesta. Pero mejor dejemos eso, ¿no?"
            lily "Sí... Mejor no hablar de eso."
    
    # Continuación de la conversación según la confianza
    if confianza > 0:
        lily "Gracias por escucharme. La verdad es que no suelo abrirme tanto con los demás."
        alex "No tienes que hacerlo si no quieres. Pero sabes que estoy aquí."
    else:
        lily "Bueno, está bien. No es algo de lo que hable mucho."
        alex "(Pensando) ¿Qué será lo que oculta? No puedo dejar de pensar en ello..."
    

label acto2_conflicto:
    scene cafeteria_atardecer with fade
    
    # Sentados en la cafetería, Lily y Alex están discutiendo sobre algo
    lily "No entiendo cómo puedes pensar que todo se soluciona con el tiempo, ¡las cosas deben cambiar ahora!"
    alex "No es tan simple, a veces lo mejor es esperar a que todo se calme. No siempre hay que apresurarse a cambiar."
    
    menu:
        "Defender su punto de vista":
            $ afinidad += 1
            alex "Creo que necesitas darle tiempo a las cosas. No todo se arregla de golpe."
            lily "Lo sé, pero siempre he tenido miedo de que el tiempo no lo cure todo..."
            
        "Tratar de convencerla de que está equivocada":
            $ afinidad -= 1
            alex "No sé, Lily. No siempre se puede cambiar todo al instante."
            lily "No me hables así... No es tan fácil para mí..."
    
    # Al final de la discusión
    if afinidad > 0:
        lily "Quizás tienes razón. Tal vez estoy siendo demasiado impulsiva."
        alex "Lo importante es que lo estamos hablando. No tienes que cargar con todo sola."
    else:
        lily "Creo que necesito estar sola un rato..."
        alex "(Pensando) ¿Qué pasó? ¿Por qué no podemos entendernos?"
    
label acto3_reconocimiento:
    scene parque_noche with fade
    
    # Alex y Lily están sentados en un banco, mirando las estrellas
    alex "(Pensando) No puedo dejar de pensar en ella. Cada vez que estamos juntos, todo parece más claro... pero, ¿cómo le digo esto?"
    lily "¿Estás bien, Alex? Te noto pensativo."
    
    menu:
        "Confesar que está pensando en ella":
            $ confianza += 1
            alex "La verdad... No puedo dejar de pensar en ti, Lily."
            lily "(Sorpresa) ¿De verdad?"
            alex "No quiero que esto arruine nuestra amistad... Pero me siento diferente."
            lily "Yo también siento algo... No estoy segura de cómo manejarlo, pero lo siento."
            
        "Cambiar de tema para evitar la confesión":
            $ confianza -= 1
            alex "No es nada... Solo estoy un poco cansado."
            lily "Si lo dices... Pero, ¿estás seguro de que no pasa nada?"
            alex "(Pensando) ¿Por qué es tan difícil hablar de esto?"
    
    # Continuación según la confianza
    if confianza > 0:
        lily "Creo que también siento algo más, pero no sé si debo decirlo."
        alex "Podemos pensar las cosas con calma. Lo importante es que estamos aquí, juntos."
    else:
        lily "Lo que pasa es que... siempre me cuesta confiar en las personas."
        alex "(Pensando) Tal vez es el momento de arriesgarse..."
    
label acto3_confesion:
    scene atardecer_con_luz_suave with fade
    
    # Lily y Alex se encuentran en el mismo lugar que antes, pero ahora la tensión es palpable
    lily "Alex, ¿tú alguna vez has tenido miedo de sentir algo por alguien?"
    alex "(Pensando) ¿Está hablando de nosotros?"
    
    menu:
        "Confesar sus sentimientos sin reservas":
            $ seguridad += 1
            alex "Sí, de hecho, tengo miedo. Miedo de que esto cambie nuestra amistad, pero... no puedo dejar de pensar en ti."
            lily "No sé qué decir... Yo también he estado pensando en esto. Pero no quiero arruinar lo que tenemos."
            alex "Lo importante es que lo estamos diciendo ahora. Podemos encontrar una forma de manejarlo."
            
        "Decir que lo necesita pensar más":
            $ seguridad -= 1
            alex "Creo que necesitamos algo de tiempo. No estoy seguro de cómo manejarlo."
            lily "Entiendo... Pero me duele escuchar eso."
            alex "(Pensando) Tal vez no estoy listo para dar este paso..."
    
    # Continuación según la seguridad
    if seguridad > 0:
        lily "No es fácil, pero si lo estamos diciendo ahora, es porque realmente lo sentimos. No vamos a dejar que esto nos separe."
        alex "Estoy dispuesto a intentarlo. Aunque tengamos miedo, lo enfrentaremos juntos."
    else:
        lily "Creo que es mejor que nos demos un poco de espacio. No sé si estoy lista para seguir adelante."
        alex "(Pensando) Tal vez esto no sea el momento adecuado..."
    
label acto3_inseguridades:
    scene cafe_intimo with fade
    
    # Alex y Lily se encuentran en el café, después de la confesión
    lily "Alex... no sé si debo seguir adelante con esto. Tengo tantas dudas."
    alex "Entiendo tus dudas. Yo también estoy asustado. Pero, ¿no crees que lo que sentimos es real?"
    
    menu:
        "Intentar calmarla y ofrecer apoyo":
            $ afinidad += 1
            alex "Podemos tomarlo con calma. No necesitamos presionarnos. Lo importante es que ambos estamos aquí, ¿verdad?"
            lily "Sí... Tienes razón. Tal vez me estaba dejando llevar por el miedo."
            alex "No tienes que hacerlo sola. Estoy aquí."
            
        "No saber qué decir y quedarse en silencio":
            $ afinidad -= 1
            alex "No sé qué decir, Lily. Yo también tengo miedo."
            lily "Eso me hace sentir peor... ¿De verdad podemos hacer esto?"
            alex "(Pensando) Tal vez todo esto está demasiado complicado..."
    
    # Continuación según la afinidad
    if afinidad > 0:
        lily "Gracias por ser paciente conmigo. Creo que puedo confiar en ti."
        alex "Siempre tendrás mi apoyo. Lo descubriremos juntos."
    else:
        lily "Quizás debería irme... Necesito pensar en todo esto."
        alex "(Pensando) ¿Estoy perdiéndola? ¿Debería haber sido más firme?"
    
label acto4_riesgo:
    scene parque_noche with fade
    
    # Alex y Lily están en el mismo lugar donde se conocieron, pero la atmósfera es diferente
    alex "(Pensando) Este es el momento... No puedo seguir esperando. Si no lo hago ahora, no lo haré nunca."
    lily "Alex, he estado pensando mucho... Estoy asustada. No quiero perder lo que tenemos, pero siento que algo más está naciendo entre nosotros."
    
    menu:
        "Decidir arriesgarse y estar juntos":
            $ seguridad += 1
            alex "Tal vez es hora de ser valientes. No quiero seguir viviendo con este miedo. Lily, quiero estar contigo."
            lily "Yo también quiero intentarlo, Alex. No sé qué depara el futuro, pero lo enfrentaremos juntos."
            
        "Decidir tomar un poco más de tiempo":
            $ seguridad -= 1
            alex "Creo que... aún necesitamos tiempo. No quiero apresurarnos en algo que no estamos listos para manejar."
            lily "Entiendo... Tal vez no es el momento adecuado. Pero siempre serás importante para mí."
    
    # Continuación según la seguridad
    if seguridad > 0:
        lily "Estoy feliz de que finalmente lo hayamos hablado. Vamos a ver a dónde nos lleva todo esto."
        alex "Estoy dispuesto a tomar el riesgo. Lo importante es que estemos juntos."
    else:
        lily "Creo que necesitamos pensar más en esto. Pero siempre te recordaré como alguien importante."
        alex "(Pensando) Tal vez este no era el momento adecuado para nosotros..."
    
label acto4_miedos_lily:
    scene cuarto_lily with fade
    
    # Lily está sola, reflexionando
    lily "(Pensando) No sé si soy lo suficientemente buena para él. Mi pasado siempre me persigue y tengo miedo de que eso lo aleje."
    
    menu:
        "Hablar con Alex sobre sus miedos":
            $ confianza += 1
            lily "Alex, hay algo que necesito contarte. No sé si debo, pero siento que es lo justo."
            alex "Lo que sea, Lily. Estoy aquí para escucharte."
            lily "Mi pasado me sigue, siempre me siento insegura. Tengo miedo de que eso nos haga daño."
            alex "Lo que hayas vivido no cambia lo que siento por ti. Estoy aquí y quiero estar a tu lado, sin importar lo que haya pasado."
            
        "Callarse y no compartir sus miedos":
            $ confianza -= 1
            lily "(Pensando) No puedo decirle todo esto... No quiero que me vea como débil."
            alex "Si necesitas hablar, sabes que siempre estoy aquí."
            lily "Gracias, Alex... Pero creo que aún no estoy lista para hablar de todo eso."
    
    # Continuación según la confianza
    if confianza > 0:
        lily "Me siento más tranquila después de hablar contigo. Gracias por entender."
        alex "No tienes que cargar con tus miedos sola, estoy aquí para apoyarte."
    else:
        lily "Creo que debo hacerlo sola... Pero gracias por tu apoyo."
        alex "(Pensando) ¿Estoy realmente ayudando? Tal vez debería ser más paciente..."
    
label acto4_compromiso:
    scene lugar_significativo with fade
    
    # El ambiente está tranquilo y relajado
    alex "Lily, ahora que hemos hablado de todo, quiero decirte algo importante..."
    lily "¿Qué pasa, Alex?"
    
    menu:
        "Proponer un compromiso serio":
            $ afinidad += 1
            alex "Quiero que seas parte de mi vida. No sé qué nos depara el futuro, pero quiero intentarlo de corazón."
            lily "Yo también quiero que esto funcione. Vamos a trabajar en esto juntos."
            
        "Decidir tomar un tiempo de descanso en la relación":
            $ afinidad -= 1
            alex "Creo que necesitamos un tiempo para aclarar nuestros pensamientos. No quiero que tomemos decisiones apresuradas."
            lily "Es lo mejor... Tal vez podamos vernos después y pensar con calma."
    
    # Continuación según la afinidad
    if afinidad > 0:
        lily "Gracias por no rendirte. Lo que tenemos es algo valioso, y quiero ver hasta dónde podemos llegar."
        alex "Estoy listo para empezar este camino contigo."
    else:
        lily "Tal vez sea lo mejor... Pero siempre recordaré lo que compartimos."
        alex "(Pensando) Quizás este no sea nuestro momento, pero siempre aprenderé de esta experiencia."
    
label final_positivo:
    scene parque_al_anochecer with fade
    
    # Alex y Lily están sentados juntos, viendo el atardecer
    alex "Nunca pensé que llegaríamos hasta aquí. Todo ha sido un viaje tan inesperado, pero aquí estamos."
    lily "Sí, no fue fácil, pero lo logramos. A veces el miedo solo nos detiene. Pero juntos... podemos con todo."
    
    alex "¿Sabes qué? Creo que todo esto fue una lección sobre el valor de arriesgarse. Y no cambiaría nada de lo que hicimos."
    lily "Ni yo. Creo que hemos encontrado algo verdadero aquí. Y aunque el futuro es incierto, sé que lo enfrentaremos juntos."
    
    # Se toman de las manos, mostrando confianza mutua
    alex "¿Te gustaría que intentáramos construir algo juntos, sin miedos?"
    lily "Sí, Alex. Quiero ver a dónde nos lleva esto. Vamos a hacerlo, sin mirar atrás."
    
    # Fin positivo con una sensación de esperanza para el futuro

    return

label final_neutro:
    scene cafe_tranquilo with fade
    
    # Lily y Alex están sentados en el café donde solían encontrarse
    lily "Creo que ambos hemos crecido mucho durante este tiempo, ¿verdad?"
    alex "Sí, y aunque no lo nuestro sea el amor que imaginamos, no quiero perder tu amistad."
    
    lily "Lo mismo pienso. Hemos compartido mucho y sé que siempre estaré aquí para ti, de una forma u otra."
    alex "Lo importante es que, sin importar lo que pase, siempre tendremos algo valioso entre nosotros."
    
    # Se quedan mirando el uno al otro con una sonrisa cálida
    lily "No sé qué nos depara el futuro, pero quiero que sigamos adelante, aunque sea de manera diferente."
    alex "De acuerdo, no importa cómo termine esto, siempre estaré agradecido por lo que compartimos."
    
    # Final con un tono de comprensión mutua y una despedida amistosa

    return

label final_triste:
    scene atardecer_solitario with fade
    
    # Alex y Lily están caminando juntos, pero hay una clara tensión
    alex "Lily... Sé que esto no ha sido fácil para ninguno de los dos."
    lily "Lo sé, Alex. Siento que hemos llegado a un punto donde lo que sentíamos ya no es suficiente."
    
    alex "Tal vez... tal vez no estamos listos. Tal vez aún hay cosas que necesitamos resolver por separado."
    lily "Sí... Tengo miedo de que todo esto se haya complicado demasiado, y no quiero arrastrarte a algo que no podemos manejar."
    
    # Pausa, ambos se miran, con una mezcla de tristeza y aceptación
    alex "Quizás el amor no siempre es suficiente. Tal vez necesitamos encontrar nuestras respuestas por separado."
    lily "Te quiero, Alex, pero lo mejor es que cada uno siga su camino."
    
    # Se separan con una mirada triste, pero con la esperanza de encontrar algo mejor en el futuro
    alex "(Pensando) Quizás algún día nos encontremos de nuevo, pero por ahora, el adiós es lo mejor."
    lily "(Pensando) A veces, el amor no es suficiente, y debemos aprender a dejar ir."
    
    return


