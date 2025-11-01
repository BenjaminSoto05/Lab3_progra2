def solo_impares(lista_numeros):
    # Recibe una lista y devuelve solo los números impares usando yield.
    for num in lista_numeros:
        if num % 2 != 0:
            yield num

# Ejemplo de uso
print("\nEjercicio 2: Filtrar números impares de una lista")
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for impar in solo_impares(mi_lista):
    print(impar)