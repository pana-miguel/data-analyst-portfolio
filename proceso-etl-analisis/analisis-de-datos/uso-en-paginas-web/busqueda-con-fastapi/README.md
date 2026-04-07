# Proyecto: Búsqueda de Cédulas con FastAPI + Frontend HTML

## 📌 Descripción

Este proyecto consiste en una aplicación web simple que permite buscar
información de cédulas a partir de un archivo CSV.

El sistema está dividido en dos partes:

-   **Backend (FastAPI)**: expone endpoints para consultar los datos
-   **Frontend (HTML + JavaScript)**: interfaz donde el usuario
    interactúa

------------------------------------------------------------------------

## ⚙️ Tecnologías usadas

-   Python
-   FastAPI
-   Uvicorn
-   Polars
-   HTML, CSS, JavaScript

------------------------------------------------------------------------

## 🚀 ¿Qué hace este proyecto?

-   Permite buscar una cédula específica
-   Muestra si existe o no
-   Retorna los datos asociados
-   Muestra los primeros 10 registros automáticamente al cargar la
    página

------------------------------------------------------------------------

## 📂 Estructura básica

    backend/
     ├── api.py
     ├── cedulas-simuladas-total.csv
    frontend/
     ├── index.html

------------------------------------------------------------------------

## ▶️ Cómo ejecutar el proyecto

### 1. Activar entorno virtual (opcional pero recomendado)

``` bash
conda activate py14
```

### 2. Instalar dependencias

``` bash
pip install fastapi uvicorn polars
```

### 3. Ejecutar el backend

Ubícate en la carpeta donde está `api.py`:

``` bash
uvicorn api:app --reload
```

Luego abre en el navegador:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

### 4. Ejecutar el frontend

Abre el archivo `index.html` en tu navegador.

------------------------------------------------------------------------

## 🔍 Endpoints disponibles

### Buscar cédula

    GET /buscar/{cedula}

### Primeros registros

    GET /primeros

------------------------------------------------------------------------

## 💡 ¿Qué puedes hacer con este proyecto?

-   Convertirlo en una aplicación más completa
-   Conectarlo con Angular o React
-   Reemplazar el CSV por una base de datos
-   Mejorar el diseño visual
-   Implementar autenticación
-   Desplegarlo en internet (Render, Vercel, etc.)

------------------------------------------------------------------------

## 🧠 Aprendizajes clave

-   Cómo crear APIs con FastAPI
-   Cómo consumir APIs con JavaScript
-   Manejo de datos con Polars
-   Integración backend + frontend

------------------------------------------------------------------------

## 📌 Nota

Asegúrate de que el archivo CSV esté en la misma ruta que `api.py` o
ajusta la ruta correctamente.

------------------------------------------------------------------------

## 👨‍💻 Autor

Proyecto desarrollado como práctica de integración de datos y desarrollo
web.
