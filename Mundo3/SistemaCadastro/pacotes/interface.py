
def linha(car = '-', tam = 42):
    print(car * tam)


def titulo(txt = ''):
    linha()
    print(txt.center(42))
    linha()


def leiaInt(msg = ''):
    vermelho = '\033[1;31m'
    padrao = '\033[0;0m'
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print(vermelho +'Erro: tipo inválido, informe um número inteiro.' + padrao)
        else:
            return n


def menu(*opc):
    titulo('Menu Principal')
    for i in range(len(opc)):
        print(f'\t{i + 1} - {opc[i]}')
    linha()
    resp = leiaInt('Informe a opção desejada: ')
    return resp
