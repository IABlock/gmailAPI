from gmailleitura import lerEmail
from gmailauth import autenticacao
from emailLink import listaLinks

if __name__ == "__main__":
  credenciais = autenticacao()
  if credenciais is not None:
    htmlEmail = lerEmail(credenciais)
    linkEncontrados = listaLinks(htmlEmail)
    print(linkEncontrados)
  else:
    print('Credenciais Invalidas')
