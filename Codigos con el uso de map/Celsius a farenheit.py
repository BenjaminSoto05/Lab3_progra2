print("\n--- Ejercicio 2: Convertir Celsius a Fahrenheit ---")
grados_celsius = [0, 10, 20, 30]
# 'lambda C: (C * 9/5) + 32':
# Es la función de conversión. Toma un valor 'C' (Celsius)
# y aplica la fórmula para devolver el valor en Fahrenheit.
# 'map(..., grados_celsius)':
# Aplica la conversión a cada temperatura de la lista.
grados_fahrenheit = list(map(lambda C: (C * 9/5) + 32, grados_celsius))

print(f"Grados Celsius: {grados_celsius}")
print(f"Grados Fahrenheit: {grados_fahrenheit}")