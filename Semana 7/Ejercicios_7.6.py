from pathlib import Path
import json

def muy_facil():
    contenido = {
        "nombre": "Alejo",
        "edad": 20,
        "ciudad": "no te importa"
    }
    ruta = Path("Semana 7")/"clase7_6"
    ruta.mkdir(parents=True, exist_ok=True)

    archivo_json = ruta / "persona.json"

    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, indent=4)

    with open(archivo_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        print(datos["nombre"])
        print(datos["edad"])
        print(datos["ciudad"])

def facil_1():
    ruta = Path("Semana 7")/"clase7_6"
    ruta.mkdir(parents=True, exist_ok=True)
    
    archivo_json = ruta / "config.json"

    contenido = {
        "idioma": "es",
        "modo_oscuro": True,
        "volumen": 80,
        "notificaciones": True
    }

    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, indent=4)

    with open(archivo_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for clave, valor in datos.items():  #esto lo busque xq no me salia
            if valor is True:
                datos[clave] = "activado"
            elif valor is False:
                datos[clave] = "desactivado"        
        print(datos)
def facil_2():
    ruta = Path("Semana 7")/"clase7_6"
    ruta.mkdir(parents=True, exist_ok=True)
        
    archivo_json = ruta / "productos.json"

    contenido = [
        { 
            "nombre": "Mouse",
            "precio": 200,
            "stock": 3
        },
        { 
            "nombre": "Teclado",
            "precio": 400,
            "stock": 0
        },
        { 
            "nombre": "Monitor",
            "precio": 700,
            "stock": 1
        }
    ]
    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, indent=4)

    with open(archivo_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        for producto in datos:
            print(producto["nombre"])

def medio_1():
    ruta = Path("Semana 7")/"clase7_6"
    ruta.mkdir(parents=True, exist_ok=True)
        
    archivo_json = ruta / "interfaz.json"    

    contenido =  {
        "usuario": "Alejo",
        "modo_oscuro": False,
        "volumen": 50
    }

    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, indent=4)
    
    with open(archivo_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        print(f"Estos son los datos: {datos}")

        while True:
            try:
                volumen_nuevo = int(input("Que volumen desea establecer: "))
            except ValueError:
                print("Error, formato invalido")
            else:
                if volumen_nuevo < 0 or volumen_nuevo > 100:
                    print("Escriba un volumen dentro del rango 0 a 100")
                else:
                    datos["volumen"] = volumen_nuevo
                    with open(archivo_json, "w", encoding="utf-8") as archivo:
                        json.dump(datos, archivo, indent=4)

                        print("Volumen actualizado correctamente.")
                        break
        print(datos)     

def dificil():
    ruta = Path("Semana 7")/"clase7_6"
    ruta.mkdir(parents=True, exist_ok=True)
            
    archivo_json = ruta / "inventario.json"    

    contenido = [
    {
        "nombre": "Mouse",
        "categoria": "Periféricos",
        "precio": 15000,
        "stock": 25
    },
    {
        "nombre": "Teclado",
        "categoria": "Periféricos",
        "precio": 28000,
        "stock": 12
    },
    {
        "nombre": "Monitor",
        "categoria": "Pantallas",
        "precio": 185000,
        "stock": 0
    },
    {
        "nombre": "Auriculares",
        "categoria": "Audio",
        "precio": 42000,
        "stock": 18
    },
    {
        "nombre": "Notebook",
        "categoria": "Computadoras",
        "precio": 980000,
        "stock": 4
    }
    ]
    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, indent=4)

    with open(archivo_json, "r", encoding="utf-8") as archivo:
        inventario = json.load(archivo)

        total_inventario = 0

        
        
        total_categoria = {}

        for producto in inventario:
            categoria = producto["categoria"]
            total = producto["precio"] * producto["stock"]
            
            if producto["stock"] == 0:
                while True:
                    try:
                        accion_stock = int(input("Sin stock detectado, desea añadir mas?\nSI: 1   NO:2"))
                    except ValueError:
                        print("Ingrese el numero correspondiente a la accion")
                        continue
                    else:
                        if accion_stock == 1:
                            while True:
                                try:
                                    agregar_stock = int(input("\nCuanto stock desea añadir: "))
                                except ValueError:
                                    print("Escriba un formato valido")
                                else:
                                    if agregar_stock < 0:
                                        print("Ingrese un stock positivo")
                                        continue
                                    producto["stock"] = agregar_stock

                                    with open(archivo_json,"w",encoding="utf-8") as archivo:
                                        json.dump(inventario, archivo, indent=4) 
                                        
                                    print("Stock actualizado correctamente")
                                    break

                                    break
                        if accion_stock == 2:
                            print(f"Continuando sin stock de {producto['nombre']}")
                            break
            if categoria not in total_categoria:
                total_categoria[categoria] = 0
            
            total_categoria[categoria] += total

        for producto in inventario:
            total_inventario += producto["precio"] * producto["stock"]

        print(f"Valor total del inventario: ${total_inventario}")
        print(f"Valor total por categoria: ${total_categoria}")

                     

if __name__ == "__main__":
    dificil()