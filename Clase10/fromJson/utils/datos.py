import json

def leer_json_productos(ruta_archivo):
    """
    Lee un archivo JSON con información de productos
    """
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        productos = json.load(archivo)
    
    # Extraer solo los nombres para parametrización
    nombres = [producto['nombre'] for producto in productos]
    return nombres

# Ejemplo de uso
if __name__ == "__main__":
    productos = leer_json_productos('datos/productos.json')
    print(productos)
    # Resultado: ['Sauce Labs Backpack', 'Sauce Labs Bike Light', ...]
