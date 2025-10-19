# 2_.Tipos de producciones. 
# Calcula cuántos títulos hay de cada tipo (por ejemplo, películas o series) e interpreta el resultado.
# (3 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Calculamos cuántas producciones hay de cada tipo con el método value_counts()
print("-- Tipos de producciones --")
print(netflix["type"].value_counts())