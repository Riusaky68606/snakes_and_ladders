class Ficha:
    def __init__(self):
        self.posicion = 1  # Se empieza desde la casilla 1

    def movimiento(self, espacios, tablero):
        # Si el movimiento excede el tablero, la posición se mantiene igual.
        if tablero.movimiento_valido(self.posicion, espacios):
            self.posicion += espacios
        return self.posicion
