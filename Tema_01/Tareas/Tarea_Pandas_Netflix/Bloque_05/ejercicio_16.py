# 16_.Género terror/horror. 
# Busca todas las producciones de género terror o horror y analiza cuál es la más reciente y de qué país procede.
# (2 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

patron_genero = r'\b(?:horror|terror)\b'

# Hacemos que todas las filas cuya columna 'genres' sea nulas se conviertan en cadenas vacías para evitar errores.
netflix['genres'] = netflix['genres'].fillna('')
netflix['release_year'] = pd.to_numeric(netflix['release_year'], errors='coerce')

# Filtrar títulos que contengan 'Horror' o 'Terror' (insensible a mayúsculas)
producciones_terror = netflix[netflix['genres'].str.contains(patron_genero, case=False, regex=True)]

# Encontrar la producción más reciente
produccion_terror_reciente = producciones_terror.sort_values('release_year', ascending=False).head(1)

print(f"La producción de terror más reciente es del año {produccion_terror_reciente['release_year'].values[0]}:")
print(produccion_terror_reciente[['title', 'type', 'production_countries']])
