# 10_.Producción por país. 
# Identifica los cinco países con más títulos producidos y ordénalos de mayor a menor.
# (3 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)


# Nos aseguramos que no haya valores nulos en la columna 'production_countries'.
netflix['production_countries'] = netflix['production_countries'].fillna('')

# Creamos un nuevo DataSet, filtrando por la columna 'production_countries'
# en el caso de que haya varios países dentro de la misma producción lo separamos
# por comas, y con el método explode() cada país ocupará su propia fila.
paises = (netflix['production_countries'].str.split(',').explode().str.strip())

print("-- Top 5 países con más producciones: --")
print(paises.value_counts().head(5))
