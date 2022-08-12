
def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'r')
        arquivo.close()
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return False
    else:
        return True


def LerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
        for linha in arquivo:
            linha = linha.replace('\n', '')
            info = linha.split(';')
            print(f' {info[0]:<30}{info[1]:>3} anos')
        arquivo.close
    except:
        print('Não foi possível ler o arquivo.')

def CadastroArquivo(nome, nome_pessoa, idade):
    try:
        arquivo = open(nome, 'a')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        try:
            arquivo.write(f'{nome_pessoa};{idade}\n')
        except:
            print('Erro no cadastro.')
        else:
            print(f'O(a) {nome_pessoa} foi cadastrado(a) com sucesso!')


def CriaArquivo(nome):
    try:
        arquivo = open(nome, 'w')
        arquivo.close()
    except:
        print('Não foi possível criar o arquivo.')
    

