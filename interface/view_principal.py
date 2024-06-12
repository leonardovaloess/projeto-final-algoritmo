import customtkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from view_adicionar_produto import adicionar_produto

def gestor():
    def barra_pesquisa():
        pesquisa = procurar.get()
        print(pesquisa)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    janela_principal = customtkinter.CTk()
    janela_principal.title("Gestor de Estoque")
    janela_principal.iconbitmap("interface/images/icon.ico")
    janela_principal.geometry("950x650+450+100")
    janela_principal.resizable(False, False)


    # Criar um frame para a barra de pesquisa e botões
    top_frame = customtkinter.CTkFrame(janela_principal)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    procurar = customtkinter.CTkEntry(top_frame, placeholder_text="Procurar Produto", width=350, height=30)
    procurar.place(x=100,y=10)

    botao_pesquisar_produto = customtkinter.CTkButton(top_frame, text="Pesquisar Produto", command=barra_pesquisa)
    botao_pesquisar_produto.place(x= 480, y = 10)

    botao_sair = customtkinter.CTkButton(top_frame, text="Sair", command=janela_principal.destroy)
    botao_sair.pack(side=RIGHT,padx=10, pady=10)

    botao_adicionar_produto = customtkinter.CTkButton(top_frame, text="Adicionar Produto", command=adicionar_produto)
    botao_adicionar_produto.pack(side=RIGHT,padx= 10, pady = 10)


    # Criar um frame para a tabela
    tabela = customtkinter.CTkFrame(janela_principal)
    tabela.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    tabela.configure(height=400)

    # Criar uma tabela com scrollbars
    tree = ttk.Treeview(tabela, columns=("Coluna 1", "Coluna 2", "Coluna 3"), show="headings")
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Definir as colunas da tabela
    tree.heading("Coluna 1", text="Data de inclusão")
    tree.heading("Coluna 2", text="Nome do Produto")
    tree.heading("Coluna 3", text="Valor")

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

    filename = 'C:\\projetos\projeto-final-algoritmo\interface\estoque.txt'

    data = read_text_file(filename)
    for row in data:
        tree.insert('', 'end', values=row)

    janela_principal.mainloop()