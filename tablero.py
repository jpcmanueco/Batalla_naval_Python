# tablero.py
import numpy as np

class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.grid = np.full((tamaño, tamaño), '.', dtype=str)
    
    def mostrar(self):
        for fila in self.grid:
            print(' '.join(fila))
    
    def colocar_barco(self, fila, columna, tamaño, orientación):
        if not self.verificar_colocacion_valida(fila, columna, tamaño, orientación):
            raise ValueError("No se puede colocar el barco en esta posición.")

        if orientación == 'horizontal':
            self.grid[fila, columna:columna + tamaño] = 'X'
        elif orientación == 'vertical':
            self.grid[fila:fila + tamaño, columna] = 'X'
    
    def verificar_colocacion_valida(self, fila, columna, tamaño, orientación):
        if orientación == 'horizontal':
            if columna + tamaño > self.tamaño:
                return False
            if any(self.grid[fila, columna + i] != '.' for i in range(tamaño)):
                return False
        elif orientación == 'vertical':
            if fila + tamaño > self.tamaño:
                return False
            if any(self.grid[fila + i, columna] != '.' for i in range(tamaño)):
                return False
        else:
            return False
        return True
    
    def realizar_disparo(self, fila, columna):
        if self.grid[fila, columna] == 'X':
            self.grid[fila, columna] = 'H'
            print("¡Impacto!")
            return True
        else:
            self.grid[fila, columna] = 'A'
            print("¡Agua!")
            return False
    
    def todos_hundidos(self):
        return 'X' not in self.grid
