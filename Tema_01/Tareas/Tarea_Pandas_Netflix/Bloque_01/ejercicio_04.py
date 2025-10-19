# 4_.Producción más antigua. 
# Indica cuál es la producción más antigua registrada y comenta si el dato parece coherente.
# (2 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Para mostrar la producción más antigua, ordenamos el DataSet por la
# columna "release_year" y con parametro ascending=True para que asi salgan ordenadas
# en función del año de estreno más antiguo. Y con el método head(1) mostramos
# la primera fila del DataSet.
print("-- La producción más antigua es: --")
print(netflix[["title", "production_countries", "release_year"]].sort_values("release_year", ascending=True).head(1))