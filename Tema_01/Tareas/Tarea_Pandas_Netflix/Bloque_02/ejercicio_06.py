# 6_.Filtro por director. 
# Muestra todas las producciones dirigidas por Steven Spielberg (si aparece en el dataset).
# (2 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Al no existir la columna director en el DataSet podemos hacer lo siguiente
# Para poder obtener las producciones dirigidas por Steven Spielberg
# buscariamos en la columna 'director' si existe algún valor que coincida con
# Steven Spierlberg, para comprobarlo bien las columnas que tengan vakores nulos
# los rellenamos con una cadena vacía y pasamos todos los valores a minúsculas.
if 'director' not in netflix.columns:
  print("No existe el campo director en el DataSet.")
else:
  producciones_spielberg = netflix["director"].fillna('').str.lower.str.contains('steven spielberg')
  print(producciones_spielberg)
  total_producciones_spielberg = producciones_spielberg.shape[0]
  print(f"Total de producciones dirigidas por Steven Spielberg: {total_producciones_spielberg}")