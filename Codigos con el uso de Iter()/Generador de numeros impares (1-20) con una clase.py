class GeneradorImpares:

    # Genera números impares del 1 al 20 usando yield en su método __iter__.

    def __iter__(self):
        for i in range(1, 21): # Del 1 al 20
            if i % 2 != 0:
                yield i

print("\nEjercicio 2: Generador de impares (1-20) en una clase")

# Creamos una instancia y la recorremos con un bucle for
for impar in GeneradorImpares():
    print(impar)