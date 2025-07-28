

FROM python:3.10
WORKDIR /app

COPY backend/ /app
COPY ai_model/ /app/ai_model/

RUN pip install fastapi uvicorn scikit-learn joblib pandas

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

