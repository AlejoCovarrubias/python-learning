def pedir_numeros():
    while True:
        try:
            numero = int(input("numero entre 1 y 10"))
            if numero >= 1 and numero <= 10:
                print(f"tu numero es {numero}")
            else:
                print("Debe ser positivo o mayor a 0.")
        except ValueError:
            print("Entrada inválida.")    

def usuario_contraseña():
    usuario = "admin"
    contraseña = "1234"

    for i in range(3):
        loginUsername = input("Usuario: ").strip().lower()
        loginPassword = input("Contraseña: ")

        if loginUsername == usuario and loginPassword == contraseña:
            print("Welcome sir")
            return
        else:
            print(f"incorrect password, you have {2-i} attemps left")
        print("blocked")
        break

def numeros_operacion():
    while True:
        try:
            numero1 = int(input("Primer numero: "))
            numero2 = int(input("Segundo numero: "))
            operacion = input("Operacion (+, -, *, /) o 'exit' para salir: ").strip().lower()

            if operacion == "exit":
                break

            if operacion == "/":
                if numero2 != 0:
                    print(f"Division: {numero1 / numero2}")
                else:
                    print("No se puede dividir por cero.")
            elif operacion == "+":
                print(f"Suma: {numero1 + numero2}")
            elif operacion == "-":
                print(f"Resta: {numero1 - numero2}")
            elif operacion == "*":
                print(f"Multiplicacion: {numero1 * numero2}")
            else:
                print("Operacion invalida.")

        except ValueError:
            print("Entrada invalida. Debes ingresar numeros enteros.")

def edad():
    while True:
            try:
                edad = int(input("edad: "))

                if edad < 0:
                    print("edad invalida, numero negativo")
                elif edad > 0 and edad < 18:
                    print("eres menor")
                elif edad > 18 and edad < 60:
                    print("eres adulto")
                elif edad > 60:
                    print("eres mayor")
            except ValueError:
                print("edad invalida. Ingresar numeros enteros")

                    
def notas():
    notas = []
    while True:
        clasificacion = input("notas del alumno: ('salir' para salir)")

        if clasificacion == "salir":
                break
        try:
            clasificacion = int(clasificacion)

        except ValueError:
            print("entrada invalida")
            continue
        
        if clasificacion < 0 or clasificacion > 10:
            print("Nota no dentro del rango admitido") 
            
        elif clasificacion >= 0 and clasificacion <= 10:
            notas.append(clasificacion)
            print("Nota añadida")
        
    if len(notas)> 0:
        promedio = sum(notas) / len(notas)
        print(f"promedio del alumno: {promedio}")
    else:
        print("no hay notas")
        
if __name__ == "__main__":
    notas()                  