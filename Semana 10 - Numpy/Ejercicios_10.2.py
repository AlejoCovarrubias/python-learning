import numpy as np
def muy_facil():
    lista_a = np.arange(0, 10)
    lista_b = np.zeros((3, 4))
    lista_c = np.ones((2, 5))
    lista_d = np.linspace(0, 100, 8)

    print(lista_a)
    print(lista_b)
    print(lista_c)
    print(lista_d)

def facil():
    mediciones = np.array([20.5, 31.0, 42.0, 49.5, 61.5])
    correciones = np.array([+0.5, -1.0, +2.0, -0.5, +1.5])

    mediciones_corregidas = mediciones - correciones

    print(mediciones_corregidas)

def medio():
    temperaturas = np.array([
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34],
    [40, 41, 42, 43, 44],
    [50, 51, 52, 53, 54]
    ]) 

    factor_de_correcion = np.array([1, -2, 0.5, 2, -1])

    print(f"Dimensiones temperaturas: {temperaturas.shape}")
    print(f"Dimensiones factor: {factor_de_correcion.shape}")

    temperaturas_corregidas = temperaturas + factor_de_correcion

    print(f"Temperaturas corregidas: {temperaturas_corregidas}")

    print(f"Promedio x maquina: {np.mean(temperaturas_corregidas, axis = 1)}")
    print(f"Promedio x medicion: {np.mean(temperaturas_corregidas, axis = 0)}")
    
if __name__ == "__main__":
    medio()