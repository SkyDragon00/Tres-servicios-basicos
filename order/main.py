from fastapi import FastAPI, HTTPException, Header
import requests
import os

PAYMENT_URL = os.getenv("PAYMENT_URL", "http://localhost:8002/verify_auth")

app = FastAPI()

@app.post("/create_order")
def create_order(authorization: str = Header(...)):
    # primero validar token / auth y simular que ya pagó
    resp = requests.get(PAYMENT_URL, headers={"Authorization": authorization})
    if resp.status_code != 200:
        raise HTTPException(status_code=403, detail="Pago no aprobado o no autenticado")
    # aquí iría la lógica de creación de orden...
    return {"order": "creada"}
