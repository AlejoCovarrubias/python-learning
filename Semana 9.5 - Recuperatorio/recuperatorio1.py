def muy_facil():
    numeros = [4 ,7 ,4 ,9 ,7, 2, 9, 1]
    numeros_unicos = set(numeros)
    numero_maximo = max(numeros)
    numero_minimo = min(numeros)
    ultimos_3 = numeros[-3:]
    mayor_5 = [numero for numero in numeros if numero > 5]

    print("Números únicos:", numeros_unicos)
    print("Número máximo:", numero_maximo)
    print("Número mínimo:", numero_minimo)
    print("Últimos 3 números:", ultimos_3)
    print("Números mayores a 5:", mayor_5)

def facil():
    productos = [
        {"nombre": "Mouse", "precio": 15000},
        {"nombre": "Teclado", "precio": 25000},
        {"nombre": "Monitor", "precio": 180000},
        {"nombre": "Auriculares", "precio": 45000}
    ]
    def productos_caros(productos):
        return [producto for producto in productos if producto["precio"] > 30000]
    print(f"Productos caros: {productos_caros(productos)}")

def medio():
    mediciones = [
        {"sensor": "T01", "valor": 23.5},
        {"sensor": "T02", "valor": 31.2},
        {"sensor": "T03", "valor": 28.7},
        {"sensor": "T04", "valor": 35.1},
        {"sensor": "T05", "valor": 29.4}
    ]
    limite = 30.0
    def filtrar_mediciones(mediciones, limite):
        return [medicion for medicion in mediciones if medicion["valor"] > limite]
    print(f"Mediciones por encima del límite: {filtrar_mediciones(mediciones, limite)}")
    
def dificil():
    def analizar_mediciones(*mediciones):
        if len(mediciones) == 0:
            raise ValueError("No se puede analizar si no hay mediciones")
        try:
            cantidad = len(mediciones)
            minimo = min(mediciones)
            maximo = max(mediciones)
            promedio = sum(mediciones) / cantidad
            mayores_a_promedio = [medicion for medicion in mediciones if medicion > promedio]
        except TypeError:
            return ("Fallo en medicion, hay un elemento erroneo")
        else:
            return {"cantidad_mediciones": cantidad,
                "minimo": minimo,
                "maximo": maximo,
                "promedio": promedio,
                "mayores_al_promedio": mayores_a_promedio
            }
    mediciones = analizar_mediciones(0.1,-5.555, 3,4,5,6)
    print(mediciones)
if __name__ == "__main__":
    dificil()