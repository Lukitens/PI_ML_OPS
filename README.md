#Proyecto Individual Número 1:#

##Introducción:##

En este proyecto trabajé con 3 archivos sobre datos de steam, estos archivos originalmente venian en formato JSON y no se podían leer, por lo que tuve que leerlos linea por linea y luego los pasé a formato CSV para optimizar los procesos de ETL y EDA ya que leer los archivos linea por linea consumen demasiado tiempo y recursos.

El objetivo de este proyecto es deployar una API hecha con FastAPI en render con 6 endpoints, 5 de ellos son para consultar datos y 1 es un modelo de recomendación

Endpoints:

def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.

def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)

def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)

def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
