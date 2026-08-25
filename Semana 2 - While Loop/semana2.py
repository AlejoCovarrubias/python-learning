def ejercicio1():
    numero = 1

    while numero <= 10:
        print(numero)
        numero += 1

def ejercicio2():
    numero = 10

    while numero >= 1:
        print(numero)
        numero -= 1
def ejercicio3():

    for i in range(1, 21):

        if i % 2 == 0:
            print(i)

def ejercicio4():

    while True:

        print("Escriba números")
        print("67 para salir")

        try:
            numero = int(input())

            if numero == 67:
                print("Terminal finalizada")
                break

        except:
            print("Número inválido")

def ejercicio5():

    numero = 1
    suma = 0

    while numero <= 100:

        suma += numero
        numero += 1

    print(suma)

def ejercicio6():

    while True:
        print("Bienvenido, para salir escriba salir")
        palabra = input("Ingrese palabras: ").strip().lower()
        if palabra == "salir":
            print("Terminal finalizada")
            break

        print("Su palabra fue:", palabra)

def ejercicio7():

    for i in range(1, 21):

        if i % 3 == 0:
            continue

        print(i)

def ejercicio8():
    while True:
            print("Ingrese contraseña: ")
            contraseña = input().lower().strip()
            
            if contraseña == "python123":
                print("contraseña correcta.")
                break
            else:
                print("Contraseña incorrecta")
            
def ejercicio9():
    for i in range(1,51):
        print(i)
        if i == 32:
            break

def ejercicio10():
    while True:
        try:
            print("Bienvenido, si desea finalizar escriba 0")
            numero = float(input("Escriba un numero positivo: "))                    
            
            if numero > 0:
                print(f"su numero es: {numero}")
            elif numero < 0:
                print('Numero negativo!!!')    
                continue
            if numero == 0:
                print('Terminal finalizada')
                break
        except:
            print('Formato no valido')
                 
def ejercicio13():
     while True:
        print("Diga su edad: ")
        print("Para finalizar diga 6767")
        try:
            edad = int(input())
            
            if edad <= 0:
                print("Edad invalida")
                continue

            if edad == 6767:
                print("Terminal Finalizada")
                break
            
            print(f"Tu edad es: {edad}")
        except:
             print('formato Invalido, escriba un numero')

def ejercicio14():
    while True:
        try:
            print("\nBienvenido, si desea finalizar escriba salir.")
            divisor = input("Escriba un divisor para 100: ").lower().strip()

            if divisor == "salir":
                print("Terminal finalizada")
                break
            divisor = float(divisor)
            if divisor == 0:
                print("Divisor nunca puede ser 0. Pruebe con otro numero")
                continue
            valor = 100/divisor

            print(f"100 dividido {divisor} es igual a: {valor} ")
        except:
            print("Formato Invalido, escriba un numero")

def ejercicio16():
    while True:
        try:
            print("\nBienvenido, seleccione 2 numeros para hacer operaciones")
            print("Si desea salir escriba 'salir'")
            numero_1 = input("Primer numero: ").lower().strip()
            if numero_1 == "salir":
                print("Terminal finalizada")
                break
            numero_2 = input("Segundo numero: ").strip().lower()
            if numero_2 == "salir":
                print("Terminal finalizada")
                break
            if numero_1 == "salir":
                print("Terminal finalizada")
                break

            numero_1 = float(numero_1)
            numero_2 = float(numero_2)
            
            print("\nSeleccione su operacion: ")
            print("\nSuma = 1 \nResta = 2 \nMultiplicacion = 3 \nDivision = 4 \nPotecia = 5")
            operacion = int(input())
            
            if operacion == 1:
                print(f"La suma es: {numero_1 + numero_2}")
            elif operacion == 2:
                print(f"La resta es: {numero_1 - numero_2}")
            elif operacion == 3:
                print(f"La multiplicacion es: {numero_1 * numero_2}")
            elif operacion == 4:
                if numero_2 == 0:
                    print("No se puede dividir por 0")
                else:
                    print(f"La division es: {numero_1 / numero_2}")
            elif operacion == 5:
                print(f"La potencia es: {numero_1 ** numero_2}")
            else:
                print("Seleccione correctamente")
        except:
            print("Formato invalido")

def ejercicio17():
    suma = 0
    while True:
        try:
            print("\nBienvenido, para salir escriba 'fin'")
            numero = input("Escriba numeros para sumarlos: ").strip().lower()
            
            if numero == "fin":
                print("Terminal finalizada")
                break
            numero = float(numero)
            suma += numero
        except:
            print("Formato invalido")
    print(f"Su suma total fue: {suma}")

def ejercicio18():

    while True:
        print("\nBienvenido, si desea salir escriba salir")
        email = input("Escriba su email: ").strip().lower()

        if email == "salir":
            print("Terminal finalizada")
            break

        if email == "":
            print("Email vacío")
            continue

        if "@" not in email and "." not in email and len(email) > 120:
            print("Email invalido")
            continue

        print("Email válido")

def ejercicio21():
    saldo = 5000

    while True:
        try:
            print("Bienvenido seleccione su siguiente operacion:")
            print("\nVer saldo: 1 \nRetirar saldo: 2 \nSalir: 3")
            opcion = int(input())

            if opcion == 3:
                print("Sesion finalizada, hasta la proxima")
                break
            if opcion == 1:
                print(f"Su saldo es: {saldo}")
                continue
            elif opcion == 2:
                retirar = int(input("Cuanto saldo desea retirar?: "))
                if retirar <= 0:
                    print("Ingrese un monto valido")
                    continue
                elif retirar > saldo:
                    print("No se puede retirar mas de lo que se tiene en su cuenta.")
                    continue
                else:
                    saldo -= retirar
                    print(f"Su saldo restante es: {saldo}")
            else:
                print("Seleccione una operacion correcta")
                continue
        except:
            print("Formato invalido") 

def ejercicio22():
    adivinar = 7
    while True:
        try:
            print("Adivina un numero para escapar!!!")
            numero = int(input())

            if numero == adivinar:
                print("Lograste escapar!")
                break
            elif numero > adivinar:
                print("Es mas chico")
            elif numero < adivinar:
                print("Es mas grande")
        except:
            print("Dije numero no otra cosa")
            continue

def ejercicio23():
    usuario = "carlos"
    contraseña = "Supercarloswatson123" 
    intentos = 3
    intentos = 3

    while intentos > 0:

        usuario_input = input("Usuario: ")
        contraseña_input = input("Contraseña: ")

        if usuario_input == usuario and contraseña_input == contraseña:
            print("Bienvenido")
            break
        intentos -= 1
        print(f"Incorrecto. Intentos restantes: {intentos}")

    if intentos == 0:
        print("Cuenta bloqueada")

def desafio3():
    
    nombre = str(input("Como se llama?: ")).strip()
    print(f"Bienvenido {nombre}, que desea hacer hoy?")
    while True:
            try:
                suma = 0
                eleccion = int(input("\nSaludar: 1 \nCalcular suma: 2 \nMostrar numeros pares: 3 \nSalir: 4"))

                if eleccion == 1:
                    print(f"Hola {nombre}!")
                    continue
                elif eleccion == 2:
                    while True:
                        try:
                            numero_suma = input("Vamos a sumar numeros,para salir escriba fin: ").strip().lower()
                            if numero_suma == "fin":
                                print(f"Calculo finalizado, suma total = {suma}")
                                break
                            numero_suma = int(numero_suma)
                            suma += numero_suma
                            continue
                        except:
                            print("Escriba un numero o fin")

                elif eleccion == 3:
                    par = []
                    for i in range (1, 101):
                        if i % 2 == 0:
                            par.append(i)
                    print(f"Los numeros pares que hay entre el 1 y el 100 son {len(par)}, y son {par}")
    
                elif eleccion == 4:
                    print(f"Hasta la proxima {nombre}")
                    break
                else:
                    print("Elija una opcion valida")
                    continue
            except:
                print("Formato no valido")    
if __name__ == "__main__":
    ejercicio23()

