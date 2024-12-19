import bentoml
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 데이터 로드 및 모델 학습
data = load_iris()
X, y = data.data, data.target
model = RandomForestClassifier()
model.fit(X, y)

# BentoML로 모델 저장
bento_model = bentoml.sklearn.save_model("iris_classifier", model)
print(f"Model saved: {bento_model}")
