import os
from notion_client import Client
from dotenv import load_dotenv
from flask import jsonify, make_response

def get_notion_table_data(database_id,notionObj):
    try:
        results = notionObj.databases.query(database_id=database_id)["results"]
        return results
    except Exception as e:
        #print(f"Erro ao obter dados da tabela: {e}")
        return None

def listDatabase():
    load_dotenv()

    NOTION_TOKEN = os.getenv('NOTION_TOKEN')  # Substitua pela sua chave
    DATABASE_ID = os.getenv('NOTION_DATABASE_ID') # Substitua pelo ID da sua tabela

    notion = Client(auth=NOTION_TOKEN)

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

