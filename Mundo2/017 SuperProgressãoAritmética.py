#Melhore o DESAFIO 011, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razao da PA: '))
cont = 0
term_ad = 10
while term_ad != 0:
    for i in range(term_ad):
        termo = termo + r
        cont = cont + 1
        print(termo, end = ', ')
    print('Pausa')
    term_ad = int(input('Quantos termos adicionais voce deseja? '))
print('\nProgressao finalizada com {} termos exibidos.' .format(cont))
