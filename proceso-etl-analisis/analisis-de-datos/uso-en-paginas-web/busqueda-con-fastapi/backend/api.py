# Importo FastAPI para crear la API
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import polars as pl

# creacion de instancia
app = FastAPI()

# Configuro CORS para permitir que cualquier frontend 
# pueda consumir esta API sin problemas de seguridad del navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],   # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  
)

archivo = pl.read_csv("cedulas-simuladas-total1.csv")

# Endpoint para buscar una cédula específica
@app.get("/buscar/{cedula}")
def buscar(cedula: str):
    # Filtro el DataFrame para encontrar coincidencias con la cédula enviada
    resultado = archivo.filter(pl.col("cedula").cast(str) == cedula)
    
    # Si encuentro resultados, lo devuelve
    if resultado.height > 0:
        return {
            "existe": True,
            "data": resultado.to_dicts()  # Convierto a formato JSON para enviar al frontend
        }
    else:
        return {"no existe": False}

# Endpoint para ver los primeros 10 registros del archivo
@app.get("/primeros")
def primeros():
    # Retorno los primeros 10 datos como lista de diccionarios
    return archivo.head(10).to_dicts()