#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))

maior = a
if(b > a and b > c):
    maior = b
elif(c > a and c > b):
    maior = c

menor = b
if(a < b and a < c):
    menor = a
elif(c < a and c < b):
    menor = c
 
print('Entre os valores {}, {} e {}\nO maior é o {}\nO é menor {} ' .format(a, b, c, maior, menor))
