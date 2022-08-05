#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
#em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

lista = []
dados = {}
lista_mulheres = []
list_Id_acimaMed = []
acumulaId = 0
while True:
    dados['nome'] = input('informe o seu nome: ')
    dados['sexo'] = input('Sexo: [M\F] ').upper()
    dados['idade'] = int(input('Informe sua idade em anos: '))
    acumulaId += dados['idade']
    
    lista.append(dados.copy())
    dados.clear()
    continua = input('Quer continuar? [S\\N] ').upper()
    if continua in 'N':
        break
    print('=+=' * 15)

print(f'\nNo total foram {len(lista)} pessoas cadastradas.')
mediaId = acumulaId / len(lista)
print(f'\nA mádia das idades é {mediaId:5.2f}')
for info in lista:
    if info['sexo'] in 'F':
        lista_mulheres.append(info['nome'])
    if info['idade'] > mediaId:
        list_Id_acimaMed.append(info['nome'])

print(f'\nMulheres cadastradas: {lista_mulheres}')
print(f'\nPessoas com idade acima da média: {list_Id_acimaMed}')
