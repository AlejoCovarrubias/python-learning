def muy_facil_1():
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
        def __str__(self):
            return f"{self.nombre} - {self.edad}"

    persona = Persona("Alejo", 20)
    print(persona)

def muy_facil_2_y_facil_1():
    class Producto:
        def __init__(self, nombre, precio,stock):
            self.nombre = nombre
            self.precio = precio
            self.stock = stock
        def __str__(self):
            return f"{self.nombre} - {self.precio} - {self.stock}" 
    
        def __repr__(self):
            return (f"Producto(nombre = {self.nombre!r}, precio = {self.precio!r}, stock = {self.stock!r})\n")

    producto1 = Producto("Mouse", 15000, 3)
    producto2 = Producto("teclado", 5000, 2)
    producto3 = Producto("Monitor", 1000, 1)
    productos = [producto1, producto2, producto3]

    print(productos)
    print(producto1)
    
def facil_2():
    class CuentaBancaria:
        def __init__(self, titular, saldo):
            self.titular = titular
            self.saldo = saldo
        def __str__(self):
            return f"{self.titular}"
        def __repr__(self):
            return (f"Cuenta(titular = {self.titular!r}, saldo = {self.saldo!r})")

    cuenta = CuentaBancaria("Alejo", 400000)
    print(cuenta)
    print(repr(cuenta))
def medio():
    class Vehiculo:
        def __init__(self, marca, modelo, año):
            self.marca = marca
            self.modelo = modelo
            self.año = año

        def __str__(self):
            return f"{self.marca} {self.modelo} ({self.año})"

        def __repr__(self):
            return (f"{self.__class__.__name__}, marca={self.marca!r}, modelo={self.modelo!r}, año={self.año!r})")

    class Auto(Vehiculo):
        pass
    class Moto(Vehiculo):
        pass
    class Camion(Vehiculo):
        pass


    vehiculos = [
        Auto("Toyota", "Corolla", 2022),
        Moto("Honda", "CB190R", 2024),
        Camion("Scania", "R450", 2021)
    ]

    print(vehiculos)
def dificil():
    class Sensor:
        def __init__(self, identificador, tipo, valor, limite):
            self.identificador = identificador
            self.tipo = tipo
            self._valor = valor
            self._limite = limite

        @property
        def valor(self):
            return self._valor
        @valor.setter
        def valor(self, valor):
            if valor < 0:
                raise ValueError("El valor debe ser mayor a 0")
            self._valor = valor
        @property
        def limite(self):
            return self._limite
        @limite.setter
        def limite(self, limite):
            if limite < 0:
                raise ValueError("El limite no puede ser negativo")
            self._limite = limite
        def esta_en_alerta(self):
            return self._valor > self._limite
        
        def __str__(self):
            estado = "Normal"
            if self.esta_en_alerta(): #is True
                estado = "Alerta"
            return f"{self.identificador} | {self.tipo} | {self.valor} | {self.limite} | {estado}\n"

        def __repr__(self):
            return f"Sensor: identificador = {self.identificador!r}, tipo = {self.tipo!r}, valor = {self.valor!r} limite = {self.limite!r}\n"
  
    sensor_1 = Sensor("Sensor 1", "Temperatura motor", 75, 70)
    sensor_2 = Sensor("Sensor 2", "Temperatura aceite", 650, 1000)
    sensor_3 = Sensor("Sensor 3", "Temperatura rotor", 75, 80)
    sensor_4 = Sensor("Sensor 4", "Temperatura cañeria", 1001, 1000)
    sensor_5 = Sensor("Sensor 5", "Presión hidráulica", 120, 150)        

    sensores = [sensor_1, sensor_2, sensor_3, sensor_4, sensor_5]
    for sensor in sensores:
        print(sensor)
    print(sensores)    
if __name__ == "__main__":
    dificil()