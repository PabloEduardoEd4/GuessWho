# GuessWho v1.2
def confirmer(value, start = 0, end = 0):
    return value.isdigit() and start <= int(value) <= end

def select(menu, start = 1, end = 1):
    while True:
        print(('\n').join(menu.split(', ')))
        inp = input('Selecione opcion: '.upper()).strip(' ')
        if confirmer(inp, start, end):
            return int(inp)
        print('OPCION INCORRECTA. INTENTE DE NUEVO.')