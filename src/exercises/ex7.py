import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from config import nom_alumne, date_time


def compute_top5_teams(data: pd.DataFrame) -> list:
    """
    Compute accumulated points for each team and return the top 5.
    Win = 3 points, Draw = 1 point, Loss = 0 points.
    """

    teams = pd.unique(data[["HomeTeam", "AwayTeam"]].values.ravel())
    points = pd.Series(0, index=teams)

    for _, row in data.iterrows():
        home = row["HomeTeam"]
        away = row["AwayTeam"]
        home_goals = row["FTHG"]
        away_goals = row["FTAG"]

        if home_goals > away_goals:
            points[home] += 3
        elif home_goals < away_goals:
            points[away] += 3
        else:
            points[home] += 1
            points[away] += 1

    top5 = points.sort_values(ascending=False).head(5).index.tolist()
    return top5


def graf(data: pd.DataFrame, selected_teams: list):
    """
    Create a graph of connections between selected teams.
    Each edge weight = number of matches between the two teams.
    """

    # Filtrar partidos donde ambos equipos están en la lista
    filtered = data[
        (data["HomeTeam"].isin(selected_teams)) &
        (data["AwayTeam"].isin(selected_teams))
    ]

    # Crear grafo
    G = nx.Graph()

    # Añadir nodos
    G.add_nodes_from(selected_teams)

    # Contar conexiones
    for _, row in filtered.iterrows():
        home = row["HomeTeam"]
        away = row["AwayTeam"]

        if G.has_edge(home, away):
            G[home][away]["weight"] += 1
        else:
            G.add_edge(home, away, weight=1)

    # Dibujar grafo
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)

    weights = [G[u][v]["weight"] for u, v in G.edges()]

    nx.draw(
        G, pos,
        with_labels=True,
        width=weights,
        node_size=2000,
        node_color="skyblue",
        font_size=10
    )

    # Etiquetas de número de conexiones
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Grafo de conexiones entre los 5 mejores equipos")
    plt.tight_layout()
    plt.savefig(f"img/grafica_ex7_{nom_alumne}_{date_time}.png")
    plt.close()
