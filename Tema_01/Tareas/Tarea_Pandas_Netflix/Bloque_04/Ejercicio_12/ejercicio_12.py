# 12_.Evolución de estrenos. 
# Representa mediante un gráfico la evolución del número de títulos a lo largo de los años.
# (3 %)
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Obtenemos el número de estrenos por año.
estrenos_por_anio = netflix['release_year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(estrenos_por_anio.index, estrenos_por_anio.values, marker='o')
plt.title("Evolución del número de estrenos por año")
plt.xlabel("Año de estreno")
plt.ylabel("Número de títulos")
plt.grid(True)
plt.show()