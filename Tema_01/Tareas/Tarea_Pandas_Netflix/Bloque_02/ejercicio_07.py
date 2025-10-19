# 7_.Filtro por palabra clave. 
# Crea un nuevo DataFrame con los títulos que contengan la palabra Love o Amor.
# (2 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Creamos un patrón para buscar "love" o "amor"
patron_love_amor = r'\b(?:love|amor)\b'

# Creamos un nuevo DataSet, el cual contenga todos los títulos que contengan
# la palabra "love" o "amor" en su título, uso el Case=False para no realizar
# distinción entre mayúsculas y minúsculas, y el regex=True para usar expresiones regulares
producciones_love_amor = netflix[netflix['title'].fillna('').str.contains(patron_love_amor, case=False, regex=True)]

total_producciones_love_amor = producciones_love_amor.shape[0]
print(f"Registros encontrados: {total_producciones_love_amor}")

print("-- Producciones Love o Amor: --")
print(producciones_love_amor)