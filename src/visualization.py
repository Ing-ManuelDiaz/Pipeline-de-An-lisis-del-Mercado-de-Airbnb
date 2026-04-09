"""
visualization.py
================
Funciones para generar gráficas consistentes y estéticas para el análisis de Airbnb.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

# Configuración global de estilo
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12

SAVE_DIR = Path(__file__).resolve().parents[1] / "reports" / "figures"

def save_fig(fig_id: str, tight_layout: bool = True, fig_extension: str = "png", resolution: int = 300) -> None:
    """Guarda la figura actual en reports/figures/."""
    path = SAVE_DIR / f"{fig_id}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
    print(f"[visualization] Figura guardada en: {path}")

def plot_price_distribution(df: pd.DataFrame, col: str = "price") -> None:
    """Grafica la distribución de precios."""
    plt.figure()
    sns.histplot(df[col], kde=True, bins=50)
    plt.title("Distribución de Precios de Listados")
    plt.xlabel("Precio")
    plt.ylabel("Frecuencia")
    plt.show()

def plot_room_type_counts(df: pd.DataFrame, col: str = "room_type") -> None:
    """Grafica el conteo de tipos de habitación."""
    plt.figure()
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.title("Conteo por Tipo de Habitación")
    plt.xticks(rotation=45)
    plt.show()

def plot_corr_heatmap(df: pd.DataFrame) -> None:
    """Grafica un heatmap de correlaciones para columnas numéricas."""
    plt.figure(figsize=(12, 8))
    numeric_df = df.select_dtypes(include=["number"])
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Heatmap de Correlaciones")
    plt.show()
