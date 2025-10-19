# 13_.Producción por país. 
# Crea un gráfico de barras con los diez países que más títulos han producido.
# (2 %)
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Nos aseguramos de que no existan valores nulos en la columna 'production_countries'.
netflix['production_countries'] = netflix['production_countries'].fillna('')

# Creamos un nuevo DataSet donde ordenamos y contamos los países de producción
# y obtenemos los 10 países con más títulos producidos y la cantidad de 
# títulos producidos por cada uno.
paises_top_10 = (netflix['production_countries'].str.split(',').explode().str.strip()).value_counts().head(10)

plt.figure(figsize=(10,5))
paises_top_10.plot(kind='bar')
plt.title('Top 10 países con más producciones')
plt.xlabel('Países')
plt.ylabel('Número de producciones')
plt.show()