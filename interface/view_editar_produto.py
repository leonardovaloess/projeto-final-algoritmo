import customtkinter as ctk, tkinter as tk
import tkinter.ttk as ttk
from customtkinter import *
from tkinter import *
from requests import editProduct # type: ignore


def editar_produto(janela_principal,tree):
    tree = tree
    def point_click(event):
        nome_produto.delete(0, tk.END)
        preco_produto.delete(0, tk.END)
        # Recebe o item selecionado
        selected_item = tree.focus()
        # Armazenar a linha do item selecionado em uma lista
        item_selecionado = {tree.item(selected_item, 'values')}
        lista_itens=list(item_selecionado)
        # [0][0] = ID, [0][1] = data, [0][2] = nome, [0][3] = preço
        nome_produto.insert(0,lista_itens[0][2]) # Irá preencher na caixa de entrada o valor da lista posicionado em [0][2]
        preco_produto.insert(0,lista_itens[0][3])# Irá preencher na caixa de entrada o valor da lista posicionado em [0][3]


    def salvar_edicao():
        # Recebe o item selecionado
        selected_item = tree.focus()
        # Armazenar a linha do item selecionado em uma lista
        item_selecionado = {tree.item(selected_item, 'values')}
        lista_itens=list(item_selecionado)
        # Pegar o Id da linha que está sendo clickada
        id_do_produto = lista_itens[0][0]

        # Forçar a variavel id_do_produto a ser inteiro, para ser armazenada no arquivo .txt
        id_do_produto = int(id_do_produto)
        nome_produto_alterado = nome_produto.get()
        # Forçar a variavel nome_produto_alterado a ser uma string, para ser armazenada no arquivo .txt
        nome_produto_alterado = str(nome_produto_alterado)
        preco_produto_alterado = preco_produto.get()
        # Forçar a variavel preco_produto_alterado a ser float, para ser armazenada no arquivo .txt
        preco_produto_alterado = float(preco_produto_alterado.replace("R$", "").replace(",", "."))
        editProduct(id_do_produto, nome_produto_alterado, preco_produto_alterado)
        msg_edicao.configure(text="Produto editado com sucesso", text_color="green")

    # Define dimensões, icone e onde a janela irá "nascer"
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela_editar_produto = ctk.CTkToplevel(janela_principal)
    janela_editar_produto.iconbitmap("interface/images/icon.ico")
    janela_editar_produto.title("Editar Produto")
    janela_editar_produto.geometry("450x350+1400+250")
    janela_editar_produto.resizable(False, False) 
    janela_editar_produto.attributes("-topmost", True)  # Faz a janela secundária sobrepor a principal

    top_frame = ctk.CTkFrame(janela_editar_produto,fg_color="#1a1a1a")
    top_frame.pack(side=ctk.TOP, pady=50, fill=ctk.Y)

    editar_produto_texto = ctk.CTkLabel(top_frame, text="Editar produto")
    editar_produto_texto.grid(row=0, column=0, columnspan=2, pady=10)

    nome_produto = ctk.CTkEntry(top_frame, placeholder_text="Nome do produto", width=300, height=35)
    nome_produto.grid(row=1, column=0, columnspan=2, pady=20, padx=10)

    preco_produto = ctk.CTkEntry(top_frame, placeholder_text="Preço do produto", width=300, height=35)
    preco_produto.grid(row=2, column=0, columnspan=2, padx=10)

    botao_salvar_edicao = ctk.CTkButton(top_frame, text="Salvar", command=salvar_edicao)
    botao_salvar_edicao.grid(row=4, column=0, pady=20,padx=10)

    botao_sair = ctk.CTkButton(top_frame, text="Sair", command=janela_editar_produto.destroy)
    botao_sair.grid(row=4, column=1, pady=20, padx=10)

    msg_edicao = ctk.CTkLabel(top_frame, text="")
    msg_edicao.grid(row=3, column=0, columnspan=2, pady=5)

    # Entrada do valor que o mouse clickou
    tree.bind('<<TreeviewSelect>>', point_click)
    janela_editar_produto.mainloop()