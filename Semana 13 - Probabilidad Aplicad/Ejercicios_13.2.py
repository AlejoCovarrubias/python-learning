import numpy as np


def ejercicio_1():
    X = np.array([0, 1 ,2, 3])

    P = np.array([0.1, 0.4, 0.3, 0.2])

    E = np.sum(X*P)
    E_elevado2 = np.sum((X**2) * P)

    Var = E_elevado2 - (E)**2

    desviacion = np.sqrt(Var)

    print(E)
    print(E_elevado2)
    print(Var)
    print(desviacion)

def ejercicio_2():
    piezas = 200
    probabilidad = 0.02

    e = piezas * probabilidad
    var = piezas*probabilidad*(1-probabilidad)
    desviacion = np.sqrt(var)

    print(e) #cada 200 piezas se espera 4 piezas defectuosas
    print(var) #que tanto varia la cantidad defectuosas
    print(desviacion) #la cantidad estara defectuosa un 1.98 del promedio, es decir redondeando a 2, entre 2 y 6 piezas defectuosas)

#Dos sensores tienen exactamente la misma probabilidad de detectar correctamente una falla.
#Sin embargo:
#Sensor A produce muchos falsos positivos.
#Sensor B produce pocos falsos positivos.
#Un motor da positivo en ambos sensores.

#No, no sería igual. Sería mayor para el Sensor B.
#P(falla∣positivo)= P(positivo∣falla)*P(falla) / P(positivo)
#​El numerador es igual para ambos pero en el denominador P(positivo) es donde aparece la diferencia:
#P(positivo)= P(positivo∣falla)⋅P(falla) + P(positivo∣no falla)⋅P(no falla)

#en el sensor A el segundo término es grande xq hay muchos falsos positivos por lo que el cociente disminuye.
#en el sensor B el segundo término es chico xq hay pocos falsos positivos por lo que el cociente aumenta.

def ejercicio_4():
    probabilidad_defectuosa = 0.04
    probabilidad_pieza_defectuosa = 0.9
    probabilidad_pieza_no_defectuosa = 0.08

    probabilidad_positivo = probabilidad_pieza_defectuosa * probabilidad_defectuosa + probabilidad_pieza_no_defectuosa * (1 - probabilidad_defectuosa) #la parte de 1-probabilidad lo hice con copilot xq no sabia

    bayes = (probabilidad_pieza_defectuosa * probabilidad_defectuosa) / probabilidad_positivo
    print(bayes)

def ejercicio_5():
    
if __name__ == "__main__":
    ejercicio_4()

