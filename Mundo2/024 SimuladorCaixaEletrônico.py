#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
#qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
#valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Informe o valor inteiro a ser sacado: R$ '))
temp = valor
contCed = 0
ced = 50
while True:
    if temp >= ced:
        temp -= ced
        contCed += 1
    else:
        if contCed > 0:
            print(f'{contCed} cédulas de {ced}')
        contCed = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if temp == 0:
            break
