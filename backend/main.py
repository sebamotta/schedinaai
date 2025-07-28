
import os
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI()

MODEL_PATH = os.path.join(os.path.dirname(__file__), "ai_model/schedina_model.pkl")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Errore nel caricamento del modello: {e}")
    model = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend attivo", "model_loaded": model is not None}
