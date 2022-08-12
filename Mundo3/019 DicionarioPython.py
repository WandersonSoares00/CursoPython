#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

dados = {}

dados['nome'] = input('Informe o nome do aluno: ')
dados['media'] = float(input('Informe a media do aluno: '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado(a)'
else:
    dados['situacao'] = 'Reprovado(a)'

print('\n', '=-' * 20)
print(f'A situação do aluno(a) {dados["nome"]} é {dados["situacao"]} .')
print('=-' * 20)
