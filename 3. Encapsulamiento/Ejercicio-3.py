class Libro:
    
    def __init__(self, titulo, autor,isbn, editorial ):
        self.__titulos = titulo
        self.__autor = autor
        self.isbn = isbn
        self.editorial  = editorial 
        
    def titulo(self):
        return self.__titulo

    def autor(self):
        return self.__autor

    def isbn(self, newisbn):
        self.isbn = newisbn

    def editorial (self,neweditorial ):
        self.editorial  = neweditorial   
    
    def showInfo(self):
        return print(f"El titulo del Libro es: {self.__titulos}\nSu autor es {self.__autor}\nSu isbn {self.isbn}\nY es de la editorial : {self.editorial }")
    
trapero = Libro("trapero",100,10,"aseo")
trapero.showInfo()
    