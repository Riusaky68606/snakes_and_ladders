from juego.tablero import Tablero
from juego.ficha import Ficha
from juego.dado import Dado

class Juego:
    def __init__(self):
        self.tablero = Tablero()  # Por defecto, tamaño 100
        self.ficha = Ficha()      # La ficha inicia en la casilla 1
        self.dado = Dado()        # Instancia del dado

    def move_token(self, espacios):
        """
        Mueve la ficha el número de espacios indicado y retorna la nueva posición.
        """
        return self.ficha.movimiento(espacios, self.tablero)

    def lanzar_y_mover(self):
        """
        Simula el lanzamiento del dado y mueve la ficha en consecuencia.
        Retorna una tupla (valor_del_dado, nueva_posicion).
        """
        valor_dado = self.dado.lanzar()
        nueva_posicion = self.move_token(valor_dado)
        return valor_dado, nueva_posicion

    def ha_ganado(self):
        """
        Retorna True si la ficha llegó a la casilla final (tamaño del tablero).
        """
        return self.ficha.posicion == self.tablero.size
