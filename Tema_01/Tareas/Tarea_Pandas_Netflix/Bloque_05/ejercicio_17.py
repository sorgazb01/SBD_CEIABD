# 17_.Colaboraciones internacionales. 
# Calcula cuántas producciones fueron realizadas en más de un país.
# (1 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Rellenamos los valores nulos con una cadena vacia para evitar errores.
netflix['production_countries'] = netflix['production_countries'].fillna('')

# Recogemos las producciones que incluyan una coma en el campo de 'production_countries'
# ya que eso indicaría que hay más de un país de producción.
colaboraciones = netflix['production_countries'].str.contains(',').sum()

# Obtenemos el total de producciones del DataSet.
total_producciones = netflix.shape[0]

# Calculamos el porcentaje de producciones con colaboraciones internacionales.
porcentaje = (colaboraciones / total_producciones) * 100

print(f"Producciones con más de un país: {colaboraciones}")
print(f"Porcentaje sobre el total: {porcentaje:.2f}%")