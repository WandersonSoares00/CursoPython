#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tc = float(input('Informe a temperatura em graus celsius: '))

tf = (9*tc/5) + 32
print('{} °C equivale a {} ºF' .format(tc, tf))
