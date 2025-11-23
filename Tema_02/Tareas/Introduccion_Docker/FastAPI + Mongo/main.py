from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI(title="API con MongoDB")

client = MongoClient("mongodb://mongodb:27017/")
db = client["bd-fastapi"]
collection = db["items"]

@app.get("/")
def home():
    return {
        "mensaje": "API FastAPI + MongoDB con Docker Compose",
    }