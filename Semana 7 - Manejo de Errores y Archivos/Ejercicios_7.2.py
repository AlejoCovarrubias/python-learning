def muy_facil():
    def convertir_entero(texto):
        texto = int(texto)
        return texto
    while True:
        try:
            texto_usuario = input("\nIntroduzca numero: ")
            texto = convertir_entero(texto_usuario)
        except ValueError:
            print("\nEscriba un numero valido y entero")
        else:
            print(f"\nEl texto convertido es: {texto}")
            break

def facil_1():
    def validar_edad(edad):
        if edad <= 0:
            raise ValueError("La edad tiene que ser mayor que 0")
        return edad
    while True:
        try:
            edad = int(input("\nIntroduzca su edad: "))

        except ValueError:
            print("Error, la edad debe ser un numero entero")
            continue
    
        try:
            validar_edad(edad)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print(f"Su edad es: {edad}")
            break

def facil_2():
    def dividir(a, b):
        if b == 0:
            raise ZeroDivisionError("No es posible dividir por 0")
        
        return a/b
            

    while True:
        try:
            numero_1 = float(input("Introduzca el numerador: "))
            numero_2 = float(input("Introduzca el denominador: "))
        except ValueError:
            print("Error: El valor debe ser un numero")
            continue
        try:
            resultado = dividir(numero_1, numero_2)    
        except ZeroDivisionError as error:
            print(f"Error: {error}")
        else:
            print(f"El resultado es: {resultado}")
            break
def medio_1():
    def obtener_precios(productos, nombre):
        if nombre not in productos:
            raise KeyError("El producto no existe")
        return productos[nombre]
        
    productos = {
           "mouse" : 200,
           "computadora" : 1000,
           "teclado" : 500
        }    
    while True:
        try:
            buscar_producto = input("Que producto desea ver el precio?: ").strip().lower()
            precio = obtener_precios(productos, buscar_producto)
        except KeyError as error:
            print(f"Error: {error}")
        else:
            print(f"El precio de su producto es: {precio}")
            break

def medio_2():
    def convertir_temperatura(celsius):
        if celsius < -273.15:
            raise ValueError("Introduzca un numero mayor a -273,15")
        
        return (celsius*1.8) + 32

    while True:
        try:
            temperatura = float(input("Cambiar temp Cº a Fº: "))
            fahrenheit = convertir_temperatura(temperatura)    
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print(f"Temperatura en Fahrenheit: {fahrenheit}")
            break
def dificil():
    def retirar(saldo, monto):
        if monto < 0:
            raise ValueError("No es posible retirar montos negativos")
        if monto == 0:
            raise ValueError("No se selecciono ningun monto")
        if monto > saldo:
            raise ValueError("No se puede retirar mas del saldo")
        
        return saldo - monto
    saldo = 5000
    while True:
        try:
            accion = int(input("Que accion desea hacer hoy?: \nVer saldo: 1 \nRetirar Saldo: 2 \nSalir: 3 \n"))
        except ValueError:
            print("Escriba una opcion valida")
            continue
        else:
            if accion < 1 or accion > 3:
                print("Esa opcion no existe")
            elif accion == 1:
                print(f"Su saldo es: {saldo}")
            elif accion == 2:
                try:
                    monto = int(input("Cuanto saldo desea retirar"))
                except ValueError:
                    print("Escriba un saldo en numeros")
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
