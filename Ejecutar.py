'''
1.	Modo individual vs computador
2.	Seleccionar el nombre del jugador número 1.
3.	Seleccionar el nombre del jugador número 2.
4.	Seleccionar la cantidad elementos a participar dentro la de la partida (mínimo 1 elementos por aliado y mínimo 1 elementos por enemigos).
5.	Seleccionar la profundidad del área de juego (Largo y ancho)
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

nombreJugador1=""
nombreJugador2=""
dificultad=0
matrizlog = []
cantBarcos=0

def popcion():
    print("╔════════════════╗","\n","   1. Jugador vs Jugador","\n","   2. Jugador vs Computador")
    print("╚════════════════╝")
def pseleccion():
    print("╔══════════════════════╗","\n","  Seleccionar la cantidad elementos ","\n","   mínimo 1 elementos por partida")
    print("╚══════════════════════╝")

def CantidadElementos():
    pseleccion()
    try:
        numElementos=int(input("Digite la cantidad de elementos: "))
    except:
        numElementos = int(input("Digite solo elementos numericos: "))
    while numElementos < 1:
        try:
            numElementos=int(input("Digite la cantidad de elementos mayor 1: "))
        except:
            numElementos = int(input("Digite solo elementos numericos: "))
        
def matriz():
        if dificultad==1:
            conta=7
        if dificultad==2:
            conta=10
        else:
            conta=13

        for i in range(conta):
                    matrizlog.append([0]*conta)

def start():
    popcion()
    try:
        modalidad=int(input("Presione la opcion  1/2: "))
    except:
        print("Digite solo elementos numericos")
        modalidad=int(input("presione la opcion 1/2: "))

    while(modalidad != 1 and modalidad !=2 ):
        print("Digite una opcion valida")
        popcion()

    nombreJugador1=input("Seleccione el nombre del Jugador 1...")
    if modalidad == 1:
        nombreJugador2=input("seleccione el nombre del jugador 2...")
    CantidadElementos()


start()
'''
def imprime_matriz():
?? ?? matriz = [ [1,2,3,4,5],[6,7,8,9,10],[1,2,3,4,5],[6,7,8,9,10]]
?? ?? for j in matriz:
?? ?? ?? ?? s= &#39?? ?? &#39.join(str(i) for i in j)
?? ?? ?? ?? print ( "%13s" %s, &#39\n&#39)
imprime_matriz()
'''