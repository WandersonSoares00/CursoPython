#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
#Nota: O site 'Pudim.com.br' é um clássico site de humor da internet brasileira que mostra uma
#foto de um pudim em baixa qualidade junto com um email, seu domínio existe desde o ano de 2000.
import urllib.request

def acesso(site):
    try:
        ac = urllib.request.urlopen(site)
    except urllib.error.URLError:
        return False
    else:
        return True


link = 'http://pudim.com.br/'

if acesso(link):
    print(f'Consegui acessar o site {link} !!!')
else:
    print(f'Você está desconectado! Não consegui acessar o site {link}.')
