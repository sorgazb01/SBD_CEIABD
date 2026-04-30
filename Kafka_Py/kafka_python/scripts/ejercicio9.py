import json
import pandas as pd
from confluent_kafka import Consumer, TopicPartition

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas_sectores'
GRUPO = 'grupo_ejercicio9'
PARTICION_ID = 0
MAX_VACIOS = 5
CSV_SALIDA = '../datos/datos_recibidos.csv'

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': GRUPO,
    'auto.offset.reset': 'earliest'
})

consumer.assign([TopicPartition(TOPIC, PARTICION_ID)])

print(f'Leyendo partición {PARTICION_ID} del topic \'{TOPIC}\'...\n')

filas = []
vacios = 0

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
        print(f'  Recibido: {datos["empresa"]} ({datos["sector"]})')

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

if filas:
    df = pd.DataFrame(filas)
    df.to_csv(CSV_SALIDA, index=False, encoding='utf-8')
    print(f'\nGuardados {len(df)} registros en \'{CSV_SALIDA}\'')
    df_verificacion = pd.read_csv(CSV_SALIDA)
    print(f'Verificación: {len(df_verificacion)} filas leídas del CSV generado.')
    print(df_verificacion.to_string(index=False))
else:
    print('\nNo se recibió ningún mensaje. No se generó el CSV.')
