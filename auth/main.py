from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET = "mi_secreto_supersecreto"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

class LoginData(BaseModel):
    username: str
    password: str

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return payload  # aquí podrías devolver user info
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

@app.post("/login")
def login(data: LoginData):
    # TODO: validar contra DB o lista fija
    if data.username == "usuario" and data.password == "pass":
        token = create_token({"sub": data.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Credenciales incorrectas")

@app.get("/verify")
def verify(authorization: str = Header(...)):
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer":
        raise HTTPException(401, "Formato de Authorization inválido")
    user = verify_token(token)
    return {"user": user["sub"]}
