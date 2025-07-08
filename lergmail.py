from gmailleitura import lerEmail
from gmailauth import autenticacao


if __name__ == "__main__":
  credenciais = autenticacao()
  htmlemail = lerEmail(credenciais)
