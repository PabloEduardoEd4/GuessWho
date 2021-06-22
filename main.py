# GuessWho v1.2
import juego
from global_funcs import confirmer, select

def jugar():
    P1 = input('INGRESE EL NOMBRE DEL JUGADOR 1 (INGRESE 0 PARA VOLVER ATRAS):\n')
    if confirmer(P1,0,0):
        return False
    P2 = input('INGRESE EL NOMBRE DEL JUGADOR 2 (INGRESE 0 PARA VOLVER ATRAS):\n')
    if confirmer(P2,0,0):
        return False
    juego.start(P1, P2, intentos)

def configuracion():
    print('EN CONSTRUCCION')
    menu = '1. CONFIGURAR INTENTOS, 2. REGRESAR, 3. SALIR'
    funcs = [config_intentos,'',salir]
    index = select(menu, 1, len(funcs))
    if index == 2:
        return True
    funcs[index-1]()

def config_intentos():
    while True:
        print('Elige 1, 3 o 5')
        inp = input()
        if confirmer(inp, 1, 5) and (int(inp) == 1 or int(inp) == 3 or int(inp) == 5):
            global intentos
            intentos = int(inp)
            return True
        print('OPCION INCORRECTA. INTENTE DE NUEVO.')
    

def highscore():
    print('EN CONSTRUCCION')
    menu = '1. REGRESAR'
    if select(menu, 1, 1) == 1:
        return True


def salir():
    global flag 
    flag = False

global flag
global intentos
flag = True
intentos = 3


def main():
    while flag:
        funcs = [jugar,configuracion,highscore,salir]
        menu = '1. JUGAR, 2. CONFIGURACION, 3. HIGHSCORES, 4. SALIR.'
        funcs[select(menu, 1, len(funcs)) - 1]()

if __name__ == '__main__':
    main()