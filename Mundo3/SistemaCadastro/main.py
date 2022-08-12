
#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em
#um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e
#listar todas as pessoas cadastradas.

from pacotes.interface import *
from pacotes.arquivo import *

arq = 'listaPessoas.txt'

if not arquivoExiste(arq):
    CriaArquivo(arq)

while True:
    titulo('Sistema de cadastro')
    alternativa = menu('Listar Pessoas', 'Cadastrar pessoas', 'Sair do sistema')
    
    if alternativa == 1:
        LerArquivo(arq)
    elif alternativa == 2:
        titulo('Cadastro de uma nova pessoa.')
        nome = input('\nInforme o nome: ')
        idade = leiaInt('Informe a idade: ')
        CadastroArquivo(arq, nome, idade)
    elif alternativa == 3:
        print('Encerrando o programa...')
        break
    else:
        print('Alternativa inválida. Escolha novamente.')
    print()
