def _validar_numeros(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser numéricos (int o float).")

def sumar(a, b):
    _validar_numeros(a, b)
    return a + b

def restar(a, b):
    _validar_numeros(a, b)
    return a - b

def multiplicar(a, b):
    _validar_numeros(a, b)
    return a * b

def dividir(a, b):
    _validar_numeros(a, b)
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b