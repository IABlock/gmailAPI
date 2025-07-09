from flask import Flask, jsonify, make_response, json

from gmailleitura import lerEmail
from gmailauth import autenticacao
from emailLink import listaLinks
from notionDatabase import listDatabase,gravaDatabase

app = Flask(__name__)

@app.route("/")
def listalinks():
  credenciais = autenticacao()
  if credenciais is not None:
    htmlEmail = lerEmail(credenciais)
    linkEncontrados = listaLinks(htmlEmail)

    lista = json.dumps(linkEncontrados)        
    response = make_response(lista,200)
    response.headers["Content-Type"]="application/json"

    return response
  else:
    print('Credenciais Invalidas')

@app.route("/notion")
def notionlink():
  return listDatabase()

@app.route("/gravanotion")
def notionrec():
  retorno = gravaDatabase()
  response = make_response(retorno, 200)
  return (response)

if __name__ == "__main__":
  app.run(debug=True)