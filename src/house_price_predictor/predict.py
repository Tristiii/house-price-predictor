from utils import get_model
from joblib import load

def predict_price(data: list[float]) -> str:
    model = load(get_model())
    ypred = model.predict([data])[0]

    return f'The predicted house price is ${round(ypred * 100000, 2)}.'