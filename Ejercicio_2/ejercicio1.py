# Ejercicio 1 
# En Python los objetos se pueden comparar por igualdad (==) o por identidad (is). Si dos objetos son idénticos, también son iguales. Sin embargo, dos objetos pueden ser iguales sin ser idénticos. Por ejemplo, dos variables pueden tener el mismo valor, pero apuntar a dos objetos diferentes.
# Implemente la clase Ciudadano, la cual permita identificar ciudadanos a partir de su DNI, nombre y apellido y permita compararlos a partir de su edad.
# Defina los métodos mágicos: __eq__,__le__,__lt__,__ge__,__gt__

class Ciudadano:
    def __init__(self, dni,nombre,apellido,edad):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __eq__(self,other):
        return self.edad == other.edad

    def __le__(self, other):
        return self.edad <= other.edad         
    
    def __lt__(self, other):
        return self.edad < other.edad
    
    def __ge__(self, other):
        return self.edad >= other.edad
    
    def __gt__(self,other):
        return self.edad > other.edad
    

ciudadano1 = Ciudadano(dni="12345678", nombre="Juan", apellido="Perez", edad=30)
ciudadano2 = Ciudadano(dni="98765432", nombre="Maria", apellido="Lopez", edad=25)

print(ciudadano1 == ciudadano2)  # False, ya que tienen edades diferentes
print(ciudadano1 <= ciudadano2)  # False, ciudadano1 es mayor que ciudadano2
print(ciudadano1 < ciudadano2)   # False, ciudadano1 es mayor o igual que ciudadano2
print(ciudadano1 >= ciudadano2)  # True, ciudadano1 es mayor que ciudadano2
print(ciudadano1 > ciudadano2)   # True, ciudadano1 es mayor que ciudadano2