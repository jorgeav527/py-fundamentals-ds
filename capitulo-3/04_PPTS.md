# INTRO
- Imaginemos que Python es como el chef de la ciencia de datos. Cuando comenzamos a cocinar, lo primero que necesitamos hacer es traer nuestros ingredientes.
- Esto es lo que llamamos carga de datos. La carga de datos en Python es el proceso de importar información desde diversas fuentes, como archivos en diferentes formatos, bases de datos relacionales y no relacionales, o incluso la web, para su análisis posterior.
- En el ámbito de la ciencia de datos, nos encontramos con la tarea de procesar una variedad de tipos de datos, que van desde datos numéricos hasta texto desestructurado.
- Para llevar a cabo esta tarea, utilizamos el proceso de Extracción, Transformación y Carga, comúnmente conocido como ETL.
- Esta metodología nos permite recopilar, dar forma y cargar datos de manera efectiva para su análisis y uso en nuestros proyectos o modelos.
- En Python, contamos con bibliotecas como Pandas que facilitan estas tareas y nos permiten manipular los datos de manera eficiente.
- Cargar datos es el primer paso esencial en el camino hacia el análisis y la obtención de información valiosa."

# AGENDA
- Comenzaremos por explorar qué es exactamente la Ciencia de Datos. Examinaremos varias definiciones para obtener una comprensión sólida.
- A continuación, exploraremos los diferentes tipos de archivos y formatos con los que trabajamos en Ciencia de Datos. Esto incluye:
    - Archivos CSV (Comma-Separated Values), que es el formato común en el que recibimos información, similar a una hoja de cálculo de Excel.
    - Formato JSON, que es un tipo de archivo utilizado para estructurar datos en documentos legibles por máquina y por la web.
- Luego, nos adentraremos en el mundo de SQL, que es un lenguaje de programación diseñado para administrar bases de datos.
- Exploraremos las bases de datos NoSQL, como MongoDB, que son ideales para el manejo de grandes cantidades de datos no estructurados.
    - Aprenderemos cómo funcionan y cuándo es adecuado utilizarlas.
- Concluiremos con el capitulo 3 con uso de la biblioteca BeautifulSoup que es una herramienta que nos permite extraer información de sitios web, un proceso conocido como web scraping.

# Ciencia de datos
- La ciencia de datos conectá y interrelaciona diferentes areas, donde los profesionales deben poseer una combinación de estas habilidades para extraer valor de los datos y tomar decisiones informadas.
  
- Hacking Skills o (Habilidades de piratería con el computador):
    - En este contexto, las habilidades de hacking se refieren a la capacidad de acceder, recopilar y limpiar datos de diversas fuentes, como bases de datos, sitios web y archivos.
    - Implica la habilidad para automatizar tareas de extracción de datos y navegar por la web para adquirir información relevante.
- La matemática y la estadística son los cimientos de la Ciencia de Datos. Estas disciplinas proporcionan las herramientas para analizar datos, modelar fenómenos y tomar decisiones basadas en evidencia. Incluyen conceptos como probabilidad, regresión, análisis multivariado y más (funciones con multiples variables, etc).
- El conocimiento de negocio implica comprender el contexto en el que se aplican los datos. Esto significa entender las necesidades y metas de la empresa o industria para la que se trabaja. Con este conocimiento, se pueden formular preguntas significativas y aplicar análisis de datos de manera efectiva.
  
- En la intersección de habilidades de hacking y matemáticas/estadísticas, encontramos la capacidad de procesar y analizar datos de manera eficiente, aplicando técnicas de limpieza, transformación y modelado estadístico.
- Cuando combinamos habilidades de hacking con conocimiento de negocio, nos adentramos en la búsqueda tradicional de datos para obtener información relevante para la industria o empresa en cuestión.
- Cuando se combina conocimiento del negocio con habilidades de matemáticas y estadísticas podemos  abordar problemas específicos dentro de una industria, lo que puede incluir la creación de modelos predictivos o la identificación de tendencias críticas.

# SQL
SQL es un lenguaje esencial para la gestión de bases de datos relacionales, los sabores como PostgreSQL, Oracle, MySQL y SQLite que son vitales en el mundo de la Ciencia de Datos y el desarrollo de aplicaciones.

- SQLAlchemy es una biblioteca en Python que proporciona una forma elegante y eficiente de interactuar con bases de datos relacionales a través de Python.
- Permite a los desarrolladores trabajar con bases de datos SQL, sin tener que escribir SQL manualmente. SQLAlchemy admite una variedad de motores de bases de datos, incluidos PostgreSQL, MySQL, SQLite y Oracle, lo que facilita la administración de múltiples sistemas de bases de datos.
- SQLAlchemy incluye un ORM (Mapeo Objeto-Relacional) que permite mapear objetos de Python a tablas de base de datos y realizar operaciones CRUD de manera más intuitiva.

# CSV
- Los archivos CSV, abreviatura de Valores Delimitados por Comas, son un formato muy común para almacenar datos en forma de texto plano.
- En un archivo CSV, los valores tambien se puden delimitar por punto y coma o tabulaciones, y cada fila representa un registro, con cada campo separado por la coma correspondiente.

# JSON 
- JSON se utiliza comúnmente en aplicaciones web y es el formato preferido para la comunicación de datos entre sistemas REST API en la web, debido a su simplicidad y flexibilidad.
- Es fácil de leer y escribir para los humanos y fácil de analizar y generar para las máquinas.
- Está compuesto por pares clave-valor y estructuras de datos anidadas.

# MongoDB
- MongoDB es un sistema de gestión de bases de datos NoSQL (Not Only SQL) que se ha vuelto popular en el mundo de la Ciencia de Datos y el desarrollo de aplicaciones. A diferencia de las bases de datos SQL tradicionales, MongoDB utiliza un modelo de base de datos de documentos en lugar de tablas y filas.
- La elección entre MongoDB y una base de datos SQL depende de los requisitos específicos del proyecto. MongoDB se destaca en aplicaciones que requieren flexibilidad y escalabilidad, así como en aquellas que manejan datos no estructurados o semiestructurados.

# Beautiful Soup
- Beautiful Soup se utiliza para analizar la estructura de páginas web y extraer información de manera específica, como recopilar datos de una página web o extraer información de un sitio web para análisis de datos.