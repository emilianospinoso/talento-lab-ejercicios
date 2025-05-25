"""
Tests para la funcionalidad de login usando Page Object Model.
Incluye casos de éxito y fallo del proceso de autenticación.
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.login
def test_login_exitoso_credenciales_validas(driver, credenciales_validas):
    """
    Verifica que un usuario pueda iniciar sesión exitosamente con credenciales válidas.
    
    Pasos:
    1. Navegar a la página de login
    2. Ingresar credenciales válidas
    3. Hacer clic en el botón de login
    4. Verificar redirección a página de inventario
    """
    # Arrancar en la página de login
    login_page = LoginPage(driver)
    login_page.abrir()
    
    # Realizar login con credenciales válidas
    login_page.realizar_login(
        credenciales_validas["usuario"], 
        credenciales_validas["password"]
    )
    
    # Verificar que hemos sido redirigidos a la página de inventario
    inventory_page = InventoryPage(driver)
    assert inventory_page.esta_en_pagina_inventario(), "No se redirigió a la página de inventario"
    
    # Verificación adicional: comprobar que el título de la página es correcto
    assert inventory_page.obtener_titulo_navegador() == "Swag Labs", "El título del navegador no es el esperado"
    
    print("✅ Login exitoso completado correctamente")


@pytest.mark.login
def test_login_falla_credenciales_invalidas(driver, credenciales_invalidas):
    """
    Verifica que el login falle apropiadamente con credenciales inválidas.
    
    Pasos:
    1. Navegar a la página de login
    2. Ingresar credenciales inválidas
    3. Hacer clic en el botón de login
    4. Verificar que aparece mensaje de error
    5. Verificar que permanece en la página de login
    """
    # Arrancar en la página de login
    login_page = LoginPage(driver)
    login_page.abrir()
    
    # Intentar login con credenciales inválidas
    login_page.realizar_login(
        credenciales_invalidas["usuario"], 
        credenciales_invalidas["password"]
    )
    
    # Verificar que aparece mensaje de error
    assert login_page.esta_mensaje_error_visible(), "No se muestra mensaje de error"
    
    # Verificar el contenido del mensaje de error
    mensaje_error = login_page.obtener_mensaje_error()
    assert "Username and password do not match" in mensaje_error, f"Mensaje de error inesperado: {mensaje_error}"
    
    # Verificar que permanecemos en la página de login
    assert login_page.esta_en_pagina_login(), "No debería haber salido de la página de login"
    
    print("✅ Validación de credenciales inválidas completada correctamente")


@pytest.mark.login
def test_login_usuario_bloqueado(driver, usuario_bloqueado):
    """
    Verifica el comportamiento con un usuario bloqueado.
    
    Pasos:
    1. Navegar a la página de login
    2. Ingresar credenciales de usuario bloqueado
    3. Hacer clic en el botón de login
    4. Verificar que aparece mensaje de error apropiado
    """
    # Arrancar en la página de login
    login_page = LoginPage(driver)
    login_page.abrir()
    
    # Intentar login con usuario bloqueado
    login_page.realizar_login(
        usuario_bloqueado["usuario"], 
        usuario_bloqueado["password"]
    )
    
    # Verificar que aparece mensaje de error
    assert login_page.esta_mensaje_error_visible(), "No se muestra mensaje de error para usuario bloqueado"
    
    # Verificar el contenido específico del mensaje de error
    mensaje_error = login_page.obtener_mensaje_error()
    assert "locked out" in mensaje_error.lower(), f"El mensaje no indica que el usuario está bloqueado: {mensaje_error}"
    
    print("✅ Validación de usuario bloqueado completada correctamente")


@pytest.mark.login
@pytest.mark.parametrize("usuario,password,deberia_funcionar", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("problem_user", "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
    ("invalid_user", "secret_sauce", False),
    ("standard_user", "wrong_password", False),
])
def test_login_multiples_escenarios(driver, usuario, password, deberia_funcionar):
    """
    Test parametrizado que prueba múltiples combinaciones de usuario/contraseña.
    
    Args:
        usuario (str): Nombre de usuario a probar
        password (str): Contraseña a probar
        deberia_funcionar (bool): Si se espera que el login sea exitoso
    """
    # Arrancar en la página de login
    login_page = LoginPage(driver)
    login_page.abrir()
    
    # Realizar intento de login
    login_page.realizar_login(usuario, password)
    
    if deberia_funcionar:
        # Si debería funcionar, verificar que estamos en inventario
        inventory_page = InventoryPage(driver)
        assert inventory_page.esta_en_pagina_inventario(), f"Login debería haber funcionado para {usuario}"
        print(f"✅ Login exitoso para usuario: {usuario}")
    else:
        # Si no debería funcionar, verificar que hay error y seguimos en login
        assert login_page.esta_mensaje_error_visible(), f"Debería haber mensaje de error para {usuario}"
        assert login_page.esta_en_pagina_login(), f"Debería permanecer en página de login para {usuario}"
        print(f"✅ Login fallido correctamente para usuario: {usuario}")


@pytest.mark.smoke
@pytest.mark.login
def test_metodo_chaining_login(driver, credenciales_validas):
    """
    Verifica que el method chaining funcione correctamente en LoginPage.
    
    Este test demuestra el uso de method chaining para una sintaxis más fluida.
    """
    # Usar method chaining para realizar todas las acciones en una línea
    LoginPage(driver).abrir().realizar_login(
        credenciales_validas["usuario"], 
        credenciales_validas["password"]
    )
    
    # Verificar resultado
    inventory_page = InventoryPage(driver)
    assert inventory_page.esta_en_pagina_inventario(), "Method chaining no funcionó correctamente"
    
    print("✅ Method chaining funcionando correctamente")