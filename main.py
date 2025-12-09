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


def menu():
    print("1 - Adicionar")
    print("2 - Listar")


while True:
    print("\n Gerenciador de Tarefas")
    menu()
    opc = input("Opção: ")

    if opc == "1":
        adicionar_tarefa()
    elif opc == "2":
        listar_tarefas()
