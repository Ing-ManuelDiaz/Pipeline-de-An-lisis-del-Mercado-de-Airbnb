# 🏠 Airbnb Market Analysis Pipeline

Pipeline de análisis del mercado de Airbnb: exploración, limpieza, modelado y visualización de datos de listados.

---

## 📁 Estructura del proyecto

```
airbnb-analysis/
├── data/                    # ← gitignoreada (no se sube al repo)
│   ├── raw/                 # datos originales, nunca se modifican
│   ├── processed/           # datos limpios y transformados
│   └── external/            # fuentes externas adicionales
│
├── notebooks/               # exploración y análisis en Jupyter
│   ├── 01_exploracion.ipynb
│   ├── 02_eda.ipynb
│   └── 03_modelo.ipynb
│
├── src/                     # módulos Python reutilizables
│   ├── data_loader.py
│   ├── cleaning.py
│   └── visualization.py
│
├── models/                  # modelos entrenados serializados
├── reports/figures/         # gráficas exportadas
│
├── .env                     # ← gitignoreada (API keys)
├── .gitignore
├── requirements.txt
├── README.md
└── docker-compose.yml
```

---

## 🚀 Inicio rápido

### 1. Clonar el repositorio
```bash
git clone <url-del-repo>
cd airbnb-analysis
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

### 3. Configurar variables de entorno
```bash
cp .env.example .env   # edita .env con tus credenciales
```

### 4. Colocar los datos crudos
Coloca los archivos originales en `data/raw/` (no se suben al repo).

### 5. Lanzar Jupyter Lab
```bash
jupyter lab
```

O con Docker:
```bash
docker-compose up
```
Accede en: http://localhost:8888

---

## 📓 Notebooks

| Notebook | Descripción |
|---|---|
| `01_exploracion.ipynb` | Primera vista del dataset: forma, tipos, nulos |
| `02_eda.ipynb` | Análisis exploratorio de datos, distribuciones y correlaciones |
| `03_modelo.ipynb` | Entrenamiento y evaluación del modelo predictivo |

---

## 🛠️ Módulos (`src/`)

| Módulo | Función |
|---|---|
| `data_loader.py` | Carga y validación de datos crudos |
| `cleaning.py` | Limpieza, imputación y transformación |
| `visualization.py` | Funciones de visualización reutilizables |

---

## 📦 Stack tecnológico

- **Python 3.11+**
- **pandas / numpy** — manipulación de datos
- **matplotlib / seaborn / plotly** — visualización
- **scikit-learn** — modelado
- **Jupyter Lab** — entorno interactivo
- **Docker** — reproducibilidad del entorno

---

## 🤝 Contribuciones

1. Crea un branch: `git checkout -b feature/mi-analisis`
2. Haz tus cambios y commitea: `git commit -m "feat: descripción"`
3. Abre un Pull Request

---

*Proyecto académico — Ingeniería de Datos*