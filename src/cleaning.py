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
    Convierte la columna de precio a float y elimina nulos en precio.
    Usa raw strings para evitar SyntaxWarnings.
    """
    if col in df.columns:
        # Primero quitamos filas con precio nulo (variable crítica)
        df = df.dropna(subset=[col]).copy()
        
        # Si la columna es tipo objeto (string), limpiamos símbolos
        if df[col].dtype == object:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(r"[$,]", "", regex=True)
                .replace("nan", np.nan)
                .astype(float)
            )
    return df


def normalize_text_cols(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Normaliza columnas de texto: minúsculas y sin espacios extra."""
    for col in cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()
    return df


def fill_review_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Llena nulos en métricas de reseñas.
    Si total de reseñas es 0, reviews_per_month debe ser 0.
    """
    if "reviews_per_month" in df.columns:
        df["reviews_per_month"] = df["reviews_per_month"].fillna(0)
    
    if "last_review" in df.columns:
        df["last_review"] = pd.to_datetime(df["last_review"])
    
    return df


def drop_high_nulls(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Elimina columnas con más del `threshold` de valores nulos.
    """
    null_ratio = df.isnull().mean()
    cols_to_drop = null_ratio[null_ratio > threshold].index.tolist()
    if cols_to_drop:
        print(f"[cleaning] Columnas eliminadas por alta nulidad (>{threshold*100:.0f}%): {cols_to_drop}")
        df = df.drop(columns=cols_to_drop)
    return df


def clean_airbnb_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pipeline completo de limpieza para el dataset de Airbnb.
    """
    # 1. Eliminar duplicados
    df = drop_duplicates(df)
    
    # 2. Limpiar precio y eliminar nulos en la variable objetivo
    df = clean_price(df)
    
    # 3. Corregir métricas de reseñas
    df = fill_review_metrics(df)
    
    # 4. Normalizar columnas clave de texto (para evitar inconsistencias en el análisis)
    text_cols = ['name', 'host_name', 'neighbourhood', 'room_type']
    df = normalize_text_cols(df, text_cols)
    
    # 5. Manejar Host Name nulos (ya normalizados a 'nan' por normalize_text_cols)
    if "host_name" in df.columns:
        df["host_name"] = df["host_name"].replace("nan", "Unknown")
        
    # 6. Eliminar columnas con casi 100% nulos
    df = drop_high_nulls(df, threshold=0.99)
    
    return df
