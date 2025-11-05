print("\n--- Ejercicio 3: Primer elemento de una lista ---")

# 'lambda lista:':
# Define una función que acepta un argumento, 'lista'.
#
# 'lista[0] if lista else None':
# Expresión ternaria. Devuelve el primer elemento (lista[0])
primer_elemento = lambda lista: lista[0] if lista else None

mi_lista = ["manzana", "pera", "naranja"]
lista_vacia = []

print(f"Primer elemento de {mi_lista}: {primer_elemento(mi_lista)}")
print(f"Primer elemento de {lista_vacia}: {primer_elemento(lista_vacia)}")