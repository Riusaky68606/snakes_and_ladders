# tests/test_juego.py
from juego.tablero import Tablero
from juego.ficha import Ficha
from juego.dado import Dado
from juego.juego import Juego

def test_posicion_inicial():
    """UAT1: Al iniciar, la ficha está en la casilla 1."""
    ficha = Ficha()
    assert ficha.posicion == 1, "La ficha debe iniciar en la casilla 1."

def test_mover_ficha_una_vez():
    """UAT2: Desde la casilla 1, mover 3 espacios lleva a la casilla 4."""
    tablero = Tablero()
    ficha = Ficha()
    ficha.movimiento(3, tablero)
    assert ficha.posicion == 4, "Mover 3 espacios desde 1 debería colocar la ficha en la casilla 4."

def test_mover_ficha_dos_veces():
    """UAT3: Desde la casilla 1, mover 3 espacios y luego 4 espacios lleva a la casilla 8."""
    tablero = Tablero()
    ficha = Ficha()
    ficha.movimiento(3, tablero)
    ficha.movimiento(4, tablero)
    assert ficha.posicion == 8, "Mover 3 espacios y luego 4 espacios debería colocar la ficha en la casilla 8."

def test_ganar_con_movimiento_exacto():
    """UAT2 - Jugador puede ganar: Desde la casilla 97, mover 3 espacios lleva a la casilla 100."""
    tablero = Tablero()
    ficha = Ficha()
    ficha.posicion = 97
    ficha.movimiento(3, tablero)
    assert ficha.posicion == 100, "Mover 3 espacios desde 97 debe llevar la ficha a la casilla 100."

def test_movimiento_excede_tablero():
    """UAT2 - Jugador no gana si el movimiento excede el tablero: Desde la casilla 97, mover 4 espacios no cambia la posición."""
    tablero = Tablero()
    ficha = Ficha()
    ficha.posicion = 97
    ficha.movimiento(4, tablero)
    assert ficha.posicion == 97, "Si el movimiento excede el tablero, la ficha debe permanecer en la misma casilla."

def test_rango_del_dado():
    """UAT1 - El dado retorna valores entre 1 y 6 inclusive."""
    dado = Dado()
    for _ in range(100):  # Se repite para mayor certeza
        valor = dado.lanzar()
        assert 1 <= valor <= 6, f"El dado retornó {valor}, que no está entre 1 y 6."

def test_lanzar_y_mover():
    """UAT2 - Simulación de dado: Si se mueve la ficha con un valor 4, la posición se incrementa en 4."""
    juego = Juego()
    posicion_inicial = juego.ficha.posicion  # Debería ser 1
    nueva_posicion = juego.move_token(4)
    assert nueva_posicion == posicion_inicial + 4, "La ficha no se movió correctamente 4 espacios."
