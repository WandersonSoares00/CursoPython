#Aprimore o desafio Cadastro de jogadores de futebol para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
dadosJogadores = list()
jogador = dict()
partidas = list()

while True:
    jogador['nome'] =  input('Informe o seu nome: ')
    part = int(input('Quantas partidas você jogou? '))
    for i in range(part):
        partidas.append(int(input(f'\tQuantos gols na partida {i + 1}: ')))
    
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    dadosJogadores.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    
    continua = input('Quer continuar? [S\\N] ').upper()
    print('=+=' * 20)
    if continua in 'N':
        break

print(f'{"Nome":>15}    {"Gols":>15}     {"Total de gols":>15}')
for i, dic in enumerate(dadosJogadores):
    print(f'{(i + 1):>3}', end=': ')
    for v in dic.values():
        print(f'{str(v):>15}', end= '')
    print()

print('\n', '-=' * 30)
while True:
    info = int(input('Quer os detalhes de qual jogador? '))
    if info > 0 and info <= len(dadosJogadores):
        for i, qtd in enumerate(dadosJogadores[info - 1]['gols']):
            print(f'O jogador {dadosJogadores[info - 1]["nome"]} fez {qtd} gols na partida {i + 1}')
    continua = input('\nQuer continuar? [S\\N] ').upper()
    if continua in 'N':
        break
    print('=+=' * 15)
