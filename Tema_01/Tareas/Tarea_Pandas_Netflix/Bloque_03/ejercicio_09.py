# 9_.Duraciones más largas. 
# Muestra las cinco producciones con mayor duración e interpreta el resultado.
# (3 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Convertir la duración a numérica, para evitar problemas por si hay valores nulos
# o no numéricos.
netflix['runtime'] = pd.to_numeric(netflix['runtime'], errors='coerce')

# Creamos un nuevo DataSet, ordenando los resultados por la columna
# 'runtime' de forma descendente y mostrando solo las 5 primeras filas.
producciones_largas = netflix.sort_values(by='runtime', ascending=False).head(5)

print("-- Las 5 producciones mas largas son: --")
print(producciones_largas)