import time
import paho.mqtt.client as mqtt


def publish_message():
    # Создание клиента
    client = mqtt.Client()

    # Подключение к MQTT брокеру
    client.connect("mqtt_servise-mosquitto-1", 1883, 60)

    # Публикация сообщения
    client.publish("test/topic", "Hello MQTT!")


if __name__ == '__main__':
    print("Скрипт запущен")
    while True:
        print("Публикация сообщения")
        publish_message()
        time.sleep(10)  # Пауза перед следующей публикацией
