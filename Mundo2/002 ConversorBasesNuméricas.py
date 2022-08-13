#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
#será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Informe um numero inteiro na base 10: '))

b = int(input('''Esscolha a base de conversao:
[ 1 ] - Binario
[ 2 ] - Octal
[ 3 ] - Hexadecimal\n'''))

if b == 1:
    print('{} na base 10 = {} na base 2' .format(num, bin(num)))
elif b == 2:
    print('{} na base 10 = {} na base 8'.format(num, oct(num)))
elif b == 3:
    print('{} na base 10 = {} na base 16'.format(num, hex(num)))
else:
    print('OPCAO INVALIDA.')

