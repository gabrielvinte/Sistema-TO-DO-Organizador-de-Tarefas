#marcar tarefa como concluída
def marcar_tarefa_como_concluida(tarefas):
    print("\nLista de tarefas:")
    for i in range(len(tarefas)):
        print(f"{i+1}. {tarefas[i]}")
#Sessão pra escolher a tarefa concluídas
    escolha = int(input("\nDigite o número da tarefa concluída: ")) - 1

    if 0 <= escolha < len(tarefas):
        tarefa = tarefas.pop(escolha)
        print(f"\nTarefa concluída: {tarefa}")
    else:
        print("\nNúmero inválido")