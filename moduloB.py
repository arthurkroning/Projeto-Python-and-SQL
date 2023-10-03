import paho.mqtt.client as mqtt
import sqlite3
from datetime import datetime

# Configurações MQTT
mqtt_broker = "broker.emqx.io"  # Substitua pelo endereço do seu broker MQTT
mqtt_topic = "projetoPI"  # Substitua pelo tópico MQTT desejado


# Callback para lidar com mensagens MQTT recebidas
def on_message(client, userdata, message):
    data = message.payload.decode("utf-8")
    print("Mensagem recebida:", data)

    # Gravar a mensagem no banco de dados SQLite3
    insert_data_to_db(data)


# Função para inserir dados no banco de dados SQLite3
def insert_data_to_db(data):
    conn = sqlite3.connect("meu_banco_de_dados.db")
    cursor = conn.cursor()

    # Insira os dados na tabela
    cursor.execute(
        """
        INSERT INTO dados_monitoramento (cpu_percent, memory_percent, disk_percent, timestamp)
        VALUES (?, ?, ?, ?)
    """,
        data.split(", ") + [datetime.now()],
    )

    # Faça commit para salvar as alterações
    conn.commit()

    # Feche a conexão com o banco de dados
    conn.close()


# Configuração do cliente MQTT
mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, 1883)  # Substitua pela porta MQTT, se for diferente
mqtt_client.on_message = on_message
mqtt_client.subscribe(mqtt_topic)

# Iniciar o loop MQTT
mqtt_client.loop_forever()
