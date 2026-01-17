# Web Price Scraper - Portafolio Analista Programador

## Descripción
Este proyecto es una herramienta de automatización escrita en **Python** que realiza Web Scraping para comparar precios de productos en tiempo real. Está diseñado para demostrar habilidades en extracción de datos, manejo de librerías externas y procesamiento de información.

## Características
- **Extracción Dinámica:** Obtiene nombres, precios y enlaces directamente del HTML.
- **Tratamiento de Datos:** Limpia strings y convierte formatos de moneda a enteros para su procesamiento.
- **Exportación:** Genera un archivo `.csv` ordenado por precio (de menor a mayor) usando la librería `pandas`.

## Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Librerías:** - `Requests`: Para la gestión de peticiones HTTP.
  - `BeautifulSoup4`: Para el parseo y extracción del DOM.
  - `Pandas`: Para la estructuración y exportación de datos.

## Cómo ejecutarlo
1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`.
3. Ejecuta `python comparador.py`.