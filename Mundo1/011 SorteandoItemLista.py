#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
#ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

a1 = input('Informe o nome do aluno 1: ')
a2 = input('Informe o nome do aluno 2: ')
a3 = input('Informe o nome do aluno 3: ')
lista = [a1, a2, a3]
sort = random.choice(lista)

print('O aluno(a) escolhido foi o(a) %s' %sort)
