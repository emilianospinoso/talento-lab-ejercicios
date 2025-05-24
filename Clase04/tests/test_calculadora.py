"""
Suite de pruebas para calculadora_modular.py
- Fixtures reutilizables
- Parametrización de datos
- Markers personalizados
- Aserciones con tolerancia para floats
"""

import pytest
from ..calculadora_modular import sumar, restar, multiplicar, dividir


# ----------  Fixtures  ----------------------------------------------------

@pytest.fixture
def numeros_enteros():
    """Dos enteros genéricos."""
    return 20, 5


@pytest.fixture
def numeros_decimales():
    """Dos floats pequeños para precisión."""
    return 0.1, 0.2


# ----------  SUMAR  -------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (1, 2, 3),
        (-1, -1, -2),
        (2.5, 0.5, 3),
    ],
)
def test_sumar_exitoso(a, b, esperado):
    assert sumar(a, b) == pytest.approx(esperado)


@pytest.mark.smoke
def test_sumar_tipo_erroneo():
    with pytest.raises(TypeError):
        sumar("a", 1)              # entrada inválida


# ----------  RESTAR  ------------------------------------------------------

@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (5, 3, 2),
        (-2, -3, 1),
        (2.5, 0.5, 2),
    ],
)
def test_restar_exitoso(a, b, esperado):
    assert restar(a, b) == pytest.approx(esperado)


def test_restar_tipo_erroneo():
    with pytest.raises(TypeError):
        restar(None, 1)


# ----------  MULTIPLICAR  -------------------------------------------------

def test_multiplicar_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == a * b


def test_multiplicar_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert multiplicar(a, b) == pytest.approx(a * b)


def test_multiplicar_tipo_erroneo():
    with pytest.raises(TypeError):
        multiplicar([], 2)


# ----------  DIVIDIR  -----------------------------------------------------

def test_dividir_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == a / b


def test_dividir_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert dividir(a, b) == pytest.approx(a / b)


@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)
