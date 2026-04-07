# Proyecto: Búsqueda de Cédulas con FastAPI + Frontend HTML

## ▶️ Cómo ejecutar el proyecto

### 1. En una nueva terminal coloca el siguiente comando 

``` bash
cd proceso-etl-analisis/analisis-de-datos/otros-usos/busqueda-con-fastapi/backend
```

### 2. activa el backend 

``` bash
uvicorn api:app --reload
```

### 3. Ejecutar el frontend

en este caso pueden devolverse hasta la carpeta deonde esta el frontend y abrir el html y poder utilizar la interfaz de la pagina web 

### 4. si se quiere usar el proyecto con todos los datos que se tienen pueden ir a la siguiente direccion [Carpeta con datos](https://drive.google.com/drive/folders/1tuugYsOuOAbYCUeusr2hhc7JakumANPW)

nombre del archivo: **cedulas-simuladas-total.csv**

esto mas que todo es para ver el rendimiento con los 4 millones de cedulas simuladas las cuales en este proyecto denotan que no hay un gran cambio en el rendimiento gracias a utilizar polars los datos se cargan de manera muy rapida por lo que no se nota lentitud en la pagina web 


## 📌 Descripción del proyecto

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


```

