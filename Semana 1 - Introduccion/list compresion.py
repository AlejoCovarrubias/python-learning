def ejercicio_1():
    lista = [1,2,3,4,5,6,7,8,9,10]

    cuadrado = [n*n for n in lista]
    print(cuadrado)

def ejercicio_2():
    pares = [n for n in range(1, 21) if n % 2 == 0]
    print(pares)

def ejercicio_3():
    lista = ["hola", "pene", "alejo"]
    
    mayuscula = [i.upper() for i in lista]
    print(mayuscula)

def ejercicio_4():
    numeros = [4,7,11,15,2,20]
    mayor_10 = [n for n in numeros if n > 10]
    print(mayor_10)

def ejercicio_5():
    palabras = ["gato","elefante","sol"]

    longitud = [len(n) for n in palabras]
    print(longitud)

def minireto():
    lista = [5,10,15,20,25]

    div_5 = [int(n / 5) for n in lista]
    print(div_5)

if __name__ == "__main__":
    minireto()