import pandas as pd
import matplotlib.pyplot as plt
from config import nom_alumne, date_time

def compute_goals_by_season(data: pd.DataFrame) -> pd.DataFrame:
    """
    Compute total home and away goals per season.
    Returns a DataFrame indexed by season.
    """

    # Agrupar por temporada
    season_stats = data.groupby("Season").agg(
        total_home_goals=("FTHG", "sum"),
        total_away_goals=("FTAG", "sum")
    )

    return season_stats


def plot_goals_by_season(season_stats: pd.DataFrame) -> None:
    """
    Plot home and away goals per season as line charts.
    Saves the figure in img/ with student name and timestamp.
    """

    plt.figure(figsize=(12, 6))

    plt.plot(season_stats.index, season_stats["total_home_goals"],
             marker="o", label="Goles Locales", color="blue")

    plt.plot(season_stats.index, season_stats["total_away_goals"],
             marker="o", label="Goles Visitantes", color="red")

    plt.title("Goles por temporada (Local vs Visitante)")
    plt.xlabel("Temporada")
    plt.ylabel("Goles totales")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"img/grafica_ex4_{nom_alumne}_{date_time}.png")
    plt.close()
