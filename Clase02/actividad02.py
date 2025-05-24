"""
Actividad 2 – Clase 02
Imprime los primeros 10 números pares (del 2 al 20)
utilizando un bucle y un condicional para validar pares.
"""

pares_impresos = 0
numero = 1

while pares_impresos < 10:
    if numero % 2 == 0:
        print(numero)
        pares_impresos += 1
    numero += 1
