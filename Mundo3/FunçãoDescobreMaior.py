#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*nums):
    if len(nums) == 0:
        maior = None
    else:
        maior = nums[0]
        print('\nValores passados: ')
        for i in range(len(nums)):
            print(nums[i], end = ' ')
            if nums[i] > maior:
                maior = nums[i]
    print(f'\nForam informados {len(nums)} valores e o maior é o {maior}.\n')


maior(2, 5, 9, 100)
maior(-3, -9, -1, -123)
maior()
