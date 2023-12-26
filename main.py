# uvicorn main:app --reload
# http://127.0.0.1:8000/docs Documentacion


#Importamos las librerias necesarias
import numpy as np
import pandas as pd
from fastapi import FastAPI

#Iniciamos la api y la guardamos en la variable app
app = FastAPI()

#Leemos los csv para poder usarlos en los endpoints

funcion1 = pd.read_csv("Csv_api//funcion1.csv")
funcion2 = pd.read_csv("Csv_api//funcion2.csv")
funcion3 = pd.read_csv("Csv_api//funcion3.csv")
funcion4 = pd.read_csv("Csv_api//funcion4.csv")
funcion4_2 = pd.read_csv("Csv_api//funcion4_2.csv")
funcion5 = pd.read_csv("Csv_api//funcion5.csv")

@app.get("/")
def read_root():
    return {"Bienvenido" : "Bienvenido a mi API del proyecto individual Nº1"}

#Funcion 1 
# def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
# Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
@app.get("/playtime/{genero}") #Establecemos la ruta de la funcion
def PlayTimeGenre( genero : str ): #Creamos la funcion y le damos su argumento
    if genero in funcion1["genres"].values: #Si el genero ingresado está en el csv devuelve el año con mas horas jugadas
        filtro = funcion1[funcion1["genres"] == genero] #Filtra el df dejando solo el genero ingresado
        valor_maximo = filtro["playtime_forever"].max() #Devuelve el valor maximo de las horas
        filtro = filtro[filtro["playtime_forever"] == valor_maximo] #Devuelve el valor maximo de horas
        return f"Año de lanzamiento con mas horas jugadas para el genero {genero} : {filtro['año'].values[0]}"
    else:
        return("Tu genero: {} no existe".format(genero)) #Si no se cumple la condicion envia este mensaje

#Funcion 2
#def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas 
# jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
#Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, 
# "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

@app.get("/UserForGenre/{genero}")
def UserForGenre(genero:str):
    if genero in funcion2["genres"].values:
        generosdf = funcion2[funcion2["genres"] == genero]
        horas_por_persona = generosdf.groupby(["user_id", "genres"])["playtime_forever"].sum().reset_index()
        maximo = horas_por_persona.loc[horas_por_persona["playtime_forever"].idxmax()].to_list()
        horas_por_año = generosdf[generosdf["user_id"] == maximo[0]]
        horas_por_año = horas_por_año[["año", "playtime_forever"]]

        respuesta = {
            "mensaje": f"Usuario con más horas para el género {genero} es {maximo[0]}.",
            "horas_totales": maximo[2],
            "horas_por_año": horas_por_año.to_dict(orient='records')
        }
        return respuesta
    else:
        return ("Selecciona un genero valido")


#Funcion 3
# def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para 
# el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
#Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}] 

@app.get("/UsersRecommend/{year}") #Establecemos la ruta de la funcion
def UsersRecommend( year : int ): #Creamos la funcion y le damos su argumento
    if year >= 2010 and year <= 2015: #Si el año ingresado esta entre 2010 y 2015 procede con la funcion
        filtro = funcion3[funcion3["year"] == year] #Filtra por el año ingresado
        filtro["valoracion"] = filtro["sentiment_analysis"] + filtro["recommend"]
        #Suma solo las reviews que sean positivas o neutrales y las recomendaciones
        top3 = filtro["valoracion"].nlargest(3).index #Devuelve los 3 mejor puntuados
        top3 = funcion3.loc[top3, "title"].tolist() #Devuelve los 3 mejor puntuados con su titulo y los pasa a una lista
        #Asignamos los juegos a variables para retornarlas
        primer_juego = top3[0]
        segundo_juego = top3[1]
        tercer_juego = top3[2]
        return [{"Puesto 1" : primer_juego, "Puesto 2" : segundo_juego, "Puesto 3" : tercer_juego}]
    else:
        return "Selecciona un año ente 2010 y 2015"

#Funcion 4
# def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios 
# para el año dado. (reviews.recommend = False y comentarios negativos)
#Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]


@app.get("/UsersNotRecommend/{year}")
def UsersNotRecommend(año: int):
    if 2010 <= año <= 2015:
        # Filtramos los DataFrames por el año ingresado
        filtro = funcion4[funcion4["year"] == año]
        filtro2 = funcion4_2[funcion4_2["year"] == año]

        # Agrupamos por el título de los juegos y contamos la cantidad de reseñas negativas que tiene cada juego
        negativos = filtro.groupby("title")["sentiment_analysis"].count().reset_index(name="cantidad_reseñas_n")
        positivos = filtro2.groupby("title")["sentiment_analysis"].count().reset_index(name="cantidad_reseñas_p")

        # Reindexar ambos DataFrames por 'title'
        negativos = negativos.set_index('title')
        positivos = positivos.set_index('title')

        # Crear una copia independiente de negativos
        resta = negativos.copy()

        # Realizar la resta
        resta["cantidad_reseñas"] = positivos["cantidad_reseñas_p"] - resta["cantidad_reseñas_n"]

        # Restaurar el índice si es necesario
        resta.reset_index(inplace=True)

        # Ordenar y obtener el top 3
        top3 = resta.sort_values(by="cantidad_reseñas", ascending=True).head(3)
        top3.drop(columns=["cantidad_reseñas_n", "cantidad_reseñas"], inplace=True)

        # Devolver el resultado en formato JSON
        return top3.to_dict(orient="records")
    else:
        return "Por favor, ingrese un año válido entre 2011 y 2015."
    
#Funcion 5
#def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista 
# con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un 
# análisis de sentimiento.
#Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}

@app.get("/sentimentanalysis/{year}") #Establecemos la ruta de la funcion
def sentiment_analysis(year: int): #Creamos la funcion y le damos su argumento
    if 2010 <= year <= 2015: #Si el año ingresado esta entre 2010 y 2015 procede con la funcion
        filtro = funcion5[funcion5["year"] == year] #Filtra por el año ingresado

        return filtro.to_dict(orient="records") #Devuelve los valores
    else:
        return "Pone un año entre 2010 y 2015"
