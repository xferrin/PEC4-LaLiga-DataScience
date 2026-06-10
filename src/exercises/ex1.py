import pandas as pd
import matplotlib.pyplot as plt
from config import nom_alumne, date_time

def load_and_eda(file: str) -> pd.DataFrame:
    data = pd.read_csv(file)
    data = data.drop(columns=["HTHG", "HTAG", "HTR"])
    return data

def plot_home_away_goals(data: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 2, 1)
    plt.boxplot(data["FTHG"])
    plt.title("Goles equipos locales")

    plt.subplot(1, 2, 2)
    plt.boxplot(data["FTAG"])
    plt.title("Goles equipos visitantes")

    plt.tight_layout()
    plt.savefig(f"img/grafica_ex1_{nom_alumne}_{date_time}.png")
    plt.close()
