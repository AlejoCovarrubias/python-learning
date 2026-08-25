def muy_facil_1():
    with open("saludo_semana7_3.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Hola, estoy aprendiendo Python.\n")
        archivo.write("Esta es la semana 7")

def muy_facil_2():
    with open("saludo_semana7_3.txt", "r", encoding="utf-8") as archivo:
        texto = archivo.read()
    print(texto)

def facil_1():
    with open("saludo_semana7_3.txt", "a", encoding="utf-8") as archivo:
        archivo.write("\nEstoy aprendiendo manejo de archivos")

    with open("saludo_semana7_3.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.readlines()
    print(contenido)
    
def facil_2():
    with open("nombres_semana7_3.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Juan\nCarlos\nRuben\nAna maria de los dolores santos\nYo")

    with open("nombres_semana7_3.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
               print(linea.strip())
def medio_1():
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("No se encontró el archivo.")
    else:
        print("Archivo leído correctamente.")
        print(contenido)
def medio_2():
        while True:
            try:
                accion = int(input("Que accion desea realizar: \nAñadir nombre: 1\nVer el archivo: 2\nSalir: 3\n"))
            except ValueError:
                print("\nIntroduzca un numero dentro del rango")
            else:
                if accion == 1:
                    nombre = (input("\nQue nombre desea añadir: "))
                    with open("usuarios_semana7_3.txt", "a", encoding="utf-8") as archivo:
                        archivo.write(nombre + "\n")
                        print("Nombre guardado")
                elif accion == 2:
                    with open("usuarios_semana7_3.txt", "r", encoding="utf-8") as archivo:
                        contenido = archivo.read()
                        print(f"El contenido es: \n{contenido}")
                elif accion == 3:
                    print("\nCerrando menu")
                    break
                else:
                    print("\nIntroduzca un numero dentro del rango")
def desafio():
    contador_lineas = 0
    contador_palabras = 0

    try:
        with open("texto.txt", "r", encoding="utf-8") as archivo_texto:
            for linea in archivo_texto:
                contador_lineas += 1

                for palabra in linea.split():
                    contador_palabras += 1
    except FileNotFoundError:
        print(f"No se encontro el archivo")
    else:
        with open("estadisticas.txt", "w", encoding="utf-8") as archivo_estadistica:
            archivo_estadistica.write(f"Cantidad de lineas: {contador_lineas}\n")
            archivo_estadistica.write(f"Cantidad de palabras: {contador_palabras}\n")
        with open("estadisticas.txt", "r", encoding="utf-8") as archivo_estadistica:
            contenido = archivo_estadistica.read()
        print(contenido)
if __name__ == "__main__":
    desafio()