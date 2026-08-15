from pathlib import Path

archivo = Path("data") / "mediciones.csv"

print(archivo.exists())