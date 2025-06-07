import pyttsx3
from datetime import datetime
import requests
import os

# Inicializa o mecanismo de fala
engine = pyttsx3.init()

def falar(texto):
    print(f"💬 {texto}")
    engine.say(texto)
    engine.runAndWait()

def dizer_hora():
    agora = datetime.now()
    hora_formatada = agora.strftime("%H horas e %M minutos")
    falar(f"Agora são {hora_formatada}.")

def previsao_tempo(cidade):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        falar("A chave da API do clima não está configurada. Configure a variável OPENWEATHER_API_KEY.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if resposta.status_code != 200:
            falar(f"Não consegui obter a previsão para {cidade}. Verifique o nome da cidade.")
            return

        descricao = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        falar(f"Em {cidade} está {temperatura:.0f} graus com {descricao}.")

    except Exception as e:
        falar("Ocorreu um erro ao tentar obter a previsão do tempo.")
