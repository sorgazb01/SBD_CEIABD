# 11_.Producción por año. 
# Indica qué año tiene más estrenos y cuántos títulos se publicaron en ese periodo.
# (3 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Obtenemos el año con más estrenos y la cantidad de títulos estrenados ese año
# con el método value_counts() y con el sort_index() los ordenamos de forma descendente
# y con el head(1) obtenemos el primero de la lista
producciones_anio_max = netflix['release_year'].value_counts().sort_index(ascending=False).head(1)

# Una vez obtenido el resultado anterior, extraemos el indice (año) 
# y el valor (cantidad de títulos)
anio_max = producciones_anio_max.index[0]
cantidad_max = producciones_anio_max.values[0]

print(f"Año con más estrenos: {anio_max}")
print(f"Cantidad de títulos estrenados ese año: {cantidad_max}")
