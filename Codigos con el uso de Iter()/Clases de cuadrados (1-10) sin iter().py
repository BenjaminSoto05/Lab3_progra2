class CuadradosLista:
    # Genera una lista completa con los cuadrados de los números
    #  del 1 al 10, sin usar __iter__ o yield.
    def __init__(self, n=10):
        self.n = n

    def obtener_lista_completa(self):
        # Construye y devuelve la lista completa de cuadrados.
        resultado = []
        for i in range(1, self.n + 1):
            resultado.append(i ** 2)
        return resultado

print("\nEjercicio 3: Cuadrados (1-10) con método de lista")

# Creamos la instancia y llamamos al método
lista_cuadrados = CuadradosLista().obtener_lista_completa()
print(lista_cuadrados)