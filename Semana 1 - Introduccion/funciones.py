def ejercicio_1():
    def square(a):
        return a * a
    print(square(5))

def ejercicio_2():
    def saludar (nombre, edad):
        mensaje = f"hola {nombre}, tienes {edad} años"
        return mensaje
    print(saludar("pedro", 70))

def ejercicio_3():
    def mayor(a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
    print(mayor(10,60,12))

def ejercicio_4():
    def sum_lista(lista):
        total = 0
        for i in lista:
            total = total + i
        return total
    print(sum_lista([1,2,3,4,5]))

def ejercicio_5():
    def par_impar(a):
        if a % 2 == 0:
            return True
        else:
            return False
    print(par_impar(1))

def ejercicio_6():
    def contar_palabras(palabra):
        contador = 0
        for letra in palabra:
            contador = contador + 1
        return contador
    print(contar_palabras("penessss"))

def ejercicio_7():
    def promedio_lista(lista):
        cantidad = len(lista)
        total = 0
        for numero in lista:
            total = total + numero
        promedio = total / cantidad
        return promedio
    print(promedio_lista([2,4,8]))

def minireto():
    def promedio_notas(lista):
        total = 0
        for numero in lista:
            total += numero 
        return total / len(lista)
    def notas_finales(lista):
        return promedio_notas(lista)

    print(notas_finales([5,8,4,10,9]))


if __name__ == "__main__":
    minireto()        