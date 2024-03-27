# funciones.py

from tablero import Tablero
import random
from variables import barco_tamaños

def mostrar_tablero(tablero):
    for fila in tablero.grid:
        print(" ".join(fila))

def colocar_barcos_jugador(tablero):
    print("Posiciona tus barcos:")
    for tamaño in barco_tamaños:
        mostrar_tablero(tablero)
        while True:
            try:
                fila = int(input(f"Ingrese la fila para el barco de tamaño {tamaño}: "))
                columna = int(input(f"Ingrese la columna para el barco de tamaño {tamaño}: "))
                orientación = input("Ingrese la orientación (horizontal o vertical): ").lower()
                tablero.colocar_barco(fila, columna, tamaño, orientación)
                break
            except (ValueError, IndexError):
                print("¡Coordenadas inválidas! Inténtalo de nuevo.")

def colocar_barcos_bot(tablero):
    tamaño = 4
    for tamaño in barco_tamaños:
        fila, columna = random.randint(0, len(tablero.grid) - 1), random.randint(0, len(tablero.grid) - 1)
        orientación = random.choice(['horizontal', 'vertical'])
        while not tablero.verificar_colocacion_valida(fila, columna, tamaño, orientación):
            fila, columna = random.randint(0, len(tablero.grid) - 1), random.randint(0, len(tablero.grid) - 1)
            orientación = random.choice(['horizontal', 'vertical'])
        tablero.colocar_barco(fila, columna, tamaño, orientación)

def realizar_disparo(fila, columna, tablero):
    if tablero.grid[fila][columna] == 'X':
        tablero.grid[fila][columna] = 'H'
        print("¡Impacto!")
        return True
    else:
        tablero.grid[fila][columna] = 'A'
        print("Agua!")
        return False

def turno_maquina(tablero):
    fila = random.randint(0, len(tablero.grid) - 1)
    columna = random.randint(0, len(tablero.grid) - 1)
    print(f"El bot dispara en la fila {fila}, columna {columna}")
    acierto = realizar_disparo(fila, columna, tablero)
    if verificar_fin_juego(tablero):
        print("¡El bot ha ganado!")
        return False
    return acierto

def verificar_fin_juego(tablero):
    for fila in tablero.grid:
        for celda in fila:
            if celda == 'X':
                return False
    return True
