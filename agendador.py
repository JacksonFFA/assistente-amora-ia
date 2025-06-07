from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pyttsx3

scheduler = BackgroundScheduler()
scheduler.start()

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def agendar_lembrete(texto, horario_str):
    horario = datetime.strptime(horario_str, "%d/%m/%Y %H:%M")
    scheduler.add_job(falar, 'date', run_date=horario, args=[texto])
    print(f"⏰ Lembrete agendado para {horario_str}")
