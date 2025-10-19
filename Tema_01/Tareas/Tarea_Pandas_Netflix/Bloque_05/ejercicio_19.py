import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Asegurarnos de que no haya NaN
netflix['genres'] = netflix['genres'].fillna('')

# Separar géneros múltiples y normalizar
generos = netflix['genres'].str.split(',').explode().str.strip()

# Contar los géneros más frecuentes
top_generos = generos.value_counts().head(10)
print("Géneros más comunes en el catálogo:")
print(top_generos)

# Analizar en qué tipo de producción predominan
generos_tipo = netflix.copy()
generos_tipo['genre_individual'] = netflix['genres'].str.split(',').apply(lambda x: [g.strip() for g in x])
generos_tipo = generos_tipo.explode('genre_individual')

# Contar por género y tipo
conteo_genero_tipo = generos_tipo.groupby(['genre_individual','type']).size().unstack(fill_value=0)
print(conteo_genero_tipo.sort_values(by='MOVIE', ascending=False).head(10))