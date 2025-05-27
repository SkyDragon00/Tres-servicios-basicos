from fastapi import FastAPI, HTTPException, Header
import requests
import os

AUTH_URL = os.getenv("AUTH_URL", "http://localhost:8001/verify")

app = FastAPI()

@app.get("/verify_auth")
def verify_auth(authorization: str = Header(...)):
    # reenvía el header al auth-service
    resp = requests.get(AUTH_URL, headers={"Authorization": authorization})
    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail="No autenticado")
    return resp.json()  # devuelve user info

# ruta de ejemplo de “pago”
@app.post("/payment")
def make_payment(authorization: str = Header(...)):
    # comprueba primero que esté autenticado
    verify_auth(authorization)
    # aquí iría la lógica real de pago...
    return {"payment": "ok"}
