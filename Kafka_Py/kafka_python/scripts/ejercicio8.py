import json
import pandas as pd
from confluent_kafka import Consumer, TopicPartition

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas_sectores'
GRUPO = 'grupo_ejercicio8'
PARTICION_ID = 0
MAX_VACIOS = 5

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': GRUPO,
    'auto.offset.reset': 'earliest'
})

consumer.assign([TopicPartition(TOPIC, PARTICION_ID)])

print(f'Leyendo únicamente la partición {PARTICION_ID} del topic \'{TOPIC}\'...\n')

filas = []
vacios = 0

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            vacios += 1
            if vacios >= MAX_VACIOS:
                print('No hay más mensajes en esta partición.')
                break
            continue

        if msg.error():
            print(f'Error: {msg.error()}')
            continue

        vacios = 0
        datos = json.loads(msg.value().decode('utf-8'))
        filas.append(datos)
        sector = msg.key().decode('utf-8') if msg.key() else 'sin_clave'
        print(f'  [offset {msg.offset()}] {datos["empresa"]} | sector: {sector}')

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

if filas:
    df = pd.DataFrame(filas)
    print(f'\nTotal mensajes leídos en partición {PARTICION_ID}: {len(df)}')
    print(df[['empresa', 'pais', 'sector']].to_string(index=False))
else:
    print(f'\nLa partición {PARTICION_ID} está vacía.')
