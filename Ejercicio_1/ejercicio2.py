# Ejercicio 2
# Se desea calcular el área de un rectángulo conociendo su base y su altura. Implemente una solución utilizando POO. En un programa cliente solicite los datos de dos rectángulos y calcule sus respectivas áreas.


class Rectangle:
    def __init__(self, base, altura):
        self.base= base
        self.altura= altura

    def calculateArea(self):
        area = self.base * self.altura
        print(f"el area del rectangulo es {area}")
        
base1 = int(input(f"ingrese la base del primer rectangulo"))
altura1 = int(input(f"ingrese la altura del primer rectangulo"))
rectangulo1 = Rectangle(base1, altura1)


base2 = int(input(f"ingrese la base del segundo rectangulo"))
altura2 = int(input(f"ingrese la altura del segundo rectangulo"))

rectangulo2 = Rectangle(base2, altura2)

rectangulo1.calculateArea()
rectangulo2.calculateArea()



