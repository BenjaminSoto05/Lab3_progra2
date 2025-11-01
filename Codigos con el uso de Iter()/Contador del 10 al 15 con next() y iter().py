print("Ejercicio 1: Contador del 10 al 15 con iter() y next()")

# Creamos un iterador para el rango de 10 a 15 (16 es exclusivo)
contador_iter = iter(range(10, 16))

# Recorremos el iterador usando next() hasta que se agote
while True:
    try:
        numero = next(contador_iter)
        print(numero)
    except StopIteration:
        # Se lanza StopIteration cuando no hay más elementos 
        break