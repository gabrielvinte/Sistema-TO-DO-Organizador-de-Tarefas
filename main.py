import os

lista_tarefas = []

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    if nome.strip() != "":
        tarefa = {"descricao": nome, "status": "Pendente"}
        lista_tarefas.append(tarefa)
        print("Tarefa adicionada!")
        salvar_dados()
    else:
        print("Nome inválido")


def listar_tarefas():
    print("\n LISTA DE TAREFAS")
    if len(lista_tarefas) == 0:
        print("sem tarefas")
    else:
        for i, t in enumerate(lista_tarefas):
            print(f"{i+1}) {t['descricao']} - {t['status']}")
    print()


def editar_tarefa():
    listar_tarefas()
    try:
        n = int(input("Qual editar? "))
        idx = n - 1
        if 0 <= idx < len(lista_tarefas):
            novo = input("Novo nome: ")
            if novo.strip() != "":
                lista_tarefas[idx]["descricao"] = novo
                print("editado")
                salvar_dados()
            else:
                print("inválido")
        else:
            print("erro ao editar, essa tarefa não existe")
    except:
        print("erro na edição")


def concluir_tarefa():
    listar_tarefas()
    try:
        n = int(input("Qual tarefa você deseja concluir? "))
        i = n - 1
        if i >= 0 and i < len(lista_tarefas):
            lista_tarefas[i]["status"] = "Concluida"
            print("Tarefa Concluida!")
            salvar_dados()
        else:
            print("Tarefa não encontrada")
    except:
        print("Erro ao concluir tarefa, digite um número válido")


def remover_tarefa():
    listar_tarefas()
    try:
        n = int(input("Remover qual? "))
        i = n - 1
        if 0 <= i < len(lista_tarefas):
            apagada = lista_tarefas.pop(i)
            print("removida:", apagada["descricao"])
            salvar_dados()
        else:
            print("não existe")
    except:
        print("erro ao remover")


def menu():
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Concluir")
    print("5 - Remover")
    print("6 - Sair")


while True:
    print("\n Gerenciador de Tarefas")
    menu()
    opc = input("Opção: ")

    if opc == "1":
        adicionar_tarefa()
    elif opc == "2":
        listar_tarefas()
    elif opc == "3":
        editar_tarefa()
    elif opc == "4":
        concluir_tarefa()
    elif opc == "5":
        remover_tarefa()
    elif opc == "6":
        print("fechando...")
        break
