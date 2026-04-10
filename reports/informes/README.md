#  Informe de Resultados: Análisis de Airbnb CDMX

Este documento resume los hallazgos estratégicos obtenidos a través del pipeline de análisis y modelado de datos.

##  1. ¿Cuál es la pregunta central que responde este proyecto?
¿Cuáles son los verdaderos motores que determinan el precio de un alojamiento en la CDMX y cómo influyen la ubicación geográfica, la reputación de los hosts y el tipo de propiedad en la rentabilidad del mercado?

##  2. ¿Qué encontraste? (Hallazgos clave)
- **Hallazgo 1:** La **ubicación** es el factor más determinante. La latitud y longitud explican el grueso de la varianza del modelo, con una brecha de precio masiva entre el Poniente corporativo (Santa Fe/Polanco) y el resto de la ciudad.
- **Hallazgo 2:** Las **reseñas** tienen una relación **no lineal** con el precio. Listings con 51-100 reseñas alcanzan la mediana más alta (**$1,065 MXN**), superando tanto a los nuevos ($1,023) como a los ultra-populares ($1,017).
- **Hallazgo 3:** El **tipo de habitación** impacta significativamente. Un departamento completo (`Entire home/apt`) tiene una mediana de precio de **$1,241 MXN**, lo cual es **4.75 veces mayor** que una habitación compartida ($261).

##  3. ¿Cómo lo reproduzco en mi máquina?
1. **Clonar el repo:** `git clone <url-del-repo>`
2. **Levantar el entorno:** Ejecutar `docker-compose up --build` en la raíz.
3. **Ejecutar:** Seguir el orden de los notebooks: `01_exploracion.ipynb`, `02_eda.ipynb` y `03_modelo.ipynb`.

##  4. ¿Qué tecnologías usaste?
- **Análisis:** Python (Pandas, NumPy).
- **Machine Learning:** Scikit-Learn (Random Forest & Linear Regression).
- **Visualización:** Seaborn y Matplotlib.
- **Infraestructura:** Docker & Docker-Compose.

##  5. ¿Qué mejorarías si tuvieras más tiempo o datos?
- **NLP:** Realizaría un análisis de sentimiento en las descripciones para ver qué palabras clave incrementan el valor percibido.
- **POIs:** Integraría datos de cercanía a estaciones de metro y museos.
- **API:** Desplegaría un microservicio para predicción de precios en tiempo real.

---
*Este informe sirve como hoja de ruta para la toma de decisiones basada en datos para el mercado de rentas cortas en Ciudad de México.*
