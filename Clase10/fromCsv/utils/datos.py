import csv
import pathlib, json

def leer_csv_login(ruta_archivo):
    """
    Lee un archivo CSV y devuelve una lista de tuplas
    para usar en parametrización de pytest
    """
    datos = []
    ruta = pathlib.Path(ruta_archivo)
    
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convertir string 'True'/'False' a booleano
            debe_funcionar = fila['debe_funcionar'].lower() == 'true'
            datos.append((fila['usuario'], fila['clave'], debe_funcionar))
    
    return datos



# Ejemplo de uso
if __name__ == "__main__":
    casos = leer_csv_login('datos/login.csv')
    print(casos)
    # Resultado: [('standard_user', 'secret_sauce', True), ...]