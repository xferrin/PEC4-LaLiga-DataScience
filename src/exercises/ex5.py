import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config import nom_alumne, date_time

def compute_correlations(data: pd.DataFrame) -> pd.DataFrame:
    """
    Compute correlation matrix for numerical variables.
    """
    numeric_data = data.select_dtypes(include=["int64", "float64"])
    corr_matrix = numeric_data.corr()
    return corr_matrix


def plot_correlation_heatmap(corr_matrix: pd.DataFrame) -> None:
    """
    Plot a heatmap of the correlation matrix.
    Saves the figure in img/ with student name and timestamp.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")

    plt.title("Mapa de calor de correlaciones")
    plt.tight_layout()

    plt.savefig(f"img/grafica_ex5_{nom_alumne}_{date_time}.png")
    plt.close()
