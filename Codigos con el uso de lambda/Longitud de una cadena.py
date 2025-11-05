print("Ejercicio 2: Longitud de una cadena")

# 'lambda s:':
#  Define una función que acepta un argumento, 's' (la cadena).
# 'len(s)':
#  Es la expresión. Devuelve la longitud de 's'.
longitud_cadena = lambda s: len(s)

print(f"Longitud de 'Hola Mundo': {longitud_cadena('Hola Mundo')}")
print(f"Longitud de 'Python': {longitud_cadena('Python')}")