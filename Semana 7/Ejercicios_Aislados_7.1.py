def muy_facil():
    try:
        numero_1 = int(input("Ingrese un numero: "))
        numero_2 = int(input("Ingrese otro numero: "))
        suma = numero_1 + numero_2
        print(f"La suma da como resultado: {suma}")
    except ValueError:
        print("Ingrese un numero valido y sin coma.")



def facil_1():
    try: 
        numero_1 = int(input("Ingrese Numerador: "))
        numero_2 = int(input("Ingrese Denominador: "))
        Division = numero_1 / numero_2
        print(f"La division da como resultado: {Division}")
    except ValueError:
        print("Ingrese un numero valido y entero")
    except ZeroDivisionError:
        print("El denominador no puede ser 0")
def facil_2():
    Productos = {
        "mouse" : 200,
        "computadora" : 1000,
        "teclado" : 500
        }    
    try:
        check = str(input("Que producto quieres acceder?: ")).strip().lower()
        print(F"Su producto es: {Productos[check]}")
    except KeyError:
        print("Valor no encontrado")

def medio():
    lista = ["Hola", 2, 2.5, "Magali", "Alejo", 100, "100", 8 , 9 , 10]
    while True:
        try:
            indice = int(input("Que indice de la lista desea conocer: "))
            print(f"El elemento de la lista en ese indice es: {lista[indice]}")
            break
        except IndexError:
            print("Introduzca un valor dentro del rango")
        except ValueError:
            print("Introduzca un valor numerico entero")

def dificil():
    def retirar(saldo, monto):
        if monto < 0:
            raise ValueError("No es posible retirar montos negativos")
        if monto == 0:
            raise ValueError("No se seleccionó ningún monto")
        if monto > saldo:
            raise ValueError("No se puede retirar más del saldo")
        return saldo - monto

    saldo = 5000
    while True:
        try:
            accion = int(input("¿Qué acción desea hacer hoy?:\nVer saldo: 1\nRetirar saldo: 2\nSalir: 3\n"))
        except ValueError:
            print("Escriba una opción válida")
            continue
        else:
            if accion < 1 or accion > 3:
                print("Esa opción no existe")

            elif accion == 1:
                print(f"Su saldo es: {saldo}")

            elif accion == 2:
                try:
                    monto = int(input("¿Cuánto saldo desea retirar?: "))

                except ValueError:
                    print("Escriba un monto válido")
                    continue

                try:
                    saldo = retirar(saldo, monto)

                except ValueError as error:
                    print(f"Error: {error}")

                else:
                    print(f"Monto retirado, saldo restante: {saldo}")

            elif accion == 3:
                print("Cerrando terminal")
                break    

if __name__ == "__main__":
    dificil()