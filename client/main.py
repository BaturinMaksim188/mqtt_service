import asyncio
from aiomqtt import Client

async def main():
    broker = 'mqtt_servise-mosquitto-1'
    port = 1883
    topic = 'test/topic'

    print("Подключение к брокеру...")
    async with Client(broker, port) as client:
        print(f"Подписка на топик {topic}...")
        await client.subscribe(topic)

        print("Ожидание сообщений...")
        async for message in client.messages:
            print(f"Получено сообщение '{message.payload.decode()}' в топике '{message.topic}'")

if __name__ == '__main__':
    print("Скрипт запущен")
    asyncio.run(main())
