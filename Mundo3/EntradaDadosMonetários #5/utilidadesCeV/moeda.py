
def aumentar(v, t, form = False):
    r = (100 + t) / 100 * v
    if form:
        return formata(r)
    else:
        return r


def diminuir(v, t, form = False):
    r = (100 - t) / 100 * v
    if form:
        return formata(r)
    else:
        return r


def dobro(v, form = False):
    r = 2 * v
    if form:
        return formata(r)
    else:
        return r


def metade(v, form = False):
    r = (v / 2)
    if form:
        return formata(r)
    else:
        return r


def formata(v):
    return f'{v:.2f} R$'.replace('.', ',')


def resumo(val, aument, red):
    print('-' * 34)
    print('Informações do valor' .center(34))
    
    v_aument = aumentar(val, aument, True)
    print(f'\nAumento de {aument}%: \t{v_aument}')
    
    v_red =diminuir(val, red, True)
    print(f'Redução de {red}%: \t{v_red}')
    
    v_dob = dobro(val, True)
    print(f'Dobro do valor: \t{v_dob}')
    
    v_met = metade(val, True)
    print(f'Metade do valor: \t{v_met}')
    print('-' * 34)
