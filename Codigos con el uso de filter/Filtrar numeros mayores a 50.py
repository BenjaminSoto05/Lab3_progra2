print("\n--- Ejercicio 3: Filtrar números mayores a 50 ---")
lista_valores = [10, 60, 30, 80, 50, 100]

mayores_a_50 = list(filter(lambda n: n > 50, lista_valores))
# La función lambda (lambda n: n > 50)
# comprueba si el número 'n' es mayor que 50.

# filter() aplica la lambda a cada número en 'lista_valores'.
print(f"Lista original: {lista_valores}")
print(f"Mayores a 50: {mayores_a_50}")