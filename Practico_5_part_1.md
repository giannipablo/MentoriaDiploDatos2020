# **Práctico 5 (Parte 1): Descripción de los Datos y la Tarea**


### 1. Ir a leer 15 ejemplos de diálogos clasificados de forma negativa y 5 positivos y copiar palabras, frases o describir otras características que les llamaron la atención en los diálogos negativos.

#### [Ver dialogos completos: Practico 5 (parte 2) - Exploración de dialogos positivos y negativos](Practico_5_part_2.ipynb#dialogos_positivos_negativos)

Características notables observamos:

* Entre los dialogos negativos predominan aquellos más cortos (menos de 20 turnos)

* En algunos casos de diálogos negativos el estudiante deja de responder y se advierten varios turnos del tutor seguidos tratando de conseguir respuesta del estudiante.

> >
    ...
    -student: No I do n't sorry
    -tutor: OK .
    -tutor: So when we perform an operation with two measurements in the sciences , the number of significant digits in the final answer should be the same as the number of significant digits in the measurement with the least number of significant digits .
    -tutor: Does that make sense ?
    -tutor: Take a second and review what I just said .
    -tutor: Are you still with me ?
    -tutor: Unfortunately you 've been away from the app for more than 5 minutes . I had to end the session so that I can help other students . Feel free to submit another request whenever you 're ready !

* En algunos casos de dialogos negativos, no se advierte que el estudiante lo va a calificar como negativo, ya que la conversación se resuelve cordialmente. 

> >
    ...
    -tutor: Can you show me how you arrived at this ? What did you have for a , b , and c ?
    -student: that ca n't be right
    -student: i apologize i have to leave ...
    -tutor: No worries . Come back anytime you would like more help !
    -tutor: Have a great day !
    -student: thjs app is great ! !
    -tutor: I agree with that !  :)

* En general se observa que la satisfacción del estudiante se hace explícita, mientras que los sentimientos negativos no se hacen expícitos en la mayoría de los casos. En cambio se observan falta de respuesta de los estudiantes, respuestas monosilábicas o finalización abrupta del dialogo por parte del estudiante. 

> >
    ...
    -tutor: That 's true , but we did n't buy 11 of each kind .
    -tutor: we bought 11 total .
    -student: I know
    -student: We only bought 11
    -tutor: we bought " x " tickets for right field , at $ 37 each .
    -tutor: so if we multiply the number of tickets by the price , what do we have ?
    -tutor: It wo n't be a number , because we do n't know yet the actual number of tickets .
    -tutor: It will be an expression .
    -student: Ok
    -tutor: Let 's go back to that apple and oranges example again .
    -student: No thank you have a good night

* En los cierres de los diálogos positivos se observa un intercambio de mensajes expresando gratitud y satisfacción que se extiende a más de un turno de cada interlocutor. Las expresiones son enfáticas y se utilizan emojis o emoticones

> >
    ...
    -student: Can we look at where to start here ?
    -student: Ok . No prob .
    -student: Thank you !
    -tutor: Thanks ! You were really nice .
    -student: 😃
    -tutor: It was fun doing maths with you .
    -student: You too
    -tutor: Thanks for using *** ! Have  a good one ! :)


> >
    ...
    -tutor: That 's correct , wonderful work , Alexa !
    -student: thank you so much !
    -tutor: You 're very welcome !
    -tutor: Do you have any other questions about how we solved that problem ?
    -student: no i think i m ok thank you very much !
    -tutor: Great ! Is there anything else I can help you with ?
    -student: i think that s all thank you !
    -tutor: Fantastic . Have a wonderful night , Alexa , and thank you for using *** !
    -student: you too !



* En muchos diálogos negativos el tutor manifiesta desconocimiento o insuficiencia en el tema de la consulta

> >
    ...
    -tutor: Unfortunately , your problem exceeds the math level we currently support


> >
    ...
    -tutor: I m afraid i m not well versed in organic chemistry


> >
    ...
    -tutor: Please accept my apology !
    -tutor: Unfortunately , your problem exceeds the math level we currently support . Is there something else I can help  you with ?


* De la lectura de varios dialogos negativos se observa que hay muchos casos en que parece no haber entendimiento y coherencia entre los interlocutores o los estudiantes solamente están bromeando o tienen conducta inapropiada.

> >
    ...
    -tutor: Do you need help with this problem ?
    -student: It 's 4 am I just downloaded the app I wanted to see how it work I do n't really need a tutor I do n't start school till September 6th
    -tutor: Okay . :)
    -student: Add me on snapchat
    -tutor: Welcome back anytime you need help with math , chemistry or physics .
    -student: Add
    -student: Me
    -student: On
    -student: Snapchat

> >
    ...
    -student: Sounds like a plan
    -tutor: Hi Ahmed ! Welcome to *** !
    -tutor: What can I help you with ?
    -student: Do want have sex
    -student: Ok

> >
    ...
    -tutor: Hello there Joe !
    -student:  I like you
    -tutor: Welcome to Yup ! :)
    -tutor: Thank you ! How can I help you ?
    -tutor: Do you have a math problem that you need help with ?
    -student: <url>
    -student: Bye shy tutor
    -tutor: Do you have a math problem that I can help you with ?

Algunas expresiones positivas

    Correct!
    Alright
    Thank you!
    Great
    Cool
    You got it right!
    Perfect ! 
    :)
    Right
    Good work
    Ok
    Okay
    🙌 Nice
    Thanks!
    awesome
    Excellent
    Excellent job ! :)
    Nice one ! :)
    Superb
    Great job
    Outstanding

Algunas expresiones negativas

    not much
    idk how to do it
    I don't know
    Nope
    Confused
    I 'm not sure
    i am lost
    Unfortunately
    doesn't work

#### 2. ¿Qué esperan ver en los clusters de palabras?

Esperamos ver palabras agrupadas por similitud semántica, es decir, palabras y frases en diferentes clusters según su significado o connotación, por ejemplo palabras que expresan agradecimiento o satisfacción agrupadas en un mismo clúster. También se espera ver algún clúster formado por fórmulas o fórmulas y números ya que como se evidenció en los anteriores prácticos existen una gran cantidad de expresiones matemáticas presentes en los diálogos debido a que los mismos corresponden a consultas realizadas por estudiantes de nivel secundario a tutores sobre asignaturas como matemática, química y física. 


#### 3. ¿Cómo les parece que se evaluará el modelo que generen?

El modelo evaluará el texto atendiendo a las similitudes y diferencias entre palabras, se espera que  maximice la similitud entre los elementos de un mismo grupo y a la vez maximice las diferencias entre los diversos grupos que forme. Si el algoritmo nos permite descubrir frases significativas para cada grupo de acuerdo a la interacciones entre estudiantes y tutores, esto nos ayudará a encontrar patrones y mejorar el servicio brindado por la plataforma y mejorar la experiencia de los estudiantes.


#### 4. ¿Cuál les parece que debe ser la duración mínima de un diálogo para poder predecir la satisfacción del estudiante? ¿Piensan que la duración del diálogo les puede servir para predecir la satisfacción?

La lógica y la intuición nos dicen que la duración del diálogo es una característica importante que será útil para predecir la satisfacción del estudiante. Teniendo en cuenta esto, consideramos que la duración mínima de un diálogo debe ser de 3 turnos para obtener información que sea de utilidad para la predicción. Por el contrario, los diálogos demasiado cortos no ofrecen información suficiente para clasificar un diálogo de manera correcta.

#### 5. Del primer cuarto, segundo cuarto, tercer cuarto y cuarto cuarto de los diálogos, ¿cuál les parece que puede ser más informativo para predecir la satisfacción del estudiante?

Creemos que la última cuarta parte del diálogo, que es la que corresponde al cierre del diálogo puede ser la que proporcione mayor información para mejorar la predicción respecto a la satisfacción del estudiante.


#### 6. El modelo que tienen en mente ¿están seguros que no usa las etiquetas hasta el final?

A las etiquetas (correspondientes a un diálogo clasificado como positivo o negativo) no la usaremos como parte del proceso de entrenamiento del modelo, sino que serán usadas recién en la etapa de evaluación del modelo


