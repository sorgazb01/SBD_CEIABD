import json
import pandas as pd
from confluent_kafka import Consumer

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas'
GRUPO = 'grupo_ejercicio5'
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
        filas.append(json.loads(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()

if not filas:
    print('No se recibió ningún mensaje.')
else:
    df = pd.DataFrame(filas)
    df['variacion'] = df['precio_eur_CY'] - df['precio_eur_LY']

    crecimiento_negativo = df[df['crecimiento_pct'] < 0].copy()
    precios_cero = df[(df['precio_eur_CY'] <= 0) | (df['precio_eur_LY'] <= 0)].copy()
    precio_baja_pero_crece = df[
        (df['precio_eur_CY'] < df['precio_eur_LY']) & (df['crecimiento_pct'] > 0)
    ].copy()
    anomalias = pd.concat([crecimiento_negativo, precios_cero, precio_baja_pero_crece]).drop_duplicates()

    print('\n=== Empresas con crecimiento negativo ===')
    if crecimiento_negativo.empty:
        print('  Ninguna detectada.')
    else:
        print(crecimiento_negativo[['empresa', 'pais', 'sector', 'crecimiento_pct', 'variacion']].to_string(index=False))

    print('\n=== Precios incoherentes (CY < LY con crecimiento positivo o precio <= 0) ===')
    incoherentes = pd.concat([precios_cero, precio_baja_pero_crece]).drop_duplicates()
    if incoherentes.empty:
        print('  Ninguno detectado.')
    else:
        print(incoherentes[['empresa', 'precio_eur_LY', 'precio_eur_CY', 'crecimiento_pct']].to_string(index=False))

    print(f'\n=== Total registros anómalos: {len(anomalias)} ===')
    print(anomalias[['empresa', 'pais', 'sector', 'precio_eur_LY', 'precio_eur_CY', 'crecimiento_pct', 'variacion']].to_string(index=False))
