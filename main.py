tarefas = []
teste = 's'
while teste != 'n':
    nova_tarefa = input('Digite o nome da tarefa:')
    tarefas.append(nova_tarefa)
    teste = input('quer continuar? [s/n]')

print('lista finalizada')