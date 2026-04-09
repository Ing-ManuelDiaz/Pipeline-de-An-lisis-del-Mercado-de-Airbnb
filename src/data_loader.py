"""
data_loader.py
==============
Funciones para cargar y validar los datos crudos de Airbnb.
"""

import pandas as pd
from pathlib import Path


DATA_RAW = Path(__file__).resolve().parents[1] / "data" / "raw"
DATA_PROCESSED = Path(__file__).resolve().parents[1] / "data" / "processed"


def load_listings(filename: str, **kwargs) -> pd.DataFrame:
    """
    Carga el archivo de listados desde data/raw/.

    Parameters
    ----------
    filename : str
        Nombre del archivo (e.g. 'listings.csv').
    **kwargs :
        Argumentos adicionales para pd.read_csv().

    Returns
    -------
    pd.DataFrame
    """
    filepath = DATA_RAW / filename
    df = pd.read_csv(filepath, **kwargs)
    print(f"[data_loader] Cargado: {filepath.name}  →  {df.shape[0]:,} filas × {df.shape[1]} columnas")
    return df


def load_processed(filename: str, **kwargs) -> pd.DataFrame:
    """Carga un archivo ya procesado desde data/processed/."""
    filepath = DATA_PROCESSED / filename
    return pd.read_csv(filepath, **kwargs)


def save_processed(df: pd.DataFrame, filename: str, index: bool = False) -> None:
    """Guarda un DataFrame en data/processed/."""
    filepath = DATA_PROCESSED / filename
    df.to_csv(filepath, index=index)
    print(f"[data_loader] Guardado: {filepath}")
