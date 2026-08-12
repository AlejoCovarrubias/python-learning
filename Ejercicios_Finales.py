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
        

if __name__ == "__main__":
    integracion_1()