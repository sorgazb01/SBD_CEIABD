import json
import pandas as pd
import matplotlib.pyplot as plt
from confluent_kafka import Consumer

BOOTSTRAP_SERVERS = 'localhost:9092'
TOPIC = 'empresas'
GRUPO = 'grupo_ejercicio11'
MAX_VACIOS = 5
TOP_N = 5

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

    top_empresas = df.nlargest(TOP_N, 'ingresos_millones')[['empresa', 'precio_eur_LY', 'precio_eur_CY']].reset_index(drop=True)

    print(f'Top {TOP_N} empresas por ingresos:\n')
    print(top_empresas.to_string(index=False))

    bar_width = 0.35
    indices = range(len(top_empresas))

    fig, ax = plt.subplots(figsize=(10, 6))

    barras_ly = ax.bar(indices, top_empresas['precio_eur_LY'], width=bar_width, label='precio_eur_LY', color='steelblue')
    barras_cy = ax.bar(
        [i + bar_width for i in indices],
        top_empresas['precio_eur_CY'],
        width=bar_width,
        label='precio_eur_CY',
        color='darkorange'
    )

    ax.set_title(f'Comparativa de precio LY vs CY — Top {TOP_N} empresas por ingresos')
    ax.set_xlabel('Empresa')
    ax.set_ylabel('Precio (€)')
    ax.set_xticks([i + bar_width / 2 for i in indices])
    ax.set_xticklabels(top_empresas['empresa'], rotation=15, ha='right')
    ax.legend()
    ax.bar_label(barras_ly, padding=3, fontsize=8)
    ax.bar_label(barras_cy, padding=3, fontsize=8)

    plt.tight_layout()
    plt.savefig('../datos/grafica_top_empresas.png', dpi=150)
    plt.show()
