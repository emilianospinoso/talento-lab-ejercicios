from behave import when, then
from utils.operaciones import multiplicar

@when('multiplico {a:d} y {b:d}')
def step_multiplicar(context, a, b):
    # Guardamos el resultado en context para usarlo en el paso Then
    context.resultado = multiplicar(a, b)

@then('obtengo {esperado:d}')
def step_validar(context, esperado):
    assert context.resultado == esperado, (
        f"Esperaba {esperado}, obtuve {context.resultado}")
