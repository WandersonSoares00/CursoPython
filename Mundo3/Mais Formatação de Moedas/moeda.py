
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

