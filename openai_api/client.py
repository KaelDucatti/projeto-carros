import os

import boto3
from dotenv import load_dotenv
from openai import OpenAI

from .prompt import car_bio_rules

# Carrega .env apenas em desenvolvimento local
load_dotenv()


def get_openai_key():
    """
    Busca a chave da OpenAI do .env local ou AWS Parameter Store
    """
    # Se estiver em desenvolvimento local (com .env)
    local_key = os.getenv("OPENAI_API_KEY")
    if local_key:
        return local_key

    # Se estiver na EC2 (produção), busca do Parameter Store
    try:
        ssm = boto3.client("ssm")
        response = ssm.get_parameter(
            Name="/projeto-carros/OPENAI_API_KEY", WithDecryption=True
        )
        return response["Parameter"]["Value"]
    except Exception as err:
        raise Exception(f"Erro ao buscar chave da OpenAI: {err}") from err


# Obtém a chave da forma apropriada para o ambiente
OPENAI_API_KEY = get_openai_key()
client = OpenAI(api_key=OPENAI_API_KEY)


def get_car_ai_bio(model, brand, year):
    response = client.chat.completions.create(  # Correção aqui
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": car_bio_rules.format(model=model, brand=brand, year=year),
            }
        ],
        max_tokens=1000,  # Correção aqui também
    )
    return response.choices[0].message.content
