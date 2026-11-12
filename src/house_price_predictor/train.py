from utils import get_model
from joblib import dump

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error

def train_model() -> tuple[float, float, float]:
    X, y = fetch_california_housing(return_X_y=True, as_frame=True)

    Xtrain, Xtest, ytrain, ytest = train_test_split(
        X.values, y.values, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(random_state=42)
    model.fit(Xtrain, ytrain)
    ypred = model.predict(Xtest)

    dump(model, get_model())
    return r2_score(ytest, ypred), mean_absolute_error(ytest, ypred), root_mean_squared_error(ytest, ypred)