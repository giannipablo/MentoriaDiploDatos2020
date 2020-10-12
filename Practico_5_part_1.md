# **Práctico 5 (Parte 1): Descripción de los Datos y la Tarea**


##  **1. Ir a leer 15 ejemplos de diálogos clasificados de forma negativa y 5 positivos y copiar palabras, frases o describir otras características que les llamaron la atención en los diálogos negativos.**



## **2. ¿Qué esperan ver en los clusters de palabras?**

Esperamos ver palabras agrupadas por similitud semántica, es decir, palabras y frases en diferentes clusters según su significado o connotación, por ejemplo palabras que expresan agradecimiento o satisfacción agrupadas en un mismo clúster. También se espera ver algún clúster formado por fórmulas o fórmulas y números ya que como se evidenció en los anteriores prácticos existen una gran cantidad de expresiones matemáticas presentes en los diálogos debido a que los mismos corresponden a consultas realizadas por estudiantes de nivel secundario a tutores sobre asignaturas como matemática, química y física mediante una app. 


## **3. ¿Cómo les parece que se evaluará el modelo que generen?**

El modelo evaluará el texto atendiendo a las similitudes y diferencias entre palabras, se espera que  maximice la similitud entre los elementos de un mismo grupo y a la vez maximice las diferencias entre los diversos grupos que forme. Si el algoritmo nos permite descubrir frases significativas para cada grupo de acuerdo a la interacciones entre estudiantes y tutores, esto nos ayudará a encontrar patrones y mejorar el servicio brindado por la plataforma y mejorar la experiencia de los estudiantes.


## **4. ¿Cuál les parece que debe ser la duración mínima de un diálogo para poder predecir la satisfacción del estudiante? ¿Piensan que la duración del diálogo les puede servir para predecir la satisfacción?**

La duración mínima de un diálogo debe ser de un 1 minuto aproximadamente. Los diálogos demasiado cortos no ofrecen la información necesaria para clasificar un diálogo de manera correcta. La lógica y la intuición nos dicen que la duración del diálogo es una característica importante que será útil para predecir la satisfacción del estudiante. Pero de acuerdo al análisis realizado en el ejercicio 3 del práctico 1y2(Practico_1y2_part_3.ipynb), en donde se analizó la correlación entre la duración del diálogo y la satisfacción del estudiante, se puede evidenciar que dicha variable no es tan útil como imaginábamos para predecir la satisfacción del estudiante. 


## **5. Del primer cuarto, segundo cuarto, tercer cuarto y cuarto cuarto de los diálogos, ¿cuál les parece que puede ser más informativo para predecir la satisfacción del estudiante?**

La cantidad de palabras utilizada en cada diálogo, si se utilizan signos de puntuación, el uso de emoticons serán características importantes al momento de predecir la satisfacción del sestudiante.

## **6. El modelo que tienen en mente ¿están seguros que no usa las etiquetas hasta el final?**

