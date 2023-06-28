#EN
Tic-Tac-Toe Game
This is a simple implementation of the Tic-Tac-Toe game (also known as "Three-in-a-Row") in Python. The game can be played in different modes, including:

Player vs Player: Two human players take turns playing against each other.
Player vs Computer: A human player plays against the computer.
Computer vs Computer: Two computer players play against each other.
Game Rules->
The game is played on a 3x3 grid.
Player 1 uses the "O" symbol, and Player 2 (or the computer) uses the "X" symbol.
Players take turns placing their symbols on empty cells.
The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.
If all cells are filled and no player has won, the game is a draw.
Usage->
Run the game.py file to start the game.
Choose the game mode:
Enter 1 for Player vs Player.
Enter 2 for Player vs Computer.
Enter 3 for Computer vs Computer.
Player vs Player->
Player 1 will be prompted to enter their moves by specifying the row and column.
Player 2 will then enter their moves in the same way.
The game will continue until a player wins or it's a draw.
Player vs Computer ->
Player 1 will be prompted to enter their moves.
The computer will generate its moves randomly.
The game will continue until a player wins or it's a draw.
Computer vs Computer->
The computer players will generate their moves randomly.
The game will continue until one of the computer players wins or it's a draw.
Contributing -->
Contributions to this Tic-Tac-Toe game project are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.
#ES
Tres en Raya->
Este es un juego de Tres en Raya implementado en Python. Permite jugar contra otro jugador o contra la máquina. También es posible simular un juego entre dos máquinas.

Clase TresEnRaya
Atributos->
FICHA_O: Una constante que representa la ficha del jugador O.
FICHA_X: Una constante que representa la ficha del jugador X.
CASILLA_VACIA: Una constante que representa una casilla vacía en el tablero.
tablero: Una matriz 3x3 que representa el estado actual del tablero.
Métodos->
__init__(): Constructor de la clase que inicializa el tablero con casillas vacías.
colocarFicha(y, x, ficha): Coloca una ficha en la posición (y, x) del tablero.
__str__(): Convierte el objeto de la clase TresEnRaya en una cadena de texto representando el tablero.
ganador(): Verifica si hay un ganador en el tablero y devuelve la ficha del ganador (FICHA_O o FICHA_X) o 0 si no hay ganador.
juegoTerminado(): Verifica si el juego ha terminado, ya sea porque hay un ganador o porque no quedan casillas vacías.
Clase Jugador->
Atributos->
nombre: El nombre del jugador.
ficha: La ficha del jugador (FICHA_O o FICHA_X).
Métodos->
__init__(nombre, ficha): Constructor de la clase que inicializa el nombre y la ficha del jugador.
colocarFicha(tablero, y, x): Coloca una ficha en el tablero en la posición (y, x).
Clase Juego
Atributos
tablero: Un objeto de la clase TresEnRaya que representa el tablero del juego.
jugadores: Una lista que contiene los jugadores que participan en el juego.
turno: Un número entero que indica el turno actual del juego.
Métodos
__init__(jugador1, jugador2): Constructor de la clase que inicializa el tablero y agrega los jugadores a la lista de jugadores.
correrJuego(): Inicia el juego y maneja los turnos de los jugadores.
Clase JugadorMaquina
Esta clase hereda de la clase Jugador y representa a un jugador controlado por la máquina.

Métodos->
generarMovimiento(tablero): Genera un movimiento válido de la máquina en el tablero.
correrJuego(): Sobrescribe el método correrJuego() de la clase Juego para manejar los movimientos de la máquina.
Ejecución del juego
En el bloque de código al final del archivo, se crea un juego con dos jugadores (jugador1 y jugador2) y se llama al método correrJuego() para iniciar el juego.

El juego permite seleccionar el modo de juego:

Jugar contra otro jugador.
Jugar contra la máquina.
Simular un juego entre dos máquinas.
Para cada turno, se muestra el estado actual del tablero y se solicita al jugador correspondiente que coloque una ficha en una posición válida. El juego continúa hasta que hay un ganador o el juego termina en empate.
