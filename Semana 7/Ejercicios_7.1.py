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

if __name__ == "__main__":
    medio()