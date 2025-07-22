import os

from dotenv import load_dotenv
from openai import OpenAI

from .prompt import car_bio_rules

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def get_car_ai_bio(model, brand, year):
    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=car_bio_rules.format(model=model, brand=brand, year=year),
        max_output_tokens=1000,
    )
    return response.output_text
