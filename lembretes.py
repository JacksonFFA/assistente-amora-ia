
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import pyttsx3
import re
import playsound
import json
import os

# Caminho do arquivo JSON
CAMINHO_JSON = os.path.join(os.path.dirname(__file__), "tarefas.json")

# Inicializa o agendador
scheduler = BackgroundScheduler()
scheduler.start()

def falar(texto):
    try:
        playsound.playsound("alarme_musical.mp3", block=False)
    except Exception as e:
        print(f"⚠️ Erro ao tocar o som: {e}")
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def salvar_lembrete_json(mensagem, data_hora):
    lembrete = {
        "mensagem": mensagem,
        "data_hora": data_hora.strftime("%Y-%m-%d %H:%M")
    }
    try:
        if os.path.exists(CAMINHO_JSON):
            with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
                tarefas = json.load(f)
        else:
            tarefas = []

        tarefas.append(lembrete)
        with open(CAMINHO_JSON, "w", encoding="utf-8") as f:
            json.dump(tarefas, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"❌ Erro ao salvar lembrete: {e}")

def carregar_lembretes_antigos():
    if not os.path.exists(CAMINHO_JSON):
        return
    try:
        with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
            tarefas = json.load(f)
            for tarefa in tarefas:
                msg = tarefa["mensagem"]
                data_str = tarefa["data_hora"]
                data_hora = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
                if data_hora > datetime.now():
                    scheduler.add_job(falar, 'date', run_date=data_hora, args=[msg])
                    print(f"🔁 Lembrete reativado: {msg} em {data_hora}")
    except Exception as e:
        print(f"⚠️ Erro ao carregar lembretes antigos: {e}")

def agendar_lembrete(mensagem, data_hora):
    scheduler.add_job(falar, 'date', run_date=data_hora, args=[mensagem])
    salvar_lembrete_json(mensagem, data_hora)
    print(f"🕒 Lembrete agendado para {data_hora.strftime('%d/%m/%Y %H:%M')}: {mensagem}")

def interpretar_comando_lembrete(frase):
    padrao_data_hora = re.search(r'(\d{1,2}/\d{1,2}/\d{4})[\sT]*(\d{1,2}:\d{2})', frase)
    padrao_minutos = re.search(r'(\d+)\s*min', frase)
    padrao_horas = re.search(r'(\d+)\s*h', frase)

    agora = datetime.now()

    if padrao_data_hora:
        data_str, hora_str = padrao_data_hora.groups()
        try:
            data_hora = datetime.strptime(f"{data_str} {hora_str}", "%d/%m/%Y %H:%M")
            mensagem = frase.split("de")[-1].strip()
            return mensagem, data_hora
        except:
            return None, None
    elif padrao_minutos:
        minutos = int(padrao_minutos.group(1))
        data_hora = agora + timedelta(minutes=minutos)
        mensagem = frase.split("de")[-1].strip()
        return mensagem, data_hora
    elif padrao_horas:
        horas = int(padrao_horas.group(1))
        data_hora = agora + timedelta(hours=horas)
        mensagem = frase.split("de")[-1].strip()
        return mensagem, data_hora
    else:
        return None, None
