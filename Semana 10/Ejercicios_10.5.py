import numpy as np


def muy_facil():
    numeros = np.array([10, 20, 30, 40, 50])   
    correccion = np.array([1, -2, 3, -1, 2])
    valores_corregidos = numeros + correccion
    print(f"corregidos: {valores_corregidos}")
    valores_corregidos += 2
    print(f"corregidos + 2: {valores_corregidos}")

def facil():
    temperaturas = np.array([
        [20, 21, 22, 23],
        [25, 26, 27, 28],
        [30, 31, 32, 33]
    ])
    correccion = np.array([1.5, -1, 0.5, 2])
    temperaturas_corregidas = temperaturas - correccion
    print(f"Temperaturas corregidas: \n{temperaturas_corregidas}")
    print(f"Promedio sensores: {np.mean(temperaturas_corregidas, axis=1)}")
    print(f"Maximo cada sensor: {np.max(temperaturas_corregidas, axis=1)}")
    print(f"Maximo sensores: {np.max(temperaturas_corregidas)}")

def medio():
    sensores = np.array([
        [20, 100, 5],
        [22, 110, 7],
        [25, 130, 9],
        [30, 150, 12],
        [35, 170, 15]
    ])
    correccion = np.array([2, -10, 0.5])
    sensores_corregidos = sensores + correccion
    print(f"promedio de cada variable: {np.mean(sensores_corregidos, axis=0)}")
    print(f"temp mayor a 30: \n{sensores_corregidos[sensores_corregidos[:,0] > 30]}")
    print(f"presion mayor a 120: \n{sensores_corregidos[sensores_corregidos[:,1] > 140]}")
    print(f"temp o vibracion alta: \n{sensores_corregidos[(sensores_corregidos[:,0] > 30) | (sensores_corregidos[:,2] > 8)]}")

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
    mediciones_graduadas = (mediciones + offset) * escala
    print(f"Promedio variables: {np.mean(mediciones_graduadas, axis=0)}")
    print(f"Desviacion variables: {np.std(mediciones_graduadas, axis=0)}")
    alerta = (mediciones_graduadas[:, 0] > 35) | (mediciones_graduadas[:,1] > 160) | (mediciones_graduadas[:,2] > 25)
    print(f"Maquinas en alerta: \n{mediciones_graduadas[alerta]}")
    print(f"Cantidad en alerta: {np.sum(alerta)}")
    print(f"Indice temp mayor: {np.argmax(mediciones_graduadas[:,0])}")
    print(f"Indice presion mayor: {np.argmax(mediciones_graduadas[:,1])}")
if __name__ =="__main__":
    dificil()