# CSV Price Filter 📊💰

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Una herramienta de línea de comandos (CLI) eficiente para filtrar catálogos de productos en formato CSV basándose en rangos de precios.

## 🚀 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/csodcaceres/csv_price_filter.git](https://github.com/csodcaceres/csv_price_filter.git)
   cd csv_price_filter


📖 Uso

Ejecuta el script pasando el archivo de entrada, el rango de precios y el nombre del archivo de salida:

   python app.py --input productos.csv --min 10 --max 50 --output filtrados.csv


Parámetros:
   --input: Archivo CSV original.
   --min: (Opcional) Precio mínimo.
   --max: (Opcional) Precio máximo.
   --output: Nombre del archivo resultante.

🛠️ Estructura del Proyecto
   app.py: Lógica principal del filtro.
 