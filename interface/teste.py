import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from customtkinter import *
from requests import editProduct, readProducts # type: ignore

def read_text_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            # Dividir cada linha em colunas separadas por tabulação
            columns = line.strip().split(',')
            data.append(columns)
    return data

def procurar_produto():
    tree.delete(*tree.get_children())
    produto_pesquisado = nome_produto.get()
    data = []
    filename = os.path.join('interface', 'estoque.txt')
    with open(filename, "r") as arquivo:
        for linha in arquivo:
            columns = linha.strip().split(',')
            data.append(columns)
        for produto_pesquisado in data:
            if produto_pesquisado in data:
                tree.insert('','end',values=produto_pesquisado)

root=tk.Tk()
tabela = ctk.CTkFrame(root)
tabela.pack(side=tk.LEFT, fill=BOTH, expand=True)
item_selecionado=[]
# Crie a Treeview
tree = ttk.Treeview(tabela, columns=("Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"), show="headings")
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

nome_produto = ctk.CTkEntry(root, placeholder_text="Nome", width=150, height=30) 
nome_produto.pack(padx=10,pady=20)

botao_salvar_edicao = ctk.CTkButton(root, text="Salvar", width=100, command=procurar_produto)
botao_salvar_edicao.pack(pady=10)

# Definir as colunas da tabela
tree.heading("Coluna 1", text="ID")
tree.heading("Coluna 2", text="Data de inclusão")
tree.heading("Coluna 3", text="Nome do Produto")
tree.heading("Coluna 4", text="Valor")



# C ----------------------------------------------------------------------------------------------------------------------------------------------------------
# Função para ler dados do arquivo de texto

# C ----------------------------------------------------------------------------------------------------------------------------------------------------------
# Ler dados do arquivo de texto e preencher o Treeview
filename = os.path.join('interface', 'estoque.txt')
data = read_text_file(filename)
for linha in data:
    tree.insert('', 'end', values=linha)
# C ----------------------------------------------------------------------------------------------------------------------------------------------------------


# Looping para armazenar os itens de cada linha separadamente e filtrar o nome
            
           

root.mainloop()