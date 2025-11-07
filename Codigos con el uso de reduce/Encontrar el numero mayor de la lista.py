from functools import reduce

print("\n--- Ejercicio 3: Encontrar el número mayor ---")
lista_valores = [10, 60, 30, 80, 50, 100]

# 'lambda max_hasta_ahora, num_actual:'
# Comparamos el máximo encontrado hasta ahora ('max_hasta_ahora')
# con el número actual ('num_actual').

# 'max_hasta_ahora if max_hasta_ahora > num_actual else num_actual':
# Expresión ternaria. Si el 'max_hasta_ahora' es mayor, se 
# mantiene como el acumulador. Si el 'num_actual' es mayor,
# se convierte en el nuevo 'max_hasta_ahora'.
mayor_numero = reduce(lambda max_hasta_ahora, num_actual: 
                      max_hasta_ahora if max_hasta_ahora > num_actual else num_actual, 
                      lista_valores)

print(f"Lista original: {lista_valores}")
print(f"Número mayor: {mayor_numero}")