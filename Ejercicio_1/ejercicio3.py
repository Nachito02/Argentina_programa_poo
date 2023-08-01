# Ejercicio 3
# Se desea representar puntos en el plano (2 dimensiones) mediante un par ordenado de valores (x,y). La representación debe poder:
# Calcular la distancia del punto con otro cualquiera en el plano. 
# Crear un punto a partir de la suma de sí mismo con otro punto cualquiera.
# Además, se deberá poder mantener la mayor distancia al origen de todos los puntos creados como un único dato común.

import math

class Punto:
    distancia_maxima_al_origen = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distancia_al_origen = math.sqrt(x ** 2 + y ** 2)

        if self.distancia_al_origen > Punto.distancia_maxima_al_origen:
            Punto.distancia_maxima_al_origen = self.distancia_al_origen

    def distancia_con(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)

    def suma_con(self, otro_punto):
        nuevo_x = self.x + otro_punto.x
        nuevo_y = self.y + otro_punto.y
        return Punto(nuevo_x, nuevo_y)

# Programa cliente
def main():
    # Ingresar coordenadas para el primer punto
    x1 = float(input("Ingrese la coordenada x del primer punto: "))
    y1 = float(input("Ingrese la coordenada y del primer punto: "))
    punto1 = Punto(x1, y1)

    # Ingresar coordenadas para el segundo punto
    x2 = float(input("Ingrese la coordenada x del segundo punto: "))
    y2 = float(input("Ingrese la coordenada y del segundo punto: "))
    punto2 = Punto(x2, y2)

    # Calcular y mostrar distancia entre los dos puntos
    distancia_entre_puntos = punto1.distancia_con(punto2)
    print(f"La distancia entre los puntos es: {distancia_entre_puntos:.2f}")

    # Crear un tercer punto como la suma de los dos primeros
    punto3 = punto1.suma_con(punto2)
    print(f"Las coordenadas del tercer punto son: ({punto3.x}, {punto3.y})")

    # Mostrar la mayor distancia al origen de todos los puntos creados
    print(f"La mayor distancia al origen es: {Punto.distancia_maxima_al_origen:.2f}")

if __name__ == "__main__":
    main()
