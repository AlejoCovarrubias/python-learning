import numpy as np


def ejercicio_1():
    A = np.array([
        [2, 1],
        [0, 3]
    ])

    B = np.array([
        [4, 2],
        [1, 5]
    ])

    v = np.array([10, 4])

    print(A+B) #suma elemento con elemento

    print(A*B) #multiplica elemento por elemento

    print(A@v) #multiplica fila por columna

    print(np.linalg.norm(v)) #modulo, distancia del vector

def ejercicio_2():
    mediciones = np.array([
        [30, 4],
        [25, 6],
        [40, 3]
    ])
    transformacion = np.array([
        [2,0],
        [0,3]
    ])
    print(mediciones @ transformacion) #si tuviera un 1 en alguna diagonal sumaria el resultado que tiene al duplicado (ej 30*2 + 4*1 = 64) dando otro resultado erroneo

def ejercicio_3():
    A = np.array([
    [1, 2], 
    [0, 1]
    ])

    v = np.array([3, 5])
    #x + 2y = 3
    #y = 5
    print(np.linalg.solve(A, v))

if __name__ == "__main__":
    ejercicio_3()