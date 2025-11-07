print("Ejercicio 1: Filtrar números pares")
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter() aplica esa lambda a cada elemento de 'lista_numeros'.
numeros_pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
# list() convierte el iterador resultante de filter() en una lista.
print(f"Lista original: {lista_numeros}")
print(f"Números pares: {numeros_pares}")