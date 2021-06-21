from random import randint

def generador():
    global nombres
    global descriptores
    file = open('nombres.txt', 'r')
    nombres = [linea.split(',') for linea in file][0]
    nombres = [nombre.split(' ')[0] for nombre in nombres]
    file = open('descriptores.txt', 'r')
    descriptores = [(linea.split(',')) for linea in file][0]
    file.close()
    del file

def random_generador(size = 1):
    out = []
    counter = 0
    while counter != size:
        if (temp := [nombres[randint(0,len(nombres)-1)], descriptores[randint(0,len(descriptores)-1)]]) not in out:
            out.append(temp)
            counter += 1
        else:
            pass
    return out


def start(P1, P2, intentos):
    global P1_selecion
    global P2_selecion
    global P1_char
    global P2_char
    generador()
    all_chr = random_generador(12)
    P1_selecion = all_chr[0:6]
    P2_selecion = all_chr[6:12]
    print(f"{' '.join([str(x) for x in P1_selecion][0:3])}\n{' '.join([str(x) for x in P1_selecion][3:6])}")
    inp = input(f'Elige tu personaje misterio, {P1}\n')
    if inp in (temp := [x[0] for x in P1_selecion]):
        P1_char = P1_selecion[temp.index(inp)]
    print(f"{' '.join([str(x) for x in P2_selecion][0:3])}\n{' '.join([str(x) for x in P2_selecion][3:6])}")
    inp = input(f'Elige tu personaje misterio, {P2}\n')
    if inp in (temp := [x[0] for x in P2_selecion]):
        P2_char = P2_selecion[temp.index(inp)]
    gameloop(P1, P2, intentos)

def gameloop(P1, P2, intentos):
    pass

def main():
    start('P1', 'P2', 2)

if __name__ == '__main__':
    main()