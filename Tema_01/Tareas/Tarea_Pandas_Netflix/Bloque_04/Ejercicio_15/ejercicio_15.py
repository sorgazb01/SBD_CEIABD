# 15_.Películas y series por año. 
# Crea una visualización que compare el número de películas y series por año.
# (1 %)
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Agrupamos por año y tipo y con la funcion size() contamos
# cuantas filas hay de cada grupo formado.
tipo_anio = netflix.groupby(['release_year','type']).size().unstack(fill_value=0)

# Creamos la visualización
plt.figure(figsize=(12,6))
plt.plot(tipo_anio.index, tipo_anio['MOVIE'], label='Películas', marker='o')
plt.plot(tipo_anio.index, tipo_anio['SHOW'], label='Series', marker='d')
plt.title("Comparación de películas y series por año")
plt.xlabel("Año de estreno")
plt.ylabel("Número de títulos")
plt.legend()
plt.grid(True)
plt.show()