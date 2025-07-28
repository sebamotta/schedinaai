
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dataset fittizio
data = pd.read_csv("schedine_storiche.csv")
X = data[["sport", "importo", "rischio"]]
y = data["esito"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "schedina_model.pkl")
