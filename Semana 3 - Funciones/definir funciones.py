def ejercicio1():
    def saludar(nombre):
        print(f"hola {nombre}")
    saludar("Alejo")

def ejercicio2():
    def cuadrado(numero):
        return numero**2
    
    print(cuadrado(5))

def ejercicio3():
    def es_par(numero):
        return numero % 2 == 0
    es_par(4)

def ejercicio4():
    def mayor(numero_1, numero_2):
        if numero_1 == numero_2:
            return False
        elif numero_1 > numero_2:
            return numero_1
        else:
            return numero_2
    mayor(20, 0)

def ejercicio5():
    def promedio(valor_1, valor_2, valor_3):
        return (valor_1 + valor_2 + valor_3) / 3

    print(promedio(10, 20 , 35))    

def ejercicio6():
    def calcular_iva(precio):
        iva = 21
        return precio + (precio * (iva / 100))

    print(calcular_iva(20))

def ejercicio7():
    def celsius_a_fahrenheit(C):
        F = (C * 1.8) + 32
        return F
    
    print(celsius_a_fahrenheit(20))

def ejercicio8():
    def contar_letras(texto):

        contador = 0

        for letra in texto:
            if letra.isalpha(): 
                contador += 1
        return contador

    frase = "Hola, mundo!"
    print("Total de letras:", contar_letras(frase))

def ejercicio9():
    def es_mayor_edad(edad):
        if edad >= 60:
            return True
        return False
    
    print(es_mayor_edad(40))

def ejercicio10():
    def maximo_lista(lista):

        maximo = lista[0]

        for numero in lista:
            if numero > maximo:
                maximo = numero
        return maximo
    
    print(maximo_lista([2,4,6,7,3,2,1,6,8,4,5200520250250205]))

def ejercicio11():
    def sumar_lista(lista):
        suma = 0
        for numero in lista:
            suma += numero

        return suma

    print(sumar_lista([20,340,320,2304,201,123,1]))      

def ejercicio12():
    def encontrar_numero(lista, numero):

        if numero in lista:
            return True
        else:
            return False 

    print(encontrar_numero([2,4,2,2,2,2,256,67,7], 2))

def ejercicio13():
    def cantidad_pares(lista):
        contador = 0

        for numero in lista:
            if numero % 2 == 0:
                contador += 1

        return contador

    print(cantidad_pares([2,54,3,3,4,5,7,1,23,4,56,]))        

def ejercicio14():
    def invertir_texto(texto):
        texto_invertido = ""

        for letra in texto:
            texto_invertido = letra + texto_invertido

        return texto_invertido
        
    print(invertir_texto("python"))

def ejercicio15():
    def factorial(n):
        resultado = 1

        for numero in range(1, n + 1):
            resultado *= numero

        return resultado

def ejercicio16():
    def sumar(a, b):
        suma = a + b
        return suma
        
    def resta(a, b):
        resta = a - b
        return resta
        
    def multiplicacion(a, b):
        multiplicacion = a * b
        return multiplicacion
        
    def division(a, b):
        if b == 0:
            return None
        else:
            division = a / b
            return division
        
    def pedir_numeros():
        while True:
            try:
                a = int(input("Eliga un numero: "))
                b = int(input("Eliga otro numero: "))
                return a, b
            
            except:
                print("Formato no valido, vuelva a ingresar su numero")
    
    def calculadora():
        print("Bienvenido que opcion desea utilizar")
        while True:
            try:
                opcion = int(input(("\nsumar: 1 \nresta: 2\nmultiplicar: 3\ndividir: 4 \nsalir: 5\n")))
                
                if opcion == 1:
                    a, b = pedir_numeros()
                    print(f"la suma es: {sumar(a, b)}")
                    continue

                elif opcion == 2:
                    a, b = pedir_numeros()
                    print(f"La resta es: {resta(a, b)}")
                    continue

                elif opcion == 3:
                    a, b = pedir_numeros()
                    print(f"La multiplicacion es: {multiplicacion(a, b)}")
                    continue

                elif opcion == 4:
                    a, b = pedir_numeros()
                    resultado = division(a, b)
                    if resultado == None:
                        print("No se puede dividir por 0")
                    else:
                        print(f"La division es: {resultado}")
                        continue                
                elif opcion == 5:
                    print("Terminal finalizada, cerrando sesion")
                    break
                else:
                    print("Elija una opcion correcta")
                    continue
            except:
                print("Formato no valido")
        
    calculadora()

def ejercicio17():
    def ingresar_saldo():
        while True:
            try:
                saldo = int(input("Ingrese cuanto saldo quiere depositar: "))
                if saldo >= 0:
                    return saldo
                else:
                    print("Ingrese un valor positivo")
            except:
                print("Formato no valido")

    def retirar_saldo(saldo):
        while True:
            try:
                retirar = int(input("Ingrese cuanto saldo quiere retirar: "))

                if retirar <= saldo:
                    return saldo - retirar

                else:
                    print("No puede retirar esa cantidad")

            except:
                print("Formato no valido")

    def mostrar_saldo(saldo):
        print(f"Tu saldo actual es: {saldo}")

    def cajero_automatico():
        saldo = 0
        print("Bienvenido al cajero")
        while True:
            try:
                opcion = int(input("\nDepositar saldo: 1\nRetirar saldo: 2\nMostrar saldo: 3\nCerrar sesion: 4\n"))

                if opcion == 1:
                    deposito = ingresar_saldo()
                    saldo += deposito

                elif opcion == 2:
                    saldo = retirar_saldo(saldo)

                elif opcion == 3:
                    mostrar_saldo(saldo)

                elif opcion == 4:
                    print("Cerrando sesion...")
                    break

                else:
                    print("Opcion invalida")

            except ValueError:
                print("Ingrese un numero valido")

    cajero_automatico()

def ejercicio20():
    def cantidad_vendida(ventas):
        cantidad = len(ventas)
        return cantidad
    
    def total_ventas(ventas):
        total = 0
        for i in ventas:
            total += i
        return total
    
    def promedio_ventas(ventas):
        suma = 0
        for i in ventas:
            suma += i
        promedio = suma / len(ventas)
        return promedio
            
    def venta_maxima(ventas):
        maximo = ventas[0]
        for i in ventas:
            if i > maximo:
                maximo = i
        return maximo
    def venta_minima(ventas):
        minimo = ventas[0]
        for i in ventas:
            if i < minimo:
                minimo = i
        return minimo
    def reporte(ventas):
        print(f"Cantidad: {cantidad_vendida(ventas)}")
        print(f"Total vendido: {total_ventas(ventas)}")
        print(f"Promedio: {promedio_ventas(ventas)}")
        print(f"Venta máxima: {venta_maxima(ventas)}")
        print(f"Venta mínima: {venta_minima(ventas)}")

    ventas = [100,200,300,400,500]
    reporte(ventas)

if __name__ == "__main__":
    ejercicio20()