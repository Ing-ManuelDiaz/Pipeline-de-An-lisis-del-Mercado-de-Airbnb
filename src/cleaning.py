"""
cleaning.py
===========
Funciones de limpieza, imputación y transformación de datos de Airbnb.
"""

import pandas as pd
import numpy as np


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina filas completamente duplicadas."""
    before = len(df)
    df = df.drop_duplicates()
    print(f"[cleaning] Duplicados eliminados: {before - len(df)}")
    return df


def clean_price(df: pd.DataFrame, col: str = "price") -> pd.DataFrame:
    """
    Convierte la columna de precio de string '$1,234.00' a float.
    """
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(r"[$,]", "", regex=True)
            .replace("nan", np.nan)
            .astype(float)
        )
    return df


def drop_high_nulls(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Elimina columnas con más del `threshold` de valores nulos.

    Parameters
    ----------
    threshold : float
        Proporción máxima de nulos permitida (0.5 = 50%).
    """
    null_ratio = df.isnull().mean()
    cols_to_drop = null_ratio[null_ratio > threshold].index.tolist()
    print(f"[cleaning] Columnas eliminadas por alta nulidad (>{threshold*100:.0f}%): {cols_to_drop}")
    return df.drop(columns=cols_to_drop)


def impute_median(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Imputa valores nulos con la mediana de cada columna."""
    for col in cols:
        if col in df.columns:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
    return df


def normalize_text_cols(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Normaliza columnas de texto: minúsculas y sin espacios extra."""
    for col in cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()
    return df
