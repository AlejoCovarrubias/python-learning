def muy_facil_1():
    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def saludar(self):
            print(f"Hola {self.nombre}")

    persona1 = Persona("Tomi", 22)

    persona1.saludar()

def muy_facil_2():
    class Rectangulo:
        def __init__(self, base, altura):
            self.base = base
            self.altura = altura

        def area(self):
            area = self.base * self.altura
            return area

        def perimetro(self):
            perimetro = (self.base * 2) + (self.altura * 2)
            return perimetro
    rectangulo1 = Rectangulo(20, 50)

    print(rectangulo1.area())
    print(rectangulo1.perimetro())

def facil_1():
    class Cuenta:
        def __init__(self, titular, saldo):
            self.titular = titular
            self.saldo = saldo

        def depositar(self, cantidad):
            if cantidad <= 0:
                return False
            
            self.saldo += cantidad
            return True

        def retirar(self, cantidad):
            if cantidad <= 0:
                return False
            
            if cantidad > self.saldo:
                return False
            
            self.saldo -= cantidad
            return True
        
    cuenta1 = Cuenta("Carlos", 5000)

    print(cuenta1.depositar(-5))
    print(cuenta1.retirar(5001))
    print(cuenta1.retirar(501))
        
def facil_2():
    class Producto:
        def __init__(self, nombre, precio, stock):
            self.nombre = nombre
            self.precio = precio
            self.stock = stock

        def vender(self):
            if self.stock <= 0:
                return False
            
            self.stock -= 1
            return True
        def reponer(self, cantidad):
            if cantidad <= 0:
                return False
            self.stock += cantidad
            return True

        def valor_stock(self):
            return self.precio * self.stock
        
    producto = Producto("Mouse", 15000, 10)

    print(producto.valor_stock())
    producto.vender()
    print(producto.stock)
    producto.reponer(5)
    print(producto.stock)

def medio():
    class Sensor:
        def __init__(self, nombre, valor, limite):
            self.nombre = nombre
            self.valor = valor
            self.limite = limite

        def actualizar(self, nuevo_valor):
            self.valor = nuevo_valor
            return nuevo_valor

        def esta_en_alerta(self):
            return self.valor > self.limite

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
    class Producto:
        def __init__(self, nombre, categoria, precio, stock):
            self.nombre = nombre
            self.categoria = categoria
            self.precio = precio
            self.stock = stock

        def vender(self, cantidad):
            if self.stock <= 0:
                return False
            if cantidad <= 0 or cantidad > self.stock:
                return False
            
            self.stock -= cantidad
            return True

        def reponer(self, cantidad):
            if cantidad <= 0:
                return False
            self.stock += cantidad
            return True

        def valor_stock(self):
            return self.precio * self.stock

        def tiene_stock(self):
            return self.stock > 0
    
    producto1 = Producto("Mouse", "Periféricos", 15000, 25)
    producto2 = Producto("Teclado", "Periféricos", 25000, 15)
    producto3 = Producto("Monitor", "Pantallas", 180000, 8)
    producto4 = Producto("Auriculares", "Audio", 45000, 0)
    producto5 = Producto("Webcam", "Accesorios", 35000, 10)        

    productos = [producto1, producto2, producto3, producto4, producto5]

    for i in range(0, 6):
        producto2.vender(2)
        producto5.reponer(1)
        producto1.reponer(1)

    total = 0
    mayor_precio = 0
    producto_mayor_precio = None
    
    for producto in productos:
        total += producto.valor_stock()

        if producto.precio > mayor_precio:
            mayor_precio = producto.precio
            producto_mayor_precio = producto
    
    print(total)
    print(producto_mayor_precio.nombre)
    print(producto_mayor_precio.precio)


if __name__ == "__main__":
    dificil()  
            