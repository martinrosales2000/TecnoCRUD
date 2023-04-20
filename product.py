class Producto:
    #Constructor con parametros del modelo
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    #Constructor de la base
    def toDBCollection(self):
        return{
           'nombre': self.nombre,
           'precio': self.precio,
           'cantidad': self.cantidad
        }