import numpy as np
from scipy import stats


def ejercicio_1():
    datos = np.array([12, 15 ,14, 10 ,19 ,15 ,13])

    media = np.mean(datos)
    mediana = np.median(datos)
    moda = stats.mode
    rango = np.max(datos) - np.min(datos)
    varianza_poblacional = np.var(datos, ddof = 0)
    desviacion_estandar = np.std(datos)

    print(f"Media:{media}")
    print(f"Mediana:{mediana}")
    print(f"Moda:{moda}")
    print(f"Rango:{rango}")
    print(f"Varianza poblacional:{varianza_poblacional}")
    print(f"Desviacion Estandar:{desviacion_estandar}")

def ejercicio_2():
    A = np.array([10, 11, 10 ,12 ,11])
    B = np.array([2, 7, 10 ,13 ,23])
    #va a tener mayor dispercion el B ya que tiene los valores mas dispersados que el A, que estan dentro de
    rango_A = np.max(A) - np.min(A)
    rango_B = np.max(B) - np.min(B)
    desviacion_A = np.std(A)
    desviacion_B = np.std(B)
    print(rango_A)
    print(rango_B)
    print(desviacion_A)
    print(desviacion_B)

if __name__ == "__main__":
    ejercicio_2()
    