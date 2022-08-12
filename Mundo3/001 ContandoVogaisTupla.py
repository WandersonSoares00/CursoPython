#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
#você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('Abelha', 'Cachorro', 'Homem', 'Guitarra', 'Quadrado', 'Computador')

print(f'\t{"Palavra":-<20}', 'Vogais')
for palavra in tupla:
    print(f'\t{palavra:.<20}', end = ' ')
    for i in range(len(palavra)):
        if palavra[i].upper() in 'AEIOU':
            print(palavra[i], end = ' ')
    print()
