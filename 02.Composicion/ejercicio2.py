# Ejercicio 2
# Implemente una cuenta telefónica que permite registrar la duración de las  llamadas. A medida que se realizan consumos, estos se van registrando y permiten luego imprimir por pantalla los movimientos. Además, permite agregar saldo a la cuenta y conocer su saldo actual. También existe la posibilidad de ajustar el precio del segundo de llamada en cualquier momento.

class Telefono:
    def __init__(self):
        self.saldo = 0
        self.precio_segundo = 0.1
        self.movimientos = []

    def recargar(self,saldo):
        self.saldo += saldo
        print(f"Su nuevo saldo es de {self.saldo}")
        return
    
    def obtener_saldo(self):
        print(self.saldo)
        return 
    
    def registrar_llamadas(self,duracion):
        costo_llamada = duracion * self.precio_segundo

        if(self.saldo <= 0):
            print('Saldo insuficiente')
        else:
            self.movimientos.append(f'Llamada - duracion {duracion} segundos - Costo: ${costo_llamada: .2f}')

    def imprimir_movimientos(self):  # Cambio de nombre del método
        print("Movimientos de la cuenta")
        for movimiento in self.movimientos:
            print(movimiento)

    def cambiar_costo(self,monto):
        antiguo = self.precio_segundo
        self.precio_segundo = monto
        print(f"el costo paso de {antiguo} a {self.precio_segundo} ")


movistar = Telefono()
movistar.recargar(1000)
movistar.obtener_saldo()
movistar.registrar_llamadas(2)
movistar.imprimir_movimientos()
movistar.cambiar_costo(10)