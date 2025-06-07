# test_microfone.py
import speech_recognition as sr

reconhecedor = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Teste de microfone: fale algo...")
    audio = reconhecedor.listen(source)

try:
    texto = reconhecedor.recognize_google(audio, language="pt-BR")
    print("Você disse:", texto)
except Exception as e:
    print("Erro:", e)
