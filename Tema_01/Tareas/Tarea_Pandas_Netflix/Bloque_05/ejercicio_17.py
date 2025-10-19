import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

netflix['production_countries'] = netflix['production_countries'].fillna('')

# Contar filas con más de un país
colaboraciones = netflix['production_countries'].str.contains(',', na=False).sum()

# Total de producciones
total_producciones = len(netflix)

# Porcentaje de colaboraciones internacionales
porcentaje = (colaboraciones / total_producciones) * 100

print(f"Producciones con más de un país: {colaboraciones}")
print(f"Porcentaje sobre el total: {porcentaje:.2f}%")