#Adapte o código do desafio ExercitandoMódulosPython, criando uma função adicional chamada formata()
#que consiga mostrar os números como um valor monetário formatado.
import moeda

valor = float(input('Informe um valor em reais: '))
print('--' * 25)
print(f'O valor {moeda.formata(valor)} aumentado em 10% é {moeda.formata(moeda.aumentar(valor, 10))}')
print(f'O valor {moeda.formata(valor)} reduzido em 20% é {moeda.formata(moeda.diminuir(valor, 20))}')
print(f'O valor {moeda.formata(valor)} dobrado é {moeda.formata(moeda.dobro(valor))}')
print(f'O valor {moeda.formata(valor)} reduzido pela metade é {moeda.formata(moeda.metade(valor))}')
print('--' * 25)
