# 14_.Décadas. 
# Añade una nueva columna llamada “década” que agrupe los años de estreno (por ejemplo, 1990, 2000, 2010...)
# y analiza qué década concentra más estrenos.
# (2 %)
import pandas as pd

url = "https://raw.githubusercontent.com/amirtds/kaggle-netflix-tv-shows-and-movies/refs/heads/main/titles.csv"
netflix = pd.read_csv(url)

# Creamos la nueva columna "década" a partir de la columna "release_year" 
# acercando el año al múltiplo de 10 más cercano por abajo
netflix['decada'] = (netflix['release_year'] // 10) * 10

# Contamos cuántas producciones se han realizado en cada década
estrenos_por_decada = netflix['decada'].value_counts().sort_index(ascending=False)

print("-- Número de estrenos por década: --")
print(estrenos_por_decada)

# Obtenemos el valor máximo
decada_max_estrenos = estrenos_por_decada.max()
print(f"La década con más estrenos es la de {estrenos_por_decada.idxmax()} con {decada_max_estrenos} producciones.")