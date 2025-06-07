from tarefas import listar_tarefas_texto

def consultar_agenda():
    tarefas = listar_tarefas_texto()

    if not tarefas:
        return "Hoje está tranquilo, Jackson! Aproveite o dia com sabedoria."

    total = len(tarefas)
    plural = "tarefas" if total > 1 else "tarefa"
    resposta = f"Você tem {total} {plural} hoje. Vamos lá: "

    for i, tarefa in enumerate(tarefas, 1):
        resposta += f"{i} — {tarefa.strip()}. "

    return resposta.strip()
