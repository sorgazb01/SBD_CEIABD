# ¿Existen títulos repetidos?
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

titulos_repetidos = netflix['title'].duplicated().sum()

if titulos_repetidos > 0:
    print(f"Existen {titulos_repetidos} títulos repetidos en el DataSet.")
else:
    print("No existen títulos repetidos en el DataSet.")