import pyttsx3
from voz import ouvir_microfone
from chatgpt import perguntar_chatgpt
from tarefas import adicionar_tarefa, listar_tarefas
from comandos import abrir_programa_ou_site
from lembretes import agendar_lembrete, interpretar_comando_lembrete
import time

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

print("\U0001F44B Assistente IA contínua iniciada! Diga algo para começar.")
falar("Olá Jackson! Assistente contínua iniciada.")

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
                falar("Lembrete agendado com sucesso!")
            else:
                tarefa = texto.replace("lembre-me de", "").replace("me acorde", "").strip()
                adicionar_tarefa(tarefa)
                falar("Tarefa adicionada com sucesso!")

        elif "listar tarefas" in texto:
            listar_tarefas()
            falar("Essas são as suas tarefas.")

        elif texto.startswith("abrir"):
            abrir_programa_ou_site(texto)
            falar("Abrindo conforme solicitado.")

        elif "quem vai ser campeão do mundial de clubes" in texto:
            falar("Flamengo é o melhor time do Mundo e será o campeão fácil.")

        else:
            resposta = perguntar_chatgpt(texto)
            print(f"💬 IA: {resposta}")
            falar(resposta)

        time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛡️ Interrompido pelo usuário.")
        break
