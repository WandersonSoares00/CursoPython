#Modifique as funções que form criadas no ExercitandoMódulosPython para que elas aceitem um parâmetro
#a mais, informando se o valor retornado por elas vai ser ou não formatado pela função formata()),
#desenvolvida no desafio FormatandoMoedas.

import moeda

valor = float(input('Informe um valor em reais: '))
print('--' * 25)
print(f'O valor {moeda.formata(valor)} aumentado em 10% é {moeda.aumentar(valor, 10, form = True)}')
print(f'O valor {moeda.formata(valor)} reduzido em 20% é {moeda.diminuir(valor, 20, form = True)}')
print(f'O valor {moeda.formata(valor)} dobrado é {moeda.dobro(valor, form = True)}')
print(f'O valor {moeda.formata(valor)} reduzido pela metade é {moeda.metade(valor, form = True)}')
print('--' * 25)
