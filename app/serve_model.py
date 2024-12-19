from fastapi import FastAPI
import pickle

app = FastAPI()

# 모델 로드
with open("saved_model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"status": "Model server is running"}

@app.get("/predict/")
def predict(input_value: float):
    prediction = model.predict([[input_value]])
    return {"prediction": prediction.tolist()}

