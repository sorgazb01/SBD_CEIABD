from fastapi import FastAPI

app = FastAPI()
@app.get("/")

def home():
    return {"mensaje": "Hola desde FastAPI en Docker!"}