import numpy as np


def muy_facil():
    temperaturas = np.array([18, 21, 24, 27, 30, 33])
    print(temperaturas[0])
    print(temperaturas[-1])
    print(temperaturas[0: 3])
    print(temperaturas[-3:])
    print(temperaturas[[1, 3, 5]])

def facil():
    velocidades = np.array([45, 62, 78, 55, 91, 67, 102, 58])
    print(f"Velocidades mayores a 70: {velocidades[velocidades > 70]}")
    print(f"Velocidades entre 50 y 80: {velocidades[(velocidades >= 50) & (velocidades <= 80)]}")
    print(f"Velocidades mayores a 90: {np.sum(velocidades > 90)}")
    velocidades[velocidades > 90] = 90 
    print(velocidades)

def medio():
    sensores = np.array([
        [20, 21, 22, 23, 24],
        [30, 31, 32, 33, 34],
        [40, 41, 42, 43, 44],
        [50, 51, 52, 53, 54]
    ])
    print(f"sensor 3: {sensores[2]}")
    print(f"segunda medicion de todos: {sensores[:, 1]}")
    print(f"bloque S2 y 3, mediciones 2-3-4: \n{sensores[1:3, 1:4]}")
    promedio_sensor = np.mean(sensores, axis= 1)
    print(f"Promedio por sensor : {promedio_sensor}")
    print(f"Sensor promedio mayor a 30 :\n{sensores[promedio_sensor > 30]}")

def dificil():
        #temp-presion-vibracion
    maquinas = np.array([
        [65.2, 21, 14],  
        [68.0, 123, 8], 
        [85.5, 38, 50], 
        [64.1, 520, 11], 
        [66.8, 222, 3], 
        [71.3, 12, 20],  
        [63.9, 221, 12],  
        [92.1, 441, 8]
    ])
    print(f"M con temp mayores a 80: \n{maquinas[maquinas[:,0] > 80]}")
    print(f"M con presion mayores a 120: \n{maquinas[maquinas[:,1] > 120]}")
    print(f"M con vibracion mayores a 10: \n{maquinas[maquinas[:,2] > 10]}")
    print(f"M con temp y vibracion alta: \n{maquinas[(maquinas[:,0] > 80) & (maquinas[:,2] > 10)]}")
    print(f"M con temp o presion alta: \n{maquinas[(maquinas[:,0] > 80) | (maquinas[:,1] > 120)]}")

    alerta = (maquinas[:, 0] > 80) | (maquinas[:,1] > 120) | (maquinas[:,2] > 10)
    print(f"clasificacion: {np.where(alerta, "ALERTA", "NORMAL")}")
    print(F"Maquinas en alerta: \n{maquinas[alerta]}")
    print(F"cantidad en alerta: {np.sum(alerta)}")

if __name__ == "__main__":
    facil()