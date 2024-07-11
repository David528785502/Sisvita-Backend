# Establecer la imagen base
FROM python:3.12-slim

# Instalar dependencias necesarias para compilar psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Establecer el PYTHONPATH
ENV PYTHONPATH=/app

# Copiar el archivo de requisitos y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo .env
COPY .env .

# Copiar el resto del código de la aplicación en el directorio de trabajo
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "app/app.py"]

