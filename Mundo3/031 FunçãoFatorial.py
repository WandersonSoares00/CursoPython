#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
#o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será
#mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show = False):
    fat = 1
    print(n, end='! = ')
    for i in range(n):
        fat *= (n - i)
        if show:
            if n - i != 1:
                print(n - i, end= ' x ')
            else:
                print(n - i, end= ' = ')
    return fat


print(fatorial(14))
print(fatorial(6, show = True))
