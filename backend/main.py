
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI()
model = joblib.load("ai_model/schedina_model.pkl")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend attivo"}

@app.post("/genera")
def genera_schedina(
    sport: str = Body(...),
    importo: float = Body(...),
    rischio: int = Body(...)
):
    pred = model.predict([[sport, importo, rischio]])
    return {"schedina": pred.tolist()}
