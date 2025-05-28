FROM python:3.12-slim

# Variables de entorno por defecto (puedes sobreescribirlas en docker-compose)
ENV SECRET="mi_secreto_supersecreto" \
    ALGORITHM="HS256" \
    ACCESS_TOKEN_EXPIRE_MINUTES=30

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código
COPY . .

# Exponemos el puerto 8001 y arrancamos uvicorn
EXPOSE 8001
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]