import numpy as np

maquinas = np.array([
    [72, 120, 8, 95],
    [85, 150, 12, 88],
    [68, 110, 6, 92],
    [91, 180, 18, 75],
    [77, 140, 10, 90],
    [95, 200, 22, 70]
])
#parte 3 y 4 aca porque se utiliza despues para parte 5 en adelante
offset = np.array([1.5, -5, 0.5, 0])
escala = np.array([1.05, 0.98, 1.1, 1])
pesos = np.array([0.4, 0.25, 0.25, -0.1])

sensores_corregidos = (maquinas + offset) * escala
indice_de_riesgo = np.dot(sensores_corregidos, pesos)
riesgo = indice_de_riesgo > 50
def parte_1():
    filas, columnas = maquinas.shape

    n_maquinas = filas
    n_variables = columnas

    print(f"Cantidad de maquinas = {n_maquinas}")
    print(f"Cantidad de variables = {n_variables}")
    print(f"Forma: {maquinas.shape}")
    print(f"Dimensiones: {maquinas.ndim}")

def parte_2():
    print(f"temperatura promedio: {np.mean(maquinas[:,0])}")
    print(f"presión promedio: {np.mean(maquinas[:,1])}")
    print(f"vibración promedio: {np.mean(maquinas[:,2])}")
    print(f"eficiencia promedio: {np.mean(maquinas[:,3])}")

    print(f"temperatura máxima: {np.max(maquinas[:,0])}")
    print(f"temperatura mínima: {np.min(maquinas[:,0])}")
    print(f"eficiencia máxima: {np.max(maquinas[:,3])}")
    print(f"eficiencia mínima: {np.min(maquinas[:,3])}")

def parte_5():
    riesgo_maximo = np.max(indice_de_riesgo)
    print(f"Riesgo maximo: {riesgo_maximo}")
    print(f"Riesgo minimo: {np.min(indice_de_riesgo)}")
    print(f"Maquina con riesgo maximo: \n{np.argmax(indice_de_riesgo)}")
    
    print(f"Maquinas en riesgo: \n{sensores_corregidos[riesgo]}")
    print(f"Cantidad en riesgo: {np.sum(riesgo)}")

def parte_6():
    print(f"M con temp superiores a 80: \n{sensores_corregidos[sensores_corregidos[:,0] > 80]}")
    print(f"M con temp entre 70 y 90: \n{sensores_corregidos[(sensores_corregidos[:,0] > 70) & (sensores_corregidos[:,0] < 90)]}")
    alerta = (sensores_corregidos[:,0] > 80) & (sensores_corregidos[:,2] > 15)
    print(f"Maquinas en alerta: \n{sensores_corregidos[alerta]}")
    print(f"Indice de las maquinas en alerta: {np.where(alerta)[0]}")

def parte_7():
    alerta_critica = (sensores_corregidos[:,0] > 95) | (sensores_corregidos[:,2] > 20) | (riesgo)
    print(f"Maquinas criticas: \n{sensores_corregidos[alerta_critica]}")
    print(f"Cantidad de maquinas criticas: {np.sum(alerta_critica)}")
    print(f"Indice de las maquinas en alerta critica: {np.where(alerta_critica)}")

#Parte 8
#maquinas.shape = (6, 4)
#offset.shape   = (4,)
#escala.shape   = (4,)
#pesos.shape    = (4,)
#A.¿Por qué: maquinas + offset puede funcionar mediante broadcasting?
#Puede funcionar porque la cantidad de columnas de maquinas coincide con la cantidad de filas que el offset. Logrando asi estirar el vector por asi decirlo y lograr hacer la operacion

#B.¿Por qué: maquinas * escala también puede funcionar?
#Por la misma razon anterior

#C.¿Qué shape esperás obtener de: np.dot(maquinas, pesos)
#Uno de una dimension (6,)

#D.Si hacés: riesgo > 50 ¿qué shape debería tener la máscara?
#El shape del array que se evalua, dando True/False

#E.Si hacés: maquinas[riesgo > 50] ¿qué representa cada fila del resultado?
#En este caso seria la maquina la cual tiene un riesgo > 50, pero en general al establecer un valor de una variable al riesgo, cuando ejecutemos el comando buscara en el array la fila la cual cumpla con las condiciones, sino devuelve []

if __name__ == "__main__":
    parte_7()
