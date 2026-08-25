def ejercicio_1(): #casi todos ejercicios en 1
    numeros = [4,7,2,9,5,1,8]
    suma = 0
    mayor = numeros[0]
    mayor_5 = 0
    for i in numeros:
        suma = suma + i
        if i > mayor:
            mayor = i
        if i > 5:
            mayor_5 += 1
    promedio = suma / len(numeros)

    print(suma)
    print(mayor)
    print(promedio)
    print(mayor_5)


def final_mes():
    datos = [45,67,23,89,12,90,56,78,34,65]
    suma = 0
    valor_max = datos[0]
    valor_min = datos [0]

    for i in datos:
        suma = suma + i

        if i > valor_max:
            valor_max = i
        
        if i < valor_min:
            valor_min = i
    
    promedio = suma / len(datos)

    print(f"Cantidad de datos: {len(datos)}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Valor máximo: {valor_max}")
    print(f"Valor mínimo: {valor_min}")

if __name__ == "__main__":
    final_mes()