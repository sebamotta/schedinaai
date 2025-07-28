
import os
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ oppure specifica "http://localhost:5174"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("ai_model/schedina_model.pkl")

@app.get("/")
def root():
    return {"message": "Backend attivo", "model_loaded": model is not None}

@app.post("/genera")
def genera_schedina(sport: str = Body(...), importo: float = Body(...), rischio: int = Body(...)):
    pred = model.predict([[sport, importo, rischio]])
    return {"schedina": pred.tolist()}
