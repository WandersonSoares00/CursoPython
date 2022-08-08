#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
#e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
#Importante: use cores.
cores = [    '\033[0;0m', #padrão
             '\033[1;32m', #verde
             '\033[1;91m', #vermelho
             '\033[1;34m' #azul 
            ]


def ajuda(comd):
    from time import sleep
    titulo(f'Manual do comando "{comd}"', 3)
    sleep(2)
    print(cores[1], end='')
    print('--' * 30)
    help(comd)
    print('--' * 30)
    print(cores[0], end='')
    sleep(3)


def titulo(msg, cor = 0):
    comp = len(msg) + 4
    print('=' * comp)
    print(cores[cor] + f'  {msg}' + cores[0])
    print('=' * comp)


while True:
    titulo('Sistema de orientação ao usuário - PyHELP', 2)
    comando = input('Função ou biblioteca: ')
    if comando.upper() == 'FIM':
        break
    ajuda(comando)
