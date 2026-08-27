import numpy as np


def ejercicio_1():
    v = np.array([6, 8])
    print(f"Suma: {np.sum(v)}")
    print(f"Norma: {np.linalg.norm(v)}")
    print(f"Multiplicado por 3: {v*3}")

def ejercicio_2():
    maquina = np.array([80, 150, 10, 90])
    referencia = np.array([75, 140, 8, 95])

    diferencia = maquina - referencia
    print(f"Diferencia: {diferencia} ") #diferencia de cada componente del vector
    print(f"Norma de la dif: {np.linalg.norm(diferencia)}") #distancia entre vectores
    print(f"Producto punto: {np.dot(maquina, referencia)}") #es una suma ponderada entre los componentes correspondientes de ambos vectores

def ejercicio_3():
    a = np.array([2, 4, 6])
    b = np.array([1, 3, 5])

    resultado = a @ b #Equivale al np.dot(a, b), es decir, el producto punto produciendo un escalar
    print(resultado)
def ejercicio_4():
    temperaturas = np.array([20, 22, 24])
    pesos = np.array([0.2, 0.5])
    print(temperaturas.shape)
    print(pesos.shape)
    #Aqui esta el error, no concuerdan las dimensiones
    #resultado = temperaturas @ pesos
    pesos_arreglado = np.array([0.2, 0.5, 0.3])
    print(np.dot(temperaturas, pesos_arreglado))

def ejercicio_5():
    medicion_1 = np.array([10, 20, 30, 40])
    medicion_2 = np.array([12, 18, 31, 37])
    diferencia = medicion_2 - medicion_1
    print(f"Magnitud: {np.linalg.norm(diferencia)}")
    #Elegi la norma porque da la magnitud o la distancia que tiene un vector al hacer la raiz de la suma de sus componentes al cuadrado
    
if __name__ =="__main__":
    ejercicio_5()
