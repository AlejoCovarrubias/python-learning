def muy_facil_1():
    from pathlib import Path

    ruta = Path("datos.txt")
    if ruta.exists():
        print("Existe esta ruta")
    else:
        print("No existe esta ruta")
    if ruta.is_file():
        print("Esto es un archivo")
    else:
        print("No es archivo")
    if ruta.is_dir():
        print("Es una carpeta")
    else:
        print("No es una carpeta")
    print(f"La ubicacion es {ruta.cwd()}")

def muy_facil_2():
    from pathlib import Path

    carpeta = Path("Semana 7") / "clase7_4" 
    datos = carpeta / "datos"
    resultados = carpeta / "resultados"

    datos.mkdir(parents=True, exist_ok=True)
    resultados.mkdir(parents=True, exist_ok=True)

def facil_1():
    from pathlib import Path

    carpeta = Path("Semana 7") / "clase7_4" / "resultados"
    carpeta.mkdir(parents=True, exist_ok=True)
    archivo = carpeta / "resultados.txt"
    with open(archivo, "w", encoding="utf-8") as file:
        file.write("Archivo creado automaticamente.\nSemana 7 - Clase 7.4")

def facil_2():
    from pathlib import Path
    ruta = Path("Semana 7") / "clase7_4" / "datos" / "ventas" / "ventas_2026.csv"
    ruta.mkdir(parents=True, exist_ok=True)

    print(f"Nombre: {ruta.name}")
    print(f"Nombre sin extensión: {ruta.stem}")
    print(f"Extensión: {ruta.suffix}")
    print(f"Carpeta padre: {ruta.parent}")

def medio_1():
    from pathlib import Path
    ruta = Path("Semana 7") / "clase7_4" / "datos"
    ruta.mkdir(parents=True, exist_ok=True)

    archivo1 = ruta / "ventas.csv"
    archivo2 = ruta / "clientes.csv"
    archivo3 = ruta / "productos.csv"
    archivo4 = ruta / "notas.txt"
    archivo5 = ruta / "config.json"

    for i in [archivo1, archivo2, archivo3, archivo4, archivo5]:
        i.touch(exist_ok=True)
    archivos_csv = ruta.glob("*.csv")

    for i in archivos_csv:
        print(i)

def medio_2():
    from pathlib import Path
    ruta = Path("Semana 7") / "clase7_4" / "proyecto"
    ruta.mkdir(parents=True, exist_ok=True)

    archivo1 = ruta / "datos.txt"
    archivo2 = ruta / "ventas.csv"
    datos = ruta / "datos"
    resultados = ruta / "resultados"

    for archivos in [archivo1, archivo2]:
        archivos.touch(exist_ok=True)

    datos.mkdir(parents=True, exist_ok=True)
    resultados.mkdir(parents=True, exist_ok=True)
    for elementos in ruta.iterdir():
        if elementos.is_file():
            print(f"Archivos encontrados: {elementos}")
        elif elementos.is_dir():
            print(f"Carpetas encontradas: {elementos}")

def dificil():
    from pathlib import Path

    ruta = Path("Semana 7/clase7_4/proyecto")
    ruta.mkdir(parents=True, exist_ok=True)
    datos = ruta / "datos"
    enero = datos / "enero"
    febrero = datos / "febrero"

    ventas_enero = enero / "ventas.csv"
    clientes_enero = enero / "clientes.txt"
    ventas_febrero = febrero / "ventas.csv"
    backups = ruta / "backups"
    backup_antiguo = backups / "antiguo.csv"

    resultados = ruta / "resultados"
    resumen_resultados = resultados / "resumen.txt"

    datos.mkdir(parents=True, exist_ok=True)
    enero.mkdir(parents=True, exist_ok=True)
    febrero.mkdir(parents=True, exist_ok=True)
    backups.mkdir(parents=True, exist_ok=True)
    resultados.mkdir(parents=True, exist_ok=True)

    for i in [ventas_enero,clientes_enero,ventas_febrero,backup_antiguo,resumen_resultados]:
            i.touch(exist_ok=True)
    
    archivos_csv = ruta.rglob("*.csv")
    for i in archivos_csv():
        print(i)
    
if __name__ == "__main__":
    dificil()