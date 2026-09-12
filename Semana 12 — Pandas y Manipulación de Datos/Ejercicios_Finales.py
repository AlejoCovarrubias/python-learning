import pandas as pd


def integracion():
    ventas = pd.DataFrame({
        "producto_id": ["101", "102", "101", "103", "102", None],
        "region": ["Norte", "Norte", "Sur", "Sur", "Sur", "Norte"],
        "cantidad": ["5", "3", "8", "10", "4", "7"],
        "precio": ["1200", "1500", "1200", "2000", None, "1500"]
    })
    print(f"informacion: \n{ventas.info()}")
    print(f"tipos: \n{ventas.dtypes}")
    print(f"columnas: \n{ventas.columns}")
    print(f"nulos: \n{ventas.isna().sum()}")
    print(f"duplicados: {ventas.duplicated().sum()}")
    #No hay duplicados, pero tenemos 2 datos nulos, uno en producto_id y otro en precio, ademas de que el formato de cantidad y precio esta en string, cuando deberia ser numerico
    
    ventas["producto_id"] = ventas["producto_id"].astype("string")
    ventas["cantidad"] = pd.to_numeric(ventas["cantidad"], errors="coerce")
    ventas["precio"] = pd.to_numeric(ventas["precio"], errors="coerce")
    resumen_region = ventas.groupby("region").agg({
        "cantidad" : "sum",
        "precio" : "mean"
    })
    print(resumen_region)
    #Si se calcula el promedio directamente de ventas, no se estaria filtrando por region sino en general de todo
    #Y solo se calcula de los datos validos porque si tomara el dato vacio como uno me daria otro promedio diferente si contara, influyendo al verdadero promedio.

    productos = pd.DataFrame({
        "producto_id": ["101", "102", "103", "104"],
        "producto": ["Tornillo", "Tuerca", "Arandela", "Eje"]
    })
    datos_limpios = ventas.merge(productos, on="producto_id", how="outer")
    print(datos_limpios)
    #El producto 4 al no existir en ventas, no tiene valores en las columnas excepto de la columna producto. La fila de este producto si convendria borrarla

def proyecto():
    ventas = pd.DataFrame({
        "producto_id": ["101", "102", "101", "103", "102", None, "103"],
        "region": ["Norte", "Norte", "Sur", "Sur", "Sur", "Norte", "Sur"],
        "cantidad": ["5", "3", "8", "10", "4", "7", "10"],
        "precio": ["1200", "1500", "1200", None, "1500", "1500", "2000"]
    })
    productos = pd.DataFrame({
        "producto_id": ["101", "102", "103", "104"],
        "producto": ["Tornillo", "Tuerca", "Arandela", "Eje"]
    })
    def diagnostico(datos):
        print(f"informacion: \n{datos.info()}")
        print(f"tipos: \n{datos.dtypes}")
        print(f"columnas: \n{datos.columns}")
        print(f"nulos: \n{datos.isna().sum()}")
        print(f"duplicados: {datos.duplicated().sum()}")
    diagnostico(ventas)

    def limpiar_datos(datos):
        datos = datos.drop_duplicates()
        datos["producto_id"] = datos["producto_id"].astype("string")
        datos["cantidad"] = pd.to_numeric(datos["cantidad"], errors="coerce")
        datos["precio"] = pd.to_numeric(datos["precio"], errors="coerce")
        return datos
    ventas = limpiar_datos(ventas)
    print(ventas)

    def combinar_datos(dataframe1, dataframe2):
        return dataframe1.merge(dataframe2, on="producto_id", how="outer")

    datos_combinados = combinar_datos(ventas, productos)
    diagnostico(datos_combinados)
    datos_combinados = limpiar_datos(datos_combinados)
    datos_combinados = datos_combinados.dropna(subset="region")
    print(datos_combinados)
    def analisis(datos): 
        return {
            "ventas_por_region": datos.groupby("region")["cantidad"].sum(),
            "precio_promedio_por_producto": datos.groupby("producto")["precio"].mean(),
            "maxima_venta_por_producto": datos.groupby("producto")["cantidad"].sum()
        }
    analisis_datos = analisis(datos_combinados)
    print(analisis_datos)
if __name__ == "__main__":
    proyecto()