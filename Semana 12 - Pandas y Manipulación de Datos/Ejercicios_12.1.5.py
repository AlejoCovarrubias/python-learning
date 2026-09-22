import pandas as pd

datos = {
    "sensor": ["S01", "S02", "S03", "S04", "S05", "S06"],
    "temperatura": [18, 27, 32, 24, 35, 29],
    "presion": [98, 103, 101, 96, 110, 99],
    "zona": ["A", "B", "A", "C", "B", "A"]
}
df = pd.DataFrame(datos)
def parte_1():
    print(df[["sensor", "temperatura"]])

def parte_2():
    print(df["temperatura"]) #Con un corchete muestra toda la informacion, el nombre de la columna y los tipos de datos q contiene
    print(df[["temperatura"]]) #Con 2 corchetes muestra la informacion como un dataframe

def parte_3():
    print(f"Sensores con temp mayores a 28: \n{df[df["temperatura"]>28]}")

def parte_4():
    print(df[
        (df["temperatura"] > 25)
        &
        (df["presion"] > 100)])

def parte_5():
    print(df.iloc[3, 1])

def parte_6():
    resultado = df[
        (df["temperatura"] > 25) 
        & #and no se utiliza para series
        (df["presion"] < 100)
    ]
    print(resultado) #sensores con temp superiores a 25 y presiones inferiores a 100
if __name__ == "__main__":
    parte_6()
