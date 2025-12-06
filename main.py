#Editar Tarefas


#Funcao para editar tarefa
def EditarTarefas(tarefa, indice):
    tarefa_modificada = input("\nDigite o novo nome para a tarefa: ")
    lista_tarefas[indice] = tarefa_modificada


    print("----Tarefa modificada com sucesso!----\n")



#lista das tarefas - Essa lista vai ser alterada!!! É apenas um modelo para o codigo funcionar
lista_tarefas = ["Estudar", "Trabalhar", "Jogar", "Limpar a pia"]


#Condicional para verificar se o usuario quer editar alguma tarefa
resposta = int(input("\nVocê deseja alterar alguma tarefa ? \n [1]---sim  \n [2]---não \n Escolha: "))
print(" ")

#Condicional para editar as tarefas
if resposta == 1:
    while resposta != 2:
        print("#-------Lista de Tarefas-------#\n")

        #Mostra toda a lista de tarefa
        contador = 0
        while contador < len(lista_tarefas):
            print(f"[{contador}]----------" ,lista_tarefas[contador] )
            contador += 1

        print(" ")

        #Usuario escolhe qual tarefa ele deseja editar
        contador = 0
        escolha = int(input("Digite o número da tarefa que deseja editar: "))


        #Chamando a funcao para editar a tarefa
        EditarTarefas(lista_tarefas[escolha], escolha)

        #Verificando se o usuario deseja alterar outra tarefa para continuar no loop
        resposta= int(input("Deseja alterar alguma outra tarefa? \n [1]---sim  \n [2]---não \n Escolha: "))
        print("")


print("\n#--------Lista de Tarefas atualizada--------#")
contador = 0
while contador < len(lista_tarefas):
    print(f"[{contador}]----------" ,lista_tarefas[contador] )
    contador += 1
