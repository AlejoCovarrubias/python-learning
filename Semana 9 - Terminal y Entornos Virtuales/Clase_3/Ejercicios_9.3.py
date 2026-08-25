import re

def muy_facil():
    texto = "Hoy tengo 20 años y mi hermano tiene 17."

    resultado = re.findall(r"\d+", texto)

    print(resultado)

def facil():
    
    texto = input("Ingrese un texto: ")
    resultado = re.fullmatch(r"\d{5}", texto)
    if resultado:
        print("valido")
    else:
        print("invalido")

def medio():
    codigo = input("Ingrese el código del sensor: ")

    resultado = re.fullmatch(r"SENSOR-\d{4}", codigo)
    if resultado:
        print("valido")
    else:
        print("invalido")

def dificil():
    texto = """
    Sensor 1: temperatura 25°C
    Sensor 2: temperatura 31°C
    Sensor 3: temperatura 28°C
    """
    temperaturas = re.findall(r"temperatura (\d+)°C", texto)
    temperaturas = [int(temp) for temp in temperaturas]

    
if __name__ == "__main__":
    dificil()