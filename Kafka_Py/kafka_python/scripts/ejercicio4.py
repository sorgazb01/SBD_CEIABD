import json
import pandas as pd
from confluent_kafka import Consumer

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas'
GRUPO = 'grupo_ejercicio4'
MAX_VACIOS = 5

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': GRUPO,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])

filas = []
vacios = 0

print(f'Escuchando el topic \'{TOPIC}\'...\n')

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            vacios += 1
            if vacios >= MAX_VACIOS:
                print('No hay más mensajes. Cerrando consumidor.')
                break
            continue

        if msg.error():
            print(f'Error: {msg.error()}')
            continue

        vacios = 0
        datos = json.loads(msg.value().decode('utf-8'))
        filas.append(datos)

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

if filas:
    df = pd.DataFrame(filas)
    df['variacion'] = df['precio_eur_CY'] - df['precio_eur_LY']
    print(f'\nDataFrame con columna \'variacion\' ({len(df)} filas):\n')
    print(df[['empresa', 'pais', 'precio_eur_LY', 'precio_eur_CY', 'variacion']].to_string(index=False))
else:
    print('No se recibió ningún mensaje.')
