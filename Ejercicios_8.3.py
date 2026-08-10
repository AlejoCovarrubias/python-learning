def muy_facil_1():
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self._edad = edad

        @property
        def edad(self):
            return self._edad

    persona1 = Persona("carlos",20)
    print(persona1.edad)

def muy_facil_2():
    class Producto:
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self._precio = precio

        @property
        def precio(self): 
            return self._precio

    producto1 = Producto("agua",300)

    print(producto1.precio)

def facil_1():
    class Cuenta:
        def __init__(self, titular, saldo):
            self.titular = titular
            self._saldo = saldo

        @property
        def saldo(self):
            return self._saldo

        def depositar(self, cantidad):
            if cantidad <= 0:
                return False

            self._saldo += cantidad
            return True

        def retirar(self, cantidad):
            if cantidad <= 0 or cantidad > self._saldo:
                return False

            self._saldo -= cantidad
            return True


    cuenta = Cuenta("Alejo", 50000)

    print(cuenta.saldo)

    cuenta.depositar(10000)
    print(cuenta.saldo)

    cuenta.retirar(20000)
    print(cuenta.saldo)      
def facil_2():
    class Producto:
        def __init__(self, nombre, precio, stock):
            self.nombre = nombre
            self._precio = precio
            self._stock = stock

        @property
        def precio(self):
            return self._precio

        @precio.setter
        def precio(self, precio):
            if precio <= 0:
                raise ValueError("El precio debe ser mayor a 0")
            self._precio = precio
        
        @property
        def stock(self):
            return self._stock
        
        @stock.setter
        def stock(self, cantidad):
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa")
            self._stock = cantidad

    producto = Producto("Mouse", 15000, 20)

    print(producto.precio)
    print(producto.stock)

    producto.precio = -100
    producto.stock = -5

def medio():
    class Sensor:
        def __init__(self, nombre, valor , limite):
            self.nombre = nombre
            self._valor = valor
            self._limite = limite 

        @property
        def valor(self):
            return self._valor
        @valor.setter
        def valor(self, valor):
            if valor < 0:
                raise ValueError("El valor debe ser numerico")

        @property
        def limite(self):
            return self._limite
        @limite.setter
        def limite(self, limite):
            if limite < 0:
                raise ValueError("El limite no puede ser negativo")

        def esta_en_alerta(self):
            if self._valor > self._limite:
                return True           
            return False
        
    sensor_1 = Sensor("Temperatura motor", 75, 70)
    sensor_2 = Sensor("Temperatura aceite", 650, 1000)
    sensor_3 = Sensor("Temperatura rotor", 75, 80)
    sensor_4 = Sensor("Temperatura cañeria", 1001, 1000)
    sensor_5 = Sensor("Presión hidráulica", 120, 150)

    sensores = [sensor_1,sensor_2,sensor_3,sensor_4, sensor_5]

    for sensor in sensores:
        if sensor.esta_en_alerta():
            print(f"El sensor {sensor.nombre} esta por encima de su limite")
        else:
            print(f"El sensor {sensor.nombre} esta normal")    

def dificil():
    class CuentaBancaria:
        def __init__(self, titular, saldo):
            self.titular = titular
            self.__saldo = saldo

        @property
        def saldo(self):
            return self.__saldo

        def depositar(self, cantidad):
            if cantidad <= 0:
                return False

            self.__saldo += cantidad
            return True

        def retirar(self, cantidad):
            if cantidad <= 0 or cantidad > self.__saldo:
                return False
            
            self.__saldo -= cantidad
            return True      
        
    cuenta1 = CuentaBancaria("Alejo", 50000)
    cuenta2 = CuentaBancaria("Juan", 30000)
    cuenta3 = CuentaBancaria("Pedro", 100000) 

    cuentas = [cuenta1, cuenta2, cuenta3]

    cuenta1.depositar(10000)
    cuenta1.retirar(5000)

    cuenta2.depositar(20000)
    cuenta2.retirar(10000)

    cuenta3.retirar(30000)
    cuenta3.depositar(15000) 

    for cuenta in cuentas:
        print(f"Titular: {cuenta.titular}")
        print(f"Saldo: {cuenta.saldo}\n")
          
    print(cuenta1.__saldo)  #No se accese a saldo xq usa __ y evita que se accesa por afuera de la clase

if __name__ == "__main__":
    dificil()