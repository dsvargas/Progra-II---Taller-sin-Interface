nombreJugador1=""
nombreJugador2=""
dificultad=0
matrizlog = []
cantBarcos=0

def printopcion():
    print("╔════════════════╗","\n","   1. Jugador vs Jugador","\n","   2. Jugador vs Computador")
    print("╚════════════════╝")

def printseleccion():
    print("╔════════════════╗","\n","Cantidad de elementos por partida")
    print("╚════════════════╝")

def start():
    printopcion()
    modalidad=int(input("Presione la opcion  1/2: "))
    while(modalidad != 1 and modalidad !=2 ):
        print("Digite una opcion valida")
        printopcion()

    nombreJugador1=input("Seleccione el nombre del Jugador 1...")
    if modalidad == 1:
        nombreJugador2=input("Digite el nombre del Jugador 2...")

    print(printseleccion())
    dificultad =  int(input("Elementos"))
    while(dificultad != 1 and dificultad !=2 and dificultad!=3):
        print("Digite una opcion valida")
        dificultad =  int(input("Digite la dificultad (1 facil  2medio 3 dificil)"))

    #cantBarcos =  int(input("Digite la cantidad de barcos..."))
    matriz()
        
def matriz():
        if dificultad==1:
            conta=7
        if dificultad==2:
            conta=10
        else:
            conta=13
        for i in range(conta):
                    matrizlog.append([0]*conta)



start()