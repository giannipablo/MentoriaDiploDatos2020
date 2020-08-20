

##  **1. ¿De qué se trata el conjunto de datos?**

El conjunto de datos consiste de diálogos escritos y sincrónicos entre un docente y un estudiante realizado a través de una aplicación de mensajería instantánea desarrollada para este fin. La empresa intermediaria vincula a docentes y estudiantes por medio de dicha aplicación y recolecta los datos de los diálogos para diversos fines, entre ellos el control de la calidad del servicio. Debido a que los alumnos son mayormente de Estados Unidos, los diálogos se encuentran en idioma Inglés mientras que los tutores particulares son de diferentes partes del mundo y no son necesariamente residentes Estadounidenses. El objetivo de los diálogos es brindar soporte a los estudiantes  de nivel secundario en las tareas de asignaturas como matemática, química y física.

El conjunto de datos completo tiene 18 mil diálogos que suman 7 mil horas. Como los diálogos se basan en didáctica "inquiry-based" los docentes hacen muchas preguntas. Hay 240 mil preguntas en el conjunto de datos. Al finalizar el diálogo los estudiantes evalúan cuán satisfechos están con la clase particular con una nota de 1 a 5, con timestamps en cada turno, con información demográfica de los participantes como género, edad, notas en exámenes, tipo de pago del servicio, país, entre otros.
¿Cuál es la variable objetivo que hay que predecir? ¿Qué significado tiene? ¿Cómo la definieron de forma binaria?
La variable objetivo es student_rating_cat, a la cual la definimos como una variable binaria que representa la satisfacción o insatisfacción del estudiante luego de una sesión con el tutor. El éxito del diálogo representa/conlleva que el estudiante quedó conforme con la labor del tutor, teniendo en cuenta que la conformidad es una cualidad subjetiva que depende del criterio del estudiante. En el conjunto de datos a la variable objetivo la derivamos del puntaje asignado por el estudiante al diálogo con el tutor. La variable puede tomar valores enteros en el rango del 1 al 5. Para binarizarla consideramos los casos con calificación en el rango 1 al 2 inclusive como caso/clase negativa, los casos con calificación en el rango 4 al 5 inclusive como caso/clase positiva mientras que los casos con calificación igual a 3 serán considerados neutros, y no serán tenidos en cuenta en el análisis. 


## **2. ¿Cuál es la variable objetivo que hay que predecir? ¿Qué significado tiene? ¿Cómo la definieron de forma binaria?**
La variable objetivo es student_rating_cat, a la cual la definimos como una variable binaria que representa la satisfacción o insatisfacción del estudiante luego de una sesión con el tutor. El éxito del diálogo representa/conlleva que el estudiante quedó conforme con la labor del tutor, teniendo en cuenta que la conformidad es una cualidad subjetiva que depende del criterio del estudiante. En el conjunto de datos a la variable objetivo la derivamos del puntaje asignado por el estudiante al diálogo con el tutor. La variable puede tomar valores enteros en el rango del 1 al 5. Para binarizarla consideramos los casos con calificación en el rango 1 al 2 inclusive como caso/clase negativa, los casos con calificación en el rango 4 al 5 inclusive como caso/clase positiva mientras que los casos con calificación igual a 3 serán considerados neutros, y no serán tenidos en cuenta en el análisis. 



## **3. ¿Qué información (atributos) hay disponibles para hacer la predicción?**

### Atributos relativos a la metadata


| Atributo | Descripción | Tipo de dato |
| -------- | -------- | -------- |
| session_id    | Clave única para la sesión de tutoría.    | Entero    |
| tutor_id   | Identificador único de tutor.  |Entero  |
| student_id   | Identificador único de estudiante.  |Entero |
| timestamp | Marca de tiempo de inicio de la sesión. |Fecha |
| feedback_score | Escala 0-1 con la calidad de la sesión puntuada. | Flotante [0,1] |
| wait_time | Tiempo de espera del estudiante antes de conectar con un tutor, en segundos. | Flotante |
| ended_by_reason | Acción final sobre cómo terminó la sesión (quién la terminó y cómo). | Categórica |
| session_category | Categorización detallada del aprendizaje del estudiante. | Categórica |
| consolidated_session_category | medidas ordinales más generales de la calidad de la sesión: sin aprendizaje, brecha aclarada, explicada, puenteada. |Categórica |
|student_complained | Indica si el alumno se quejó o no de características específicas del servicio. | Booleano |
| student_complained_clarity | Indica si el alumno se quejó o no de características específicas del servicio: claridad | Booleano |
|student_complained_speed | Indica si el alumno se quejó o no de características específicas del servicio: velocidad.| Booleano |
|student_complained_subject | Indica si el alumno se quejó o no de características específicas del servicio: tema. | Booleano |
| student_complained_other | Indica si el alumno se quejó o no de características específicas del servicio: otros. |Booleano |
| session_tag_cheating | El tutor marcó la sesión como estudiante haciendo trampa. | Booleano |
| session_tag_inappropriate | El tutor marcó la sesión porque el estudiante se comportó de manera inapropiada. | Booleano |
| session_tag_other_subject |El tutor marcó la sesión como estudiante preguntando sobre otro tema. | Booleano |
| session_tag_no_material | El tutor marcó la sesión porque no se está enviando contenido. | Booleano |
| session_tag_student_left |El tutor marcó la sesión cuando el alumno abandonó la sesión. | Booleano | 
|session_tag_student_no_engaging | El tutor marcó la sesión porque el estudiante no coopera. | Booleano |
| session_tag_used_whiteboard |El tutor marcó la sesión como sesión con pizarra. | Booleano |
| student_rating | Calificación de 1 a 5 estrellas de la calidad de la sesión por parte del estudiante. | Entero Ordinal |
|length_of_session | Duración de la sesión en  segundos. |Flotante |
| avg_tutor_response_time | Número medio de segundos desde la expresión del alumno hasta la declaración del tutor. | Flotante |
| subject |Matemáticas, Física, Química. |Categórica |
| subtopic | Álgebra, Geometría, Calc, etc. | Categórica |
| rubric_version | Identifica qué versión de la escala de feedback se utilizó. | Categórica |
| tutor_gender | Género del tutor M / F. | Categórica |
| tutor_fired | Tutor despedido de la plataforma | Booleano |
| tutor_math_exam_score | Puntaje del tutor en un examen de ingreso sobre matemáticas. | Flotante [0,100] |
| tutor_physics_exam_score | Puntaje del tutor en un examen de ingreso sobre física. | Flotante [0,100] |
| tutor_chemistry_exam_score | Puntaje del tutor en un examen de ingreso sobre química. | Flotante [0,100] |
| tutor_last_sign_in_country | Dirección IP extranjera del último ingreso del tutor. | Categórica |
| tutor_age | Edad del tutor en años. | Entero |
| student_platform | IOS y versión. | |Categórica |
| student_app_version |IOS y versión. | Categórica |
| student_transactions_amount | Indicador de si se compraron o no servicios. | Entero |


### Atributos relativos a los diálogos entre tutor y estudiante


|Atributo | Descripción | Tipo de dato |
| -------- | -------- | -------- |
| nturnos_tutor | Número de turnos del tutor. | Entero |
| nturnos_student | Número de turnos del estudiante. | |Entero |
| twlen_tutor | Cantidad de palabras totales de tutor por diálogo. | Entero  |
| twlen_student  | Cantidad de palabras totales del estudiante por diálogo.  | Entero  |
 |avtwlen_tutor  | Promedio de la cantidad de palabras por turno del tutor.  | Flotante  
|avtwlen_student  | Promedio de la cantidad de palabras por turno del estudiante.  | Flotante  |
 | text | Texto del turno tokenizado.  | Lista de cadena de caracteres  |
 
## **4. ¿Qué atributos imagina usted que pueden ayudar en la predicción?**

### Atributos relativos a la metadata



| Atributos |
| -------- | 
| tutor_age     | 
| session_tag_no_material |
|session_tag_student_left |
| session_tag_student_no_engaging |
| student_complained |
| student_complained_clarity |
| student_complained_speed |
| student_complained_subject |
| student_complained_other |
| session_tag_cheating |
| session_tag_inappropriate |
| session_tag_other_subject |
| session_tag_no_material |
| session_tag_student_left |
| session_tag_student_no_engaging 

### Atributos relativos a los diálogos entre tutor y estudiante



| Atributo| 
| -------- | 
| nturnos_tutor | 
| nturnos_student |
| twlen_tutor |
| twlen_student |
| avtwlen_tutor |
| avtwlen_student |
| text |




 

 


