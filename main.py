import os
import tkinter as tk
from tkinter import messagebox

lista_tarefas = []

# SISTEMA

def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    prioridade = input("Prioridade (1- Alta | 2- Média | 3- Baixa): ")

    if prioridade not in ["1", "2", "3"]:
        print("Prioridade inválida, definida como 3 (Baixa).")
        prioridade = "3"

    if nome.strip() != "":
        tarefa = {"descricao": nome, "status": "Pendente", "prioridade": prioridade}
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
            pri = {"1":"Alta", "2":"Média", "3":"Baixa"}[t['prioridade']]
            print(f"{i+1}) {t['descricao']} - {t['status']} (Prioridade: {pri})")
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


def carregar_dados():
    if os.path.exists("tarefas.txt"):
        arq = open("tarefas.txt", "r")
        coisas = arq.readlines()
        for c in coisas:
            p = c.replace("\n", "").split(";")
            if len(p) == 3:
                lista_tarefas.append({"descricao": p[0], "status": p[1], "prioridade": p[2]})
        arq.close()


def salvar_dados():
    arq = open("tarefas.txt", "w")
    for t in lista_tarefas:
        arq.write(t["descricao"] + ";" + t["status"] + ";" + t["prioridade"] + "\n")
    arq.close()


# INTERFACE TKINTER 

root = tk.Tk()
root.title("Gerenciador de Tarefas")
root.geometry("500x500")

entrada_desc = tk.Entry(root, width=40)
entrada_desc.pack(pady=5)

prioridade_var = tk.StringVar(value="3")

frame_radio = tk.Frame(root)
frame_radio.pack(pady=5)

tk.Label(root, text="Prioridade:").pack()

tk.Radiobutton(frame_radio, text="Alta", variable=prioridade_var, value="1").grid(row=0, column=0)
tk.Radiobutton(frame_radio, text="Média", variable=prioridade_var, value="2").grid(row=0, column=1)
tk.Radiobutton(frame_radio, text="Baixa", variable=prioridade_var, value="3").grid(row=0, column=2)

lista_box = tk.Listbox(root, width=55, height=15)
lista_box.pack(pady=10)


def atualizar_lista_interface():
    lista_box.delete(0, tk.END)
    for i, t in enumerate(lista_tarefas):
        pri = {"1":"Alta", "2":"Média", "3":"Baixa"}[t['prioridade']]
        lista_box.insert(tk.END, f"{i+1}) {t['descricao']} - {t['status']} (Prioridade: {pri})")


def ui_adicionar():
    descricao = entrada_desc.get().strip()
    prioridade = prioridade_var.get()

    if descricao == "":
        messagebox.showerror("Erro", "Descrição inválida")
        return

    lista_tarefas.append({"descricao": descricao, "status": "Pendente", "prioridade": prioridade})
    salvar_dados()
    atualizar_lista_interface()
    entrada_desc.delete(0, tk.END)


def ui_remover():
    sel = lista_box.curselection()
    if not sel:
        return
    idx = sel[0]
    lista_tarefas.pop(idx)
    salvar_dados()
    atualizar_lista_interface()


def ui_concluir():
    sel = lista_box.curselection()
    if not sel:
        return
    lista_tarefas[sel[0]]["status"] = "Concluida"
    salvar_dados()
    atualizar_lista_interface()


def ui_editar():
    sel = lista_box.curselection()
    if not sel:
        return
    novo = entrada_desc.get().strip()
    if novo == "":
        return
    lista_tarefas[sel[0]]["descricao"] = novo
    salvar_dados()
    atualizar_lista_interface()
    entrada_desc.delete(0, tk.END)


frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Adicionar", width=10, command=ui_adicionar).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Editar", width=10, command=ui_editar).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Concluir", width=10, command=ui_concluir).grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="Remover", width=10, command=ui_remover).grid(row=0, column=3, padx=5)

tk.Button(root, text="Sair", width=10, command=root.destroy).pack(pady=10)


carregar_dados()
atualizar_lista_interface()

root.mainloop()


# MENU
print("\nSistema em modo texto também está disponível\n")

while True:
    print("\n Gerenciador de Tarefas (Modo Texto)")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Editar")
    print("4 - Concluir")
    print("5 - Remover")
    print("6 - Sair")

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
