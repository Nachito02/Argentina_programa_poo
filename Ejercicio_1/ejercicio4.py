import math

class Circulo:
    def __init__(self, centro_x, centro_y, radio):
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def esta_punto_dentro(self, punto_x, punto_y):
        distancia_centro_punto = math.sqrt((punto_x - self.centro_x) ** 2 + (punto_y - self.centro_y) ** 2)
        return distancia_centro_punto <= self.radio

# Programa cliente
def main():
    # Obtener datos del círculo
    centro_x = float(input("Ingrese la coordenada x del centro del círculo: "))
    centro_y = float(input("Ingrese la coordenada y del centro del círculo: "))
    radio = float(input("Ingrese el radio del círculo: "))
    
    # Crear objeto circulo
    circulo = Circulo(centro_x, centro_y, radio)

    # Calcular y mostrar el área y perímetro del círculo
    print(f"El área del círculo es: {circulo.area():.2f}")
    print(f"El perímetro del círculo es: {circulo.perimetro():.2f}")

    # Verificar si un punto está dentro o fuera del círculo
    punto_x = float(input("Ingrese la coordenada x del punto: "))
    punto_y = float(input("Ingrese la coordenada y del punto: "))

    if circulo.esta_punto_dentro(punto_x, punto_y):
        print("El punto está dentro del círculo.")
    else:
        print("El punto está fuera del círculo.")

if __name__ == "__main__":
    main()
