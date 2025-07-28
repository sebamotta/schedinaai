from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("ai_model/schedina_model.pkl")

class RichiestaSchedina(BaseModel):
    sport: str
    importo: float
    rischio: int

@app.get("/")
def root():
    return {"message": "Backend attivo", "model_loaded": model is not None}

@app.post("/genera")
def genera_schedina(richiesta: RichiestaSchedina):
    pred = model.predict([[richiesta.sport, richiesta.importo, richiesta.rischio]])
    return {"schedina": pred.tolist()}
