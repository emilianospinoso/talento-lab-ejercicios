"""
Actividad 1 – Clase 02
Solicita nombre, edad y profesión por teclado
y muestra un saludo personalizado.
"""

def main() -> None:
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    profesion = input("Introduce tu profesión: ")

    print(f"¡Hola, {nombre}! Tienes {edad} años y eres {profesion}.")

if __name__ == "__main__":
    main()
