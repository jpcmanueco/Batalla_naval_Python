# funciones.py
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
                print("¡Coordenadas inválidas o barco no cabe en esta posición! Inténtalo de nuevo.")

def colocar_barcos_bot(tablero):
    for tamaño in barco_tamaños:
        colocado = False
        while not colocado:
            fila, columna = random.randint(0, tablero.tamaño - 1), random.randint(0, tablero.tamaño - 1)
            orientación = random.choice(['horizontal', 'vertical'])
            try:
                tablero.colocar_barco(fila, columna, tamaño, orientación)
                colocado = True
            except ValueError:
                continue

def realizar_disparo(fila, columna, tablero):
    return tablero.realizar_disparo(fila, columna)

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
    return tablero.todos_hundidos()

