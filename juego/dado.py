import random

class Dado:
    def lanzar(self):
        # Devuelve un número aleatorio entre 1 y 6 (inclusive).
        return random.randint(1, 6)
