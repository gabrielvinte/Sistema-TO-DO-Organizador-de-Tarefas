  ##Função para mostrar a Lista numerada
def listar_tarefas(tarefas):
    if len(tarefas) == 0:      ##Se a contagem das tarefas for zero não há tarefas.
        print("Não há tarefas cadastradas.\n")
        return
    
    print("\n=== TAREFAS DISPONÍVEIS ===")
    for i, tarefa in enumerate(tarefas, start=1):   ##Loop para passar por todas as tarefas, cada loop vai printar a status, nome e prioridade de uma tarefa.
        # Mostra nome e prioridade se existir
        prioridade = tarefa.get('prioridade', 'Não definida')      ##Guardamos o variavel prioridade no array 0 da biblioteca tarefa, se não ouver o array 0 então não foi definida, e pula para o array 1.
        status = "✓" if tarefa.get('concluida', False) else " "     ## Guardamos a variavel status na biblioteca tarefa, Se estiver retornar concluida então printa "✓", se não for concluida, então printa falso e define o valor de status para " " (não concluida).
        print(f"{i}. [{status}] {tarefa['nome']} - Prioridade: {prioridade}")  ##Printa resultado.
    print("===========================\n")
