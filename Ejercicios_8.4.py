def muy_facil_1():
    class Animal:
        def __init__(self, nombre):
            self.nombre = nombre

        def comer(self):
            print(f"{self.nombre} esta comiendo")

    class Perro(Animal):
        pass
    class Gato(Animal):
        pass

    perro = Perro("Miki")
    gato = Gato("Guapo")

    perro.comer()
    gato.comer()

def muy_facil_2():
    class Vehiculo:
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        def mostrar_info(self):
            print(f"Marca: {self.marca}, Modelo: {self.modelo}")

    class Auto(Vehiculo):
        def __init__(self, marca, modelo, puertas):
            super().__init__(marca, modelo)
            self.puertas = puertas

    class Moto(Vehiculo):
        def __init__(self, marca, modelo, cilindrado):
            super().__init__(marca, modelo)
            self.cilindrado = cilindrado

    auto = Auto("Golf", 2005, 4)
    moto = Moto("Kawasaki", 3000, 150)

    auto.mostrar_info()
    moto.mostrar_info()

    print(auto.puertas)
    print(moto.cilindrado)

def facil_1():
    class Animal:
        def __init__(self, nombre):
            self.nombre = nombre

        def hacer_sonido(self):
            print("El animal hace un sonido extraño")

    class Perro(Animal):
        def hacer_sonido(self):
            super().hacer_sonido()
            print("GUAGUGUAGUGAU")

    class Gato(Animal):
        def hacer_sonido(self):
            super().hacer_sonido()
            print("MIAU MIAU MIAU")

    perro = Perro("scubi")
    gato = Gato("Garfield")

    animales = [perro, gato]
    for animal in animales:
        animal.hacer_sonido()
    
def facil_2():
    class Empleado:
        def __init__(self, nombre, salario):
            self.nombre = nombre
            self.salario = salario

        def mostrar_info(self):
            print(f"Nombre: {self.nombre}. Salario: {self.salario}")

    class Ingeniero(Empleado):
        def __init__(self, nombre, salario, casco):
            super().__init__(nombre, salario)
            self.casco = casco
        def mostrar_info(self):
            super().mostrar_info()
            print("Hermoso y coqueto")
    class Vendedor(Empleado):
        def __init__(self, nombre, salario, productos):
            super().__init__(nombre, salario)
            self.productos = productos

        def mostrar_info(self):
            super().mostrar_info()
            print("pobre")

    ingeniero = Ingeniero("Raul", 5000, "hierro")
    vendedor = Vendedor("pedro", 1, 50)

    empleados = [ingeniero, vendedor]
    for empleado in empleados:
        empleado.mostrar_info()

def medio():
    class Maquina:
        def __init__(self, nombre, potencia):
            self.nombre = nombre
            self.potencia = potencia
            self.estado = False

        def encender(self):
            self.estado = True
            print(f"{self.nombre} está encendida.")

        def apagar(self):
            self.estado = False
            print(f"{self.nombre} está apagada.")

    class Torno(Maquina):
        def mecanizar(self):
            print(f"{self.nombre} está mecanizando una pieza.")

    class Fresadora(Maquina):
        def fresar(self):
            print(f"{self.nombre} está fresando una pieza.")

    torno1 = Torno("Torno CNC", 5000)
    fresadora1 = Fresadora("Fresadora Industrial", 7500)

    maquinas = [torno1, fresadora1]

    for maquina in maquinas:
        maquina.encender()

    for maquina in maquinas:
        maquina.apagar()

def dificil():
    class Vehiculo:
        def __init__(self, marca, modelo, año):
            self.marca = marca
            self.modelo = modelo
            self.año = año

        def describir(self):
            print(f"Marca: {self.marca}. Modelo: {self.modelo}. Año: {self.año}")

        def calcular_costo_mantenimiento(self):
            return 0

    class Auto(Vehiculo):
        def __init__(self, marca, modelo, año, cantidad_puertas):
            super().__init__(marca, modelo, año)
            self.cantidad_puertas = cantidad_puertas

        def describir(self):
            return (f"Auto: {self.marca} {self.modelo}, ({self.año}) - {self.cantidad_puertas} puertas")

        def calcular_costo_mantenimiento(self):
            return 50000 + self.cantidad_puertas * 5000

    class Moto(Vehiculo):
        def __init__(self, marca, modelo, año, cilindrada):
            super().__init__(marca, modelo, año)
            self.cilindrada = cilindrada

        def describir(self):
            return (f"Moto: {self.marca} {self.modelo}, ({self.año}) - {self.cilindrada} cc")

        def calcular_costo_mantenimiento(self):
            return 30000 + self.cilindrada * 20


    class Camion(Vehiculo):
        def __init__(self, marca, modelo, año, capacidad_carga):
            super().__init__(marca, modelo, año)
            self.capacidad_carga = capacidad_carga

        def describir(self):
            return (f"Camión: {self.marca} {self.modelo}, ({self.año}) - Carga: {self.capacidad_carga} toneladas")

        def calcular_costo_mantenimiento(self):
            return 100000 + self.capacidad_carga * 15000

    auto1 = Auto("Toyota", "Corolla", 2022, 4)
    auto2 = Auto("Ford", "Focus", 2020, 5)

    moto1 = Moto("Honda", "CB125F", 2023, 125)
    moto2 = Moto("Yamaha", "FZ", 2021, 150)

    camion1 = Camion("Mercedes-Benz", "Actros", 2019, 20)

    vehiculos = [auto1, auto2, moto1, moto2, camion1]

    for vehiculo in vehiculos:
        print(vehiculo.describir())
        print(f"Mantenimiento: ${vehiculo.calcular_costo_mantenimiento()}\n")

    mantenimiento_total = 0

    for vehiculo in vehiculos:
        mantenimiento_total += vehiculo.calcular_costo_mantenimiento()

    print(f"Mantenimiento total: ${mantenimiento_total}")

    vehiculo_mayor_costo = None
    mayor_mantenimiento = 0
    for vehiculo in vehiculos:
        mantenimiento = vehiculo.calcular_costo_mantenimiento()
        if mantenimiento > mayor_mantenimiento:
            mayor_mantenimiento = mantenimiento
            vehiculo_mayor_costo = vehiculo

    print(f"Mantenimiento mas caro: {mayor_mantenimiento}")
    print(f"Vehiculo mayor costo: {vehiculo_mayor_costo.describir()}")
    

if __name__ == "__main__":
    dificil()