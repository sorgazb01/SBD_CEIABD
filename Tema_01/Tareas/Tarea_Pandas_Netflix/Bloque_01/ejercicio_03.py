# 3_.Producciones recientes.
# Muestra las diez producciones más recientes junto con su país y año de estreno.
# (2 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Para mostrar las 10 producciones más recientes, ordenamos el DataSet por la
# columna "release_year" y con parametro ascending=False para que asi salgan ordenadas
# en función del año de estreno más reciente. Y con el método head(10) mostramos
# las 10 primeras filas del DataSet.
print("-- Las 10 producciones más recientes: --")
print(netflix[["title", "production_countries", "release_year"]].sort_values("release_year", ascending=False).head(10))