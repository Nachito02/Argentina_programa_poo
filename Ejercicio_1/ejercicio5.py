import random

class DadoNoConvencional:
    def __init__(self, caras):
        self.caras = caras

    def lanzar(self):
        return random.choice(self.caras)

def competencia_dados(jugador1, jugador2):
    resultados_jugador1 = []
    resultados_jugador2 = []

    for _ in range(3):
        resultados_jugador1.append(jugador1.lanzar())
        resultados_jugador2.append(jugador2.lanzar())

    print("Resultados del jugador 1:", resultados_jugador1)
    print("Resultados del jugador 2:", resultados_jugador2)

    ganador_jugador1 = all(x <= y for x, y in zip(resultados_jugador1, resultados_jugador2))
    ganador_jugador2 = all(x >= y for x, y in zip(resultados_jugador1, resultados_jugador2))

    if ganador_jugador1:
        print("¡El jugador 1 gana la competencia!")
    elif ganador_jugador2:
        print("¡El jugador 2 gana la competencia!")
    else:
        print("La competencia termina en empate.")

if __name__ == "__main__":
    # Crea dos dados no convencionales con diferentes caras
    jugador1 = DadoNoConvencional([1, 2, 3, 4, 5, 6])
    jugador2 = DadoNoConvencional([2, 4, 6, 8, 10, 12])

    # Inicia la competencia
    competencia_dados(jugador1, jugador2)
