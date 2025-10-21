import ast
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Para evitar problemas a la hora de tratar los datos rellenamos los valores nulos
# de las columnas con las que vamos a trabajar
netflix['genres'] = netflix['genres'].fillna('[]')
netflix['type'] = netflix['type'].fillna('')

# Creamos una ArrayList para almacenar una lista de los géneros
# de cada una de las filas del DataSet
lista_generos = []
# Con un blucle comenzamos a recorrer la columna 'genres' del DataSet
# fila a fila
for genero in netflix['genres']:
    # Al existir en el DataSet valores que no son unicamente listas,
    # ya que hay valores que son string, usamos ast.literal_eval para
    # evaluar cada uno de los valores y convertirlos en listas.
    try:
        genero_parseado = ast.literal_eval(genero)   
    except Exception:
        lista_generos.append([])  
        continue
    # Comprobamos si la fila actual es un string, en ese caso
    # lo convertimos en una lista.
    if isinstance(genero_parseado, str):
        lista_generos.append([genero_parseado.strip()])
    # Y en caso de no ser un string. Lo añadimos directamente a la lista.
    else:
        lista_generos.append(genero_parseado)

# Asignamos la nueva lista de generos a la columna 'genres' del DataSet
netflix['genres'] = lista_generos

# De cada fila del DataSet separamos los generos en filas independientes
# para poder contar las veces que aparece cada uno de los géneros
# esto lo podemos hacer gracias al conventir la columna 'genres' en una lista
generos_mas_comunes = (netflix.explode('genres'))['genres'].value_counts()

print("-- Top 10 géneros más comunes: --")
print(generos_mas_comunes.head(10))

# Lo primero que hacemos es volver a separar los géneros en filas independientes
# para poder contar las veces que aparece cada uno de los géneros, y agrupamos
# los resultados por géneros y tipo de producción. Con la funcion size() contamos
# cuantas filas hay de cada grupo formado.
producciones_por_genero = netflix.explode('genres').groupby(['genres', 'type']).size()                               

# Muestro 20 filas porque el resultado viene en un formato que aparce en dos filas 
# drama     MOVIE    1864
#           SHOW     1037
print("-- Producciones por género y tipo: --")
print(producciones_por_genero.head(20))
