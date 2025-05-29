"""
Tests para la funcionalidad del carrito de compras usando Page Object Model.
Incluye agregar productos, verificar contenido y navegación del carrito.
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def usuario_logueado(driver, credenciales_validas):
    """
    Fixture que proporciona un usuario ya logueado en la página de inventario.
    
    Returns:
        InventoryPage: Instancia de la página de inventario con usuario logueado
    """
    # Realizar login
    login_page = LoginPage(driver)
    login_page.abrir().realizar_login(
        credenciales_validas["usuario"], 
        credenciales_validas["password"]
    )
    
    # Retornar instancia de inventory page
    return InventoryPage(driver)


@pytest.mark.smoke
@pytest.mark.cart
def test_agregar_producto_al_carrito(usuario_logueado):
    """
    Verifica que se pueda agregar un producto al carrito correctamente.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Verificar carrito inicialmente vacío
    3. Agregar primer producto al carrito
    4. Verificar que el contador del carrito se incremente
    """
    inventory_page = usuario_logueado
    
    # Verificar que el carrito está inicialmente vacío
    assert inventory_page.esta_carrito_vacio(), "El carrito debería estar inicialmente vacío"
    
    # Agregar el primer producto al carrito
    nombre_producto_agregado = inventory_page.agregar_primer_producto()
    
    # Verificar que el contador del carrito ahora muestra 1
    contador_carrito = inventory_page.obtener_contador_carrito()
    assert contador_carrito == 1, f"El contador del carrito debería ser 1, pero es {contador_carrito}"
    
    # Verificar que el carrito ya no está vacío
    assert not inventory_page.esta_carrito_vacio(), "El carrito no debería estar vacío después de agregar un producto"
    
    print(f"✅ Producto '{nombre_producto_agregado}' agregado correctamente al carrito")


@pytest.mark.smoke
@pytest.mark.cart
def test_verificar_producto_en_carrito(usuario_logueado):
    """
    Verifica que el producto agregado aparezca correctamente en la página del carrito.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Agregar un producto al carrito
    3. Navegar a la página del carrito
    4. Verificar que el producto esté presente
    5. Verificar que sea el mismo producto agregado
    """
    inventory_page = usuario_logueado
    
    # Agregar producto al carrito
    nombre_producto_agregado = inventory_page.agregar_primer_producto()
    
    # Navegar al carrito
    cart_page = inventory_page.ir_al_carrito()
    
    # Verificar que estamos en la página del carrito
    assert cart_page.esta_en_pagina_carrito(), "No se navegó correctamente a la página del carrito"
    
    # Verificar que hay exactamente un producto en el carrito
    cantidad_productos = cart_page.obtener_cantidad_productos()
    assert cantidad_productos == 1, f"Debería haber 1 producto en el carrito, pero hay {cantidad_productos}"
    
    # Verificar que el producto en el carrito es el mismo que agregamos
    assert cart_page.contiene_producto(nombre_producto_agregado), \
        f"El producto '{nombre_producto_agregado}' no se encuentra en el carrito"
    
    # Verificar que el nombre coincide exactamente
    nombres_productos_carrito = cart_page.obtener_nombres_productos()
    assert nombre_producto_agregado in nombres_productos_carrito, \
        f"El producto agregado '{nombre_producto_agregado}' no coincide con los productos en el carrito: {nombres_productos_carrito}"
    
    print(f"✅ Producto '{nombre_producto_agregado}' verificado correctamente en el carrito")


@pytest.mark.cart
def test_agregar_multiples_productos(usuario_logueado):
    """
    Verifica que se puedan agregar múltiples productos al carrito.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Agregar el primer producto
    3. Agregar el segundo producto
    4. Verificar que el contador muestre 2
    5. Verificar en el carrito que ambos productos estén presentes
    """
    inventory_page = usuario_logueado
    
    # Agregar primer producto
    primer_producto = inventory_page.agregar_producto_por_indice(0)
    
    # Verificar contador después del primer producto
    assert inventory_page.obtener_contador_carrito() == 1, "Contador incorrecto después del primer producto"
    
    # Agregar segundo producto
    segundo_producto = inventory_page.agregar_producto_por_indice(1)
    
    # Verificar contador después del segundo producto
    contador_final = inventory_page.obtener_contador_carrito()
    assert contador_final == 2, f"El contador debería ser 2, pero es {contador_final}"
    
    # Ir al carrito y verificar ambos productos
    cart_page = inventory_page.ir_al_carrito()
    
    # Verificar cantidad de productos en el carrito
    cantidad_en_carrito = cart_page.obtener_cantidad_productos()
    assert cantidad_en_carrito == 2, f"Debería haber 2 productos en el carrito, pero hay {cantidad_en_carrito}"
    
    # Verificar que ambos productos estén presentes
    assert cart_page.contiene_producto(primer_producto), f"El primer producto '{primer_producto}' no está en el carrito"
    assert cart_page.contiene_producto(segundo_producto), f"El segundo producto '{segundo_producto}' no está en el carrito"
    
    print(f"✅ Múltiples productos agregados: '{primer_producto}' y '{segundo_producto}'")


@pytest.mark.cart
def test_titulo_pagina_carrito(usuario_logueado):
    """
    Verifica que el título de la página del carrito sea correcto.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Navegar al carrito
    3. Verificar título de la página
    """
    inventory_page = usuario_logueado
    
    # Navegar al carrito
    cart_page = inventory_page.ir_al_carrito()
    
    # Verificar título de la página del carrito
    titulo_carrito = cart_page.obtener_titulo_pagina()
    assert titulo_carrito == "Your Cart", f"Título del carrito incorrecto: {titulo_carrito}"
    
    print("✅ Título de la página del carrito verificado")


@pytest.mark.cart
def test_carrito_vacio_inicialmente(usuario_logueado):
    """
    Verifica que el carrito esté vacío cuando se accede sin agregar productos.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Ir directamente al carrito sin agregar productos
    3. Verificar que esté vacío
    """
    inventory_page = usuario_logueado
    
    # Ir al carrito sin agregar productos
    cart_page = inventory_page.ir_al_carrito()
    
    # Verificar que el carrito está vacío
    assert cart_page.esta_carrito_vacio(), "El carrito debería estar vacío"
    
    # Verificar que no hay productos
    cantidad_productos = cart_page.obtener_cantidad_productos()
    assert cantidad_productos == 0, f"No debería haber productos en el carrito, pero hay {cantidad_productos}"
    
    print("✅ Carrito vacío verificado correctamente")


@pytest.mark.cart
def test_continuar_comprando_desde_carrito(usuario_logueado):
    """
    Verifica la funcionalidad de "Continue Shopping" desde el carrito.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Ir al carrito
    3. Hacer clic en "Continue Shopping"
    4. Verificar regreso a la página de inventario
    """
    inventory_page = usuario_logueado
    
    # Ir al carrito
    cart_page = inventory_page.ir_al_carrito()
    
    # Continuar comprando
    inventory_page_returned = cart_page.continuar_comprando()
    
    # Verificar que estamos de vuelta en inventario
    assert inventory_page_returned.esta_en_pagina_inventario(), "No se regresó correctamente a la página de inventario"
    
    print("✅ Funcionalidad 'Continue Shopping' verificada correctamente")


@pytest.mark.cart
def test_remover_producto_del_carrito(usuario_logueado):
    """
    Verifica que se pueda remover un producto del carrito.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Agregar un producto al carrito
    3. Ir al carrito
    4. Remover el producto
    5. Verificar que el carrito esté vacío
    """
    inventory_page = usuario_logueado
    
    # Agregar producto
    nombre_producto = inventory_page.agregar_primer_producto()
    
    # Ir al carrito
    cart_page = inventory_page.ir_al_carrito()
    
    # Verificar que el producto está en el carrito
    assert cart_page.contiene_producto(nombre_producto), "El producto no está en el carrito antes de removerlo"
    
    # Remover el producto
    cart_page.remover_producto_por_indice(0)
    
    # Verificar que el carrito está vacío
    assert cart_page.esta_carrito_vacio(), "El carrito debería estar vacío después de remover el producto"
    
    print(f"✅ Producto '{nombre_producto}' removido correctamente del carrito")


@pytest.mark.cart
def test_informacion_completa_producto_en_carrito(usuario_logueado):
    """
    Verifica que la información completa del producto se muestre en el carrito.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Agregar un producto al carrito
    3. Ir al carrito
    4. Verificar que se muestre nombre, descripción y precio
    """
    inventory_page = usuario_logueado
    
    # Agregar producto
    nombre_producto = inventory_page.agregar_primer_producto()
    
    # Ir al carrito
    cart_page = inventory_page.ir_al_carrito()
    
    # Obtener información del producto en el carrito
    nombres = cart_page.obtener_nombres_productos()
    descripciones = cart_page.obtener_descripciones_productos()
    precios = cart_page.obtener_precios_productos()
    
    # Verificar que hay información completa
    assert len(nombres) > 0, "No se encontraron nombres de productos en el carrito"
    assert len(descripciones) > 0, "No se encontraron descripciones de productos en el carrito"
    assert len(precios) > 0, "No se encontraron precios de productos en el carrito"
    
    # Verificar que el producto agregado está en la lista
    assert nombre_producto in nombres, f"El producto '{nombre_producto}' no aparece en los nombres del carrito"
    
    # Verificar que los precios tienen formato correcto (empiezan con $)
    for precio in precios:
        assert precio.startswith('$'), f"El precio '{precio}' no tiene el formato correcto"
    
    print(f"✅ Información completa del producto verificada en el carrito")


@pytest.mark.regression
@pytest.mark.cart
def test_flujo_completo_carrito(usuario_logueado):
    """
    Test de regresión que verifica el flujo completo del carrito.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Agregar producto al carrito
    3. Verificar contador en inventario
    4. Ir al carrito
    5. Verificar producto en carrito
    6. Continuar comprando
    7. Verificar regreso a inventario
    8. Verificar que el contador se mantiene
    """
    inventory_page = usuario_logueado
    
    # Paso 1: Agregar producto
    nombre_producto = inventory_page.agregar_primer_producto()
    
    # Paso 2: Verificar contador
    assert inventory_page.obtener_contador_carrito() == 1, "Contador incorrecto después de agregar producto"
    
    # Paso 3: Ir al carrito
    cart_page = inventory_page.ir_al_carrito()
    
    # Paso 4: Verificar producto en carrito
    assert cart_page.contiene_producto(nombre_producto), "Producto no encontrado en el carrito"
    
    # Paso 5: Continuar comprando
    inventory_page = cart_page.continuar_comprando()
    
    # Paso 6: Verificar regreso a inventario
    assert inventory_page.esta_en_pagina_inventario(), "No se regresó correctamente al inventario"
    
    # Paso 7: Verificar que el contador se mantiene
    assert inventory_page.obtener_contador_carrito() == 1, "El contador del carrito no se mantuvo"
    
    print("✅ Flujo completo del carrito verificado correctamente")


@pytest.mark.smoke
@pytest.mark.cart
@pytest.mark.parametrize("indice_producto", [0, 1, 2])
def test_agregar_diferentes_productos_parametrizado(usuario_logueado, indice_producto):
    """
    Test parametrizado que verifica agregar diferentes productos al carrito.
    
    Args:
        indice_producto (int): Índice del producto a agregar
    """
    inventory_page = usuario_logueado
    
    # Verificar que hay suficientes productos
    cantidad_productos = inventory_page.obtener_cantidad_productos()
    if indice_producto >= cantidad_productos:
        pytest.skip(f"No hay suficientes productos. Solicitado: {indice_producto}, Disponibles: {cantidad_productos}")
    
    # Agregar producto específico
    nombre_producto = inventory_page.agregar_producto_por_indice(indice_producto)
    
    # Verificar en el carrito
    cart_page = inventory_page.ir_al_carrito()
    assert cart_page.contiene_producto(nombre_producto), f"Producto con índice {indice_producto} no está en el carrito"
    
    print(f"✅ Producto con índice {indice_producto} ('{nombre_producto}') agregado correctamente")