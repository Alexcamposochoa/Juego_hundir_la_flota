import numpy as np
import time
import random


def bienvenida():

    import time
    print("Hola grumete!! Bienvenido a tu primera práctica en la flota del general Miguel Pata de palo, yo soy el comandante general de su flota, me llaman Capitán Pytón...")  # time.sleep(2)
    print("...       ...       ...")
    time.sleep(4)
    print("Para el día de hoy tenemos una misión sencilla, tendrás que destruir todos los barcos de la flota de nuestros temibles enemigos 'La banda de los TA's malvados'")
    time.sleep(4)
    print("...       ...       ...")
    time.sleep(4)
    print("Pero antes de continuar, ¿como demonios te llamas?")
    time.sleep(3)
    nombre = input("Escribe tu nick de grumete")
    print(
        f"Muy bien!{nombre} espero que estés preparad@ para lo que te espera")
    time.sleep(4)
    print("Vamos a darle caña a estos bribones")
    time.sleep(3)
    print("...       ...       ...")
    time.sleep(2)
    print("La dinámica es sencilla, se colocarán los barcos de manera aleatoria y tú comenzarás disparando en la coordenada que creas que se han escondido estos granujas.")
    time.sleep(4)
    print("Por ejemplo: Coordenada 0 del eje X , coordenada 5 del eje Y!!! DISPAREEEEN!!!MUahahahaHAHahAHahAHa")
    time.sleep(4)
    print("Si acertaste te mostraremos esa casilla con una 'X'")
    time.sleep(4)
    print("En caso de no haber pillado cacho mostraremos la casilla con un '~'")
    time.sleep(3)
    print("...       ...       ...")
    time.sleep(2)
    print("Cada participante tiene una flota compuesta por 10 barcos en total. 1 barco de 4 casillas, 2 barcos de 3 casillas, 3 barcos de 2 casillas y 4 barcos de 1 casilla")
    time.sleep(4)
    print("Que hacen un total de 20 vidas")
    time.sleep(2)
    print("El primero que consiga destruir todos los barcos del enemigo y lo deje sin vidas, ganará la batalla")
    time.sleep(3)
    print("Estás preparad@?")
    time.sleep(2)


def crear_tablero(tamaño=(10, 10)):
    tablero = np.full(tamaño, ' ')
    return tablero


def colocar_barcos(tablero):
    eslora_barcos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    for eslora in eslora_barcos:
        while True:
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(["horizontal", "vertical"])

            if orientacion == "horizontal":
                if columna + eslora <= 10 and all(tablero[fila, i] == ' ' for i in range(columna, columna + eslora)):
                    for i in range(columna, columna + eslora):
                        tablero[fila, i] = str(eslora)
                    break
            else:
                if fila + eslora <= 10 and all(tablero[i, columna] == ' ' for i in range(fila, fila + eslora)):
                    for i in range(fila, fila + eslora):
                        tablero[i, columna] = str(eslora)
                    break


def disparo_jugador(tablero, tablero_maquina, tablero_adivinar, vidas_jugador, vidas_maquina):
    import time
    time.sleep(2)
    print("Recuerda que las coordenadas van del 0 al 9 grumete, no te equivoques!!")
    time.sleep(1)

    # Sistema básico de vidas, siempre que sean mayor a 0
    while vidas_jugador > 0 and vidas_maquina > 0:
        print("                                     ")
        frase = random.choice(["Observa el mar y dime las coordenadas donde quieres disparar grumete, confía en la fuerza....",
                              "Vamos!! donde crees que se han escondido esos granujas!", "Grita las coordenadas y hunde sus barcos!"])
        print(frase)
        print("                                     ")
        print(tablero_adivinar)
        print("                                     ")

        # inputs de las coordenadas
        fila = int(input("Mete el número de la fila entre 0 y 9: "))
        columna = int(
            input("Ahora mete el número de la columna entre 0 y 9: "))
        print(
            f"Disparen en la fila {fila} y en la columna {columna}!! Arrrr marineros!!")
        print("                                     ")

        if 0 <= fila < 10 and 0 <= columna < 10:  # comprueba que los inputs estén bien
            # comprobamos las coordenadas en el tablero de la maquina
            if tablero_maquina[fila, columna] == ' ':
                # modificamos el tablero_adivinar
                tablero_adivinar[fila, columna] = '~'
                print(tablero_adivinar)
                print("Agua!! Has fallado, turno del enemigo!")
                time.sleep(1.5)
                print("...      ...      ...")
                time.sleep(1.5)
                print("Turno del enemigo grumete!!!")
                print("                                     ")
                time.sleep(1.5)
                print("                                     ")
                print(f" Nos quedan {vidas_jugador} vidas")
                print("                                     ")
                time.sleep(1.5)
                print("                                     ")
                turno_maquina(tablero, vidas_jugador)

            # comprueba si las coordenadas coinciden con un digito
            elif tablero_maquina[fila, columna].isdigit():
                # modifica el tablero adivinar y marca "X"
                tablero_adivinar[fila, columna] = 'X'
                print(tablero_adivinar)
                print("Tocado!! Les diste en toda la madre, ¡sigue así!")
                print("                                     ")
                vidas_maquina -= 1  # resta 1 y añade modificacion a la lista de vidas de la maquina
                print(
                    f"A la banda de los TA's les quedan {vidas_maquina} vidas")

            else:
                # seguridad en caso de repeticion
                print(
                    "Ya has disparado en esa casilla o has metido una coordenada incorrecta. Vuelve a intentarlo.")

        else:
            # seguridad en caso de error de inputs
            print("Coordenadas fuera de los límites del tablero. Inténtalo de nuevo.")

    if vidas_jugador == 0:  # fin del juego si las vidas llegan a 0
        print(
            "Grumete... tengo una mala noticia, no nos quedan barcos, hemos sido derratos.")
        print("¡Los malvados TA's han ganado!")
    else:
        print(" ")
        print("*redoble de tambores*")
        time.sleep(1)
        print("*suenan las trompetas*")
        time.sleep(1)
        print("GRUMETE!!!! Tengo una noticia estupenda, no quedan barcos en el horizonte!!")
        time.sleep(1)
        print("Has derrotado a la banda de los TA's malvados!!! Enhorabuena!!")
        time.sleep(1)
        print("HAS GANADO!!")


def turno_maquina(tablero, vidas_jugador):

    # while infinito que dispara la funcion y comprueba si el jugador tiene vidas.
    while vidas_jugador > 0:
        # random para determinar el disparo de la maquina en fila y columna
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        print(
            f"Los malvados TA's han disparo en la fila {fila}, columna {columna}")
        time.sleep(1.5)
        print("                                     ")

        if tablero[fila, columna] == ' ':  # comprueba si está vacio
            tablero[fila, columna] = '~'  # modfica el tablero del jugador
            print(tablero)
            print("                                     ")
            time.sleep(1.5)
            print("Agua!! jaJÁ El enemigo ha fallado.")
            print("                                     ")
            time.sleep(2)
            print("Ahora es nuestro momento, aprovecha y no falles!!")
            return  # esta funcion ha sido llamada dentro de otra, con lo que este return saca el flujo al bucle while del disparo jugador

        elif tablero[fila, columna].isdigit():  # comprueba si hay un barco (un digito)
            tablero[fila, columna] = 'X'  # modifica el tablero
            print(tablero)
            print("Nos han dado grumete!! Tocado!!.")
            time.sleep(2)
            vidas_jugador -= 1  # resta 1 y añade modificacion a la lista de vidas de la maquina
            print(f"Nos quedan {vidas_jugador} vidas!.")


tablero = crear_tablero()
tablero_maquina = crear_tablero()
tablero_adivinar = crear_tablero()
vidas_jugador = 20
vidas_maquina = 5

bienvenida()
colocar_barcos(tablero)
print("Mostramos el tablero_maquina solo para la demo")
print("                                     ")
colocar_barcos(tablero_maquina)
print(tablero_maquina)
print("                                     ")
disparo_jugador(tablero, tablero_maquina, tablero_adivinar,
                vidas_jugador, vidas_maquina)
