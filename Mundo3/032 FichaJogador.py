#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
#do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome = '<desconhecido>', gols = 0):
    if gols.isnumeric() and float(gols) == int(float(gols)) and int(gols) > 0:
        pass
    else:
        gols = 0
    if nome.isspace and len(nome) < 3:
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s).')


print('--' * 20)
jogador = input('Informe o nome do jogador: ')
qtdGol = input('informe a quantidade de gols que ele marcou: ')
print('--' * 20)
ficha(jogador, qtdGol)
