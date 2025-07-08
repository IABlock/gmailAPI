import base64

def decodificar_mensagem(mensagem_codificada):
  """Decodifica uma mensagem codificada em Base64url.

  Args:
    mensagem_codificada: A mensagem codificada em Base64url.

  Returns:
    A mensagem decodificada como string.
  """
  mensagem_codificada = mensagem_codificada.encode('utf-8')
  mensagem_decodificada = base64.urlsafe_b64decode(mensagem_codificada).decode('utf-8')
  return mensagem_decodificada


def emailDecodeHtml(data_str_base64):
    mensagem_codificada = data_str_base64   
    mensagem_decodificada = decodificar_mensagem(mensagem_codificada)
    print(mensagem_decodificada)
    return mensagem_decodificada