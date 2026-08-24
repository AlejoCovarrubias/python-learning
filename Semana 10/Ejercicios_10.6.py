import numpy as np


def muy_facil():
    a = np.array([2, 4, 6])
    b = np.array([3, 5, 7])
    print(f"Elemento por elemento: {a*b}")
    print(f"Producto punto: {np.dot(a, b)}")
    #uno multiplica uno por uno y da una matriz, otro multiplica por columna las filas y va sumando un total, dando un escalar

def facil():
    mediciones = np.array([80, 50, 20])
    pesos = np.array([0.5, 0.3, 0.2])

    promedio_normal = np.mean(mediciones)
    promedio_ponderado = np.dot(mediciones, pesos)

    es_mayor = "Promedio Normal" if promedio_normal > promedio_ponderado else "Promedio Ponderado"

    print(f"Promedio normal: {promedio_normal}")
    print(f"Promedio ponderado: {promedio_ponderado}")
    print(f"El mayor valor es el: {es_mayor}")

def medio():
    maquinas = np.array([
        [20, 100, 5],
        [25, 120, 7],
        [30, 150, 9],
        [35, 180, 12],
        [40, 200, 15]
    ])
    pesos = np.array([0.5, 0.3, 0.2])
    indice_ponderado = np.dot(maquinas, pesos)
    print(f"Indice mayor: {np.max(indice_ponderado)}")
    print(f"Indice menor: {np.min(indice_ponderado)}")
    print(f"Indice de la maquina con mayor indice: {np.argmax(indice_ponderado)}")
    print(f"Maquinas con indice mayor a 100: {indice_ponderado[indice_ponderado > 100]}")

def dificil():
    mediciones = np.array([
    [20, 100, 5],
    [22, 110, 7],
    [25, 130, 9],
    [30, 150, 12],
    [35, 170, 15],
    [40, 190, 18]
    ])
    offset = np.array([1.5, -8, 0.5])
    escala = np.array([1.1, 0.95, 2])
    pesos = np.array([0.4, 0.35, 0.25])
    calibracion = (mediciones + offset) * escala
    indice_de_riesgo = np.dot(calibracion, pesos)
    print(f"Riesgo de las maquinas: {indice_de_riesgo}")
    print(f"Riesgo mayor: {np.max(indice_de_riesgo)}")
    print(f"Riesgo menor: {np.min(indice_de_riesgo)}")
    print(f"Indice de la maquina con mayor indice: {np.argmax(indice_de_riesgo)}")
    riesgo = indice_de_riesgo > 60
    print(f"Maquinas en riesgo: \n{calibracion[riesgo]}")
    print(f"Cantidad en riesgo: {np.sum(riesgo)}")
if __name__ == "__main__":
    dificil()