# 5_.Filtro por año.
# Muestra las producciones estrenadas en el año 2020 y cuenta cuántas hay.
# (2 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Filtramos el DataSet para obtener las producciones estrenadas en 2020
producciones_2020 = netflix[(netflix["release_year"] == 2020)]
# Contamos el total de producciones estrenadas en 2020 con el atributo shape[0] (número de filas)
total_producciones_2020 = producciones_2020.shape[0]

print("-- Producciones estrenadas en 2020: --")
print(producciones_2020)
print(f"Total de producciones estrenadas en 2020: {total_producciones_2020}")