import time
import numpy as np
def muy_facil():
    numeros = np.array([4, 8, 12, 16, 20])
    print(f"Numeros por 3: {numeros * 3}")
    print(f"Numeros dividido 2: {numeros / 2}")
    print(f"Numeros al cuadrados: {np.square(numeros)}")
    print(f"Suma numeros: {np.sum(numeros)}")
    print(f"Promedio: {np.mean(numeros)}")
    print(f"Maximo: {np.max(numeros)}")
    print(f"Minimo: {np.min(numeros)}")

def facil():
    temperaturas = np.array([18.2, 19.5, 21.0, 20.3, 22.1, 23.7, 21.8])
    promedio = np.mean(temperaturas)
    print(f"Promedio: {promedio}")
    print(f"Maxima: {np.max(temperaturas)}")
    print(f"Posicion maxima: {np.argmax(temperaturas)}")
    print(f"Minima: {np.min(temperaturas)}")
    print(f"Posicion minima: {np.argmin(temperaturas)}")
    print(f"Desviacion: {np.std(temperaturas)}")
    print(f"Medicion por encima del promedio: {np.sum(temperaturas > promedio)}")

def medio():
    maquinas = np.array([
        [20, 22, 21, 23],
        [30, 32, 31, 35],
        [25, 24, 26, 27],
        [40, 42, 41, 45],
        [18, 19, 20, 21],
        [35, 36, 34, 37]
    ])
    promedio_maquina = np.mean(maquinas, axis=1)
    print(f"Promedio de cada máquina: {promedio_maquina}")
    print(f"Máximo de cada máquina: {np.max(maquinas, axis=1)}")
    print(f"Mínimo de cada máquina: {np.min(maquinas, axis=1)}")
    print(f"Desviación estándar de cada máquina: {np.std(maquinas, axis=1)}")
    print(f"Número de la máquina con mayor promedio: {np.argmax(promedio_maquina) + 1}")
    print(f"Número de la máquina con menor promedio: {np.argmin(promedio_maquina) + 1}")
    print(F"Promedio de cada momento de medición: {np.mean(maquinas, axis=0)}")
    print(f"Máximo registrado en cada momento de medición: {np.max(maquinas, axis=0)}")

def dificil():
    valores = np.arange(1, 1000001)

    inicio_loop = time.perf_counter()
    resultado_loop = []
    for x in valores:
        resultado_loop.append(x**2 + 3*x - 7)
        
    fin_loop = time.perf_counter()
    tiempo_loop = fin_loop - inicio_loop

    inicio_np = time.perf_counter()

    resultado_np = valores**2 + 3*valores - 7

    fin_np = time.perf_counter()
    tiempo_np = fin_np - inicio_np
    resultado_loop = np.array(resultado_loop)
    print(np.array_equal(resultado_loop, resultado_np))
    print(f"tiempo con loop: {tiempo_loop}")
    print(f"tiempo con numpy: {tiempo_np}")
if __name__ == "__main__":
    dificil()