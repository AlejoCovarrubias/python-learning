import csv
from pathlib import Path
def muy_facil():

    ruta = Path("Semana 7/clase7_5")
    ruta.mkdir(parents=True, exist_ok=True)

    archivo_csv = ruta / "productos_1.csv"


    with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
        campos = ["producto", "precio"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows([
            {"producto": "Mouse", "precio": 200},
            {"producto": "Teclado", "precio": 500},
            {"producto": "Monitor", "precio": 1000}
        ])

    with open(archivo_csv, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        filas = list(lector) #para poder leer 2 veces el csv

        print("Ejercicio 1")
        for fila in filas:
           print(fila) 

        print("Ejercicio 2")
        for fila in filas:
            producto = fila["producto"]
            precio = float(fila["precio"])
            print(f"Producto: {producto} | Precio: {precio}")

def facil_1():
    ruta = Path("Semana 7") / "clase7_5"
    ruta.mkdir(parents=True, exist_ok=True)     

    archivo_csv = ruta / "productos_2.csv"

    with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
        campos = ["producto", "precio", "cantidad"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
         
        escritor.writeheader()

        escritor.writerows([
            {"producto": "Mouse", "precio": 200, "cantidad" : 3},
            {"producto": "Teclado", "precio": 500, "cantidad" : 2},
            {"producto": "Monitor", "precio": 1000, "cantidad" : 1}
        ])  
    with open(archivo_csv, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            producto = fila["producto"]
            precio = float(fila["precio"])
            cantidad = int(fila["cantidad"])

            total = precio * cantidad
            print(f"{producto} → {total}")    

def facil_2():
    ruta = Path("Semana 7") / "clase7_5"
    ruta.mkdir(parents=True, exist_ok=True)

    archivo_csv = ruta / "resumen.csv"

    with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
        campos = ["producto", "total"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows([
            {"producto": "Mouse", "total": 600},
            {"producto": "Teclado", "total": 1000},
            {"producto": "Monitor", "total": 1000}
        ]) 

def medio_1():
    ruta = Path("Semana 7") / "clase7_5"
    ruta.mkdir(parents=True, exist_ok=True)

    archivo_csv = ruta / "productos_3.csv"

    with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
        campos = ["producto", "precio", "cantidad"]
        lector = csv.DictWriter(archivo, fieldnames=campos)

        lector.writeheader()
        lector.writerows([
            {"producto": "Mouse", "precio": 200, "cantidad": 3},
            {"producto": "Teclado", "precio": 500, "cantidad": 2},
            {"producto": "Monitor", "precio": "abc", "cantidad": 1},
            {"producto": "Auriculares", "precio": 150, "cantidad": 4},
            {"producto": "Webcam", "precio": 300, "cantidad": -2},
        ])
    with open(archivo_csv, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for numero_fila, fila in enumerate(lector, start=2):
            try:
                precio = float(fila["precio"])
                cantidad = int(fila["cantidad"])

            except ValueError:
                print(f"Error en la fila {numero_fila}: {fila}")
                print("Formato invalido")
                continue
            else:
                if cantidad < 0:
                    print(f"Error en la fila {numero_fila}: {fila}")
                    print("No puede existir cantidades negativas")
                    continue
def medio_2():
        ruta = Path("Semana 7") / "clase7_5"
        ruta.mkdir(parents=True, exist_ok=True)
    
        archivo_csv = ruta / "productos_4.csv"
        archivo_limpio = ruta / "ventas_limpias.csv"

        with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
            campos = ["producto", "precio", "cantidad"]
            lector = csv.DictWriter(archivo, fieldnames=campos)
    
            lector.writeheader()
            lector.writerows([
                {"producto": "Mouse", "precio": 200, "cantidad": 3},
                {"producto": "Teclado", "precio": "abc", "cantidad": 2},
                {"producto": "Monitor", "precio": 1000, "cantidad": 1},
                {"producto": "Auriculares", "precio": 150, "cantidad": -5},
                {"producto": "Webcam", "precio": 300, "cantidad": 2}, 
            ])      
        with open(archivo_csv, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            with open(archivo_limpio, "w", newline="", encoding="utf-8") as limpio:
                campos = ["producto", "precio", "cantidad"]
                escritor = csv.DictWriter(limpio, fieldnames=campos)

                escritor.writeheader()

                procesadas = 0
                Validas = 0
                Descartadas = 0

                for numero_fila, fila in enumerate(lector, start=2):
                    procesadas += 1

                    try:
                        precio = float(fila["precio"])
                        cantidad = int(fila["cantidad"])

                    except ValueError:
                        Descartadas += 1
                        print(f"Error en la fila {numero_fila}: {fila}")
                        print("Formato invalido")
                        continue

                    if cantidad < 0:
                        Descartadas += 1
                        print(f"Error en la fila {numero_fila}: {fila}")
                        print("No puede existir cantidades negativas")
                        continue

                    Validas += 1
                    escritor.writerow(fila)
            with open(archivo_limpio, "r", newline="", encoding="utf-8") as limpio:
                lector_2 = csv.DictReader(limpio) 
                print("Filas limpias")
                for fila in lector_2:
                    print(fila)
def dificil():
    ruta = Path("Semana 7") / "clase7_5"
    ruta.mkdir(parents=True, exist_ok=True)
        
    archivo_csv = ruta / "productos_5.csv"
    archivo_limpio = ruta / "resumen_categorias.csv"
    
    with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
        campos = ["producto", "categoria", "precio", "cantidad"]
        lector = csv.DictWriter(archivo, fieldnames=campos)
        
        lector.writeheader()
        lector.writerows([
            {"producto": "Mouse", "categoria": "Perifericos", "precio": 200, "cantidad": 3},
            {"producto": "Teclado", "categoria": "Perifericos", "precio": 300, "cantidad": 2},
            {"producto": "Monitor", "categoria": "Hardware", "precio": 1000, "cantidad": 1},
            {"producto": "Webcam", "categoria": "Perifericos", "precio": 300, "cantidad": 4},
            {"producto": "SSD", "categoria": "Hardware", "precio": 800, "cantidad": 2}
        ])      
    with open(archivo_csv, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
    
        with open(archivo_limpio, "w", newline="", encoding="utf-8") as limpio:
            campos = ["categoria", "total"]
            escritor = csv.DictWriter(limpio, fieldnames=campos)
    
            escritor.writeheader()

            total_hardware = 0
            total_perifericos = 0
            for numero_fila, fila in enumerate(lector, start=2):
                try:
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    
                except ValueError: 
                    print(f"Error en la fila {numero_fila}: {fila}")
                    print("Formato invalido")
                    continue
                else:
                    if fila["categoria"] == "Hardware":
                        total_hardware += precio * cantidad
                    elif fila["categoria"] == "Perifericos":
                        total_perifericos += precio * cantidad
            escritor.writerow({
                "categoria": "Hardware",
                "total": total_hardware
                })

            escritor.writerow({
                "categoria": "Perifericos",
                "total": total_perifericos
                })

if __name__ == "__main__":
    dificil()

