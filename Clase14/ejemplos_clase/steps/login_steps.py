from behave import given, when, then
from pages.login_page import LoginPage

@given('el navegador abre la página de login')
def step_open_login(context):
    """Abre la página de login de SauceDemo"""
    context.login_page = LoginPage(context.driver)
    context.login_page.abrir()

@when('ingreso usuario "{usuario}" y clave "{clave}"')
def step_login(context, usuario, clave):
    """Ingresa credenciales y hace login"""
    context.login_page.login_completo(usuario, clave)

@then('la URL contiene "{texto}"')
def step_check_url(context, texto):
    """Verifica que la URL actual contenga el texto especificado"""
    assert texto in context.driver.current_url, (
        f"La URL {context.driver.current_url} no contiene {texto}")

@then('aparece un mensaje de error')
def step_check_error(context):
    """Verifica que aparezca un mensaje de error"""
    error_element = context.driver.find_element_by_css_selector("[data-test='error']")
    assert error_element.is_displayed(), "No se mostró mensaje de error"