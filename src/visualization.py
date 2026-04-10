"""
visualization.py
================
Funciones para generar gráficas consistentes y estéticas para el análisis de Airbnb.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path

# Configuración global de estilo
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12

SAVE_DIR = Path(__file__).resolve().parents[1] / "reports" / "figures"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

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


def plot_price_boxplot(df: pd.DataFrame, group_col: str = "neighbourhood", price_col: str = "price", top_n: int = 10, use_p95: bool = True) -> None:
    """
    Genera un boxplot de precios por barrio.
    Si use_p95 es True, ajusta el límite visual al percentil 95.
    """
    top_neighbourhoods = df[group_col].value_counts().nlargest(top_n).index
    df_subset = df[df[group_col].isin(top_neighbourhoods)]
    
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df_subset, x=group_col, y=price_col, order=top_neighbourhoods)
    
    if use_p95:
        p95 = df[price_col].quantile(0.95)
        plt.ylim(0, p95)
        plt.title(f"Distribución de Precios en Top {top_n} Barrios (Limitado al P95: ${p95:,.0f})")
    else:
        plt.title(f"Distribución de Precios en Top {top_n} Barrios")
        
    plt.xticks(rotation=45)
    plt.xlabel("Barrio")
    plt.ylabel("Precio")
    plt.show()


def plot_scatter_reviews_price(df: pd.DataFrame) -> None:
    """Relación entre número de reseñas y precio."""
    plt.figure()
    sns.scatterplot(data=df, x="number_of_reviews", y="price", alpha=0.5)
    plt.title("Relación: Número de Reseñas vs Precio")
    plt.xlabel("Número de Reseñas")
    plt.ylabel("Precio")
    plt.show()


def plot_scatter_nights_price(df: pd.DataFrame) -> None:
    """Relación entre mínimo de noches y precio."""
    plt.figure()
    sns.scatterplot(data=df, x="minimum_nights", y="price", alpha=0.5)
    plt.title("Relación: Mínimo de Noches vs Precio")
    plt.xlabel("Mínimo de Noches")
    plt.ylabel("Precio")
    plt.show()


def plot_corr_heatmap(df: pd.DataFrame, include_categorical: list[str] = None) -> None:
    """
    Grafica un heatmap de correlaciones. 
    Permite incluir columnas categóricas convirtiéndolas a códigos numéricos.
    """
    df_corr = df.copy()
    
    # Codificar categóricas seleccionadas
    if include_categorical:
        for col in include_categorical:
            if col in df_corr.columns:
                df_corr[col] = df_corr[col].astype('category').cat.codes
    
    plt.figure(figsize=(12, 8))
    # Seleccionar solo numéricas (incluyendo las codificadas) y excluir IDs
    numeric_cols = df_corr.select_dtypes(include=[np.number]).columns
    cols_to_plot = [c for c in numeric_cols if 'id' not in c.lower()]
    
    sns.heatmap(df_corr[cols_to_plot].corr(), annot=True, cmap="coolwarm", fmt=".2f", square=True)
    plt.title("Heatmap de Correlaciones (Numéricas + Categóricas Codificadas)")
    plt.show()
