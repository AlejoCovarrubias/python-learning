import re
from pathlib import Path
def integracion_1():
    codigo1 = input("ingrese un codigo para motor: ")
    codigo2 = input("ingrese un codigo para sensor: ")
    codigo3 = input("ingrese un codigo para bomba: ")
    codigo4 = input("ingrese un codigo para reloj: ")

    resultado1 = re.fullmatch(r"MOTOR-\d{4}", codigo1)
    resultado2 = re.fullmatch(r"SENSOR-\d{4}", codigo2)
    resultado3 = re.fullmatch(r"BOMBA-\d{4}", codigo3)
    resultado4 = re.fullmatch(r"RELOJ-\d{4}", codigo4)

    resultados = [resultado1, resultado2, resultado3, resultado4]

    for resultado in resultados:
        if resultado:
            print(f"{resultado} valido")
        else:
            print(f"{resultado} invalido")
    codigos = [codigo1, codigo2, codigo3, codigo4]
    print("Codigos ingresados:", codigos)

def integracion_2():
    temperaturas = """""
    Temperatura: 25 ºC
    Temperatura: 31 ºC
    Temperatura:  28      ºC
    Temperatura: ERROR
    Temperatura: 30 ºC
    """""
    valores = re.findall(r"Temperatura: (\d+) ºC", temperaturas)
    limpio = re.sub(r"\s+", " ", temperaturas)
    print(valores)

    valores = [int(valor) for valor in valores]
    
    mediciones_correctas = len(valores)
    temp_max = max(valores)
    temp_min = min(valores)

    print(f"Mediciones correctas: {mediciones_correctas}")
    print(f"Temperatura máxima: {temp_max} ºC")
    print(f"Temperatura mínima: {temp_min} ºC")

def integracion_3():
    ruta = Path("Semana_9") / "sensor_analysis" / "data"
    archivo = ruta / "registros.txt"
    with open(archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        
        temperaturas = []
        for linea in contenido.splitlines():
            resultado = re.fullmatch(r"TEMP-(\d{4});(\d+)", linea)
            if resultado:
                id_sensor = resultado.group(1)
                temp = int(resultado.group(2))
                temperaturas.append(temp)
                print(f"Registro válido: {linea}")
            else:
                print(f"Registro inválido: {linea}")

        
        print(f"Temperatura máxima: {max(temperaturas)} ºC")
        print(f"Temperatura mínima: {min(temperaturas)} ºC")
        

if __name__ == "__main__":
    integracion_3()

    
