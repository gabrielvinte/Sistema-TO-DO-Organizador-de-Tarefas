# Remover uma tarefa
tarefas= ['estudar']
num = int(input('Digite o número da tarefa que você deseja remover: '))

if 0 <= num < len(tarefas):
    t_removida = tarefas.pop(num)
    print(f'Tarefa removida: {t_removida}')
else:
    print('Número inválido.')

# Mostra a lista das tarefas que restaram
print('Lista após remoção da tarefa:')
for x, tarefa in enumerate(tarefas):
    print(f'{x} - {tarefa}')
