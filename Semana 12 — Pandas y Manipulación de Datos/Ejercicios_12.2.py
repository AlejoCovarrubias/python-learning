import pandas as pd

def ejercicio_1():
    datos = {
        "sector": [
            "Mecanizado",
            "Ensamblaje",
            "Mecanizado",
            "Calidad",
            "Ensamblaje",
                "Mecanizado"
        ],
        "produccion": [120, 90, 135, 80, 100, 125],
        "defectos": [4, 7, 3, 2, 6, 5]
    }

    df = pd.DataFrame(datos)

    promedio_produccion = df.groupby("sector")["produccion"].mean()

    maxima_produccion = df.groupby("sector")["produccion"].max()

    promedio_defectos = df.groupby("sector")["defectos"].mean()

    resumen = df.groupby("sector").agg({
        "produccion": ["mean", "max"],
        "defectos": "mean"
    })
    print(resumen)
    #La diferencia entre apicar .mean directo a la columna y hacerlo mediante groupby es que con .mean consigo un solo promedio en general de todo.
    #Mientras que con groupby separo los promedios por grupos o en este caso por sector

def ejercicio_2():
    ventas = pd.DataFrame({
        "producto": [
            "A",
            "B",
            "A",
            "C",
            "B",
            "A",
            "C",
            "B"
        ],
        "region": [
            "Norte",
            "Norte",
            "Sur",
            "Sur",
            "Norte",
            "Norte",
            "Sur",
            "Sur"
        ],
        "cantidad": [10, 5, 8, 12, 7, 15, 9, 6],
        "importe": [1000, 750, 800, 1800, 1050, 1500, 1350, 900]
    })
    #2 maneras de hacerlo: con varios groupby o con 1 agg. Conviene mucho mas hacerlo con 1 agg ya que es mas claro y sencillo que tener muchos groupby
    total_cantidad_producto = ventas.groupby("producto")["cantidad"].sum()
    total_importe_producto = ventas.groupby("producto")["importe"].sum()
    promedio_importe_producto = ventas.groupby("producto")["importe"].mean()

    resumen_producto = ventas.groupby("producto").agg({
        "cantidad": "sum",
        "importe": ["sum", "mean"]
    })
    print(resumen_producto)

    total_cantidad_region = ventas.groupby("region")["cantidad"].sum()
    importe_maximo_region = ventas.groupby("region")["importe"].max()

    resumen_region = ventas.groupby("region").agg({
        "cantidad": "sum",
        "importe": "max"
    })
    print(resumen_region)

def ejercicio_3():
    ventas = pd.DataFrame({
        "producto_id": [101, 102, 103, 101, 102],
        "cantidad": [5, 3, 8, 2, 4]
    })

    productos = pd.DataFrame({
        "producto_id": [101, 102, 103],
        "nombre": ["Tornillo", "Tuerca", "Arandela"],
        "precio": [100, 150, 80]
    })

    resultado = ventas.merge(
        productos,
        on="producto_id", #A partir de esta columna se juntan los dataframe
        how="outer"
    )
    print(resultado) #no sale el producto 104 xq no existe directamente

def ejercicio_4():
    ventas = pd.DataFrame({
        "producto_id": [101, 102, 103, 101, 102],
        "cantidad": [5, 3, 8, 2, 4]
    })

    productos = pd.DataFrame({
        "producto_id": [101, 102, 103, 104],
        "nombre": ["Tornillo", "Tuerca", "Arandela", "Rodamiento"],
        "precio": [100, 150, 80, 500]
    })
    inner = ventas.merge(productos, on="producto_id", how="inner")

    left = ventas.merge(productos, on="producto_id", how="left")

    right = ventas.merge(productos, on="producto_id", how="right")

    outer = ventas.merge(productos, on="producto_id", how="outer")
    print(inner)
    print(right)
    print(left)
    print(outer)

def ejercicio_5():
    ventas = pd.DataFrame({
        "producto_id": [101, 102, 101, 103, 102, 101],
        "region": ["Norte", "Norte", "Sur", "Sur", "Sur", "Norte"],
        "cantidad": [5, 3, 8, 10, 4, 7]
    })

    productos = pd.DataFrame({
        "producto_id": [101, 102, 103],
        "producto": ["Tornillo", "Tuerca", "Arandela"],
        "precio": [100, 150, 80]
    })
    datos_limpios = ventas.merge(productos, on="producto_id", how="left")
    importe = datos_limpios["cantidad"] * datos_limpios["precio"]
    datos_limpios["importe"] = importe
    ventas_por_region = datos_limpios.groupby("region").agg({
        "cantidad": "sum",
        "importe": "sum"
    })
    ventas_por_productos = datos_limpios.groupby("producto").agg({
            "cantidad": "sum",
            "importe": "sum"
        })
    ventas_por_producto_region = datos_limpios.groupby(["producto", "region"]).agg({
        "cantidad": "sum",
        "importe": "sum"
    })
    print(ventas_por_region)
    print(ventas_por_productos)
    print(ventas_por_producto_region)

if __name__ == "__main__":
    ejercicio_5()
