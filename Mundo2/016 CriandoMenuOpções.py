"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep
v1, v2 = input('Informe dois valores: ').split()
v1, v2 = int(v1), int(v2)
opcao = 1
while opcao != 5:
    print('''
    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos numeros
    [ 5 ] - Sair\n''')
    opcao = int(input('Informe a opcao referente a acao desejada: '))
    if opcao == 1:
        print('{} + {} = {}' .format(v1, v2, v1 + v2))
    elif opcao == 2:
        print('{} x {} = {}' .format(v1, v2, v1 * v2))
    elif opcao == 3:
        if v1 != v2:
            if v1 > v2:
                maior = v1
            elif v2 > v1:
                maior = v2
            print('O maior valor  eh {}' .format(maior))
        else:
            print('Os valores sao iguais.')
    elif opcao == 4:
        v1, v2 = input('Informe dois valores: ').split()
        v1, v2 = int(v1), int(v2)
    elif opcao == 5:
        print('Finalisando...')
    else:
        print('Opcao invalida. Tente novamente')
    sleep(2)

