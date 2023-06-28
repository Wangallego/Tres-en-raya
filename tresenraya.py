

class TresEnRaya:
    FICHA_O = 'O'
    FICHA_X = 'X'
    CASILLA_VACIA = 0
    def __init__(self):
        self.tablero = [[TresEnRaya.CASILLA_VACIA for _ in range(3)]for _ in range(3)]
        
   
    
    def colocarFicha(self, y, x, ficha):
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise ValueError("Posicion incorrecta")
        if self.tablero[y][x] != TresEnRaya.CASILLA_VACIA:
            raise ValueError("La casilla está ocupada")  
        else:
            self.tablero[y][x] = ficha
    def __str__(self) -> str:#Nombre reservado, el objetivo es transformar un objeto de ka clase tresEnRaya en un Str
        tablero_str = ""
        for fila in self.tablero:
            fila_str = " | ".join(str(casilla) for casilla in fila)
            tablero_str += f"{fila_str}\n{'-' * 9}\n"
        return tablero_str
    
    def ganador(self):
        CASILLA_VACIA = 0
        #Filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != CASILLA_VACIA:
                return fila[0]
        #Columnas
        for k in range(3):
            if self.tablero[0][k] == self.tablero[1][k] == self.tablero[2][k] != CASILLA_VACIA:
                return self.tablero[0][k]
         #Diagonales   
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != CASILLA_VACIA) or (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != CASILLA_VACIA):
            return self.tablero[1][1]
        else:
            return 0
    def juegoTerminado(self):
        return self.ganador() or all(self.tablero[x][y]  for x in range(3) for y in range(3))
   

class Jugador:

    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

    def colocarFicha(self, tablero, y, x):
        TresEnRaya.colocarFicha(tablero, y, x, self.ficha)

import random

class Juego:
    def __init__(self, jugador1, jugador2,):
        self.tablero = TresEnRaya()
        self.jugadores = []
        self.turno = 0

    def correrJuego(self):

        modo_juego = int(input("Modo de juego:\n1. Jugar contra otro jugador\n2. Jugar contra la máquina\n3.Maquina VS Maquina \nElige una opción: "))
        """
        Aqui preguntamos primero el modo de juego, luego le decimos que guadores se añaden segun
        la eleccion del jugador
        """
        if modo_juego == 1:
            print("¡Jugando contra otro jugador!")
            jugador1 = Jugador("Jugador 1", TresEnRaya.FICHA_O)
            self.jugadores.append(jugador1)
            jugador2 = Jugador("Jugador 2", TresEnRaya.FICHA_X)
            self.jugadores.append(jugador2)
        elif modo_juego == 2:
            jugador1 = Jugador("Jugador 1", TresEnRaya.FICHA_O)
            self.jugadores.append(jugador1)
            print("¡Jugando contra la máquina!")
            jugador2 = JugadorMaquina("Máquina", TresEnRaya.FICHA_X)
            self.jugadores.append(jugador2)
        elif modo_juego == 3:
            jugador1 = JugadorMaquina("Maquina 1", TresEnRaya.FICHA_O)
            self.jugadores.append(jugador1)
            print("Maquina VS Maquina")
            jugador2 = JugadorMaquina("Máquina 2", TresEnRaya.FICHA_X)
            self.jugadores.append(jugador2)
        else:
            print("Opción inválida. Se jugará contra otro jugador por defecto.")
        
        """
        Iniciamos el metodo de juego, declarando jugadores actuales, que previamente se han
        seleccionado con los modos de juego, mostramos el tablero y hacemos que vaya eligiendo las fichas
        tanto si son jugadores como si es la maquina.
        """
        """
        Hicimos un try except para comprobar si esta fuera de la fila no mete los numeros etc
        """


        while True:
            jugador_actual = self.jugadores[self.turno]
            ficha = jugador_actual.ficha

            # Mostrar el estado actual del tablero
            print(self.tablero)

            # Pedir al jugador que coloque una ficha
            if isinstance(jugador_actual, JugadorMaquina):
                fila, columna = jugador_actual.generarMovimiento(self.tablero)
                print(f"{jugador_actual.nombre} ha elegido la posición: ({fila}, {columna})")
            else:
                fila = int(input(f"{jugador_actual.nombre}, ingresa la fila: "))
                columna = int(input(f"{jugador_actual.nombre}, ingresa la columna: "))

            try:
                self.tablero.colocarFicha(fila, columna, ficha)
            except ValueError as error:
                print(error)
                continue

            # Verificar si hay un ganador
            ganador = self.tablero.ganador()
            if ganador != 0:
                print(self.tablero)
                print(f"¡{jugador_actual.nombre} ha ganado!")
                break

            # Verificar si hay empate
            if self.tablero.juegoTerminado():
                print("El juego ha terminado en empate.")
                break

            # Cambiar al siguiente turno
            self.turno = (self.turno + 1) % len(self.jugadores)
        """
        Aqui indicamos el metodo de juego para el jugador maquina, comprobamos que la casilla que quiera poner 
        este vacia, y la almacena en un array vacio, para luego poder seleccionar de manera random las posiciones
        """

class JugadorMaquina(Jugador):
    def generarMovimiento(self, tablero):
        # Generar una posición aleatoria no ocupada en el tablero
        posiciones_vacias = []
        for fila in range(3):
            for columna in range(3):
                if tablero.tablero[fila][columna] == TresEnRaya.CASILLA_VACIA:
                    posiciones_vacias.append((fila, columna))
        
        if posiciones_vacias:
            return random.choice(posiciones_vacias)
        else:
            raise ValueError("No hay posiciones disponibles en el tablero.")

        """
        Aqui corremos el juego 
        """
    def correrJuego(self):
        while True:
            jugador_actual = self.jugadores[self.turno]
            ficha = jugador_actual.ficha

            # Mostrar el estado actual del tablero
            print(self.tablero)

            # Pedir al jugador que coloque una ficha
            fila = int(input(f"{jugador_actual.nombre}, ingresa la fila: "))
            columna = int(input(f"{jugador_actual.nombre}, ingresa la columna: "))

            try:
                self.tablero.colocarFicha(fila, columna, ficha)
            except ValueError as error:
                print(error)
                continue

            # Verificar si hay un ganador
            ganador = self.tablero.ganador()
            if ganador != 0:
                print(f"¡{jugador_actual.nombre} ha ganado!")
                break

            # Verificar si hay empate
            if self.tablero.juegoTerminado():
                print("El juego ha terminado en empate.")
                break

            # Cambiar al siguiente turno
            self.turno = (self.turno + 1) % 2

if __name__ == "__main__":
    jugador1 = Jugador("Jugador 1", TresEnRaya.FICHA_O)
    jugador2 = Jugador("Jugador 2", TresEnRaya.FICHA_X)
  
    juego = Juego (jugador1, jugador2)
    juego.correrJuego()


