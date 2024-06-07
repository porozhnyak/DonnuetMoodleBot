# Используйте базовый образ Python
FROM python:3.9

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Копируйте зависимости проекта и установите их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируйте все остальные файлы проекта в рабочую директорию
COPY . .

RUN apt-get update \
    && apt-get install -y wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Запустите ваше приложение
CMD ["python", "BOT/BotMain.py"]