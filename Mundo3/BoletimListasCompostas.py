#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
#as notas de cada aluno individualmente.
dados = []
temp = ['', '', '', '']
while True:
    temp[0] = input('Informe o nome do aluno: ')
    temp[1] = float(input('Informe a primeira nota: '))
    temp[2] = float(input('Informe a segunda nota: '))
    temp[3] = (temp[1] + temp[2]) / 2
    continua = input('\nDeseja cadastrar mais aluno? [S\\N] ').upper()
    dados.append(temp)
    temp = ['', '', '', '']
    if continua[0] == 'N':
        break
    print()
    
print('\n', '*' * 15, 'BOLETIM', '*' * 15)
for i in range(len(dados)):
    print(f'\nAluno {i + 1}: {dados[i][0]:-<16} Nota: {dados[i][3]}')

mais = ''
while True:
    continua = input(f'\nConferir a nota de {mais}algum aluno? [S\\N] ').upper()
    if continua[0] == 'N':
        break
    aluno = int(input(f'Digite o número correspondente ao aluno: [1 a {len(dados)}] '))
    if aluno > 0 and aluno <= len(dados):
        print(f'\nAs notas do aluno(a) {dados[aluno-1][0]} foram {dados[aluno-1][1]} e {dados[aluno-1][2]}\nA media resultou em {dados[aluno-1][3]}')
        mais = 'mais '