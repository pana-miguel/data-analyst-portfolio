# 📊 Proceso ETL y Análisis de Datos
## 📌 Introducción

En esta sección del repositorio se explora el uso de herramientas fundamentales para el análisis de datos y la construcción de procesos ETL (Extract, Transform, Load). Se trabajará principalmente con librerías como Polars y Pandas, que permiten realizar tareas de extracción, transformación y limpieza de datos de manera eficiente.

Además, se utilizarán entornos como Jupyter Notebooks, ideales para documentar y ejecutar procesos paso a paso, junto con herramientas de visualización como Matplotlib, que permiten representar los datos de forma gráfica para facilitar su comprensión.

Aunque Matplotlib es compatible tanto con Pandas como con Polars, en este repositorio se prioriza su uso junto con Pandas debido a su integración más directa y facilidad para la generación de visualizaciones y se usara mas polars para la carga y descarga de informacion gracias a su velocidad de procesamiento.

El enfoque principal de este repositorio está en entender el proceso ETL y el análisis de los datos, más que en la visualización avanzada. El objetivo es construir datasets bien estructurados y de calidad, que posteriormente puedan ser utilizados para la creación de dashboards interactivos en herramientas de Business Intelligence.

## 🧪 Datos de Prueba y Acceso a Información Completa

En cada proyecto o prueba dentro de este repositorio, se incluye un archivo de datos con aproximadamente 10,000 filas, diseñado para facilitar la ejecución rápida, pruebas y experimentación.

Sin embargo, si se requiere trabajar con el conjunto de datos completo, cada proyecto incluirá un enlace para descargar el archivo completo. Una vez descargado, es importante ubicarlo correctamente dentro de la estructura del proyecto.

## 📂 Estructura esperada

Si tienes un proyecto con la siguiente estructura:
```bash
proceso-etl-analisis/proyecto1/analisis.ipynb
```
El archivo de datos descargado debe ubicarse en la misma carpeta del notebook, de esta forma:
```bash
proceso-etl-analisis/proyecto1/datos.csv
```

## ⚠️ Importante

Esto es necesario porque cada proyecto está configurado para ejecutarse desde su propia carpeta. Mantener el archivo de datos en la misma ubicación garantiza que las rutas funcionen correctamente y evita errores al cargar la información.