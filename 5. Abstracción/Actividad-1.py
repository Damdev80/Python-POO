#Ejercicio 2: Crea una clase abstracta Empleado con un método abstracto calcular_salario(). Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen calcular_salario() de manera distinta.
import time
from os import system

class Empleado:
    def __init__(self,nombre, cargo, edad):
        self.nombre = nombre
        self.cargo = cargo 
        self.edad = edad
        
    def calcular_salario(self):
        
        system("cls")
        print("------------------------------------------")
        print("Calculando el sueldo de su empleado")
        print("------------------------------------------")
        time.sleep(3)
        sueldo = 1462000
        system("cls")
        confirmacion = input("¿Su empleado esta aferrado al salario minimo mas sus prestaciones sociales? y/n")
        resultado = confirmacion.lower()
        if confirmacion == "y":
            system("cls")
            return print(f"El sueldo a pagar a su empleado es de: ${sueldo} pesos colombianos")
        else:
            system("cls")
            Horas = input("¿Cuantas horas trabajo su empleado? Ingrese aqui:")
            Sueldo = Horas * 4833
            print(f"El sueldo e su empleado es de: ${sueldo} pesos colombianis")
            
        
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, cargo, edad):
        super().__init__(nombre, cargo, edad)

    
    def calcular_salario(self):
        
        system("cls")
        print("------------------------------------------")
        print("Calculando el sueldo de su empleado")
        print("------------------------------------------")
        time.sleep(3)
        sueldo = 1462000
        system("cls")
        confirmacion = input("¿Su empleado esta aferrado al salario minimo mas sus prestaciones sociales? y/n")
        resultado = confirmacion.lower()
        if confirmacion == "y":
            system("cls")
            return print(f"El sueldo a pagar a su empleado es de: ${sueldo} pesos colombianos")
        else:
            system("cls")
            Horas = input("¿Cuantas horas trabajo su empleado? Ingrese aqui:")
            Sueldo = Horas * 4833
            print(f"El sueldo e su empleado es de: ${sueldo} pesos colombianis")
            
            
            
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, cargo, edad):
        super().__init__(nombre, cargo, edad)
    
    def calcular_salario(self):
        
        system("cls")
        print("------------------------------------------")
        print("Calculando el sueldo de su empleado")
        print("------------------------------------------")
        time.sleep(3)
        sueldo = 1462000
        system("cls")
        confirmacion = input("¿Su empleado esta aferrado al salario minimo mas sus prestaciones sociales? y/n")
        resultado = confirmacion.lower()
        if confirmacion == "y":
            system("cls")
            return print(f"El sueldo a pagar a su empleado es de: ${sueldo} pesos colombianos")
        else:
            system("cls")
            Horas = input("¿Cuantas horas trabajo su empleado? Ingrese aqui:")
            Sueldo = Horas * 4833
            print(f"El sueldo e su empleado es de: ${sueldo} pesos colombianis")
            
            
empleado1 = EmpleadoTiempoCompleto("Daniel","Ingeniero",18)
empleado1.calcular_salario()
