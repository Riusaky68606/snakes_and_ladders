# Snakes and Ladders 

Este proyecto es una implementación del juego **Snakes and Ladders** (Serpientes y Escaleras) en Python. Se ha desarrollado con un enfoque en la programación orientada a objetos (POO) y cuenta con una suite de pruebas unitarias (utilizando **pytest**)

---

## Resumen del Proyecto

- **Objetivo:**  
  Implementar la lógica básica del juego donde la ficha del jugador se mueve según el lanzamiento de un dado y se verifica la condición de victoria (alcanzar la casilla final del tablero).

- **Características Implementadas:**  
  - **Movimiento de la ficha:**  
    La ficha inicia en la casilla 1 y se mueve de acuerdo al valor obtenido al lanzar el dado. Si el movimiento supera la casilla final, la ficha no se mueve.
  - **Condición de victoria:**  
    Cuando la ficha llega exactamente a la última casilla (por defecto, 100), se considera que el jugador ha ganado.
  - **Lanzamiento del dado:**  
    El dado genera números aleatorios entre 1 y 6, añadiendo un elemento de azar al juego.
  - **Pruebas Unitarias:**  
    Se han creado tests para verificar que:
    - La ficha inicia en la casilla 1.
    - El movimiento de la ficha se realiza correctamente (por ejemplo, mover 3 y luego 4 espacios lleva a la casilla 8).
    - La ficha llega a la casilla final con el movimiento exacto.
    - No se mueve la ficha si el movimiento excede el tamaño del tablero.
    - El dado siempre retorna un valor entre 1 y 6.

- **Resultados Esperados:**  
  Al ejecutar la aplicación, se mostrará en la consola la posición inicial de la ficha y, tras cada lanzamiento del dado, la nueva posición. Cuando la ficha alcance la casilla final, se mostrará un mensaje de felicitación. Los tests deben confirmar que la lógica del juego funciona según lo especificado.
![image](https://github.com/user-attachments/assets/240783af-beb6-49cd-bd46-40a1d5c30bda)


## Requisitos

- **Python 3.6+**
- **pytest** 
