import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login

from utils.datos import leer_json_productos

PRODUCTOS = leer_json_productos('datos/productos.json')

@pytest.mark.parametrize("nombre_producto", PRODUCTOS)
def test_agregar_producto_al_carrito(driver, nombre_producto):
    # Primero hacer login
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")
    
    # Ir al inventario y agregar producto
    inventario = InventoryPage(driver)
    contador_inicial = inventario.obtener_contador_carrito()
    
    inventario.agregar_producto_por_nombre(nombre_producto)
    
    contador_final = inventario.obtener_contador_carrito()
    assert contador_final == contador_inicial + 1

