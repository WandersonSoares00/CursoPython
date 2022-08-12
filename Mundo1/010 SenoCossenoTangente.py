#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

a = float(input('Informe um angulo: '))

cos = math.cos(math.radians(a))
sen = math.sin(math.radians(a))
tan = math.tan(math.radians(a))
print('O cosseno de {}º é {:.2f} rad \nO seno de {}º é {:.2f} rad' .format(a, cos, a, sen))
print('A tangente de {}° é {:.2f} rad' .format(a ,tan))
