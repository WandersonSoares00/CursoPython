#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
#em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
#contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

#Convencionou-se que, independente do sexo, a aposentadoria seria com 35 anos de contribuição

dados = {}
dados['nome'] = input('Informe o seu nome: ')
dados['nascimento'] = int(input('Informe seu ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (Digite 0 caso não tiver): '))
dados['idade'] = 2022 - dados['nascimento']

if dados['ctps'] != 0:
    dados['ano de contratação'] = int(input('Informe o ano de contratação: '))
    dados['salário'] = float(input('Informe seu salário: R$ '))
    dados['idade de aposentadoria'] = ((dados['ano de contratação'] + 35) - 2022) + dados['idade']
else:
    del(dados['ctps'])

print('\n', '=+' * 7, 'Dados: ', '=+' * 7)
for k, v in dados.items():
    print(f'\t{k.upper()}: {v}')
