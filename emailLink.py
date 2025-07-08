import os
from dotenv import load_dotenv

def listaLinks(str_html):
  load_dotenv()
  
  palavra = os.getenv('LINK_BUSCA')
  indice = 0
  ocorrencias = []
  linksAchados = []

  while True:
    indice = str_html.find(palavra, indice)
    if indice == -1:
        break
    fimLink = str_html.find('"', indice)
    link = str_html[indice:fimLink]
    linksAchados.append(link)
    ocorrencias.append(indice)
    indice += len(palavra)

  #print(f"A palavra '{palavra}' foi encontrada {len(ocorrencias)} vezes.")
  #print(f"Índices das ocorrências: {ocorrencias}")  
  #print(f"Links encontrados: {linksAchados}")
  listalimpa = list(set(linksAchados))
  return listalimpa