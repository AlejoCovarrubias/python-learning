import pandas as pd

df = pd.DataFrame({
        "sensor": ["S01", "S02", "S03", "S03", "S04"],
        "temperatura": ["22.5", None, "21.0", "21.0", "error"],
        "presion": [101, 104, None, 99, 108],
        "fecha": [
            "2026-08-01",
            "2026-08-01",
            "2026-08-02",
            "2026-08-02",
            None
        ]
    })
def ejercicio_1():
    
    print(df.info())
    print(df.isna().sum()) #temperatura, presion y fecha tienen un valor nulo
    print(f"duplicados: {df.duplicated().sum()}")
    print(df.dtypes)
    #Los errores que hay son: Las temperaturas deberian ser numericas, ademas de haber un valor nulo, hay un valor str 
    #Fecha aparte de estar en texto, deberia de configurarlo con df.to_datatime ya que son fechas

def ejercicio_2():
    df = pd.DataFrame({
        "sensor": ["S01", "S02", "S03", "S03", "S04"],
        "temperatura": ["22.5", None, "21.0", "21.0", "error"],
        "presion": [101, 104, None, 99, 108],
        "fecha": [
            "2026-08-01",
            "2026-08-01",
            "2026-08-02",
            "2026-08-02",
            None
        ]
    })
    df["temperatura"] = pd.to_numeric(df["temperatura"], errors="coerce") 
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    print(f"Duplicados: {df.duplicated().sum()}")
    df = df.drop_duplicates()
    print(df.dtypes)
    print(df.info())
    print(df.isna().sum())
    print(df)
def ejercicio_3():
    ventas = pd.DataFrame({
        "producto_id": ["101", "102", "101", "103", "102", None],
        "region": ["Norte", "Norte", "Sur", "Sur", "Sur", "Norte"],
        "cantidad": ["5", "3", "8", "10", "4", "7"],
        "precio_unitario": ["1000", "1500", "1000", "2000", "1500", "error"]
    })
    ventas["cantidad"] = pd.to_numeric(ventas["cantidad"], errors="coerce")
    ventas["precio_unitario"] = pd.to_numeric(ventas["precio_unitario"], errors="coerce")
    ventas = ventas.dropna(subset=["producto_id"])
    print(ventas.duplicated().sum())
    print(ventas)
    
if __name__ == "__main__":
    ejercicio_3()
    