def muy_facil():
    numeros = [4, 8, 15, 16, 23, 42]
    def busqueda_lineal(valor, numeros):
        for numero in numeros:
            if numero == valor:
                return True
        return False
    print(busqueda_lineal(8, numeros))

def facil():
    def bubble_sort(numeros):
        n = len(numeros)

        for i in range(n):
            for j in range(n - 1 - i):
                if numeros[j] > numeros[j + 1]:
                    numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

        return numeros

    numeros = [8, 3, 1, 9, 4, 2]

    resultado = bubble_sort(numeros)

    print(resultado)

def medio():
    pila = []


    def agregar_elemento(elemento):
        pila.append(elemento)


    def sacar_elemento():
        if esta_vacia():
            return None
        return pila.pop()


    def ver_superior():
        if esta_vacia():
            return None
        return pila[-1]


    def esta_vacia():
        return len(pila) == 0

def dificil():
    temperaturas = [18, 22, 25, 27, 30, 34, 38, 41, 45]


    def busqueda_binaria(lista, buscado):
    
        inicio = 0
        fin = len(lista) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2

            if lista[medio] == buscado:
                return medio

            elif lista[medio] < buscado:
                inicio = medio + 1

            else:
                fin = medio - 1

        return "no esta"
    print(busqueda_binaria(temperaturas, 34))
    print(busqueda_binaria(temperaturas, 30))
    print(busqueda_binaria(temperaturas, 20))
if __name__ == "__main__":
    dificil()