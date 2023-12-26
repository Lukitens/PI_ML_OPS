# Proyecto Individual Número 1: #

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

Los archivos CSV limpios los subí a un drive de google ya que son muy pesados y github no me permite subirlos:

[Archivos CSV limpios](https://drive.google.com/drive/folders/1NgPKIbytor0SxQnDtnOZLPK3SKXXSCSq?usp=drive_link)

## EDA: ##
Realizé un analisis exploratorio de datos para tratar de encontrar patrones y tendencias en los datos y tambien para detectar valores outliers, medias, etc. Esto lo hice usando graficos de las librerias seaborn y matplotlib

## Funciones de la API: ##

Primero preparé los CSV para cada funcion de la api, luego hice las funciones de la api, todo esto en los notebooks que se llaman CSV_Funcion para una mayor comodidad y después adapté las funciones para la API que se encuentran en el archivo **main.py**

**def PlayTimeGenre( genero : str ):** Debe devolver año con mas horas jugadas para dicho género.

**def UserForGenre( genero : str ):** Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

**def UsersRecommend( año : int ):** Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

**def UsersNotRecommend( año : int ):** Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

**def sentiment_analysis( año : int ):** Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

**def recomendacion_juego( id de producto ):** Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.