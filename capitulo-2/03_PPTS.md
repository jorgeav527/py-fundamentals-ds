# AGENDA
- Python es un lenguaje popular en Data Science debido a su facilidad de uso y las herramientas especializadas que ofrece para analizar datos.
- Luego conceptos como OOP, Manejo de errores, List Comprenhensions, funciones Lammda, Generadores o Decoradores, son fundamentales en Python y ayudarán a escribir código más eficiente. o Codigo bonito.
# PYTHON EN DATA SCIENCE
- Estos son algunos de los terminos que van a escuchar en DS, la Exploración de datos, el Procesamiento del Lenguaje Natural (Natural Language Processing en inglés), La visualización de datos que es los graficos que se extraen de los datos y por lo tanto diferente a la visión por computadora que es un campo de la inteligencia artificial que se enfoca en enseñar a las computadoras a interpretar y comprender imágenes y videos. Machine learning y deep learning, mientras que el Machine Learning se basa en modelos más simples y requiere menos datos en general, el Deep Learning se destaca en la capacidad de aprender representaciones complejas de datos. "Big Data" es un término que se utiliza para describir conjuntos de datos extremadamente grandes y complejos, vamos a tocar cada uno de ellos de manera superficial para brindar una idea y como se podria aplicar.
### La Exproración de datos
- La Exproración de datos, también conocida como EDA (Exploratory Data Analysis), es una fase fundamental en el proceso de análisis de datos el objetivo principal es comprender y familiarizarse con los datos antes de realizar análisis más avanzados como modelajes.
    - **Resumen Estadístico**: Calcular estadísticas descriptivas básicas, como media, mediana, desviación estándar, mínimo y máximo, para obtener una visión general de los datos.
    - **Visualización de Datos**: Utilizar gráficos y visualizaciones para representar los datos de manera efectiva. Ejemplos de esto incluyen histogramas, diagramas de dispersión, diagramas de caja, gráficos de barras y gráficos de líneas.
    - **Limpieza de Datos**: Identificar y tratar valores atípicos, datos faltantes o inconsistentes que puedan afectar la calidad de los análisis posteriores.
    - **Análisis de Distribución**: Comprender la distribución de los datos para evaluar si siguen una distribución normal u otra distribución específica.
    - **Exploración de Relaciones**: Analizar relaciones entre variables, como correlaciones, para entender cómo se interrelacionan los datos.
    - **Análisis de Tendencias**: Identificar patrones o tendencias en los datos a lo largo del tiempo o en diferentes categorías.
    - **Segmentación de Datos**: Dividir los datos en grupos o segmentos para analizarlos de manera independiente y detectar patrones específicos en cada grupo.
    - **Análisis de Valores Extremos**: Identificar valores atípicos que pueden ser errores o indicar información importante.
    - **Extracción de Características**: Identificar características relevantes para un análisis posterior o modelado predictivo.
    - **Documentación**: Registrar y documentar observaciones, decisiones y pasos realizados durante la exploración de datos para futuros análisis y para compartir resultados con otros.
### Visualización
- La visualización de datos se refiere a la representación gráfica de datos numéricos o información para ayudar a comprender patrones, tendencias y relaciones en los datos. En Python, se utilizan bibliotecas como Matplotlib, Seaborn y Plotly para crear gráficos y visualizaciones que ayuden a analizar y comunicar datos de manera efectiva.
- Aqui tenemos dos librerias que facilitan la visualización de los datos Matplotlib y Plotly.
- Matplotlib es una biblioteca poderosa y ampliamente utilizada para visualización de datos estática, mientras que Plotly se destaca por su capacidad de crear visualizaciones de datos interactivas y dinámicas, lo que lo hace ideal para aplicaciones web y paneles de control. La elección entre estas dos bibliotecas depende de tus necesidades específicas de visualización y el nivel de interactividad que deseas ofrecer en tus gráficos.
### Machine Learning
- Machine Learning es una rama de la inteligencia artificial que se enfoca en desarrollar algoritmos y modelos que pueden aprender automáticamente a partir de datos y realizar tareas específicas sin necesidad de programación explícita.
- Algunas de las aplicaciones de machine learning se utiliza en una amplia gama de aplicaciones, como reconocimiento de patrones, procesamiento de lenguaje natural, visión por computadora, recomendación de productos, diagnóstico médico y mucho más.
- Estos conceptos son fundamentales en Machine Learning y se aplican en una variedad de problemas y escenarios. Cada uno de ellos tiene sus propias técnicas y algoritmos específicos que se utilizan para abordar tareas específicas en el aprendizaje automático.
- **La clasificación** es una tarea en la que se asigna una etiqueta o categoría a un conjunto de datos en función de sus características. El objetivo es entrenar un modelo que pueda predecir la clase correcta para nuevos ejemplos no etiquetados.
- Ejemplo: Un ejemplo común de clasificación es el reconocimiento de dígitos escritos a mano, donde se asigna a cada imagen de dígito una etiqueta que indica qué número representa (por ejemplo, 0, 1, 2, ...).
- **La regresión** es otra tarea en la que se predice un valor numérico o continuo en función de las características de entrada. En otras palabras, se busca modelar una relación continua entre las variables.
- Ejemplo: Un ejemplo de regresión es predecir el precio de una casa en función de sus características, como el tamaño, la ubicación y el número de habitaciones.
- **El clustering** es una técnica que se utiliza para agrupar datos similares en conjuntos o clústeres. Los datos dentro de un clúster son más similares entre sí que con los datos en otros clústeres.
- Ejemplo: Un caso de clustering podría ser agrupar clientes en segmentos de mercado basados en su comportamiento de compra, lo que permite a las empresas realizar estrategias de marketing específicas para cada grupo.
- **La reducción de dimensionalidad** es un proceso en el que se reduce el número de variables o características en un conjunto de datos sin perder demasiada información. Esto puede ayudar a simplificar modelos y reducir el riesgo de sobreajuste.
- Ejemplo: Principal Component Analysis (PCA) es una técnica común de reducción de dimensionalidad que se utiliza para reducir la cantidad de características en un conjunto de datos mientras se conserva la mayor cantidad posible de información relevante.
### Procesamiento del Lenguaje Natural
- (Natural Language Processing en inglés), es una rama de la inteligencia artificial que se ocupa de la interacción entre las computadoras y el lenguaje humano.
    - NLP se utiliza para analizar opiniones y emociones en texto (Análisis de Sentimiento). Por ejemplo, en redes sociales, se puede determinar si un comentario es positivo o negativo.
    - También los servicios como Google Translate utilizan NLP para traducir texto de un idioma a otro.
    - Los hatbots como Siri de Apple o asistentes virtuales como Amazon Alexa utilizan NLP para comprender y responder preguntas en lenguaje natural.
    - El NLP puede utilizarse para resumir grandes cantidades de texto de manera automática, como resúmenes de noticias o informes.
    - En aplicaciones como el filtrado de spam de correo electrónico o la categorización de noticias, NLP se utiliza para clasificar el texto en diferentes categorías.
    - NLP puede ayudar a extraer información clave de textos no estructurados, como nombres, fechas o ubicaciones.
    - En la creación de contenido automático, como generación de texto para chatbots o incluso escritura de noticias, NLP se utiliza para generar texto coherente y relevante.
    - Las herramientas de corrección gramatical y ortográfica utilizan NLP para identificar y corregir errores en el texto.
    - Los motores de búsqueda como Google utilizan algoritmos de NLP para comprender las consultas de búsqueda y ofrecer resultados relevantes.
    - Las empresas pueden utilizar NLP para analizar las opiniones de los clientes sobre productos y servicios y tomar decisiones basadas en esos análisis.
- SpaCy es una herramienta de programación en Python que ayuda a las computadoras a entender y trabajar con texto en lenguaje humano. Puede ayudar a dividir el texto en palabras, encontrar el significado de las palabras y mucho más.
### Computer vision
- La visión por computadora es un campo de la inteligencia artificial que se enfoca en enseñar a las computadoras a interpretar y comprender imágenes y videos. Implica tareas como detección de objetos, reconocimiento facial, seguimiento de objetos, segmentación de imágenes y más. En Python, bibliotecas como OpenCV y TensorFlow se utilizan comúnmente para trabajar en proyectos de visión por computadora.
### Deep Learning
-  Keras, TensorFlow y PyTorch son tres de las principales bibliotecas utilizadas en la implementación de modelos de Deep Learning. La elección entre ellas a menudo depende de las preferencias personales, las necesidades específicas del proyecto y la comunidad en la que te encuentres. Todas son poderosas y adecuadas para diferentes situaciones.
### Big Data
- "Big Data" es un término que se refiere a conjuntos de datos extremadamente grandes y complejos que son difíciles de manejar y analizar con herramientas tradicionales de procesamiento de datos.
- Las características clave de Big Data son las famosas "3V":
    - Volumen: Se refiere a la cantidad masiva de datos generados y acumulados. Los conjuntos de datos de Big Data pueden ser de terabytes, petabytes o incluso exabytes.
    - Velocidad: Hace referencia a la velocidad a la que se generan y se actualizan los datos. En muchos casos, los datos de Big Data se generan en tiempo real o a alta velocidad.
    - Variedad: Significa que los datos pueden provenir de diversas fuentes y tener formatos muy diferentes. Pueden incluir texto, imágenes, videos, registros de transacciones, datos de sensores, redes sociales, etc.
- Estos conjuntos de datos suelen ser tan grandes y rápidos que resulta desafiante almacenarlos, gestionarlos y analizarlos de manera efectiva con métodos convencionales.
# Programación orientada a objetos.
La programación orientada a objetos es una forma de escribir programas que se centra en crear objetos que tienen propiedades (como datos) y comportamientos (como acciones). Esto nos ayuda a organizar y diseñar programas de manera más fácil y comprensible, porque los objetos se parecen a las cosas del mundo real con las que estamos familiarizados.
- **Paradigma**: La programación orientada a objetos es un enfoque o manera de escribir programas. Es como una forma particular de hacer las cosas en la programación.
- **Modelar Objetos**: Cuando programamos en POO, pensamos en el mundo como si estuviera lleno de "objetos". Un objeto es como un paquete que contiene tanto la información (llamada "propiedades") como las acciones que puede realizar (llamadas "comportamiento").
- **Propiedades**: Los objetos tienen "propiedades" que son como características o datos que describen el objeto. Por ejemplo, si tienes un objeto que representa un automóvil, las propiedades podrían ser el color, la marca, el modelo y la velocidad.
# Manejo de errores
El manejo de errores en Python se refiere a la capacidad de un programador para lidiar con situaciones excepcionales o errores que puedan ocurrir durante la ejecución. 
- raise y assert son dos mecanismos en Python para manejar errores y excepciones, pero tienen diferentes propósitos y se utilizan en contextos diferentes
- La diferencia clave entre raise y assert es que raise se usa para generar una excepción cuando se detecta una condición excepcional, mientras que assert se usa para verificar que una condición es verdadera y, si no lo es, genera una excepción. raise es más flexible y se utiliza para generar excepciones personalizadas, mientras que assert es una forma más concisa de realizar verificaciones de condiciones en el código.
- Ponemos el código que podría generar un error en un bloque try, y luego manejas ese error en un bloque except. Si se produce un error en el bloque try, Python ejecutará el código en el bloque except.
python
-  Opcionalmente, podemos usar un bloque else después del bloque except para ejecutar código si no se produce ningún error en el bloque try.
- También podemos usar un bloque finally que se ejecutará siempre, ya sea que se produzca un error o no. Esto es útil para tareas de limpieza, como cerrar archivos o conexiones de red.
# List comprehensions
Las list comprehensions son una forma elegante y eficiente de construir listas en una sola línea de código. Se utilizan para aplicar una expresión a cada elemento de una secuencia (como una lista, tupla o rango) y crear una nueva lista a partir de los resultados.
`nueva_lista = [expresion for elemento in secuencia if condicion]`
- Expresion es la expresión que se aplica a cada 
- Elemento es una variable que toma el valor de cada elemento en la secuencia.
- Secuencia es la secuencia de entrada (por ejemplo, una lista, tupla o rango) sobre la cual se aplicará la expresión.
- Condicion es una condición opcional que filtra los elementos de la secuencia antes de aplicar la expresión.
# Funciones Lambda
- Las funciones lambda, también conocidas como expresiones lambda o funciones anónimas, son funciones pequeñas y anónimas en Python que se definen utilizando la palabra clave lambda. A diferencia de las funciones normales que se definen con la palabra clave def, las funciones lambda se utilizan para crear funciones simples y de una sola línea sin necesidad de darles un nombre.
- Las funciones lambda son útiles cuando necesitas definir una función pequeña y rápida sin darle un nombre formal. Se utilizan a menudo en combinación con funciones de orden superior como map(), filter(), sorted(), y otras funciones que toman funciones como argumentos.
    - Map aplica una misma función en distintos elementos.
    - Filter aplica un filtro a aquellos elementos que se evalúan como False.
    - Reduce es una función que agrega y reduce el número de elementos en una colección.
# Generadores
- Los generadores en Python son una forma eficiente de crear secuencias de elementos iterables (como listas o tuplas) de una manera más eficiente en términos de memoria y procesamiento. Funcionan como iteradores y se crean utilizando una función especial que contiene la palabra clave yield.
- En resumen, los generadores son una forma eficiente de crear secuencias de elementos en Python, especialmente cuando necesitas trabajar con grandes conjuntos de datos y deseas ahorrar memoria. Utilizan la palabra clave yield para crear funciones generadoras y se pueden iterar mediante bucles o next() para obtener elementos de manera incremental.
# Decoradores
- Es una función que extiende la funcionalidad de otra función son modificarla.
Se distinguen por @.


- Map/Reduce: Son funciones que permiten aplicar operaciones a listas y reducir listas a un solo valor.

- Generadores: Son útiles cuando trabajas con datos grandes ya que te permiten procesarlos poco a poco en lugar de cargar todo en la memoria.
- Decoradores: Permiten modificar el comportamiento de funciones.

