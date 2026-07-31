def corregir1():
    lista=[1,2,3,4]           #LISTA ORIGINAL: lista=[1,2,3]

    print(lista[3])           #No existia el cuarto elemento en esa lista

def corregir2():
    while True:
        try:
            numero=input("Escriba un numero, para salir escriba exit")          #Variable inicial: numero=input()
            if numero == "exit":
                print("Finalizando")
                break
            numero
            resultado=numero+10
            print(resultado)
        except:
            print("Ingrese un resultado valido")
def encontrar_error1():
    def maximo(lista):
        mayor= lista[0]         #Valor inicial: mayor=0

        for numero in lista:
            if numero>mayor:
                mayor=numero
        return mayor
    
def encontrar_error2():
    biblioteca={}

    def agregar(biblioteca):
        Libro = str(input('\nDiga el nombre del libro: '))
        while True:
            try:
                cantidad_libro = int(input('Diga la cantidad del libro: '))

                if Libro in biblioteca:
                    biblioteca[Libro] += cantidad_libro
                else:
                    biblioteca[Libro] = cantidad_libro
                break
            except:
                print("Ingrese un numero valido")

def mini_proyecto_semana_6():

    inventario = {
        "teclado":5,
        "mouse":10
    }

    def agregar_producto(inventario):
        producto = str(input("Que elemento desea añadir al inventario? "))
        while True:
            try:
                cantidad_producto = int(input(f"Cantidad de {producto}?: "))
                if cantidad_producto > 0:
                    if producto in inventario:
                        inventario[producto] += cantidad_producto
                    else:
                        inventario[producto] = cantidad_producto
                    break
                else:
                    print("No se puede añadir libros con cantidades negativas o iguales a 0")
            except:
                print("Ingrese una cantidad valida")
    def eliminar_producto(inventario):
        while True:
            eliminar_producto = str(input("Que producto desea eliminar?. Si desea salir escriba exit: "))
            if eliminar_producto == "exit":
                print("Saliendo de eliminar producto")
                break
                
            if eliminar_producto in inventario:
                print(f"\nSe ha eliminado {eliminar_producto} del inventario")
                del inventario[eliminar_producto]
                break
            else:
                print("No se encontro el producto en el inventario")
            
    def buscar_producto(inventario):
        while True:
            try:
                buscar_producto = str(input("Que producto desea buscar hoy?. Si desea salir escriba exit:"))
                if buscar_producto == "exit":
                    print("Saliendo de buscar productos...")
                    break
                if buscar_producto in inventario:
                    print(f"\n{buscar_producto} esta disponible en el inventario y hay {inventario[buscar_producto]}")
                else:
                    print("\nNo se encontro ese articulo en el inventario")
            except:
                print("Ingreso un dato invalido, vuelva a intentarlo")

    def mostrar_inventario(inventario):
        for producto, cantidad_producto in inventario.items():
            print(f"\n{producto} --- {cantidad_producto}")

    print("Bienvenido al inventario, que desea hacer hoy")
    while True:
        try:
            opcion = int(input("\nAgregar producto: 1"
            "\nEliminar producto: 2"
            "\nBuscar producto: 3"
            "\nMostrar inventario: 4"
            "\nSalir: 5\n"))
            if opcion == 1:
                agregar_producto(inventario)
            elif opcion == 2:
                eliminar_producto(inventario)
            elif opcion == 3:
                buscar_producto(inventario)
            elif opcion == 4:
                mostrar_inventario(inventario)
            elif opcion == 5:
                print("Saliendo del inventario")
                break
            else:
                print("Introduzca una opcion valida")
                continue
        except:
            print("Debe ingresar un número")
        


def desafio():
    usuarios = {

    }
    def crear_usuario(usuarios):
        nuevo_usuario = str(input("Ingrese el nombre para su nueva cuenta: "))
        while True:
            try:
                nuevo_saldo = int(input("Ingrese la cantidad de saldo: "))
                if nuevo_saldo > 0:
                    if nuevo_usuario in usuarios:
                        print("Saldo agregado")
                        usuarios[nuevo_usuario] += nuevo_saldo
                    else:
                        print("Saldo agregado")
                        usuarios[nuevo_usuario] = nuevo_saldo
                    break
                else:
                    print("No se puede ingresar saldo negativo")
            except:
                print("Ingrese un numero valido")

    def depositar(usuarios):
        while True:
            cuenta_existente = str(input("A que cuenta desea añadirle saldo?: "))

            if cuenta_existente in usuarios:
                print(f"Bienvenido {cuenta_existente}, cuanto dinero va a depositar?: ")
                while True:
                    try:
                        monto_depositar = int(input("Ingrese el monto a depositar"))
                        if monto_depositar > 0:
                            usuarios[cuenta_existente] += monto_depositar
                            print(f"\nSe ha añadido {monto_depositar} a su cuenta")
                        else:
                            print("Ingrese un monto mayor a 0")
                        break
                    except ValueError:
                        print("Ingrese un monto valido")
            else:
                print("Esa cuenta no esta registrada, vuelva a intertarlo")
            break
    def retirar_saldo(usuarios):
        while True:
            cuenta_existente_2 = str(input("\nA que cuenta desea retirarle saldo?: "))
            
            if cuenta_existente_2 in usuarios:
                while True:
                    try:
                        saldo_para_retirar = int(input("\nCuanto saldo desea retirar?: "))
                        if saldo_para_retirar <= usuarios[cuenta_existente_2]["saldo"]:
                            usuarios[cuenta_existente_2]["saldo"] -= saldo_para_retirar

                            print("Retiro realizado correctamente")
                            break
                        else:
                            print("Saldo insuficiente")

                    except ValueError:
                        print("Ingrese un número válido")
                break
            else:       
                print("La cuenta no existe")
    def transferir_saldo(usuarios):
        while True:
            try:
                existe_cuenta_1 = str(input("Ingresar a cuenta: "))
                if existe_cuenta_1 in usuarios:
                    while True:
                        try:
                            existe_cuenta_2 = str("Cuenta a la cual vas a transferir?: ")
                            if existe_cuenta_2 in usuarios:
                                while True:
                                    try:
                                        monto_a_transferir = int(input(f"Ingrese el monto para transferirle a {existe_cuenta_2}: "))

                                        if monto_a_transferir <= usuarios[existe_cuenta_1]["Saldo"] and monto_a_transferir > 0:
                                            usuarios[existe_cuenta_1]["saldo"] -= monto_a_transferir
                                            usuarios[existe_cuenta_2]["saldo"] += monto_a_transferir
                                            break
                                        else:
                                            print("Saldo para transferir insuficiente")
                                    except ValueError:
                                        print("Ingrese un monto valido")
                                break
                            else:
                                print("Ingrese una cuenta que existe en usuarios")
                        except ValueError:
                            print("ingrese una cuenta que exista en los usuarios")
                    break
                else:
                    print("Esa cuenta no existe en usuarios")
            except ValueError:
                print("Ingrese una cuenta valida")        

if __name__ == "__main__":
    mini_proyecto_semana_6()