FROM python:3.12-slim

# URL del payment-service
ENV PAYMENT_URL="http://payment:8002/verify_auth"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8003
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]