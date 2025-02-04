class Tablero:
    def __init__(self, size=100):
        self.size = size

    def movimiento_valido(self, posicion_actual, movimiento):
        """Verifica que el movimiento no exceda el tamaño del tablero."""
        return posicion_actual + movimiento <= self.size
