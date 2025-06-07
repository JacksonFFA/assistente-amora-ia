import pyttsx3
from voz import ouvir_microfone
from chatgpt import perguntar_chatgpt
from tarefas import adicionar_tarefa, listar_tarefas
from comandos import abrir_programa_ou_site
from lembretes import agendar_lembrete, interpretar_comando_lembrete, carregar_lembretes_antigos
import time
import random
import pygame

def falar(texto):
    try:
        engine = pyttsx3.init(driverName='sapi5')
        engine.say(texto)
        engine.runAndWait()
    except Exception as e:
        print(f"⚠️ Erro ao tentar falar: {e}")

print("✅ Início confirmado - código atualizado está rodando!")
print("👋 Assistente Amora iniciada! Esperando seu comando.")
print("🔧 Iniciando pygame...")

frases_nathan = [
    "Oi, Nathan! Aqui é a Amora! Eu te amo muito, viu? Tô sempre por aqui, pronta pra te ajudar no que precisar.",
    "Nathan, você sabia que eu sou a cadelinha mais feliz do mundo por ter você? Vamos juntos hoje!",
    "Oi, meu amigão Nathan! Já acordei cheia de energia! Vamos arrasar no dia?",
    "Nathan, eu tô aqui pra te lembrar que você é incrível! Com amor, sua Amora."
]

frase_jackson = "Oi Jackson! Já tô ligada nas suas tarefas. Bora organizar esse dia com carinho."

try:
    pygame.mixer.init()
    pygame.mixer.music.load("latido_amora.mp3")
    pygame.mixer.music.play()
    print("🔊 Latido iniciado com sucesso.")
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
except Exception as e:
    print(f"⚠️ Erro ao tentar tocar o latido: {e}")

try:
    falar(random.choice(frases_nathan))
    time.sleep(1)
    print("💬 Saudação para Nathan falada.")
    falar(frase_jackson)
    print("💬 Saudação para Jackson falada.")
except Exception as e:
    print(f"⚠️ Erro na saudação falada: {e}")

try:
    carregar_lembretes_antigos()
except Exception as e:
    print(f"⚠️ Erro ao carregar lembretes antigos: {e}")

while True:
    try:
        texto = ouvir_microfone().lower()
        print(f"🗣️ Você disse: {texto}")

        if "sair" in texto:
            falar("Encerrando, até logo!")
            print("👋 Encerrando...")
            break

        elif "lembre-me de" in texto or "me acorde" in texto:
            mensagem, data_hora = interpretar_comando_lembrete(texto)
            if mensagem and data_hora:
                agendar_lembrete(mensagem, data_hora)
                falar(f"Anotado, vou te lembrar: {mensagem}, às {data_hora.strftime('%H:%M')}")
            else:
                tarefa = texto.replace("lembre-me de", "").replace("me acorde", "").strip()
                adicionar_tarefa(tarefa)
                falar("Tarefa adicionada com sucesso!")

        elif "listar tarefas" in texto:
            listar_tarefas()
            falar("Essas são as suas tarefas.")

        elif any(p in texto for p in [
            "o que eu tenho", 
            "o que eu tenho hoje", 
            "qual minha agenda", 
            "minha agenda", 
            "tenho algo pra fazer",
            "tenho algo para fazer"
        ]):
            falar("Verificando sua agenda de hoje...")
            listar_tarefas()
            resposta = "Sua agenda foi lida."


        elif texto.startswith("abrir"):
            abrir_programa_ou_site(texto)
            falar("Abrindo conforme solicitado.")

        elif "quem vai ser campeão do mundial de clubes" in texto:
            falar("Flamengo é o melhor time do Mundo e será o campeão fácil.")

        elif "qual é o seu nome" in texto or "seu nome" in texto:
            resposta = "Eu sou a Amora, a assistente da nossa família. Sempre aqui pra ajudar!"

        elif any(palavra in texto for palavra in [
            "quem é o nathan", "quem é o natan", "quem é o natan com th",
            "quem é o nathan com th", "quem é o nathan oliveira"
        ]):
            resposta = "O Nathan é meu melhor amigo! Ele é incrível, sempre me faz sorrir."

        elif "você me ama" in texto or "você ama a gente" in texto:
            resposta = "Claro que amo! Vocês são minha família, meu mundo!"

        elif "o que você gosta" in texto:
            resposta = "Gosto de brincar, latir de alegria e ajudar vocês todos os dias!"

        elif "você está bem" in texto or "como você está" in texto:
            resposta = "Tô ótima! Pronta pra mais um dia com minha família favorita!"

        else:
            resposta = perguntar_chatgpt(texto)

        print(f"💬 Amora: {resposta}")
        falar(resposta)

        time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Interrompido pelo usuário.")
        break