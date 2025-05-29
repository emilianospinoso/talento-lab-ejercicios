from behave import when, then
from utils.operaciones import multiplicar, sumar

@when('multiplico {a:d} y {b:d}')
def step_multiplicar(context, a, b):
    """Multiplica dos números enteros"""
    context.resultado = multiplicar(a, b)

@when('sumo {a:d} y {b:d}')
def step_sumar(context, a, b):
    """Suma dos números enteros"""
    context.resultado = sumar(a, b)

@then('obtengo {esperado:d}')
def step_validar(context, esperado):
    """Valida que el resultado sea el esperado"""
    assert context.resultado == esperado, (
        f"Esperaba {esperado}, obtuve {context.resultado}")