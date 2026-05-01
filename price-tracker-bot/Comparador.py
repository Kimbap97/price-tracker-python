import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

class ComparadorPrecios:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def buscar_mercado_libre(self, producto):
        print(f"Buscando '{producto}' en Mercado Libre...")
        # Adaptar URL según país (ej: .cl para Chile, .com.ar para Argentina)
        url = f"https://listado.mercadolibre.cl/{producto.replace(' ', '-')}"
        
        try:
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            productos = []

            # Buscamos los contenedores de los resultados
            items = soup.find_all('li', {'class': 'ui-search-layout__item'})[:5] # Limitamos a los 5 primeros

            for item in items:
                titulo = item.find('h2', {'class': 'ui-search-item__title'}).text
                precio_entero = item.find('span', {'class': 'andes-money-amount__fraction'}).text
                link = item.find('a', {'class': 'ui-search-link'})['href']
                
                productos.append({
                    'Tienda': 'Mercado Libre',
                    'Producto': titulo,
                    'Precio': int(precio_entero.replace('.', '').replace(',', '')),
                    'Enlace': link
                })
            return productos
        except Exception as e:
            print(f"Error en Mercado Libre: {e}")
            return []

    def exportar_datos(self, lista_productos):
        if not lista_productos:
            print("No se encontraron datos para exportar.")
            return

        df = pd.DataFrame(lista_productos)
        df = df.sort_values(by='Precio', ascending=True) # Ordenar por el más barato
        
        nombre_archivo = f"comparativa_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
        print(f"\nÉxito: Reporte generado como '{nombre_archivo}'")
        print(df[['Producto', 'Precio']].head())

# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    bot = ComparadorPrecios()
    busqueda = input("¿Qué producto deseas comparar?: ")
    
    resultados = bot.buscar_mercado_libre(busqueda)
    # Aquí se puede agregar métodos para otras tiendas (Amazon, Falabella, etc.), asi garantizamos un modelo de trabajo mas global
    # No solo cerrado a ciertos servicios
    
    bot.exportar_datos(resultados)


