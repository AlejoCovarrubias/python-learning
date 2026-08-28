import numpy as np


def ejercicio_1():
    A = np.array([
        [2, 0],
        [0, 4]
    ])
    
    v = np.array([3, 5]) 

    resultado = A @ v #2*3 + 0*3, 0*5+4*5
    print(resultado)

def ejercicio_2():
    A = np.array([
        [3, 1],
        [1, 2]
    ])

    b = np.array([9, 8])
    print(f"Solucion: {np.linalg.solve(A, b)}") #X=2 Y=3
    #3*2 + 3 = 9
    #2 + 3*2 = 8
def ejercicio_3():
    A = np.array([
    [2, 0],
    [0, 5]
    ])
    v1 = np.array([1, 0]) #va a dar (2,0) eigenvalue 2 siendo eigenvector
    v2 = np.array([0, 1]) #va a dar (0, 5) eigenvalue 5 siendo eigenvector
    v3 = np.array([1, 1]) #No va a ser eigenvector porque trata de buscar un escalar que de 2 y a la vez de 5 con el mismo numero
    print(A@v1)
    print(A@v2)
    print(A@v3)
def ejercicio_4():
    A = np.array([
        [2, 1],
        [3, 4]
    ])

    b = np.array([10, 20])
    #2x + y = 10
    #3x + 4y = 20

    resultado = np.linalg.solve(A, b) #b, A no iria, esta al revez, intenta con 10 y 20 dar 4 resultados, A seria los coeficientes que acompañan a las incógnitas, y B el valor

    print(resultado)

if __name__ == "__main__":
    ejercicio_4()