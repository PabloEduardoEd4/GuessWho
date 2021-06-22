# GuessWho v1.2
from random import randint
from global_funcs import confirmer, select

global space
global dividor
global gamewinner
space = 18
dividor = '|'
gamewinner = ''

class Player():
    def __init__(self, name, P_selecion, intentos):
        self.name = name
        self.selecion = P_selecion
        self.intentos = intentos
    def setchar(self, P_char):
        self.char = P_char



def generador():
    file = open('nombres.txt', 'r')
    nombres = [linea.split(',') for linea in file][0]
    nombres = [nombre.split(' ')[0] for nombre in nombres]
    file = open('descriptores.txt', 'r')
    descriptores = [(linea.split(', ')) for linea in file][0]
    file.close()
    del file
    return nombres, descriptores

def random_generador(lista1, lista2, size = 1):
    out = []
    counter = 0
    while counter != size:
        if (temp := [lista1[randint(0,len(lista1)-1)], lista2[randint(0,len(lista2)-1)]]) not in out:
            out.append(temp)
            counter += 1
        else:
            pass
    return out


def start(P1, P2, intentos):
    nombres, descriptores = generador()
    all_chr = random_generador(nombres, descriptores, 6)
    p1 = Player(P1, all_chr[:], intentos)
    p2 = Player(P2, all_chr[:], intentos)
    p1.setchar(name_selector(all_chr, P1))
    p2.setchar(name_selector(all_chr, P2))
    game(p1, p2)
    print(f"FELICIDADES {gamewinner}")
    

def name_selector(all_chr, P):
    while True:
        print(f"{' '.join([str(x) for x in all_chr][0:3])}\n{' '.join([str(x) for x in all_chr][3:6])}")
        inp = input(f'Elige tu personaje misterio, {P}\n')
        if inp in (temp := [x[0] for x in all_chr]):
            return all_chr[temp.index(inp)]
        print('OPCION INCORRECTA. INTENTE DE NUEVO.')

def game(p1, p2):
    while True:
        res = gameloop(p1, p2)
        if gamewinner != '':
            return True
        res = gameloop(p2, p1)
        if gamewinner != '':
            return True


def gameloop(player, notPlayer):
    global gamewinner
    print(f'Es tu turno de {player.name}')
    board_print(player)
    menu = '1. ADIVINAR PERSONAJE, 2. HACER PREGUNTA'
    sel = select(menu, start = 1, end = 2)
    if sel == 1:
        inp = input('QUIEN:')
        anws = adiv(player, notPlayer, inp)
        if anws == True:
            return True
        player.intentos = player.intentos - 1
        print(f"Tiene {player.intentos} intentos")
        if player.intentos == 0:
            print(f"Lo siento {player.name}, se quedo sin intentos")
            gamewinner = notPlayer.name
            return True
    if sel == 2:
        inp = input('PREGUNTA: ')
        anws = preg(player, notPlayer, inp)
    board_print(player)
    print(f"Jugador ha respodido: {['no', 'si'][anws]}")
    print(f"Tiene {player.intentos} intentos")
    list_rem(player,  input("Ingrese una lista de personajes a remover tablero: ").replace(' ','').split(','))
    board_print(player)
    input()
    

def board_print(player):
    disp = [' '.join([x[0], x[1],' '*(space - len(x[0]) - len(x[1]) - 1)]) for x in player.selecion]
    #print(f"|{'|  |'.join(disp[0:3])}|\n|{'|  |'.join(disp[3:6])}|")
    print(f"|  {'|  '.join(disp[0:3])}|\n|  {'|  '.join(disp[3:6])}|")
    print(f"{(space*3)//2 * ' '}|{' '.join(player.char)}|")

def adiv(player, notPlayer, Persona):
    input()
    global gamewinner
    print('Su contricante esta tratando de adivinar su personaje')
    print(f"Su personaje actual: es {notPlayer.char} . El personaje adivinado era {Persona}")
    menu = '1. ES CORRECTO, 2. ES INCORRECTO'
    if select(menu, start = 1, end = 2) == 1:
        gamewinner = f'{player.name}'
        return True
    else:
        return False

def preg(player, notPlayer, pregunta):
    input()
    board_print(notPlayer)
    print('Su contricante le ha hecho la siguiente pregunta:')
    print(pregunta)
    menu = '1. SI, 2. NO'
    return select(menu, start = 1, end = 2) == 1

def list_rem(player, remove):
    nombre = [x[0] for x in player.selecion]
    for x in remove:
        if x in nombre:
            player.selecion[nombre.index(x)] = ['X', '']

def main():
    start('P1', 'P2', 1)
    

if __name__ == '__main__':
    main()