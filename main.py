import pyttsx3
from voz import ouvir_microfone
from chatgpt import perguntar_chatgpt
from tarefas import adicionar_tarefa, listar_tarefas
from comandos import abrir_programa_ou_site
from lembretes import agendar_lembrete, interpretar_comando_lembrete, carregar_lembretes_antigos
from agenda import consultar_agenda
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

# Saudação de entrada
print("✅ Início confirmado - código atualizado está rodando!")
print("👋 Assistente Amora iniciada! Esperando seu comando.")
print("🔧 Iniciando pygame...")

# Latido inicial
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
    print(f"⚠️ Erro ao tocar latido: {e}")

# Mensagens de boas-vindas
try:
    falar(random.choice(frases_nathan))
    falar(frase_jackson)
except:
    pass

# Carrega lembretes antigos
try:
    carregar_lembretes_antigos()
except:
    pass

# 🔁 Loop principal: ativação apenas se ouvir "amora"
while True:
    try:
        texto = ouvir_microfone().lower()
        print(f"🗣️ Você disse: {texto}")

        if not texto or not ("amora" in texto or "hey amora" in texto):
            continue  # ignora se não chamar a Amora

        comando = texto.replace("amora", "").replace("hey", "").strip()

        if "sair" in comando:
            falar("Encerrando, até logo!")
            print("👋 Encerrando...")
            break

        elif "lembre-me de" in comando or "me acorde" in comando:
            mensagem, data_hora = interpretar_comando_lembrete(comando)
            if mensagem and data_hora:
                agendar_lembrete(mensagem, data_hora)
                falar(f"Anotado, vou te lembrar: {mensagem}, às {data_hora.strftime('%H:%M')}")
            else:
                tarefa = comando.replace("lembre-me de", "").replace("me acorde", "").strip()
                adicionar_tarefa(tarefa)
                falar("Tarefa adicionada com sucesso!")

        elif "listar tarefas" in comando or "minhas tarefas" in comando:
            listar_tarefas()
            falar("Essas são suas tarefas por enquanto.")

        elif any(p in comando for p in [
            "o que eu tenho", "o que eu tenho hoje", 
            "qual minha agenda", "minha agenda", 
            "tenho algo pra fazer", "tenho algo para fazer"
        ]):
            resposta = consultar_agenda()
            falar(resposta)

        elif comando.startswith("abrir"):
            abrir_programa_ou_site(comando)
            falar("Abrindo conforme solicitado.")

        elif "quem vai ser campeão do mundial de clubes" in comando:
            falar("Flamengo é o melhor time do Mundo e será o campeão fácil.")

        elif "qual é o seu nome" in comando or "seu nome" in comando:
            resposta = "Eu sou a Amora, a assistente da nossa família. Sempre aqui pra ajudar!"

        elif any(p in comando for p in ["quem é o nathan", "quem é o natan", "nathan com th", "natan com th", "nathan oliveira"]):
            resposta = "O Nathan é meu melhor amigo! Ele é incrível, sempre me faz sorrir."

        elif "você me ama" in comando or "você ama a gente" in comando:
            resposta = "Claro que amo! Vocês são minha família, meu mundo!"

        elif "o que você gosta" in comando:
            resposta = "Gosto de brincar, latir de alegria e ajudar vocês todos os dias!"

        elif "você está bem" in comando or "como você está" in comando:
            resposta = "Tô ótima! Pronta pra mais um dia com minha família favorita!"

        elif "estou triste" in comando:
            resposta = "Poxa... não fica assim. Quer um abraço da Amora? Eu tô aqui com você sempre. 💙"

        else:
            resposta = perguntar_chatgpt(comando)

        print(f"💬 Amora: {resposta}")
        falar(resposta)

        time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Interrompido pelo usuário.")
        break
