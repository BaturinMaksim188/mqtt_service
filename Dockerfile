# Используйте официальный образ Python как базовый
FROM python:3.8-slim

# Установите рабочую директорию в контейнере
WORKDIR /app

# Копируйте файлы проекта в контейнер
COPY . .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запускайте Python приложение
CMD ["python", "client/main.py"]
