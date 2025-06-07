import speech_recognition as sr
import pyttsx3
import time

# Inicializa o mecanismo de fala
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Inicializa o reconhecimento de voz
recognizer = sr.Recognizer()
microfone = sr.Microphone()

falar("👋 Amora iniciada! Diga 'Olá Amora' para começar.")

while True:
    with microfone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎙️ Aguardando comando: 'Olá Amora'...")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language='pt-BR').lower()
        print(f"🗣️ Você disse: {texto}")

        if "olá amora" in texto or "hey amora" in texto:
            falar("Oi Jackson! Estou ouvindo.")

            # Agora escuta o comando real
            with microfone as source:
                recognizer.adjust_for_ambient_noise(source)
                print("🎧 Pode falar seu comando...")
                audio = recognizer.listen(source)

            try:
                comando = recognizer.recognize_google(audio, language='pt-BR').lower()
                print(f"🎤 Comando: {comando}")

                # Aqui você trata os comandos reais, por exemplo:
                if "que horas são" in comando:
                    agora = time.strftime("%H:%M")
                    falar(f"Agora são {agora}")
                elif "me acorde" in comando:
                    falar("Certo! Lembrete para acordar agendado. Em breve adicionaremos isso.")
                else:
                    falar("Desculpe, não entendi o comando.")
            except sr.UnknownValueError:
                falar("Não consegui entender o que você disse.")

    except sr.UnknownValueError:
        print("❌ Não entendi o que foi dito.")
    except sr.RequestError as e:
        print(f"Erro na requisição de reconhecimento de voz: {e}")
