from funciones import *
from variables import *

bienvenida()
colocar_barcos(tablero)
print("Mostramos el tablero_maquina solo para la demo")
print("                                     ")
colocar_barcos(tablero_maquina)
print(tablero_maquina)
print("                                     ")
disparo_jugador(tablero, tablero_maquina, tablero_adivinar,
                vidas_jugador, vidas_maquina)
