def nivel1():
    datitos = [1,-2,3 ,0]

    def minimo(lista):
        minimo = lista[0]
        for dato in lista:
            if dato < minimo:
                minimo = dato
        return minimo
    
    print(minimo(datitos))

    def buscar_repetidos(lista):
        veces_repetido = 0
        while True:
            try:
                repetido = input("q numero desea revisar si esta repetido?Para salir escriba exit")
                if repetido == "exit":
                    print("Finalizado")
                    break
                repetido = int(repetido)
                for dato in lista:
                    if dato == repetido:
                        veces_repetido += 1
                print(f"Se repetio el nº{repetido} {veces_repetido} veces")
                return veces_repetido
            except:
                print("Error")

def nivel2():
    numeros = [3,5,3,8,5,4,3,2,5,67,8] 
    def eliminar_duplicados(numeros):
    
        for i in range(len(numeros)):

            for j in range(i+1, len(numeros)):

                if numeros[i] == numeros[j]:

                    numeros.pop(j)
                    return eliminar_duplicados(numeros)
                   

    def acomodar_lista(lista):
        for i in range(len(lista)):

            for j in range(len(lista)-1):

                if lista[j] > lista[j+1]:

                    lista[j], lista[j+1] = lista[j+1], lista[j]

    
        return lista
    acomodar_lista(numeros)
    eliminar_duplicados(numeros)
    print(numeros)
    
if __name__ == "__main__":
    nivel2()