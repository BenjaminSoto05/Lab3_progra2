print("Ejercicio 2: Filtrar palabras que empiezan con 'p'")
lista_palabras = ["perro", "gato", "pato", "hamster"]

palabras_con_p = list(filter(lambda palabra: palabra.startswith("p"), lista_palabras))
# El método .startswith() distingue mayúsculas de minúsculas.
# filter() aplica la lambda a cada palabra en 'lista_palabras'.
print(f"Lista original: {lista_palabras}")
print(f"Palabras con 'p': {palabras_con_p}")