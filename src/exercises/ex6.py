import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from config import nom_alumne, date_time

def train_regression_model(data: pd.DataFrame):
    """
    Train a linear regression model to predict total goals.
    Features: FTHG (goles locales), FTAG (goles visitantes)
    Target: total goals
    """
    data = data.copy()
    data["TotalGoals"] = data["FTHG"] + data["FTAG"]

    X = data[["FTHG", "FTAG"]]
    y = data["TotalGoals"]

    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)

    return model, y, predictions


def plot_regression_results(real, predicted):
    """
    Scatter plot comparing real vs predicted total goals.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(real, predicted, alpha=0.6, color="purple")
    plt.xlabel("Goles reales")
    plt.ylabel("Goles predichos")
    plt.title("Regresión lineal: Goles reales vs predichos")
    plt.tight_layout()

    plt.savefig(f"img/grafica_ex6_{nom_alumne}_{date_time}.png")
    plt.close()
