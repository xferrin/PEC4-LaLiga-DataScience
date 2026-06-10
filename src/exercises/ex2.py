import pandas as pd
import matplotlib.pyplot as plt
from config import nom_alumne, date_time

def compute_goal_stats(data: pd.DataFrame) -> dict:
    """
    Compute mean home goals, mean away goals and mean total goals.
    Returns a dictionary with the results.
    """
    mean_home = data["FTHG"].mean()
    mean_away = data["FTAG"].mean()
    mean_total = (data["FTHG"] + data["FTAG"]).mean()

    return {
        "mean_home_goals": mean_home,
        "mean_away_goals": mean_away,
        "mean_total_goals": mean_total
    }

def plot_total_goals_histogram(data: pd.DataFrame) -> None:
    """
    Plot histogram of total goals per match.
    Saves the figure in img/ with student name and timestamp.
    """
    total_goals = data["FTHG"] + data["FTAG"]

    plt.figure(figsize=(8, 6))
    plt.hist(total_goals, bins=15, color="skyblue", edgecolor="black")
    plt.title("Histograma de goles totales por partido")
    plt.xlabel("Goles totales")
    plt.ylabel("Frecuencia")

    plt.tight_layout()
    plt.savefig(f"img/grafica_ex2_{nom_alumne}_{date_time}.png")
    plt.close()
