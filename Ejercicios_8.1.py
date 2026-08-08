def muy_facil_1():
    class Persona:

        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

    persona_1 = Persona("Carlos", 20)
    persona_2 = Persona("Yo", 15)

    print(persona_1.nombre)
    print(persona_1.edad)
    print(persona_2.nombre)
    print(persona_2.edad)

def muy_facil_2():
    class Producto:

        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio

    producto_1 = Producto("Detergente", 200)
    producto_2 = Producto("cumpu", 4555555)
    producto_3 = Producto("Mouse", 12)

    print(producto_3.precio)

    producto_3.precio = 5999

    print(producto_3.precio)

def facil_1():
    class Vehiculo:
        def __init__(self, marca, modelo, año):
            self.marca = marca
            self.modelo = modelo
            self.año = año

    vehiculo_1 = Vehiculo("auto", "deportivo", 2005)
    vehiculo_2 = Vehiculo("auto", "casual", 2020)
    vehiculo_3 = Vehiculo("moto", "deportiva", 2015)

    vehiculos = {
        vehiculo_1,
        vehiculo_2,
        vehiculo_3
    }
    for auto in vehiculos:
        print(auto.marca, auto.modelo, auto.año)

def facil_2():
    class Sensor:
        def __init__(self, nombre, valor, unidad):
            self.nombre = nombre
            self.valor = valor
            self.unidad = unidad
    sensor_1 = Sensor("Temperatura motor", 75,"celsius")
    sensor_2 = Sensor("Temperatura aceite", 60,"celsius")
    sensor_3 = Sensor("Presión hidráulica", 120, "celsius")

    sensores = {
        sensor_1,
        sensor_2,
        sensor_3
    }
    for sensor in sensores:
        print(sensor.nombre, sensor.valor, sensor.unidad)
    print(sensor_2.__dict__)

def medio_1():
    class Maquina:
        def __init__(self, nombre, temperatura, estado):
            self.nombre = nombre
            self.temperatura = temperatura
            self.estado = estado

    maquina_1 = Maquina("Torno CNC", 102, "apagada")
    maquina_2 = Maquina("Fresadora CNC", 54, "apagada")
    maquina_3 = Maquina("Sierra", 1, "apagada")

    maquinas = {
        maquina_1,
        maquina_2,
        maquina_3
    }

    maquina_1.temperatura = 40
    maquina_2.estado = "encendida"
    
    for maquina in maquinas:
        print(maquina.nombre, maquina.temperatura, maquina.estado)

def medio_2():
    class Sensor:

        unidad = "ºC"

        def __init__(self, valor):
            self.valor = valor

    sensor_1 = Sensor(75)
    sensor_2 = Sensor(60)
    sensor_3 = Sensor(120)

    print(sensor_1.unidad)
    print(sensor_1.valor)

    print(Sensor.unidad)

def dificil():
    class Producto:
        def __init__(self, nombre, categoria, precio, stock):
            self.nombre = nombre
            self.categoria = categoria
            self.precio = precio
            self.stock = stock

    producto1 = Producto("Mouse", "Periféricos", 15000, 25)
    producto2 = Producto("Teclado", "Periféricos", 25000, 15)
    producto3 = Producto("Monitor", "Pantallas", 180000, 8)
    producto4 = Producto("Auriculares", "Audio", 45000, 12)
    producto5 = Producto("Webcam", "Accesorios", 35000, 10)

    productos = [
        producto1,
        producto2,
        producto3,
        producto4,
        producto5
    ]

    mayor_precio = 0
    producto_mayor_precio = None
    total = 0

    for producto in productos:

        total += producto.precio * producto.stock 

        if producto.precio > mayor_precio:
            mayor_precio = producto.precio
            producto_mayor_precio = producto  

    print(f"Total: {total}")
    print(f"Mayor precio: {mayor_precio}")
    print(f"Stock antiguo producto 3: {producto3.stock}")
    producto3.stock = 15
    print(f"Stock nuevo producto 3: {producto3.stock}")
    print(producto3.__dict__)

if __name__ == "__main__":
    dificil()