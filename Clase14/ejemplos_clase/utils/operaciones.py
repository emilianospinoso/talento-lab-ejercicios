"""Operaciones matemáticas simples utilizadas por el micro-servicio de cálculo."""

def multiplicar(a: int, b: int) -> int:
    """Devuelve el producto de dos enteros y registra la operación."""
    return a * b

def sumar(a: int, b: int) -> int:
    """Devuelve la suma de dos enteros."""
    return a + b

def restar(a: int, b: int) -> int:
    """Devuelve la resta de dos enteros."""
    return a - b

def dividir(a: int, b: int) -> float:
    """Devuelve la división de dos enteros."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b