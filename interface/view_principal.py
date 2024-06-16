import customtkinter as ctk
import tkinter as tk
import tkinter.ttk as ttk
import os
from view_adicionar_produto import adicionar_produto
from view_deletar_produto import deletar_produto
from view_editar_produto import editar_produto


def gestor(janela_login):

    def read_text_file(filename):
        data = []
        with open(filename, 'r') as file:
            for line in file:
                columns = line.strip().split(',')
                data.append(columns)
        return data
    
    def atualizar_tabela(data):
        tree.delete(*tree.get_children())
        for row in data:
            tree.insert('', 'end', values=row)

    def buscar_produto():
        palavra_chave = procurar.get().strip().lower()
        if palavra_chave == "":
            return
        # Limpar o Treeview
        # Ler dados do arquivo de texto
        filename = os.path.join('interface', 'estoque.txt')
        data = read_text_file(filename)
        # Preencher o Treeview apenas com os resultados da pesquisa
        for row in data:
            if palavra_chave in row[2].lower():  # Comparar com o nome do produto (terceira coluna)
                tree.delete(*tree.get_children())
                tree.insert('', 'end', values=row)
            else:
                procurar_texto.configure(text="Não foi possível encontrar este produto")


    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela_principal = ctk.CTk()
    janela_principal.title("Gestor de Estoque")
    janela_principal.iconbitmap("interface/images/icon.ico")
    janela_principal.geometry("950x650+490+150")
    janela_principal.resizable(False, False)

    janelas = [janela_login, janela_principal]
    def fechar_janelas(janelas):
        for janela in janelas:
            janela.destroy()
    
    top_frame = ctk.CTkFrame(janela_principal, fg_color="#1a1a1a")
    top_frame.pack(side=tk.TOP, fill=tk.BOTH)

    procurar = ctk.CTkEntry(top_frame, placeholder_text="Procurar Produto", width=200,height=30)
    procurar.grid(row=0, column=0, padx=5, pady=30, columnspan=3)

    procurar_texto = ctk.CTkLabel(top_frame, text="")
    procurar_texto.place(x=10,y=-2)

    botao_pesquisar_produto = ctk.CTkButton(top_frame, text="Pesquisar Produto", width=20,height=35,command=buscar_produto)
    botao_pesquisar_produto.grid(row=0, column=3, padx=5, pady=10)

    botao_editar_produto = ctk.CTkButton(top_frame, text="Editar Produto", width=100,height=35, command=lambda:editar_produto(janela_principal, tree))
    botao_editar_produto.grid(row=0, column=4, padx=5, pady=10)

    botao_adicionar_produto = ctk.CTkButton(top_frame, text="Adicionar Produto", command=lambda: adicionar_produto(janela_principal), width=20, height=35)
    botao_adicionar_produto.grid(row=0, column=5, padx=5, pady=10)

    botao_deletar_produto = ctk.CTkButton(top_frame, text="Deletar Produto", command=lambda:deletar_produto(janela_principal), width=20, height=35)
    botao_deletar_produto.grid(row=0, column=6, padx=5, pady=10)

    botao_atualizar_tabela = ctk.CTkButton(top_frame, text="Atualizar Tabela", command=lambda: atualizar_tabela(read_text_file(filename)), width=20, height=35)
    botao_atualizar_tabela.grid(row=0, column=7, padx=5, pady=10)

    botao_sair = ctk.CTkButton(top_frame, text="Sair", command=lambda:fechar_janelas(janelas), width=120, height=35)
    botao_sair.grid(row=0, column=8, padx=5, pady=10)

    tabela = ctk.CTkFrame(janela_principal)
    tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(tabela, columns=("Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"), show="headings")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    tree.heading("Coluna 1", text="ID")
    tree.heading("Coluna 2", text="Data de inclusão")
    tree.heading("Coluna 3", text="Nome do Produto")
    tree.heading("Coluna 4", text="Valor")

    scrollbar_y = tk.Scrollbar(tabela, orient=tk.VERTICAL, command=tree.yview)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scrollbar_y.set)

    filename = os.path.join('interface', 'estoque.txt')
    data = read_text_file(filename)
    for row in data:
        tree.insert('', 'end', values=row)

    janela_principal.mainloop()
