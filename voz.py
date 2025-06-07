import sounddevice as sd
import speech_recognition as sr
import numpy as np

def ouvir_microfone():
    recognizer = sr.Recognizer()

    print("🎙️ Fale agora...")

    # Grava 4 segundos de áudio com o microfone padrão
    fs = 44100  # taxa de amostragem
    seconds = 4
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Converte o áudio capturado para AudioData do SpeechRecognition
    audio_data = sr.AudioData(audio.tobytes(), fs, 2)

    try:
        texto = recognizer.recognize_google(audio_data, language='pt-BR')
        print(f"🗣️ Você disse: {texto}")
        return texto.lower()
    except sr.UnknownValueError:
        print("❌ Não entendi o que foi dito.")
        return ""
    except sr.RequestError:
        print("❌ Erro ao se conectar com o serviço da Google.")
        return ""
