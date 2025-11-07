class CuadradosGenerador:
    # Clase cuyo método __iter__ usa yield para generar los cuadrados de los números del 1 al 10.
    def __iter__(self):
        for i in range(1, 11): # Del 1 al 10 (incluso)
            yield i ** 2

# Ejemplo de uso
print("\nEjercicio 3: Clase que genera cuadrados (1-10)")
# Creamos una instancia de la clase
generador_de_cuadrados = CuadradosGenerador()

# Iteramos sobre la instancia (esto llama a __iter__)
for cuadrado in generador_de_cuadrados:
    print(cuadrado)