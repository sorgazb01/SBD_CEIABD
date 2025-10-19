# 1_. Carga y exploración básica.
# Explica qué información contiene el dataset, cuántas filas y columnas tiene, y qué representa cada una.
# (3 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Explicamos qué información contiene el DataSet con el método info()
print("-- Información del DataSet: --")
netflix.info()

# Mostramos el nombre de cada una de las columnas que componen el DataSet con el atributo columns
print("-- Nombres de las columnas: --")
print(netflix.columns)

# Mostramos el tamaño del DataSet con los valores del artributo shape
print("-- Tamaño del DataSet --")
print(f"Número de filas: {netflix.shape[0]}")
print(f"Número de columnas: {netflix.shape[1]}")