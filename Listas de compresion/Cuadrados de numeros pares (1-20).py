print("\nEjercicio 2: Cuadrados de pares del 1 al 20")
# itera del 1 al 20, revisa cuales son pares por "i % 2" y le aplica el cuadrado.
cuadrados_pares = [i**2 for i in range(1, 21) if i % 2 == 0]
print(cuadrados_pares)