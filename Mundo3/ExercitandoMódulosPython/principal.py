#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
#e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

valor = float(input('Informe um valor em reais: '))
print(f'O valor {valor} aumentado em 10% é {moeda.aumentar(valor, 10)}')
print(f'O valor {valor} reduzido em 20% é {moeda.diminuir(valor, 20)}')
print(f'O valor {valor} dobrado é {moeda.dobro(valor)}')
print(f'O valor {valor} reduzido pela metade é {moeda.metade(valor)}')
