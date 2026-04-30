import json
import pandas as pd
from confluent_kafka import Consumer

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas'
GRUPO = 'grupo_ejercicio10'
MAX_VACIOS = 5

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': GRUPO,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])

filas = []
vacios = 0

print(f'Leyendo mensajes del topic \'{TOPIC}\'...\n')

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
        filas.append(json.loads(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

if not filas:
    print('No se recibió ningún mensaje.')
else:
    df = pd.DataFrame(filas)

    idx_mayor_ingreso = df['ingresos_millones'].idxmax()
    empresa_mayor_ingreso = df.loc[idx_mayor_ingreso]

    idx_mayor_crecimiento = df['crecimiento_pct'].idxmax()
    empresa_mayor_crecimiento = df.loc[idx_mayor_crecimiento]

    print('=== Empresa con mayor ingreso ===')
    print(f'  Empresa:           {empresa_mayor_ingreso["empresa"]}')
    print(f'  País:              {empresa_mayor_ingreso["pais"]}')
    print(f'  Sector:            {empresa_mayor_ingreso["sector"]}')
    print(f'  Ingresos (M€):     {empresa_mayor_ingreso["ingresos_millones"]:,}')

    print('\n=== Empresa con mayor crecimiento ===')
    print(f'  Empresa:           {empresa_mayor_crecimiento["empresa"]}')
    print(f'  País:              {empresa_mayor_crecimiento["pais"]}')
    print(f'  Sector:            {empresa_mayor_crecimiento["sector"]}')
    print(f'  Crecimiento (%):   {empresa_mayor_crecimiento["crecimiento_pct"]}')
