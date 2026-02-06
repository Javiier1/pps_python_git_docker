# Fase 1: Resolución de dependencias
FROM python:3.11-slim AS dependencies

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Fase 2: Ejecución
FROM python:3.11-slim

WORKDIR /app

COPY --from=dependencies /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY app.py bayeta.py mongo_handler.py frases.txt ./

# Variables de entorno para MongoDB
ENV MONGO_HOST=mongo
ENV MONGO_PORT=27017

EXPOSE 5000

CMD ["python", "app.py"]
