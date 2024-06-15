import customtkinter as ctk, os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from view_adicionar_produto import adicionar_produto
from view_deletar_produto import deletar_produto
from view_editar_produto import editar_produto

def gestor(janela_login):

    # Função para ler todos os dados do arquivo txt e preencher o Treeview
    def atualizar_tabela(tree):
        def read_text_file(filename):
            data = []
            with open(filename, 'r') as file:
                for line in file:
                    # Dividir cada linha em colunas separadas por tabulação
                    columns = line.strip().split(',')
                    data.append(columns)
            return data
        tree.delete(*tree.get_children())

        # Ler dados do arquivo de texto através da função e preencher o Treeview com o for
        filename = os.path.join('interface', 'estoque.txt')
        data = read_text_file(filename)
        for row in data:
            tree.insert('', 'end', values=row)

    # Define dimensões, icone e onde a janela irá "nascer"
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela_principal = ctk.CTk()
    janela_principal.title("Gestor de Estoque")
    janela_principal.iconbitmap("interface/images/icon.ico")
    janela_principal.geometry("950x650+490+150")
    janela_principal.resizable(False, False)

    # Lista e função para armazenar as janelas para poder fechar todas de uma vez só
    janelas = [janela_login, janela_principal]
    def fechar_janelas(janelas):
        for janela in janelas:
            janela.destroy()

    # Criar um frame para a barra de pesquisa e botão para pesquisar produto ficarem em cima
    top_frame = ctk.CTkFrame(janela_principal,fg_color="#1a1a1a")
    top_frame.pack(side=tk.TOP, fill=tk.BOTH)

    # Criando o Entry para procurar produto
    procurar = ctk.CTkEntry(top_frame, placeholder_text="Procurar Produto", width=200)
    procurar.grid(row=0, column=0, padx=5, pady=10, columnspan=3)

    # Botão para pesquisar produto
    botao_pesquisar_produto = ctk.CTkButton(top_frame, text="Pesquisar Produto", width=20)
    botao_pesquisar_produto.grid(row=0, column=3, padx=5, pady=10)

    # Botão para editar produto
    botao_editar_produto = ctk.CTkButton(top_frame, text="Editar Produto", width=100, command=lambda:editar_produto(janela_principal,tree))
    botao_editar_produto.grid(row=0, column=4, padx=5, pady=10)


    # Botão para adicionar produto
    botao_adicionar_produto = ctk.CTkButton(top_frame, text="Adicionar Produto", command=lambda: adicionar_produto(janela_principal), width=20)
    botao_adicionar_produto.grid(row=0, column=5, padx=5, pady=10)

    # Botão para deletar produto
    botao_deletar_produto = ctk.CTkButton(top_frame, text="Deletar Produto", command=lambda:deletar_produto(janela_principal), width=20)
    botao_deletar_produto.grid(row=0, column=6, padx=5, pady=10)

    # Botão para atualizar tabela
    botao_atualizar_tabela = ctk.CTkButton(top_frame, text="Atualizar Tabela", command=lambda: atualizar_tabela(tree), width=20)
    botao_atualizar_tabela.grid(row=0, column=7, padx=5, pady=10)

    # Botão para sair
    botao_sair = ctk.CTkButton(top_frame, text="Sair", command=lambda:fechar_janelas(janelas), width=120)
    botao_sair.grid(row=0, column=8, padx=5, pady=10)



    # Criar um frame para a tabela
    tabela = ctk.CTkFrame(janela_principal)
    tabela.pack(side=tk.LEFT, fill=BOTH, expand=True)

    # Criar uma tabela com scrollbars
    tree = ttk.Treeview(tabela, columns=("Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"), show="headings")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Definir as colunas da tabela
    tree.heading("Coluna 1", text="ID")
    tree.heading("Coluna 2", text="Data de inclusão")
    tree.heading("Coluna 3", text="Nome do Produto")
    tree.heading("Coluna 4", text="Valor")

    # Criar um scrollbar vertical
    scrollbar_y = tk.Scrollbar(tabela, orient=tk.VERTICAL, command=tree.yview)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scrollbar_y.set)

    # Função para ler dados do arquivo de texto
    def read_text_file(filename):
        data = []
        with open(filename, 'r') as file:
            for line in file:
                # Dividir cada linha em colunas separadas por tabulação
                columns = line.strip().split(',')
                data.append(columns)
        return data

    # Ler dados do arquivo de texto e preencher o Treeview

    filename = os.path.join('interface', 'estoque.txt')

    data = read_text_file(filename)
    for row in data:
        tree.insert('', 'end', values=row)

    janela_principal.mainloop()