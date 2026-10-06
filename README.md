# Proyecto 3: Flujo de Datos de SQL a Python

## 📋 Descripción del Proyecto

Este proyecto tiene como objetivo principal diseñar e implementar un **flujo de trabajo integral de datos** que conecta una base de datos relacional (SQL) con un entorno de procesamiento y análisis en Python.

El proyecto abarca la consulta de datos mediante SQL, la extracción programática hacia DataFrames de Pandas, la limpieza y transformación de datos, y el análisis exploratorio final para extraer conclusiones clave.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguajes:** SQL, Python
* **Base de Datos:** MySQL
* **Librerías de Python:**
  * `pandas` & `numpy` - Manipulación y transformación de datos
  * `sqlalchemy` / `mysql-connector` - Conexión y extracción desde SQL
  * `matplotlib` & `seaborn` - Visualización de datos y gráficos exploratorios
* **Entorno de Trabajo:** Jupyter Notebook, MySQL Workbench, VS Code, Git/GitHub

---

## 🔄 Metodología y Pasos del Proyecto

El desarrollo del proyecto se estructuró en **5 fases principales**:

1. **Diseño y Consultas en SQL:**
   * Análisis del modelo relacional de la base de datos (tablas, claves primarias y foráneas).
   * Redacción y optimización de consultas SQL (`JOINs`, agregaciones, `GROUP BY`, subconsultas) para seleccionar el conjunto de datos relevante.

2. **Conexión entre SQL y Python:**
   * Configuración de la cadena de conexión mediante `SQLAlchemy` / conector nativo.
   * Carga de los resultados de las consultas SQL directamente a DataFrames de Pandas.

3. **Limpieza y Transformación de Datos:**
   * Tratamiento de valores nulos, duplicados e inconsistencias.
   * Conversión y estandarización de tipos de datos (fechas, cadenas, valores numéricos).
   * Creación de variables derivadas relevantes para el análisis.

4. **Análisis Exploratorio de Datos:**
   * Cálculo de métricas y estadísticas descriptivas clave.
   * Análisis de distribuciones, agrupaciones y tendencias mediante visualizaciones.

5. **Consolidación y Conclusiones:**
   * Interpretación de los resultados obtenidos para responder a las preguntas del proyecto.

---

## 📁 Estructura del Repositorio

```text
├── data/                  # Directorio destinado al almacenamiento de conjuntos de datos y resultados (.csv)
│   └── .gitkeep           # Archivo para mantener la estructura de la carpeta en Git
├── images/                # Imágenes de prueba y consultas utilizadas en el análisis
│   ├── query1.png
│   ├── query2.png
│   └── query3.png
├── notebooks/             # Notebook de Jupyter con el flujo completo
│   └── limpiezafinal.ipynb
├── sql/                   # Queries y scripts de consulta SQL
│   └── df.sql
├── src/                   # Funciones auxiliares o módulos de conexión
│   ├── config.py
│   └── main.py
├── .env_example           # Plantilla de configuración con las variables de entorno requeridas
├── .gitignore             # Archivos excluidos del control de versiones
├── LICENSE                # Licencia del proyecto
├── README.md              # Documentación del proyecto
└── requirements.txt       # Lista de librerías y dependencias de Python
```

---

## 🚀 Requisitos e Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

### 2. Crear y activar un entorno virtual

Se recomienda el uso de un entorno virtual para aislar las dependencias del proyecto:

* **En Windows 🪟:**

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

* **En Linux 🐧 / macOS 🍎:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar dependencias

Instala todas las librerías necesarias mediante `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuración del Entorno (.env)

El proyecto hace uso de variables de entorno para gestionar parámetros de configuración y credenciales de forma segura.

1. Crea una copia del archivo de ejemplo `.env_example`:

   ```bash
   cp .env_example .env
   ```

3. Abre el archivo `.env` y completa los campos necesarios con las claves o rutas correspondientes a tu entorno local.

---

## 🧪 Uso del Proyecto y Pruebas

* **Base de Datos (SQL):** Ejecuta la query ubicada en `sql/df.sql` dentro de MySQL Workbench para verificar la consulta base.
* **Datos:** Asegúrate de colocar los archivos de entrada requeridos dentro del directorio `data/`.
* **Imágenes de Consulta:** Las capturas ubicadas en la carpeta `images/` (`query1.png`, `query2.png`, `query3.png`) son las *queries* de entrada para la evaluación y visualización de los resultados esperados.
* **Ejecución del Análisis:** Abre y ejecuta el notebook interactivo en `notebooks/limpiezafinal.ipynb`.
