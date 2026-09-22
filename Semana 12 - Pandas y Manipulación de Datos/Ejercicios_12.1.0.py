import pandas as pd


def ejercicio_1():
    datos = {
        "sensor" : ["S01","S02","S03","S04"],
        "temperatura" : [22, 25, 21, 28],
        "presion" : [101, 104, 99, 108]
    }
    df = pd.DataFrame(datos)
    print(f"Filas y columnas: {df.shape}")
    print(f"Columnas: {df.columns}")
    print(f"Tipo de datos: {df.dtypes}")

def ejercicio_2():
    datos = {
        "producto" : ["A", "B", "C", "D"],
        "precio" : [120, 250, 90, 400],
        "stock" : [15, 9 ,30, 4]
    }
    df = pd.DataFrame(datos)
    print(df.info())
    print(df.shape)
    print(df.columns)
    print(df.dtypes)
#ejercicio 3
#Si df.shape devuelve (500, 7), significa que hay 500 filas o observaciones con 7 columnas que pueden ser variables
# si df.columns devuelve Index(['id', 'temperatura', 'presion', 'ciudad', 'estado', 'fecha', 'alarma']) significa que hay 7 variables las cuales no necesariamente deben ser todas numeros
#Por ej ciudad y estado no creo que se deba representar mediante numeros, por lo que cada fila va a tener diferentes tipos de datos, siendo las filas una observacion completa

if __name__ == "__main__":
    ejercicio_2()