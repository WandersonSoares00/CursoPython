#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo' ,'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Curitiba', 'Avaí', 'Ponte preta', 'Atlético-GO')

print('\t\t----Tabela do Campeonato Brasileiro de Futebol----')
print(f'5 primeiros times: {times[:5]}\n')
print(f'Ultimos 4 colocados: {times[-4:]}\n')
print('Times em ordem alfabética:\n')
for time in sorted(times):
    print(time, end = ', ')
print('Fim')
print(f'\nChapecoense está na {times.index("Chapecoense") + 1}° posição.')
