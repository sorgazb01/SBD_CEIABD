import json
import pandas as pd
from confluent_kafka import Consumer

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas'
GRUPO = 'grupo_ejercicio3'
MAX_VACIOS = 5

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': GRUPO,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])

filas = []
vacios = 0

print(f'Escuchando el topic \'{TOPIC}\'... (se detiene tras {MAX_VACIOS}s sin mensajes)\n')

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
    print(f'\nDataFrame reconstruido con {len(df)} filas:\n')
    print(df.to_string(index=False))
else:
    print('No se recibió ningún mensaje.')
