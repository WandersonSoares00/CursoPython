#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função
#input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(msg = ''):
    n = input(msg)
    while not n.isnumeric():
        print('Entrada inválida, digite um número inteiro.')
        n = input(msg)
    return int(n)

num = leiaInt('Informe um valor inteiro: ')
print(f'\nVocê digitou o número {num}')
