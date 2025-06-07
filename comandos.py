import webbrowser
import os

def abrir_programa_ou_site(texto):
    if "tcs" in texto:
        webbrowser.open("https://www.tcs.com")
    elif "github" in texto:
        webbrowser.open("https://github.com")
    elif "vs code" in texto:
        os.system("code")  # VS Code instalado?
    else:
        print("❌ Comando não reconhecido.")
