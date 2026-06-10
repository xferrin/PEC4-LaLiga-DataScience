import pandas as pd
import matplotlib.pyplot as plt
from config import nom_alumne, date_time

def compute_team_stats(data: pd.DataFrame) -> pd.DataFrame:
    """
    Compute matches played, wins, draws and losses for each team.
    Returns a DataFrame indexed by team name.
    """

    teams = pd.unique(data[["HomeTeam", "AwayTeam"]].values.ravel())

    stats = pd.DataFrame(index=teams, columns=["Played", "Wins", "Draws", "Losses"])
    stats[:] = 0

    for _, row in data.iterrows():
        home = row["HomeTeam"]
        away = row["AwayTeam"]
        home_goals = row["FTHG"]
        away_goals = row["FTAG"]

        # Both teams played
        stats.loc[home, "Played"] += 1
        stats.loc[away, "Played"] += 1

        # Determine match result
        if home_goals > away_goals:
            stats.loc[home, "Wins"] += 1
            stats.loc[away, "Losses"] += 1
        elif home_goals < away_goals:
            stats.loc[away, "Wins"] += 1
            stats.loc[home, "Losses"] += 1
        else:
            stats.loc[home, "Draws"] += 1
            stats.loc[away, "Draws"] += 1

    return stats


def plot_team_wins(stats: pd.DataFrame) -> None:
    """
    Plot number of wins per team as a bar chart.
    Saves the figure in img/ with student name and timestamp.
    """

    plt.figure(figsize=(12, 6))
    stats["Wins"].sort_values(ascending=False).plot(kind="bar", color="green")

    plt.title("Victorias por equipo")
    plt.xlabel("Equipo")
    plt.ylabel("Número de victorias")
    plt.tight_layout()

    plt.savefig(f"img/grafica_ex3_{nom_alumne}_{date_time}.png")
    plt.close()
