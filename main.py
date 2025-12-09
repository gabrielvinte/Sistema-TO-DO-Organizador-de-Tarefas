#Editar Tarefas


#Funcao para editar tarefa
def EditarTarefas(tarefa, indice):
    tarefa_modificada = input("\nDigite o novo nome para a tarefa: ")
    lista_tarefas[indice] = tarefa_modificada


    print("----Tarefa modificada com sucesso!----\n")



#lista das tarefas - Essa lista vai ser alterada!!! É apenas um modelo para o codigo funcionar
lista_tarefas = ["Estudar", "Trabalhar", "Jogar", "Limpar a pia"]

escolha = "entrada" #variável com valor para não repetir a pegunta a linha 40 e linha 52

#Condicional para verificar se o usuario quer editar alguma tarefa
resposta = int(input("\nVocê deseja alterar alguma tarefa ? \n Digite o numero: \n [1]---sim  \n [2]---não \n Escolha: "))
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

        if(escolha == "entrada"):
            escolha = int(input("Digite o número da tarefa que deseja editar: "))

        if  escolha >= 0 and escolha <= (len(lista_tarefas) -1):
            #Chamando a funcao para editar a tarefa
            EditarTarefas(lista_tarefas[escolha], escolha)

            #Verificando se o usuario deseja alterar outra tarefa para continuar no loop
            resposta= int(input("Deseja alterar alguma outra tarefa? \n [1]---sim  \n [2]---não \n Escolha: "))
            print("")
        else:
            while escolha < 0 or escolha > (len(lista_tarefas) -1):
                print("Por favor digite o numero da tarefa de acordo com a lista apresentada acima! \n")
                escolha = int(input("Digite o número da tarefa que deseja editar: "))

                print("")


    print("\n#--------Lista de Tarefas atualizada--------#")
    contador = 0
    while contador < len(lista_tarefas):
        print(f"[{contador}]----------", lista_tarefas[contador])
        contador += 1

#Condicional para verificar se o usuário irá digitar apenas os numeros 1 ou 2
else:
    while resposta != 1 and resposta != 2:
        print("Por favor digite o número 1 para sim ou o 2 para não")
        resposta = int(input("\nVocê deseja alterar alguma tarefa ? \n Digite o numero: \n [1]---sim  \n [2]---não \n Escolha: "))


#print para pular linha no terminal
print("")


