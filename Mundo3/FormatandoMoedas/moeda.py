
def aumentar(v, t):
    r = (100 + t) / 100 * v
    return r


def diminuir(v, t):
    r = (100 - t) / 100 * v
    return r


def dobro(v):
    r = 2 * v
    return r


def metade(v):
    r = (v / 2)
    return r


def formata(v):
    return f'{v:.2f} R$'.replace('.', ',')

