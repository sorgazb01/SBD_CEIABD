# Ejercicio 1. Exploración inicial
# Leer el CSV y mostrar: número de filas, columnas disponibles y tipos de datos.
import pandas as pd

csv_file_path = '../datos/data_empresas.csv'
df = pd.read_csv(csv_file_path)
print(f'Número de filas: {df.shape[0]}')
print(f'Número de columnas: {df.shape[1]}')
print('Columnas disponibles:')
for i, col in enumerate(df.columns, 1):
    print(f'{i} {col}')
print('Tipos de datos:')
print(df.dtypes)
print('Primeras filas:')
print(df.head())
