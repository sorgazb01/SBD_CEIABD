# 15_.Películas y series por año. 
# Crea una visualización que compare el número de películas y series por año.
# (1 %)
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)


# Agrupar por año y tipo
conteo_tipo_anio = netflix.groupby(['release_year','type']).size().unstack(fill_value=0)


# Crear gráfico de líneas
plt.figure(figsize=(12,6))
plt.plot(conteo_tipo_anio.index, conteo_tipo_anio['MOVIE'], label='Películas', marker='o')
plt.plot(conteo_tipo_anio.index, conteo_tipo_anio['SHOW'], label='Series', marker='d')
plt.title("Comparación de películas y series por año")
plt.xlabel("Año de estreno")
plt.ylabel("Número de títulos")
plt.legend()
plt.grid(True)
plt.show()