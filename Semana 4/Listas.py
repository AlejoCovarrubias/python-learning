def facil():
    datos = [1,2,3,4,5,6,7,8,9,10]

    suma = 0
    pares = 0
    mayor = datos[0]
    menor = datos[0]
    for i in datos:
        suma += i

        if i > mayor:
            mayor = i

        if i < menor:
            menor = i
            
        if i % 2 == 0:
            pares += 1
        
    print(datos)
    print(suma)
    print(mayor)
    print(menor)
    print(pares)


def medio():
    numeros = []
    veces_pedidas = 0
    while veces_pedidas <= 10:
        try:
            pedir_numeros = int(input("Ingrese un numero: "))
            numeros.append(pedir_numeros)

            veces_pedidas += 1
        except:
            print("Vuelva a ingresar un numero valido")

    cuadrados = []
    for i in numeros:
        cuadrados.append(i**2)

    sin_repetidos = set(numeros)
    lista_invertida = []
    for i in numeros[4]:
        lista_invertida.append(i)


    print(f"Los numeros ingresados fueron: {numeros}")
    print(f"Los cuadrados de los numeros ingresados son: {cuadrados}")
    print(f"La lista sin numeros repetidos es: {sin_repetidos}")


#los siguientes ejercicios eran repeticiones o muy simples por lo que sigo con los desafios

def mini_proyecto():
    biblioteca = {}
    def agregar_libro(biblioteca):
        Libro = str(input('\nDiga el nombre del libro: '))
        while True:
            try:
                cantidad_libro = int(input('Diga la cantidad de se libro: '))

                if Libro in biblioteca:
                    biblioteca[Libro] += cantidad_libro
                else:
                    biblioteca[Libro] = cantidad_libro
            except:
                print("Ingrese un numero valido")


    def eliminar_libro(biblioteca):
        while True:
            print('Que libro desea eliminar? Si desea salir escriba 0: ')
    
            borrar_libro = (input())

            if borrar_libro == "0":
                print('Saliendo de eliminar libros')
                break
        
            borrar_libro = str(borrar_libro)
            if borrar_libro in biblioteca:
                del biblioteca[borrar_libro]
            else:
                print("No se encontro el libro deseado")
             
    def encontrar_libro(biblioteca):
        print('\nBienvenido que libro desea ver si hay?')
        while True:
            encontrar_libro = input('Si desea salir escriba 0: ')
            if encontrar_libro == "0":
                print('Saliendo de encontrar libro')
                break
            
            if encontrar_libro in biblioteca:
                print(f"Se ha encontrado el libro {encontrar_libro}")
            else:
                print("No se encontro el libro deseado")    

    def mostrar_datos(biblioteca):
        for libro, cantidad in biblioteca.items():
            print(libro, "-", cantidad)
    
    def mostrar_cantidad_libros(biblioteca):
        print(f"Se encontró {encontrar_libro}, cantidad: {biblioteca[encontrar_libro]}")
              
    while True:
        try:
            print("\nQue opcion desea utilizar hoy")
            opcion = int(input("1 Agregar libro\n2 Eliminar libro\n3 Encontrar libro\n4 Mostrar libros\n5 Mostrar cantidad de libros\n6 Salir\n"))

            if opcion == 1:
                agregar_libro(biblioteca)
            elif opcion == 2:
                eliminar_libro(biblioteca)
            elif opcion == 3:
                encontrar_libro(biblioteca)
            elif opcion == 4:
                mostrar_datos(biblioteca)
            elif opcion == 5:
                mostrar_cantidad_libros(biblioteca)
            elif opcion == 6:
                print("Saliendo de biblioteca")
                break
            else:
                print("Introduzca una opcion valida")
                continue
        except:
            print("Debe ingresar un número")

if __name__ == "__main__":
    mini_proyecto()