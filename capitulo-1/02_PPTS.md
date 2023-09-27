# OBJETIVOS
- Bienvenidos a nuestra primera clase. Hoy vamos a sumergirnos en el emocionante mundo de Python. 
- Vamos a aprender lo esencial sobre Python y por qué es una herramienta crucial en el campo de la ciencia de datos y más allá.
- Primero, exploraremos qué es Python y un poco de su historia para entender por qué es tan relevante hoy en día. - Luego, hablaremos sobre las diversas aplicaciones de Python, desde el análisis de datos hasta el desarrollo web y la automatización de procesos. 
- Además, introduciremos los conceptos básicos como la sintaxis de Python, tipos de variables, estructuras de datos, operadores, entre muchas otras cosas más.
- Segundo, entenderemos qué es exactamente Jupyter Notebook y por qué es tan popular en el mundo de la ciencia de datos. 
- Luego, veremos cómo instalar Jupyter Notebook en sus propias máquinas virtuales para que puedan usarlo en su trabajo. Vamos a aprender a crear un nuevo cuaderno de Jupyter el cual es llamado notebook y cómo ejecutar código Python en sus celdas. 
- También exploraremos cómo imprimir resultados y cómo utilizar Markdown para agregar texto descriptivo y formato a sus notebooks.
- Las aplicaciones de IA están a punto de despegar, y los científicos de datos que se preparen ahora serán los que más se beneficien en el futuro. ¡Empecemos!
# AGENDA
La agenda para hoy es la siguiente:
- ¿Qué es Python?
- El Zen de Python
- Usos de Python
- ¿Quiénes usan Python?
- Vamos a poner manos a la obra ejecutando ipython en los famosos notebooks. 
# PYTHON
## 1. ¿Qué es Python?
- Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Que fue creado por Guido Van Rossum en 1991 ya con más de 30 años ha ganado una tremenda popularidad en todo el mundo. Pero, ¿qué significa exactamente todo lo que dije?
- "Lenguaje de alto nivel" significa que Python está diseñado para que los humanos lo lean y escriban fácilmente, lo que lo hace muy legible y comprensible.
- "Interpretado" implica que no necesitas compilar el código antes de ejecutarlo; el intérprete de Python lo hace en tiempo real.
- "De propósito general" o multi paradígma que  significa que Python se puede utilizar en una amplia gama de aplicaciones, desde el desarrollo web hasta la inteligencia artificial, y juegos.
- Python es un lenguaje orientado a objetos, lo que significa que puedes crear clases y objetos para modelar tu programa. Conceptos como abstracción, herencia, encapsulamiento y polimorfismo facilita la creación de sistemas de software eficientes y bien estructurados.
- Si desean obtener más detalles sobre la historia y características técnicas de Python, pueden consultar este enlace: Enlace a Wikipedia.
## 2. El Zen de Python
El "Zen de Python", que es una guía de estilo para escribir código en Python. Estos principios promueven la legibilidad, la simplicidad y la claridad en el código. Aquí está una breve explicación de cada uno de los principios mencionados:
- Beautiful is better than ugly. (Lo bonito es mejor que lo feo): Se refiere a la importancia de escribir código que sea estéticamente agradable y fácil de leer.
- Explicit is better than implicit. (Lo explícito es mejor que lo implícito): Significa que es preferible ser claro y directo (explícito) en lugar de dejar cosas al entendimiento (implícito).
- Simple is better than complex. (Lo simple es mejor que lo complejo): Aboga por la simplicidad en el diseño del código en lugar de la complejidad innecesaria.
- Complex is better than complicated. (Lo complejo es mejor que lo complicado): Indica que cuando la complejidad es necesaria, debe ser evidente y no confusa.
- Flat is better than nested. (Lo plano es mejor que lo anidado): Sugiere que se deben evitar niveles excesivos de anidación en el código.
- Sparse is better than dense. (Lo disperso es mejor que lo denso): Destaca la importancia de usar espacio y líneas en blanco para hacer que el código sea más legible.
- Readability counts. (La legibilidad es importante): Subraya que la legibilidad del código es fundamental para su mantenimiento y comprensión.
- Special cases aren't special enough to break the rules. (Los casos especiales no son lo suficientemente especiales como para romper las reglas): Implica que las reglas generales de estilo y diseño de código deben aplicarse de manera consistente.
- Although practicality beats purity. (Aunque la practicidad vence a la pureza): Reconoce que, en la práctica, a veces es necesario hacer compromisos entre la pureza del diseño y la eficiencia o la funcionalidad.
- Errors should never pass silently. (Los errores nunca deben pasar en silencio): Significa que es importante manejar los errores de manera adecuada y no ignorarlos.
- Unless explicitly silenced. (A menos que estén silenciados de manera explícita): Indica que, en algunos casos, puede ser apropiado silenciar deliberadamente los errores.
- In the face of ambiguity, refuse the temptation to guess. (Ante la ambigüedad, rechaza la tentación de adivinar): Sugiere que es mejor ser explícito y evitar suposiciones cuando el significado no está claro.
- There should be one-- and preferably only one --obvious way to do it. (Debería haber una, y preferiblemente solo una, manera obvia de hacerlo): Aboga por la simplicidad y la consistencia en la forma en que se realiza una tarea en Python.
- Although that way may not be obvious at first unless you're Dutch. (Aunque esa forma puede no ser obvia al principio a menos que seas holandés): Un toque humorístico que hace referencia al creador de Python, Guido van Rossum, quien es holandés.
- Now is better than never. (Ahora es mejor que nunca): Enfatiza la importancia de tomar acción y no postergar tareas innecesariamente.
- Although never is often better than right now. (Aunque nunca a menudo es mejor que ahora mismo): Reconoce que, a veces, es mejor esperar y pensar antes de actuar impulsivamente.
- If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. (Si la implementación es difícil de explicar, es una mala idea. Si la implementación es fácil de explicar, puede ser una buena idea): Impulsa a escribir código que sea claro y fácil de entender.
- Namespaces are one honking great idea -- let's do more of those. (Los espacios de nombres son una idea genial, hagamos más de esos): Resalta la utilidad de los espacios de nombres en Python para evitar conflictos de nombres.
Puedes obtener más información sobre el "Zen de Python" y su importancia en el enlace proporcionado: PEP 20 - The Zen of Python
## 3. Usos de python
Python se utiliza en una variedad de aplicaciones:
- Desarrollo web: Python es ideal para crear sitios y aplicaciones web dinámicas.
- Análisis de datos: Python es ampliamente utilizado en el campo del análisis de datos para examinar grandes conjuntos de datos.
- Ciencia de la computación: Los científicos de la computación recurren a Python para investigaciones y desarrollo de software.
- Inteligencia artificial: Python es una herramienta clave en el desarrollo de aplicaciones de inteligencia artificial.
### Desarrollo Web:
- Django: Es un framework web de alto nivel que facilita la creación de aplicaciones web seguras y escalables.
- Flask: Es un microframework web que es fácil de aprender y utilizar para crear aplicaciones web pequeñas y medianas.
- FastAPI es un framework diseñado específicamente para el desarrollo rápido de API RESTful de alto rendimiento.
### Testing: 
- PyTest: Es una biblioteca popular para escribir pruebas unitarias y de integración en Python.
### Web Scraping:
- Beautiful Soup: Es una biblioteca para extraer información de páginas web y analizar documentos HTML y XML.
- Scrapy: Es un framework para la extracción de datos a gran escala y la navegación por sitios web.
- Selenium: Una herramienta ampliamente utilizada para la automatización de navegadores web. Se puede utilizar para realizar tareas de web scraping interactivas.
### Análisis de Datos y Visualización:
- Pandas: Es una biblioteca poderosa para el análisis y manipulación de datos.
- Matplotlib: Es una biblioteca para crear gráficos y visualizaciones de datos.
- Seaborn: Es una biblioteca que mejora la visualización de datos y se integra bien con Pandas y Matplotlib.
### Machine Learning:
- scikit-learn: Es una biblioteca ampliamente utilizada para machine learning que proporciona herramientas para clasificación, regresión, agrupación y más.
- TensorFlow: Es una plataforma de aprendizaje automático de código abierto desarrollada por Google que es ampliamente utilizada en aplicaciones de redes neuronales y deep learning.
- Keras: Es una API de alto nivel que se ejecuta sobre TensorFlow y facilita la creación de modelos de aprendizaje profundo.
- PyTorch: Es una biblioteca de aprendizaje profundo que se ha vuelto muy popular debido a su flexibilidad y facilidad de uso.
### Big Data:
- Apache Spark: Aunque está principalmente escrito en Scala, Python es uno de los lenguajes compatibles para programar aplicaciones en Spark, lo que lo hace relevante para big data.
- Apache Hadoop: Un framework de procesamiento distribuido que se utiliza para el procesamiento y almacenamiento de grandes conjuntos de datos.
- Apache Kafka: Una plataforma de streaming en tiempo real que se utiliza para la transmisión de datos y procesamiento de eventos en tiempo real.
- Apache Flink: Un framework de procesamiento de datos en tiempo real y por lotes que se utiliza para análisis de datos y procesamiento de transmisiones.
- Apache Hive: Una herramienta de análisis de datos que se utiliza para consultas y administración de datos en entornos de Big Data.
### Internet de las Cosas (IoT):
- MicroPython: Es una implementación de Python 3 diseñada para ejecutarse en microcontroladores y placas de desarrollo utilizadas en proyectos de IoT.
## 4. ¿Qué compañias usan python?
Python es un lenguaje que atrae a una amplia audiencia:
- Muchos estudiantes comienzan su viaje de programación con Python debido a su facilidad de aprendizaje.
- Python es versátil y puede ser utilizado para una amplia variedad de proyectos personales.
- Desarrolladores de software, científicos de datos e ingenieros de aprendizaje automático utilizan Python en sus trabajos diarios.
Google: TensorFlow.
Facebook: Django.
Instagram: Django.
Netflix:
Dropbox: Pyston.
Spotify:
NASA:
Tesla: Django.
Reddit: Pylons.
Quora: Django.
Uber:
Airbnb: Airflow.
## 5. Lenguaje
### Indentación
- La característica de Python que hace que se destaque en términos de sintaxis es su "indentación significativa". En lugar de utilizar llaves o paréntesis para delimitar bloques de código como en otros lenguajes, Python se basa en la cantidad de espacios o tabulaciones al comienzo de una línea para definir la estructura del código, es una característica única y poderosa que contribuye a la belleza y la claridad del lenguaje Python.
- Fíjence cómo el código dentro de la función y dentro del if else tienen un nivel de indentación mayor. Python usa esta indentación para saber qué partes del código están relacionadas y cuáles no.
- Esta característica hace que el código Python sea muy legible y limpio, ya que se enfoca en la organización visual. Sin embargo, debes ser coherente en la forma en que aplicas la indentación, utilizando la misma cantidad de espacios o tabulaciones en todo el código.
- En resumen, la indentación es como un "marcador visual" que define la estructura del código y facilita su comprensión.
### Tipos de Datos en Python:
- Enteros (int): Representan números enteros, positivos o negativos, sin parte decimal. Ejemplos: 3, -42, 0.
- Flotantes (float): Representan números decimales o de punto flotante. Ejemplos: 3.14, -0.5, 2.0.
- Cadenas de Texto (str): Representan secuencias de caracteres. Ejemplos: "Hola, mundo", 'Python', "12345".
- Booleanos (bool): Representan valores de verdad, es decir, Verdadero (True) o Falso (False).
### Operadores en Python:
- Operadores Aritméticos: Se utilizan para realizar operaciones matemáticas.
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Módulo (%) (obtiene el resto de una división)
    - Potencia (**)
- Operadores de Comparación: Se utilizan para comparar valores y devuelven un valor booleano (Verdadero o Falso).
    - Igual (==)
    - No igual (!=)
    - Mayor que (>)
    - Menor que (<)
    - Mayor o igual que (>=)
    - Menor o igual que (<=)
- Operadores Lógicos: Se utilizan para combinar expresiones lógicas y devuelven un valor booleano.
    - Y lógico (and)
    - O lógico (or)
    - No lógico (not)
- Operadores de Asignación: Se utilizan para asignar valores a variables.
    - Asignación (=)
    - Asignación con suma (+=)
    - Asignación con resta (-=)
    - Asignación con multiplicación (*=)
    - Asignación con división (/=)
- Operadores de Pertenencia: Se utilizan para verificar si un valor está presente en una secuencia.
    - Pertenencia (in)
    - No pertenencia (not in)
- Operadores de Identidad: Se utilizan para comparar la identidad de dos objetos.
    - Identidad (is)
    - No identidad (is not)
### Colecciones de datos
- Listas: Son colecciones ordenadas y modificables de elementos. Pueden contener elementos de diferentes tipos. Ejemplo: [1, 2, 3, 'Python'].
- Tuplas: Son similares a las listas, pero son inmutables, es decir, no pueden modificarse una vez creadas. Ejemplo: (1, 2, 3, 'Python').
- Conjuntos (set): Son colecciones desordenadas de elementos únicos. Ejemplo: {1, 2, 3}.
- Diccionarios: Representan pares clave-valor. Cada elemento tiene una clave única. Ejemplo: {'nombre': 'Juan', 'edad': 30}.
### Estructura de Control if:
- Permite ejecutar un bloque de código si se cumple una condición.
- Puede ir acompañado de una o más cláusulas elif (else if) para manejar múltiples condiciones.
- Puede tener una cláusula else para especificar qué hacer si ninguna de las condiciones anteriores se cumple.
### Bucles for:
- Se utilizan para iterar sobre una secuencia (como una lista, tupla o cadena) o cualquier objeto iterable.
- Pueden ejecutar un bloque de código para cada elemento en la secuencia.
### Bucles while:
- Se utilizan para repetir un bloque de código mientras se cumple una condición.
- Puede ejecutarse un número indefinido de veces mientras la condición sea verdadera.
### Estructura de Control break y continue:
- break se utiliza para salir de un bucle antes de que se complete.
- continue se utiliza para omitir el resto de la iteración actual y pasar a la siguiente.
### Estructura de Control try y except:
- Se utiliza para manejar excepciones y errores.
- Permite ejecutar un bloque de código y capturar y gestionar excepciones si ocurren.
### Funciones 
- Las funciones en Python son bloques de código que realizan tareas específicas y se pueden reutilizar en un programa. Se definen usando def, seguido del nombre de la función y paréntesis. Los argumentos (valores que la función recibe) se colocan dentro de los paréntesis.
- Las funciones pueden tener argumentos para realizar tareas específicas. Los valores pasados como argumentos se llaman "argumentos reales".
- Las funciones también pueden devolver valores utilizando return. El valor devuelto se llama "valor de retorno".
- Finalmente, las funciones también pueden ser recursivas, lo que significa que pueden llamarse a sí mismas para resolver problemas que pueden dividirse en subproblemas similares más pequeños.
### Librerias
- Las librerías en Python son conjuntos de módulos y funciones predefinidos que amplían las capacidades del lenguaje y permiten realizar diversas tareas sin tener que escribir todo el código desde cero. Python tiene una amplia variedad de librerías disponibles, muchas de las cuales son muy populares






