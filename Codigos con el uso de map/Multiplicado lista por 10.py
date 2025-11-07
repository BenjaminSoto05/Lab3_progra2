print("--- Ejercicio 1: Multiplicar lista por 10 ---")
lista_numeros = [1, 2, 3, 4, 5]
# 'lambda x: x * 10':
# Es la función que se aplicará. Toma un número 'x' y 
# devuelve 'x' multiplicado por 10.
# 'map(..., lista_numeros)':
# Aplica la función lambda a cada elemento de 'lista_numeros'.
# 'list(...)':
# Convierte el objeto 'map' (que es un iterador) en una lista.
multiplicados = list(map(lambda x: x * 10, lista_numeros))

print(f"Lista original: {lista_numeros}")
print(f"Lista multiplicada: {multiplicados}")