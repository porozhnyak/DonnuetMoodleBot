
FROM python:3.9


WORKDIR /app


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .
COPY BOT/credit/.env .

RUN apt-get update \
    && apt-get install -y wkhtmltopdf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


CMD ["python", "BOT/BotMain.py"]