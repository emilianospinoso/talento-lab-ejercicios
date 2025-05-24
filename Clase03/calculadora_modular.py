"""
Clase 03 · Calculadora modular con manejo de excepciones
Autor: Tu Nombre
"""

# --- 1. Operaciones atómicas (4 funciones) -------------------------------

def sumar(a: float, b: float) -> float:
    return a + b

def restar(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b


# --- 2. Funciones de apoyo -----------------------------------------------

def pedir_numero(mensaje: str) -> float:
    """Solicita un número por teclado y valida la entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")


# --- 3. Orquestador / UI --------------------------------------------------

def calculadora() -> None:
    print("\n--- CALCULADORA PYTHON (modular) ---")
    a = pedir_numero("Primer número: ")
    b = pedir_numero("Segundo número: ")

    print("1) Sumar | 2) Restar | 3) Multiplicar | 4) Dividir")
    opcion = input("Elige (1-4): ")

    operaciones = {
        "1": sumar,
        "2": restar,
        "3": multiplicar,
        "4": dividir,
    }

    if opcion not in operaciones:
        print("Opción inválida.")
        return

    try:
        resultado = operaciones[opcion](a, b)
        print(f"Resultado: {resultado}")
    except ZeroDivisionError as err:
        print(f"Error: {err}")


# --- 4. Punto de entrada --------------------------------------------------

if __name__ == "__main__":
    calculadora()
