# 8_.Filtro por país. 
# Calcula qué porcentaje del total del catálogo corresponde a producciones de Estados Unidos.
# (2 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)


# Creamos un nuevo DataSet con las producciones de que en su columna de
# 'production_countries' contenga '["US"]', aquellas filas que tengan valor null
# les asignamos una cadena vacía para evitar errores.
producciones_usa = netflix['production_countries'].fillna('').str.contains('["US"]')

# Una vez obtenido el DataSet con las producciones de Estados Unidos,
# obtenemos el total de producciones y el total de las producciones de Estados Unidos
# para poder calcular el porcentaje.
total_producciones = netflix.shape[0]
total_producciones_usa = producciones_usa.sum()
porcentaje_usa = (total_producciones_usa / total_producciones) * 100

print(f"Producciones de Estados Unidos: {total_producciones_usa}")
print(f"Porcentaje del catálogo: {porcentaje_usa:.2f}%")