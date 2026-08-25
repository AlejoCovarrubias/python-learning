def prueba_1():
    suma = 0
    mayores = 0

    for i in range(5):
        numero = int(input("5 numeros: "))

        suma += numero

        if numero > 10:
            contador_mayores += 1

    promedio = suma / 5

def prueba_2():
    suma = 0
    cantidad = 0
    mayor = None
    while True:
        numero = (input("escribi numeros:  (Terminar con salir)")).strip().lower()
    
        if numero == "salir":
            break

        try:
            numero_int = int(numero)

        except ValueError:
            print("Invalid input. Please enter a number.")
        continue

    suma += numero_int
    cantidad += 1

    if mayor is None or numero_int > mayor:
        mayor = numero_int
    if cantidad > 0:
        promedio = suma / cantidad
        print(promedio)
    else:
        print("Cantidad nula")
    print(suma)
    print(cantidad)
    print(mayor)

def prueba_3():
    suma_positivos = 0
    suma_negativos = 0
    cantidad_positivos = 0
    cantidad_negativos = 0

    while True:
        numero = (input("escribi numeros:  (Terminar con 0)"))
    
        try:
            numero_int = int(numero)
            
        except ValueError:
            print("Numero invalido, intenta de nuevo")
            continue
        if numero_int == 0:
            break

        if numero_int > 0:
            suma_positivos += numero_int
            cantidad_positivos += 1
        elif numero_int < 0:
            suma_negativos += numero_int
            cantidad_negativos += 1

    print(f"positivos: {suma_positivos, cantidad_positivos}, negativos: {suma_negativos, cantidad_negativos}")

def prueba_4():
    total_ventas = 0
    cantidad_ventas = 0
    venta_promedio = 0
    venta_alta = None
    venta_baja = None

    while True:
        ventas = input("precio venta: .(terminar con 0)")

        try:
            ventas_int = int(ventas)

        except ValueError:
            print("Venta invalida, intentar de vuelta")
            continue

        if ventas_int == 0:
            break

        total_ventas += ventas_int
        cantidad_ventas += 1

        if venta_alta is None or ventas_int > venta_alta:
            venta_alta = ventas_int

        if venta_baja is None or ventas_int < venta_baja:
            venta_baja = ventas_int

    if cantidad_ventas > 0:
        venta_promedio = total_ventas / cantidad_ventas
        print("Total:", total_ventas)
        print("Cantidad:", cantidad_ventas)
        print("Promedio:", venta_promedio)
        print("Venta más alta:", venta_alta)
        print("Venta más baja:", venta_baja)
    else:
        print("No se ingresaron ventas")

if __name__ == "__main__":
    prueba_4()