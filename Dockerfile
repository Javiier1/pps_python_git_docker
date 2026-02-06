# Fase 1: Resolución de dependencias
FROM python:3.11-slim AS dependencies

WORKDIR /app

# Copiar requirements y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Fase 2: Ejecución
FROM python:3.11-slim

WORKDIR /app

# Copiar dependencias instaladas desde la fase anterior
COPY --from=dependencies /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copiar código de la aplicación
COPY app.py bayeta.py frases.txt ./

# Exponer puerto
EXPOSE 5000

# Comando de ejecución
CMD ["python", "app.py"]
