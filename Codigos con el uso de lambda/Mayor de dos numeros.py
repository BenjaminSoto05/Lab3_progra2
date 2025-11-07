print("Ejercicio 1: Mayor de dos números")
# 'lambda a, b:': 
#  Define una función anónima que acepta dos argumentos, 'a' y 'b'.
# 'a if a > b else b':
#  Es la expresión. Devuelve 'a' SI 'a' es mayor que 'b', 
mayor = lambda a, b: a if a > b else b

print(f"El mayor entre 10 y 5 es: {mayor(10, 5)}")
print(f"El mayor entre 3 y 8 es: {mayor(3, 8)}")