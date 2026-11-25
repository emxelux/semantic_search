from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()



def chat_groq(input):
    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    response = client.responses.create(
        input=input,
        model="openai/gpt-oss-20b",
    )
    return response.output_text

