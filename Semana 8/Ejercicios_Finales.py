def integracion_1():
    class Producto:
        def __init__(self, nombre, categoria, precio, stock):
            self.nombre = nombre
            self.categoria = categoria
            self.precio = precio
            self.stock = stock

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

        def vender(self, cantidad):
            if cantidad <= 0 or cantidad > self._stock:
                return False
            self._stock -= cantidad
            return True    
        def reponer(self, cantidad):
            if cantidad <= 0:
                return False
            self._stock += cantidad
            return True     
        def valor_stock(self):
            return self._precio * self._stock

        def tiene_stock(self):
            return self._stock > 0

        def __str__(self):
            return f"{self.nombre} | {self.categoria} | {self._precio} | {self._stock}"

        def __repr__(self):
            return (
                f"Producto(Nombre: {self.nombre!r}."
                f"Categoria: {self.categoria!r}."
                f"Precio: {self._precio!r}."
                f"Stock: {self._stock!r})\n"
                    )
        
    producto1 = Producto("Mouse", "perifericos", 15000, 3)
    producto2 = Producto("teclado", "perifericos", 5000, 20)
    producto3 = Producto("Monitor", "perifericos", 1000, 1)
    producto4 = Producto("Disco", "hardware ", 6000, 1)
    producto5 = Producto("Camara", "perifericos", 4200, 6)
    producto6 = Producto("Ram", "hardware", 700, 4)

    producto1.vender(2)
    producto2.vender(3)

    producto3.reponer(40)
    producto4.reponer(2)

    productos = [producto1, producto2, producto3, producto4, producto5, producto6]
    
    total = 0
    producto_mayor_precio = None
    mayor_precio = 0
    producto_mayor_stock = None
    mayor_stock = 0
    
    for producto in productos:
        total += producto.valor_stock()

        if producto.precio > mayor_precio:
            mayor_precio = producto.precio
            producto_mayor_precio = producto

        if producto.stock > mayor_stock:
            mayor_stock = producto.stock
            producto_mayor_stock = producto

        if not producto.tiene_stock():
            print(f"Producto sin stock: {producto}\n")

    print(f"Total: {total}\n")
    print(f"Producto mayor stock: {producto_mayor_stock}\n")
    print(f"Producto mayor precio: {producto_mayor_precio}\n")
    print(productos)

def integracion_2():
    class Sensor:
        def __init__(self, identificador, tipo, valor, limite, unidad):
            self.identificador = identificador
            self.tipo = tipo
            self._valor = valor
            self._limite = limite
            self.unidad = unidad

        @property
        def valor(self):
            return self._valor

        @valor.setter
        def valor(self, valor):
            if self.valor <= 0:
                raise ValueError("El valor debe ser mayor a 0")
            self._valor = valor

        @property
        def limite(self):
            return self._limite
        
        @limite.setter
        def limite(self, limite):
            if self.limite <= 0:
                raise ValueError("El limite debe ser mayor a 0")
            self._limite = limite   

        def esta_en_alerta(self):
            return self.valor > self.limite

        def actualizar_valor(self, nuevo_valor):
            if nuevo_valor <= 0:
                return False
            self._valor += nuevo_valor
            return True

        def __str__(self):
            estado = "Normal"
            if self.esta_en_alerta(): #is True
                estado = "Alerta"
            return f"{self.identificador} | {self.tipo} | {self.valor} | {self.limite} | {self.unidad} | {estado}\n"

        def __repr__(self):
            return f"Sensor: identificador = {self.identificador!r}, tipo = {self.tipo!r}, valor = {self.valor!r}, limite = {self.limite!r}, unidad = {self.unidad}\n"     

    class SensorTemperatura(Sensor):
        def __init__(self, identificador, valor, limite):
            super().__init__(identificador, "Temperatura", valor, limite, "°C")

        def clima(self):
            if self.valor < 10:
                return "Hace frío"
            elif self.valor <= 30:
                return "Temperatura normal"
            else:
                return "Hace calor"
    class SensorPresion(Sensor):
        def __init__(self, identificador, valor, limite):
            super().__init__(identificador, "Presión", valor, limite, "Pa")

        def nivel_presion(self):
            if self.valor < 80:
                return "Presión baja"
            elif self.valor <= self._limite:
                return "Presión normal"
            else:
                return "Presión alta"
    class SensorVelocidad(Sensor):
        def __init__(self, identificador, valor, limite):
            super().__init__(identificador, "Velocidad", valor, limite, "m/s")

        def estado_movimiento(self):
            if self.valor == 0:
                return "Detenido"
            elif self.valor <= self._limite:
                return "Circulando"
            else:
                return "Exceso de velocidad"


    sensor_temp1 = SensorTemperatura("T1", 25, 30)
    sensor_temp2 = SensorTemperatura("T2", 5, 40)
    sensor_temp3 = SensorTemperatura("T3", 77, 30)

    sensor_presion1 = SensorPresion("P1", 800, 80)
    sensor_presion2 = SensorPresion("P2", 10, 50)
    sensor_presion3 = SensorPresion("P3", 900, 1000)

    sensor_velocidad1 = SensorVelocidad("V1", 155, 90)
    sensor_velocidad2 = SensorVelocidad("V2", 15, 20)
    sensor_velocidad3 = SensorVelocidad("V3", 60, 40)

    sensores = [sensor_temp1, sensor_temp2, sensor_temp3, sensor_presion1, sensor_presion2, sensor_presion3, sensor_velocidad1, sensor_velocidad2, sensor_velocidad3]

    sensores_en_alerta = []
    desviacion = 0
    sensor_con_mayor_desviacion = None

    for sensor in sensores:
        sensor.actualizar_valor(10)
        if sensor.esta_en_alerta():
            sensores_en_alerta.append(sensor)
        
        nueva_desviacion = sensor.valor - sensor.limite
        if nueva_desviacion > desviacion:
            desviacion = nueva_desviacion
            sensor_con_mayor_desviacion = sensor

        print(f"Informacion: {sensor}")

    print(f"Sensores en alerta: {len(sensores_en_alerta)}")
    print(f"Sensor con mayor desviacion: {sensor_con_mayor_desviacion}")

    print(f"Lista con repr: {sensores}")

def integracion_3():
    class Vehiculo:
        def __init__(self, marca, modelo, año):
            self.marca = marca
            self.modelo = modelo
            self.año = año

        def describir(self):
            return f"{self.marca} {self.modelo} ({self.año})"
        
        def calcular_costo_mantenimiento(self):
            return 0

        def __str__(self):
            return f"{self.marca} {self.modelo} ({self.año})"

        def __repr__(self):
            return f"Vehiculo: marca = {self.marca!r}, modelo = {self.modelo!r}, año = {self.año!r}"
    class Auto(Vehiculo):
        def __init__(self, marca, modelo, año, cantidad_puertas):
            super().__init__(marca, modelo, año)
            self.cantidad_puertas = cantidad_puertas

        def calcular_costo_mantenimiento(self):
            return 5000 + self.cantidad_puertas * 500

    class Moto(Vehiculo):
        def __init__(self, marca, modelo, año, cilindrada):
            super().__init__(marca, modelo, año)
            self.cilindrada = cilindrada

        def calcular_costo_mantenimiento(self):
            return 3000 + self.cilindrada * 20

    class Camion(Vehiculo):
        def __init__(self, marca, modelo, año, capacidad_carga):
            super().__init__(marca, modelo, año)
            self.capacidad_carga = capacidad_carga

        def calcular_costo_mantenimiento(self):
            return 7000 + self.capacidad_carga * 100

    class Flota:
        def __init__(self):
            self.vehiculos = []

        def agregar_vehiculo(self, vehiculo):
            self.vehiculos.append(vehiculo)

        def eliminar_vehiculo(self, vehiculo):
            if vehiculo in self.vehiculos:
                self.vehiculos.remove(vehiculo)
                return True
            return False

        def buscar_vehiculo(self, marca, modelo):
            for vehiculo in self.vehiculos:
                if vehiculo.marca == marca and vehiculo.modelo == modelo:
                    return vehiculo
            return None
        
        def costo_total_mantenimiento(self):
            costo_total = 0
            for vehiculo in self.vehiculos:
                costo_total += vehiculo.calcular_costo_mantenimiento()
            return costo_total

        def vehiculo_mas_caro(self):
            if not self.vehiculos:
                return None
            vehiculo_mas_caro = self.vehiculos[0]
            for vehiculo in self.vehiculos:
                if vehiculo.calcular_costo_mantenimiento() > vehiculo_mas_caro.calcular_costo_mantenimiento():
                    vehiculo_mas_caro = vehiculo
            return vehiculo_mas_caro

    auto = Auto("Toyota", "Corolla", 2022, 4)
    moto = Moto("Honda", "CB125F", 2023, 125)
    camion = Camion("Mercedes-Benz", "Actros", 2019, 20) 

    flota = Flota()
    flota.agregar_vehiculo(auto)
    flota.eliminar_vehiculo(auto)

    flota.agregar_vehiculo(moto)
    flota.agregar_vehiculo(camion)

    print(auto.describir())
    print(moto.calcular_costo_mantenimiento())
    print(flota.buscar_vehiculo("Honda", "CB125F"))
    print(flota.costo_total_mantenimiento())
    print(flota.vehiculo_mas_caro())

def integracion_4():
    class CuentaBancaria:
        def __init__(self, titular, saldo):
            self.titular = titular
            self.__saldo = saldo

        @property
        def saldo(self):
            return self.__saldo

        @saldo.setter
        def saldo(self, saldo):
            if saldo < 0:
                raise ValueError("El saldo no puede ser negativo")
            self.__saldo = saldo

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

        def mostrar_saldo(self):
            return self.__saldo

    class CuentaAhorro(CuentaBancaria):
        def __init__(self, titular, saldo, tasa_interes, limite_extraccion):
            super().__init__(titular, saldo)
            self.tasa_interes = tasa_interes
            self.limite_extraccion = limite_extraccion

        def calcular_interes(self):
            return self.saldo * self.tasa_interes / 100

    class Banco:
        def __init__(self):
            self.cuentas = []

        def crear_cuenta(self, cuenta):
            self.cuentas.append(cuenta)

        def buscar_cuenta(self, titular):
            for cuenta in self.cuentas:
                if cuenta.titular == titular:
                    return cuenta
        def depositar(self, titular, cantidad):
            if cantidad <= 0:
                return False
            cuenta = self.buscar_cuenta(titular)
            if cuenta:
                return cuenta.depositar(cantidad)
            return False

        def retirar(self, titular, cantidad):
            if cantidad <= 0:
                return False
            cuenta = self.buscar_cuenta(titular)
            if cuenta:
                if cantidad > cuenta.limite_extraccion or cantidad > cuenta.saldo:
                    return False
                return cuenta.retirar(cantidad)
            return False

        def mostrar_cuentas(self):
            for cuenta in self.cuentas:
                print(f"Titular: {cuenta.titular}, Saldo: {cuenta.mostrar_saldo()}")

    cuenta1 = CuentaAhorro("Juan", 1000, 2, 500)
    cuenta2 = CuentaBancaria("Maria", 2000)
    cuenta3 = CuentaAhorro("Pedro", 1500, 1.5, 300)

    banco = Banco()
    banco.crear_cuenta(cuenta1)
    banco.crear_cuenta(cuenta2)
    banco.crear_cuenta(cuenta3)

    banco.mostrar_cuentas()

    print(banco.buscar_cuenta("Maria"))
    print(banco.depositar("Juan", 500))
    print(banco.retirar("Pedro", 200))
    print(cuenta1.calcular_interes())
    print(cuenta3.calcular_interes())
    
    banco.mostrar_cuentas()

def integracion_5():
    import json
    from pathlib import Path
    class Producto:
        def __init__(self, nombre, categoria, precio, stock):
            self.nombre = nombre
            self.categoria = categoria
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
        def stock(self, stock):
            if stock < 0:
                raise ValueError("El stock no puede ser negativo")
            self._stock = stock
        def vender(self, cantidad):
            if cantidad <= 0 or cantidad > self._stock:
                return False
            self._stock -= cantidad
            return True
        def cambiar_stock(self, nuevo_stock):
            if nuevo_stock < 0:
                return False
            self._stock = nuevo_stock
            return True
        def reponer(self, cantidad):
            if cantidad <= 0:
                return False
            self._stock += cantidad
            return True
        def __str__(self):
            return f"{self.nombre} | {self.categoria} | {self._precio} | {self._stock}"
        def __repr__(self):
            return (
                f"Producto(Nombre: {self.nombre!r}."
                f"Categoria: {self.categoria!r}."
                f"Precio: {self._precio!r}."
                f"Stock: {self._stock!r})\n"
                    )
    class Inventario:
        def __init__(self):
            self.productos = []

        def crear_producto(self, producto):
            self.productos.append(producto)

        def cambiar_stock_producto(self, producto, nuevo_stock):
            if nuevo_stock < 0:
                return False
            if producto in self.productos:
                return producto.cambiar_stock(nuevo_stock)
            return False
        def eliminar_producto(self, producto):
            if producto in self.productos:
                self.productos.remove(producto)
                return True
            return False

        def vender_producto(self, producto, cantidad):
            if cantidad <= 0:
                return False
            if producto in self.productos:
                return producto.vender(cantidad)
            return False

        def reponer_producto(self, producto, cantidad):
            if producto in self.productos:
                return producto.reponer(cantidad)
            return False

    producto1 = Producto("Mouse", "perifericos", 15000, 3)
    producto2 = Producto("teclado", "perifericos", 5000, 20)
    producto3 = Producto("Monitor", "perifericos", 1000, 1)
    producto4 = Producto("Disco", "hardware ", 6000, 1)
    producto5 = Producto("Camara", "perifericos", 4200, 6)
    producto6 = Producto("Ram", "hardware", 700, 4)

    productos = [producto1, producto2, producto3, producto4, producto5, producto6]
    inventario = Inventario()
    
    for producto in productos:
        inventario.crear_producto(producto)
    
    ruta = Path("Semana 8") / "Datos"
    ruta.mkdir(parents=True, exist_ok=True)

    archivo = ruta / "Integracion_5.json"

    inventario.vender_producto(producto1, 2)
    inventario.cambiar_stock_producto(producto2, 15)
    inventario.reponer_producto(producto3, 5)
    
    producto7 = Producto("Auriculares", "perifericos", 3000, 10)
    inventario.crear_producto(producto7)
    
    productos_dict = []
    for producto in inventario.productos:
        productos_dict.append({
            "nombre": producto.nombre,
            "categoria": producto.categoria,
            "precio": producto.precio,
            "stock": producto.stock
        })

    with open(archivo, "w", encoding="utf-8") as archivo:
        json.dump(productos_dict, archivo, indent=4)        
    

if __name__ == "__main__":
    integracion_5()