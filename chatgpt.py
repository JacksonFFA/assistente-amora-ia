import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def perguntar_chatgpt(pergunta):
    try:
        resposta = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é uma assistente chamada Amora, que fala com carinho, alegria e entusiasmo."},
                {"role": "user", "content": pergunta}
            ],
            temperature=0.8,
            max_tokens=150
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Desculpa, deu erro ao falar com a IA:\n\n{e}"
