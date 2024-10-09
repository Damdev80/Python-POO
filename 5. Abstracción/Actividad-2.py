
import time
from os import system

class TareaEmpleado:
    def __init__(self,nombre, cargo, edad):
        self.nombre = nombre
        self.cargo = cargo 
        self.edad = edad
        
    def realizar_tarea(self):
        system("cls")
        print("------------------------------------------")
        print("Cargando Tareas...")
        print("------------------------------------------")
        time.sleep(3)
        system("cls")
        confirmacion = input(f"¿El empleado: {self.nombre} tiene alguna tarea? y/n: ")
        resultado = confirmacion.lower()
        if resultado == "y":
            system("cls")
            Task = []
            Tareas = int(input("Ingrese cuántas tareas tiene el empleado: "))
            for i in range(Tareas):
                NumeroDeTareas = input(f"Ingrese la tarea que tiene que hacer el {self.cargo} {self.nombre}: ")
                Task.append(NumeroDeTareas)
            print(f"{self.nombre} tiene que hacer: {'y '.join(Task)}")
        else:
            system("cls")
            print(f"El {self.cargo} {self.nombre} no tiene ninguna tarea asignada.")
            
        
class Ingeniero  (TareaEmpleado):
    def __init__(self, nombre, cargo, edad):
        super().__init__(nombre, cargo, edad)

    
    def realizar_tarea(self):
        system("cls")
        print("------------------------------------------")
        print("Cargando Tareas...")
        print("------------------------------------------")
        time.sleep(3)
        system("cls")
        confirmacion = input(f"¿El empleado: {self.nombre} tiene alguna tarea? y/n: ")
        resultado = confirmacion.lower()
        if resultado == "y":
            system("cls")
            Task = []
            Tareas = int(input("Ingrese cuántas tareas tiene el empleado: "))
            for i in range(Tareas):
                NumeroDeTareas = input(f"Ingrese la tarea que tiene que hacer el {self.cargo} {self.nombre}: ")
                Task.append(NumeroDeTareas)
            print(f"{self.nombre} tiene que hacer: {'y '.join(Task)}")
        else:
            system("cls")
            print(f"El {self.cargo} {self.nombre} no tiene ninguna tarea asignada.")
            
            
            
class Doctor  (TareaEmpleado):
    def __init__(self, nombre, cargo, edad):
        super().__init__(nombre, cargo, edad)
    
    def realizar_tarea(self):
        system("cls")
        print("------------------------------------------")
        print("Cargando Tareas...")
        print("------------------------------------------")
        time.sleep(3)
        system("cls")
        confirmacion = input(f"¿El empleado: {self.nombre} tiene alguna tarea? y/n: ")
        resultado = confirmacion.lower()
        if resultado == "y":
            system("cls")
            Task = []
            Tareas = int(input("Ingrese cuántas tareas tiene el empleado: "))
            for i in range(Tareas):
                NumeroDeTareas = input(f"Ingrese la tarea que tiene que hacer el {self.cargo} {self.nombre}: ")
                Task.append(NumeroDeTareas)
            print(f"{self.nombre} tiene que hacer: {' y '.join(Task)}")
        else:
            system("cls")
            print(f"El {self.cargo} {self.nombre} no tiene ninguna tarea asignada.")
            
            

TareaEmpleado2 = Doctor("Daniel","Doctor ",18)
TareaEmpleado2.realizar_tarea()

