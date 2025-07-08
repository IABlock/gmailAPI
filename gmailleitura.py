from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from emailDecode import emailDecodeHtml


def lerEmail(creds):
  try:
    # Lista Geral de um remitente especifico
    # https://www.googleapis.com/gmail/v1/users/me/messages?q=in:sent after:2014/01/01 before:2014/02/01
    servico = build("gmail","v1",credentials=creds,)
    resultado = servico.users().messages().list(userId="me", maxResults=500, q='from:no-reply@99freelas.com.br').execute()
    ids=[]
    for message in resultado['messages']:      
      ids.append(message['id'])

    #print(ids)
    idmessage = '197e454e6a078944'
    #for idmessage in ids:
    resultado = servico.users().messages().get(userId="me", id=idmessage).execute()
    data_str_html = resultado['payload']['body']['data']
    resultadoHtml = emailDecodeHtml(data_str_html)
    print(resultadoHtml)

    return resultadoHtml

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")