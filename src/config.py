import os
from pathlib import Path
from dotenv import load_dotenv

# Configuración de rutas (RAIZ apunta a la carpeta principal del proyecto)
RAIZ = Path(__file__).parent.parent
EXCEL_FILE = RAIZ / "dashboard" / "Olist_Dashboard.xlsx"

# Cargar variables del archivo .env
load_dotenv(RAIZ / ".env")

# Credenciales de Base de Datos
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "olist")

# Cadena de conexión para SQLAlchemy
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Variable para saber si se debe abrir Excel al terminar
AUTO_OPEN_EXCEL = os.getenv("AUTO_OPEN_EXCEL", "true").lower() == "true"
