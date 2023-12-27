# Proyecto Individual Número 1: #
![Steam Logo](https://raw.githubusercontent.com/Lukitens/PI_ML_OPS/main/steam%20logo.webp)
## Introducción: ##

En este proyecto trabajé con 3 archivos sobre datos de steam, estos archivos originalmente venian en formato JSON que luego los transforme a CSV. Estos archivos eran:
  - users_items.json.gz
  - steam_games.json.gz
  - user_reviews.json.gz

El objetivo de este proyecto es deployar una API hecha con FastAPI en render con 6 endpoints, 5 de ellos son para consultar datos y 1 es un modelo de recomendación

Los archivos JSON originales los subí a un drive de google ya que son muy pesados y github no me permite subirlos:

[Archivos JSON](https://drive.google.com/drive/folders/1ho75x6-e320yu06KCBog08ERFh2hIDne?usp=drive_link)

## ETL: ##
Al principio del proyecto los archivos originalmente venian en formato JSON y venian con errores, lo que provocaba que no se pudieran leer, por lo que tuve que leerlos linea por linea y luego los pasé a formato CSV para optimizar los procesos de ETL y EDA ya que leer los archivos linea por linea consumen demasiado tiempo y recursos.
También tuve que limpiar los archivos originales eliminando nulos, duplicados y datos irrelevantes para el correcto funcionamiento de los endpoints

[Notebook del ETL](https://github.com/Lukitens/PI_ML_OPS/blob/main/limpieza.ipynb)

Los archivos CSV limpios los subí a un drive de google ya que son muy pesados y github no me permite subirlos:

[Archivos CSV limpios](https://drive.google.com/drive/folders/1NgPKIbytor0SxQnDtnOZLPK3SKXXSCSq?usp=drive_link)

## EDA: ##
Realizé un analisis exploratorio de datos para tratar de encontrar patrones y tendencias en los datos y tambien para detectar valores outliers, medias, etc. Esto lo hice usando graficos de las librerias seaborn y matplotlib.

[Notebook del EDA](https://github.com/Lukitens/PI_ML_OPS/blob/main/eda.ipynb)

## Funciones de la API: ##

Primero preparé los CSV para cada funcion de la api, luego hice las funciones de la api, todo esto en los notebooks que se llaman CSV_Funcion para una mayor comodidad y después adapté las funciones para la API que se encuentran en el archivo **main.py**

**def PlayTimeGenre( genero : str ):** Debe devolver año con mas horas jugadas para dicho género.
[Notebook de PlayTimeGenre](https://github.com/Lukitens/PI_ML_OPS/blob/main/CSV_Funcion1.ipynb)

**def UserForGenre( genero : str ):** Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
[Notebook de UserForGenre](https://github.com/Lukitens/PI_ML_OPS/blob/main/CSV_Funcion2.ipynb)

**def UsersRecommend( año : int ):** Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
[Notebook de UsersRecommend](https://github.com/Lukitens/PI_ML_OPS/blob/main/CSV_Funcion3.ipynb)

**def UsersNotRecommend( año : int ):** Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
[Notebook de UsersNotRecommend](https://github.com/Lukitens/PI_ML_OPS/blob/main/CSV_Funcion4.ipynb)

**def sentiment_analysis( año : int ):** Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
[Notebook de sentiment_analysis](https://github.com/Lukitens/PI_ML_OPS/blob/main/CSV_Funcion5.ipynb)

**def recomendacion_juego( id de producto ):** Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
[Notebook de recomendacion_juego](https://github.com/Lukitens/PI_ML_OPS/blob/main/FuncionML.ipynb)

## Sistema de recomendación: ##
El sistema de recomendación que hice se basa en recomendar juegos parecidos al que se le ingresa.
Para este sistema de recomendación utilicé la similitud del coseno en base a los generos de los juegos. Luego apliqué el modelo a todos los juegos del data frame y los guarde en un csv, ya que si ingresaba directamente el modelo de machine learning a render no funcionaba el endpoint ya que consumía demasiados recursos.

[Notebook del modelo de machine learning](https://github.com/Lukitens/PI_ML_OPS/blob/main/FuncionML.ipynb)

## Deploy de la API: ##
Para deployar la API y que cualquiera pueda acceder a ella utilicé render [API en render](https://lucas-api-pi.onrender.com/docs).

[Archivo .py de la API](https://github.com/Lukitens/PI_ML_OPS/blob/main/main.py)

Si se quiere deployar la api de manera local hay que:
  1. Tener las librerias necesarias instaladas
  2. Abrir la terminal de python
  3. Pegar esto en la consola: uvicorn main:app --reload
  4. Abrir cualquier navegador
  5. Pegar la ruta que sale en el output de la consola, en mi caso la ruta es: http://127.0.0.1:8000
  6. Para poder probar todas las funciones agregarle /docs al final de la ruta. ejemplo: http://127.0.0.1:8000/docs

[Autor](https://www.linkedin.com/in/lucas-raña-49120a271/)
