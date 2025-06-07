from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def perguntar_chatgpt(pergunta):
    resposta = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": pergunta}]
    )
    return resposta.choices[0].message.content.strip()
