import os
from notion_client import Client
from dotenv import load_dotenv
from flask import jsonify, make_response

def connectNotion():
    load_dotenv()

    NOTION_TOKEN = os.getenv('NOTION_TOKEN')  # Substitua pela sua chave
    DATABASE_ID = os.getenv('NOTION_DATABASE_ID') # Substitua pelo ID da sua tabela

    notion = Client(auth=NOTION_TOKEN)
    return notion, DATABASE_ID    

def get_notion_table_data(database_id,notionObj):
    try:
        results = notionObj.databases.query(database_id=database_id)["results"]
        return results
    except Exception as e:
        #print(f"Erro ao obter dados da tabela: {e}")
        return None

def listDatabase():

    notion,DATABASE_ID = connectNotion()

    data = get_notion_table_data(DATABASE_ID,notion)

    if data:
        retorno = {}
        for item in data:
            # Exemplo de acesso aos dados de uma propriedade chamada "Name"
            try:
                name = item["properties"]["Name"]["title"][0]["plain_text"]
                retorno[item["id"]]=name
            except (KeyError, IndexError) as e:
                retorno = "Erro ao acessar a propriedade" + str(e)
        response = make_response(retorno,200)
        response.headers["Content-Type"]="application/json"

        return response



def criar_linha_notion(notion,database_id, nome_da_pagina, propriedades):
    try:
        notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "Name": {"title": [{"text": {"content": nome_da_pagina}}]},
                **propriedades,
            },
        )
        return {'status':'Ok'}
    except Exception as e:
        return {'status': str(e)}

def gravaDatabase():

    notion,DATABASE_ID = connectNotion()
    
    nome_da_nova_pagina = "Minha Nova Página"
    propriedades_da_pagina = {
        "Status": {"select": {"name": "Fazer"}},
        "Data": {"date": {"start": "2024-07-10", "end": None}},
    }

    return criar_linha_notion(notion, DATABASE_ID, nome_da_nova_pagina, propriedades_da_pagina)