#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
tupla = (   int(input(f'Informe o valor da 1° posição: ')),
            int(input(f'Informe o valor da 2° posição: ')),
            int(input(f'Informe o valor da 3° posição: ')),
            int(input(f'Informe o valor da 4° posição: '))
        )
print(tupla)
print(f'O valor 9 apareceu {tupla.count(9)} vezes na tupla.')
if 3 in tupla:
    print(f'A primeira ocorrência do valor 3 foi na posição {tupla.index(3) + 1}')
else:
    print('Não houve ocorrência do valor 3 na tupla.')
print('Os pares da tupla foram: (', end = ' ')
for valor in tupla:
    if valor % 2 == 0:
        print(valor, end= ' ')
print(')')
