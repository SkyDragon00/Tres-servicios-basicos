FROM python:3.12-slim

# URL del auth-service, apuntando al nombre de servicio Docker
ENV AUTH_URL="http://auth:8001/verify"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8002
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
