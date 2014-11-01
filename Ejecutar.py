'''
6.	Estadísticas
1.	AcertarBlancoAliado();
2.	FallarBlancoAliado();
3.	AcertarrBlancoEnemigo();
4.	FallarBlancoEnemigo();
5.	SumarAliadosDestruidos();
6.	SumarEnemigosDestruidos();
7.	EscogerJugadorAliado();
8.	EscogerJugadorEnemigo();
9.	EscogerCeldaAliado();
10.	EscogerCeldaEnemigo();
11.	Ganador();
12.	Perdedor();
13.	Turno();
14.	CantidadDePartidasJugadas();
15.	CantidadDePartidasGanadasJugador1();
16.	CantidadDePartidasGanadasJugador2();
17.	CantidadDePartidasPerdidasJugador1();
18.	CantidadDePartidasPerdidasJugador2();
19.	Rendirse();
20.	TotalDeAliadosDestruidos();
21.	TotalDeEnemigosDestruidos();
22.	Jugar();
23.	IniciarNuevaPartida();
24.	VerEstadisticas();

'''
from random import *

x = 0
y = 0
campos = 0
nombreJugador1 = ""
nombreJugador2 = ""

matrizJugador1 = []
matrizJugador2 = []
numElementos = 0
modalidad = 0


def popcion():
    print("╔════════════════╗", "\n", "   1. Jugador vs Jugador", "\n", "   2. Jugador vs Computador")
    print("╚════════════════╝")


def pseleccion():
    print("╔══════════════════════╗", "\n", "  Seleccionar la cantidad elementos ", "\n",
          "   mínimo 1 elementos por partida")
    print("╚══════════════════════╝")


def MatrizJuegador1():
    print("═════════ Jugador 1 ════════════")
    for i in matrizJugador1:
        print(i)
    print("════════════════════════════")


def MatrizJugador2():
    print("═════════ Jugador 2 ════════════")
    for i in matrizJugador2:
        print(i)
    print("════════════════════════════")


def matriz():
    global x
    global y
    global campos
    x = int(input("Digite la cantidad de filas: "))
    y = int(input("Digite la cantidad de columnas: "))
    if x <= 1 or y <= 1:
        print("Debe digitar un numero mayor a 1")
        matriz()
    campos = x * y
    for j in range(x):
        matrizJugador1.append([0] * y)
        matrizJugador2.append([0] * y)


def CantidadElementos():  # digita la cantidad de barcos y me valida que hayan mas de 1 elementos o uno
    # y que los elementos no sean mas que la mitad de todos los campos de la matriz
    pseleccion()
    global numElementos
    try:
        numElementos = int(input("Digite la cantidad de elementos: "))
    except:
        numElementos = int(input("Digite solo elementos numericos: "))

    while (numElementos <= 1) and (numElementos > campos // 2):
        try:
            numElementos = int(input("Digite la cantidad de elementos mayor 1: "))
        except:
            numElementos = int(input("Digite solo elementos numericos: "))


def colocarElementos():
    conta1 = 0
    conta2 = 0
    while conta1 < numElementos:  # coloca la cantidad de  elementos que el usuario ingreso
        MatrizJuegador1()
        try:
            i = int(input("Digite la fila donde quiere colocar el elemento "))
            j = int(input("Digite la columna donde quiere colocar el elemento "))
        except:
            print("Solo numeros")
            i = int(input("Digite la fila donde quiere colocar el elemento "))
            j = int(input("Digite la fila donde quiere colocar el elemento "))

        if i < 0 or i > x - 1 or j < 0 or j > y - 1:  # valida que no se salga de rango de la matriz
            print("Posicion invalida")
        elif matrizJugador1[i][j] != 0:
            print("Campo esta ocupado")
        else:
            matrizJugador1[i - 1][j - 1] = 1
            conta1 += 1
    if modalidad == 1:
        while conta2 < numElementos:
            MatrizJugador2()
            i = int(input("Digite la fila donde quiere colocar el elemento "))
            j = int(input("Digite la columna donde quiere colocar el elemento "))
            if i < 0 or i > x - 1 or j < 0 or j > y - 1:
                print("Posicion invalida")
            elif matrizJugador2[i][j] != 0:
                print("Campo esta ocupado")
            else:
                matrizJugador2[i][j] = 1
                conta2 += 1


def colocarElementos2():
    global x
    global y
    conta1 = 0
    conta2 = 0
    while conta1 < numElementos:  # coloca la cantidad de  elementos que el usuario ingreso
        MatrizJuegador1()
        try:
            i = int(input("Digite la fila donde quiere colocar el elemento "))
            j = int(input("Digite la columna donde quiere colocar el elemento "))
        except:
            print("Solo numeros")
            i = int(input("Digite la fila donde quiere colocar el elemento "))
            j = int(input("Digite la fila donde quiere colocar el elemento "))

        if i < 0 or i > x - 1 or j < 0 or j > y - 1:  # valida que no se salga de rango de la matriz
            print("Posicion invalida")
        elif matrizJugador1[i][j] != 0:
            print("Campo esta ocupado")
        else:
            matrizJugador1[i - 1][j - 1] = 1
            conta1 += 1
    if modalidad == 2:
        while conta2 < numElementos: # Haga si contador es menor al numero de elementos
            MatrizJugador2()
            fila = random.randint(0,5)-1
            columna = random.randint(0,5)-1

            if matrizJugador2[fila][columna] == 0:
                matrizJugador2[fila][columna] = 1
                conta2+=1
                MatrizJugador2()




def start():
    popcion()
    global modalidad
    global nombreJugador1
    global nombreJugador2
    try:
        modalidad = int(input("Presione la opcion  1/2: "))
    except:
        print("Digite solo elementos numericos")
        modalidad = int(input("presione la opcion 1/2: "))

    while (modalidad != 1 and modalidad != 2 ):
        print("Digite una opcion valida")
        popcion()

    if modalidad == 1:
        nombreJugador1 = input("Seleccione el nombre del Jugador 1...")
        nombreJugador2 = input("seleccione el nombre del jugador 2...")
        matriz()
        CantidadElementos()
        colocarElementos()
    else:
        nombreJugador1 = input("Seleccione el nombre del Jugador 1...")
        matriz()
        CantidadElementos()
        #colocarElementos2()



start()



