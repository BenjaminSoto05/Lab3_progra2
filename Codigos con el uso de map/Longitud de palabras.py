print("\n--- Ejercicio 3: Longitud de palabras ---")
lista_palabras = ["uno", "dos", "tres"]
# 'len':
# 'map' la aplicará a cada elemento (palabra) de la lista.
# 'map(len, lista_palabras)':
# Calcula la longitud de "uno", luego "dos", luego "tres".
longitudes = list(map(len, lista_palabras))

print(f"Lista de palabras: {lista_palabras}")
print(f"Longitud de palabras: {longitudes}")