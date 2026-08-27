import numpy as np


def muy_facil():
    A = np.array([
        [4, 8, 12],
        [2, 6, 10]
    ])
    filas, columnas = A.shape
    print(f"Shape: {A.shape}")
    print(f"Filas: {filas}")
    print(f"Columnas: {columnas}")
    print(A[0, 2])  #Devuelve 12
    print(A[1, 1])  #Devuelve 6

def facil():
    A = np.array([
        [1, 2],
        [3, 4]
    ])

    B = np.array([
        [2, 5],
        [1, 3]
    ])
    print([[1*2, 2*5],
           [3*1, 4*3]])
    print(f"Elemento elemento: {A*B}")
    print([[(1*2)+(2*1), (1*5)+(2*3)],
           [(3*2)+(4*1), (3*5)+(4*3)]])
    print(f"P punto: {np.dot(A,B)}")


#A (2x3)(3x5) es posible, concuerdan dimensiones internas (3=3) dando como resultado una (2x5)
#B (4x2)(2x1) es posible, concuerdan dimensiones internas (2=2) dando como resultado una (4x1)
#C (3x4)(2x3) no es posible, no concuerdan dimensiones internas (4!=2)
#D (5x1)(1x5) es posible, concuerdan dimensiones internas (1=1) dando como resultado una (5x5)

def dificil():
    V = np.array([[10],
                  [20],
                  [30]])
    A = np.array([[2, 0, 0],
                  [0, 0.5, 0],
                  [0, 0, 3]])
    print(V.ndim)
    print(A.ndim)
    print(V.shape)
    print(A.shape)
    #No concuerdan las dimensiones internas (1!=3) por lo tanto no se puede realizar el producto punto
if __name__ == "__main__":
    dificil()    
    