import json
from pathlib import Path

ARQUIVO_TAREFAS = Path("tarefas.json")

def carregar_tarefas():
    if ARQUIVO_TAREFAS.exists():
        with open(ARQUIVO_TAREFAS, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(tarefas, f, indent=2)

def adicionar_tarefa(texto):
    tarefas = carregar_tarefas()
    tarefas.append({"tarefa": texto})
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada!")

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("🎉 Sem tarefas por enquanto!")
    else:
        print("📋 Tarefas pendentes:")
        for i, t in enumerate(tarefas, 1):
            print(f"{i}. {t['tarefa']}")
