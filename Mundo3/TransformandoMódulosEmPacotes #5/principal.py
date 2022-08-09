#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
#Transfira todas as funções utilizadas nos desafios moeda #1, #2 e #3 para o primeiro pacote
#e mantenha tudo funcionando.

from utilidadesCeV import moeda

valor = float(input('Informe um valor em reais: '))
moeda.resumo(valor, 10, 25)
