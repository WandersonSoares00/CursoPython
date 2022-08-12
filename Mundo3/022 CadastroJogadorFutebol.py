#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome 
#do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dadosJog = dict()
listaGols = list()
somatGols = 0

dadosJog['nome'] = input('Informe seu nome: ')
part = int(input('Quantas partidas você jogou? '))
for i in range(part):
    listaGols.append(int(input(f'Quantos gols na partida {i + 1}: ')))   
    somatGols += listaGols[i]

dadosJog['gols'] = listaGols
dadosJog['total'] = somatGols
print('-=' * 30)
for k, v in dadosJog.items():
    print(f'O campo {k} possui valor {v}')
i = 0
print('-=' * 30)
for i, qtdgols in enumerate(dadosJog['gols']):
    print(f'Na partida {i + 1} o jogador {dadosJog["nome"]} fez {qtdgols} gols.')
print(f'O total de gols foi {dadosJog["total"]}')
print('-=' * 30)
