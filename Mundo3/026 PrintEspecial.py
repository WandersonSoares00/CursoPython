#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
#como parâmetro e mostre uma mensagem com tamanho adaptável.
def mensagem(msg):
    comp = int(len(msg) / 2) + 2
    print("\n\t", "=+" * comp)
    print(f'\t  {msg}')
    print("\t", "=+" * comp)


mensagem("Hello World")
mensagem("Aprendendo Python")
mensagem("^^")
