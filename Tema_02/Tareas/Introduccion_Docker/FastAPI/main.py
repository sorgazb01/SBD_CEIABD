from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Hola desde FastAPI en Docker!"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"¡Hola {nombre}!"}