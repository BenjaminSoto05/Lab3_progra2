from functools import reduce

print("Ejercicio 1: Suma de todos los elementos")
lista_numeros = [1, 2, 3, 4, 5]

suma_total = reduce(lambda acumulador, elemento: acumulador + elemento, lista_numeros)
# 'lambda acumulador, elemento:'
# Define la función. 'acumulador' es la suma hasta el momento 
# y 'elemento' es el número actual de la lista.

# 'acumulador + elemento':
# Es la expresión. El resultado de esta suma se convierte en el 
# 'acumulador' para la siguiente iteración.

# Proceso por ejemplo:
# 1 (acc) + 2 (elem) = 3 (nuevo acc)
suma_total = reduce(lambda acumulador, elemento: acumulador + elemento, lista_numeros)
print(f"Lista original: {lista_numeros}")
print(f"Suma total: {suma_total}")