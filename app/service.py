import bentoml
from bentoml.io import JSON
import pickle

# 저장된 모델 로드
model_ref = bentoml.sklearn.get("iris_model:latest")
model = model_ref.to_runner()

# Bento 서비스 정의
svc = bentoml.Service("iris_classifier_service", runners=[model])

@svc.api(input=JSON(), output=JSON())
def predict(input_data):
    """
    API 엔드포인트: /predict
    요청 데이터: JSON 형식
    """
    result = model.run(input_data["features"])
    return {"prediction": result.tolist()}
