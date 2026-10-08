import os
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path  # <--- NUEVA IMPORTACIÓN
from src.config import DATABASE_URL

# Configuración de consultas y su grano (clave única)
CONSULTAS = {
    "vendedores": "seller_product_id"
}

def obtener_conexion():
    """Crea y devuelve la conexión a la base de datos."""
    try:
        engine = create_engine(DATABASE_URL)
        return engine
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

def ejecutar_etl():
    """Ejecuta el proceso ETL para cada consulta configurada."""
    engine = obtener_conexion()
    if not engine:
        return {} 

    os.makedirs("output", exist_ok=True)
    
    resultados = {} 

    for nombre_archivo, clave_grano in CONSULTAS.items():
        ruta_sql = f"queries/{nombre_archivo}.sql"
        ruta_csv = Path(f"output/{nombre_archivo}.csv") # <--- AHORA ES UN OBJETO PATH

        print(f"Procesando: {nombre_archivo}...")

        try:
            with open(ruta_sql, 'r', encoding='utf-8') as file:
                query = file.read()
        except FileNotFoundError:
            print(f"  ❌ No se encontró el archivo {ruta_sql}")
            continue

        try:
            df = pd.read_sql(query, con=engine)
            filas_totales = len(df)
        except Exception as e:
            print(f"  ❌ Error ejecutando la consulta: {e}")
            continue

        # Validación del Grano
        valores_unicos = df[clave_grano].nunique()
        if filas_totales != valores_unicos:
            print(f"  🚨 ERROR DE GRANO: {filas_totales} filas vs {valores_unicos} '{clave_grano}' únicos.")
            continue
            
        # Exportar a CSV
        df.to_csv(ruta_csv, index=False, encoding='utf-8')
        print(f"  ✅ Éxito: {filas_totales} filas exportadas a {ruta_csv}")
        
        # Guardamos el registro de éxito, SI ESTO FUNCIONA Y SALE EN GITHUB, YO, MARTÍN, LO HE HECHO BIEN.
        resultados[nombre_archivo] = (filas_totales, ruta_csv)

    print("\nETL Finalizado.")
    return resultados