import os

from openai import OpenAI

from .prompt import car_bio_rules

API_KEY = os.getenv("API_KEY")
client = OpenAI(api_key=API_KEY)


def get_car_ai_bio(model, brand, year):
    response = client.responses.create(
        model="gpt-3.5-turbo",
        input=car_bio_rules.format(model=model, brand=brand, year=year),
        max_output_tokens=1000,
    )
    return response.output_text
