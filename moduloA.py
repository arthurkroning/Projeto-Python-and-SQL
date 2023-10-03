import psutil
import paho.mqtt.publish as publish
import time

# Configurações do MQTT
mqtt_broker = "broker.emqx.io"  # Substitua pelo endereço do seu broker MQTT
mqtt_topic = "projetoPI"  # Substitua pelo tópico MQTT desejado

while True:
    # Coleta de informações do sistema
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    # Monta a mensagem com as informações coletadas
    message = f"CPU: {cpu_percent}%, Memória: {memory_percent}%, Disco: {disk_percent}%"

    # Publica a mensagem no tópico MQTT
    publish.single(mqtt_topic, message, hostname=mqtt_broker)

    print(f"Mensagem enviada: {message}")

    # Aguarda um intervalo de tempo (por exemplo, 10 segundos) antes de coletar e enviar novamente
    time.sleep(10)
