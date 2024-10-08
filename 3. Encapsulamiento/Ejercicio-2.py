class Producto:
    
    def __init__(self, nombre, precio,cantidad, categoria):
        self.__nombres = nombre
        self.__precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        
    def nombre(self):
        return self.__nombre

    def precio(self):
        return self.__precio

    def cantidad(self, newCantidad):
        self.cantidad = newCantidad

    def categoria(self,newCategoria):
        self.categoria = newCategoria  
    
    def showInfo(self):
        return print(f"El nombre del producto es: {self.__nombres}\nSu precio es {self.__precio}\nExisten {self.cantidad} de unidades\nY es de categoria: {self.categoria}")
    
trapero = Producto("trapero",100,10,"aseo")
trapero.showInfo()
    