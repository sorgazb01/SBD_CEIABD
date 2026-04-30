import json
import pandas as pd
from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas_claves'
CSV_PATH = '../datos/data_empresas.csv'

admin = AdminClient({'bootstrap.servers': BOOTSTRAP_SERVERS})
nuevo_topic = NewTopic(topic=TOPIC, num_partitions=3, replication_factor=1)
resultado = admin.create_topics(new_topics=[nuevo_topic])
for topic, future in resultado.items():
    try:
        future.result()
        print(f'Topic \'{topic}\' creado.')
    except Exception as e:
        print(f'Topic \'{topic}\': {e}')

df = pd.read_csv(CSV_PATH)
producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})

print(f'\nEnviando {len(df)} mensajes con clave (empresa) al topic \'{TOPIC}\'...')

for _, row in df.iterrows():
    clave = row['empresa']
    mensaje = json.dumps(row.to_dict())
    producer.produce(TOPIC, key=clave, value=mensaje)
    producer.poll(0)

producer.flush()
print('Mensajes enviados.\n')

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': 'grupo_ejercicio6',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])

distribucion = {}
vacios = 0
MAX_VACIOS = 5

print('Verificando distribución de mensajes por partición...\n')

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
        clave = msg.key().decode('utf-8') if msg.key() else 'sin_clave'

        if particion not in distribucion:
            distribucion[particion] = []
        distribucion[particion].append(clave)

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

print('Distribución de mensajes por partición:')
for particion, claves in sorted(distribucion.items()):
    print(f'  Partición {particion}: {len(claves)} mensajes -> {claves}')
