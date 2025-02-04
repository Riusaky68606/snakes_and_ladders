from juego.juego import Juego


def main():
    juego = Juego()
    print("Bienvenido a Snakes and Ladders")
    print(f"Tu ficha comienza en la casilla {juego.ficha.posicion}")
    
    while not juego.ha_ganado():
        input("Presiona Enter para lanzar el dado...")
        valor_dado, nueva_posicion = juego.lanzar_y_mover()
        print(f"Has sacado un {valor_dado}. Tu ficha se mueve a la casilla {nueva_posicion}.")
        if juego.ha_ganado():
            print("¡Felicidades, has ganado el juego!")
            break

if __name__ == '__main__':
    main()
