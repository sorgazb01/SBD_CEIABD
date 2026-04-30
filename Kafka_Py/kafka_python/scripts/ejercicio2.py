import json
import pandas as pd
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas'
CSV_PATH = '../datos/data_empresas.csv'

admin = AdminClient({'bootstrap.servers': BOOTSTRAP_SERVERS})
nuevo_topic = NewTopic(topic=TOPIC, num_partitions=3, replication_factor=1)
resultado = admin.create_topics(new_topics=[nuevo_topic])

for topic, future in resultado.items():
    try:
        future.result()
        print(f'Topic \'{topic}\' creado correctamente.')
    except Exception as e:
        print(f'Topic \'{topic}\' ya existe o no se pudo crear: {e}')

df = pd.read_csv(CSV_PATH)
print(f'\nEnviando {len(df)} filas al topic \'{TOPIC}\'...\n')

producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})

def delivery_report(err, msg):
    if err is not None:
        print(f'Error al enviar mensaje: {err}')
    else:
        print(f'Mensaje enviado -> partición {msg.partition()}, offset {msg.offset()}')

for _, row in df.iterrows():
    mensaje = json.dumps(row.to_dict())
    producer.produce(TOPIC, value=mensaje, callback=delivery_report)
    producer.poll(0)

producer.flush()
print('\nTodos los mensajes han sido enviados.')
