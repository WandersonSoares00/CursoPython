#Reescreva a função leiaInt() que fizemos no desafio Validando Entrada de dados, incluindo agora a
#possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função
#leiaFloat() com a mesma funcionalidade.

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


def leiaFloat(msg = ''):
    vermelho = '\033[1;31m'
    padrao = '\033[0;0m'
    while True:
        try:
            v = float(input(msg))
        except ValueError:
            print(vermelho +'Erro: tipo inválido, informe um número inteiro.' + padrao)
        else:
            return v


num1 = leiaInt('Informe um nùmero inteiro: ')
print(f'\nVocê digitou o valor {num1}')
num2 = leiaFloat('Informe um nùmero real: ')
print(f'\nVocê digitou o valor {num2}')
