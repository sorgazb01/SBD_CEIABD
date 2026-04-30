import json
import pandas as pd
from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas_sectores'
NUM_PARTICIONES = 5
CSV_PATH = '../datos/data_empresas.csv'

admin = AdminClient({'bootstrap.servers': BOOTSTRAP_SERVERS})
nuevo_topic = NewTopic(topic=TOPIC, num_partitions=NUM_PARTICIONES, replication_factor=1)
resultado = admin.create_topics(new_topics=[nuevo_topic])
for topic, future in resultado.items():
    try:
        future.result()
        print(f'Topic \'{topic}\' creado con {NUM_PARTICIONES} particiones.')
    except Exception as e:
        print(f'Topic \'{topic}\': {e}')

df = pd.read_csv(CSV_PATH)
producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})

print(f'\nEnviando {len(df)} mensajes. Clave = sector...')
sectores = df['sector'].unique()
print(f'Sectores en el CSV: {list(sectores)}\n')

for _, row in df.iterrows():
    clave = row['sector']
    mensaje = json.dumps(row.to_dict())
    producer.produce(TOPIC, key=clave, value=mensaje)
    producer.poll(0)

producer.flush()
print('Mensajes enviados.\n')

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': 'grupo_ejercicio7',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])

distribucion = {i: set() for i in range(NUM_PARTICIONES)}
vacios = 0
MAX_VACIOS = 5

print('Verificando distribución por sector y partición...\n')

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            vacios += 1
            if vacios >= MAX_VACIOS:
                break
            continue

        if msg.error():
            print(f'Error: {msg.error()}')
            continue

        vacios = 0
        particion = msg.partition()
        sector = msg.key().decode('utf-8') if msg.key() else 'sin_clave'
        distribucion[particion].add(sector)

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

print('Sectores por partición:')
for particion, sectores_part in sorted(distribucion.items()):
    print(f'  Partición {particion}: {sorted(sectores_part) if sectores_part else "(vacía)"}')
