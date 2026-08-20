import numpy as np
def muy_facil():
    velocidades = np.array([60, 65, 70, 68, 72])
    print(velocidades)
    print(velocidades.shape)
    print(velocidades.ndim)
    velocidades_mas_5 = velocidades + 5
    print(velocidades_mas_5)

def facil():
    temperaturas_con_error = np.array([18.5, 19.2, 20.1, 21.7, 22.4])
    temperaturas_corregidas = temperaturas_con_error - 1.3
    print(temperaturas_corregidas)
def medio():
    Sensor_A = np.array([20, 21, 23, 25, 24])
    Sensor_B = np.array([22, 20, 24, 26, 23])

    Promedio_sensores = (Sensor_A + Sensor_B) / 2
    print("Promedios:", Promedio_sensores)
    print("Promedio general:", np.mean(Promedio_sensores))
    print("Valor máximo:", np.max(Promedio_sensores))
    print("Valor mínimo:", np.min(Promedio_sensores))
def dificil():
    maquina = np.array([
        [20, 30, 35, 40, 35, 24],
        [1, 2, 6, 33, 4, 5],
        [10, 20, 30, 40, 50, 60],
        [0, 0, 0, 0, 0, 1]
    ])
    print(f"Shape: {maquina.shape}")
    print(f"Mediciones sensor 2: {maquina[1]}")
    print(f"Medicion tercera sensores: {maquina[:, 2]}")
    print(f"Promedio cada sensor: {np.mean(maquina, axis=1)}")
    print(f"Promedio mas alto: {np.max(np.mean(maquina, axis=1))}")
    print(f"Medicion mas alto: {np.max(maquina)}")
    
    
    
if __name__ == "__main__":
    dificil()