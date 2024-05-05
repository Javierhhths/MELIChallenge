# MELIChallenge
MELI's data engineering role technical challenge

# Similitud

## Descripción general

Para el cálculo de la similitud, se desarrolló la clase `Similarity`, la cual toma como atributos el dataset de nombres transformado, un nombre y un umbral de porcentaje de similitud ingresados por el usuario y devuelve un diccionario, el cual, por cada `"id"` (llave) de usuario que cumpla con este umbral, contiene un diccionario subsiguiente, que contiene el nombre del dataset con el cual el nombre de entrada fue comparado (`"name"`) y el porcentaje de similitud (`"similarity"`) entre ambos nombres.

Usando la librería `flask` se implementó una API, la cual, a través de un formulario HTML, solicita al usuario final el nombre y el umbral de porcentaje de solicitud mencionados y entrega los resultados calculados por la clase en formato *.json*.

## Contenido

 - **templates**. Directorio que contiene el template *.html* utilizado para el formulario de la API implementada (*form.html*).
 - **app.py**. Archivo principal. Contiene la configuración y la ejecución de la API implementada.
 - **similarity.py**. Código fuente de la clase construida para el ejercicio.
 - **names_dataset.csv**. Dataset que contiene los nombres con los que se comparará el nombre-entrada del usuario.

## Librerías utilizadas

Se utilizaron las siguientes librerías:

 - `flask`
 - `pandas`
 - `unidecode`
 - `Levenshtein`

## Dataset

El dataset fue importado por medio del método .`read_csv()` de la librería `pandas`. Para los cálculos de similaridad, se creó una columna nueva de nombres llamada `"full_name_transformed"`, la cual sólo tiene en cuenta los caracteres alfanuméricos en minúscula, sin espacios ni acentos, de la columna de nombres (`"Full Name"`) para facilitar las comparaciones de acuerdo al algoritmo escogido (basado en la distancia de Levenshtein). De manera similar, se creó una nueva columna de nombres llamada `"full_name_cleansed"`, la cual limpia la columna `"Full Name"` de caracteres que no sean alfanuméricos (a excepción de puntos y espacios), para mostrar un output limpio al usuario final.

Para tales propósitos, se utilizó el método `.map()` de `pandas` y una función lambda que, para cada cadena de texto presente en la columna `"Full Name"`, realiza las tareas de eliminación de acentos (usando la función `unidecode` de la librería homónima), conversión a minúsculas (usando el método nativo `.lower()`), y limpieza de caracteres no alfanuméricos (usando el método nativo `.isalnum()`).

El dataset transformado es cargado como atributo de la clase `Similarity`.

## Cálculo del porcentaje de similitud

