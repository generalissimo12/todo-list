# Используем образ с Python
FROM python:3.12-slim

# Создаем папку для приложения
WORKDIR /app

# Копируем скрипт в контейнер
COPY app.py .

# Создаем папку для данных
VOLUME /data

# Команда запуска приложения
CMD ["python", "app.py"]
