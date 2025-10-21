# 18_.Director más frecuente. 
# Indica qué director aparece con mayor frecuencia en el conjunto de datos.
# (1 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Al no existir el campo 'director' en el DataSet, mostramos un mensaje indicándolo.
if 'director' not in netflix.columns:
  print("No existe el campo director en el DataSet.")