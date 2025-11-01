def primeros_diez_pares():
    # Genera los primeros 10 números pares usando yield.
    for i in range(10):
        yield i * 2

# Recorrer el generador con un bucle for
print("Ejercicio 1: Primeros 10 números pares")
for numero in primeros_diez_pares():
    print(numero)