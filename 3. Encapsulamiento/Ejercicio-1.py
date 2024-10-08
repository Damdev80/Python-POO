class Personas:
    def __init__(self, nombres, apellidos,identidad, fechaDeNacimiento, sexo):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__identidad = identidad
        self.fechaDeNacimiento = fechaDeNacimiento
        self.sexo = sexo
    
    def getName(self):
        return self.__nombres
    
    def getLastname(self):
        return self.__apellidos
    
    def getId(self):
        return self.__identidad

    def changeName(self, newName):
        self.__nombres = newName
        
    def changeLastName(self, LastName):
        self.__apellidos = LastName
        
    def showInfo(self):
        print(f"Nombre: {self.__nombres}\nApellido: {self.__apellidos}\nN° Identidad: {self.__identidad}\nFecha nacimiento: {self.fechaDeNacimiento}\nSexo: {self.sexo}")
persona = Personas("Jorge","Rojas",112345678,"14/09/2000","M")
persona.showInfo