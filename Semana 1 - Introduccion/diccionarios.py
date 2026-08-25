def ejercicio_1(): #claves
    persona = {
        "nombre": "carlos",
        "edad": 19,
    "pais": "argentina"
    }

    for i in persona:
        print(i)

def ejercicio_2(): #valores
    persona = {
        "nombre": "carlos",
        "edad": 19,
    "pais": "argentina"
    }

    for i in persona.values():
        print(i)

def ejercicio_3(): #los 2
    persona = {
        "nombre": "carlos",
        "edad": 19,
    "pais": "argentina"
    }

    for i in persona.items():
        print(i)

def ejercicio_4(): #modificar edad
    persona = {
        "nombre": "carlos",
        "edad": 19,
    "pais": "argentina"
    }

    persona["edad"] = 20 # :(
    print(persona["edad"])


if __name__ == "__main__":
    ejercicio_4()