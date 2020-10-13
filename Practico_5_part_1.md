# **Práctico 5 (Parte 1): Descripción de los Datos y la Tarea**


##  **1. Ir a leer 15 ejemplos de diálogos clasificados de forma negativa y 5 positivos y copiar palabras, frases o describir otras características que les llamaron la atención en los diálogos negativos.**


## **2. ¿Qué esperan ver en los clusters de palabras?**

Esperamos ver palabras agrupadas por similitud semántica, es decir, palabras y frases en diferentes clusters según su significado o connotación, por ejemplo palabras que expresan agradecimiento o satisfacción agrupadas en un mismo clúster. También se espera ver algún clúster formado por fórmulas o fórmulas y números ya que como se evidenció en los anteriores prácticos existen una gran cantidad de expresiones matemáticas presentes en los diálogos debido a que los mismos corresponden a consultas realizadas por estudiantes de nivel secundario a tutores sobre asignaturas como matemática, química y física. 


## **3. ¿Cómo les parece que se evaluará el modelo que generen?**

El modelo evaluará el texto atendiendo a las similitudes y diferencias entre palabras, se espera que  maximice la similitud entre los elementos de un mismo grupo y a la vez maximice las diferencias entre los diversos grupos que forme. Si el algoritmo nos permite descubrir frases significativas para cada grupo de acuerdo a la interacciones entre estudiantes y tutores, esto nos ayudará a encontrar patrones y mejorar el servicio brindado por la plataforma y mejorar la experiencia de los estudiantes.


## **4. ¿Cuál les parece que debe ser la duración mínima de un diálogo para poder predecir la satisfacción del estudiante? ¿Piensan que la duración del diálogo les puede servir para predecir la satisfacción?**

La lógica y la intuición nos dicen que la duración del diálogo es una característica importante que será útil para predecir la satisfacción del estudiante. Teniendo en cuenta esto, consideramos que la duración mínima de un diálogo debe ser de 3 turnos para obtener información que sea de utilidad para la predicción. Por el contrario, los diálogos demasiado cortos no ofrecen información suficiente para clasificar un diálogo de manera correcta.

## **5. Del primer cuarto, segundo cuarto, tercer cuarto y cuarto cuarto de los diálogos, ¿cuál les parece que puede ser más informativo para predecir la satisfacción del estudiante?**

Creemos que la última cuarta parte del diálogo, que es la que corresponde al cierre del diálogo puede ser la que proporcione mayor información para mejorar la predicción respecto a la satisfacción del estudiante.


## **6. El modelo que tienen en mente ¿están seguros que no usa las etiquetas hasta el final?**

A las etiquetas (correspondientes a un diálogo clasificado como positivo o negativo) no la usaremos como parte del proceso de entrenamiento del modelo, sino que serán usadas recién en la etapa de evaluación del modelo


