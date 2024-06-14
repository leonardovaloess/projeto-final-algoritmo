import customtkinter as ctk
import tkinter as tk
from tkinter import *
from requests import createProduct  # type: ignore


def adicionar_produto(janela_principal):

    def adicionar_produto():
        nome = entrada_nome.get()
        preco = entrada_preco.get()
        
        if not nome or not preco:
            mostrar_erro("Erro ao cadastrar produto: Campos vazios")
        else:
            try:
                preco = float(preco)
                createProduct(nome,preco)
                mostrar_erro("Produto cadastrado com sucesso", sucesso=True)
            # Se o usuário digitar um valor com "," irá dar erro
            except ValueError:
                mostrar_erro("Erro ao cadastrar produto: Preço inválido")

    def mostrar_erro(mensagem, sucesso=False):
        msg_erro.configure(text=mensagem, text_color="green" if sucesso else "red")


    # Configurações da janela principal
    janela_novo_produto = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela_novo_produto = ctk.CTkToplevel(janela_principal)
    janela_novo_produto.title("Registrar Produto")
    janela_novo_produto.iconbitmap("interface/images/icon.ico")
    janela_novo_produto.geometry("450x350+600+250")
    janela_novo_produto.resizable(False, False)
    janela_novo_produto.grab_set()   
    janela_novo_produto.attributes("-topmost", True)  # Faz a janela secundária sobrepor a principal
    janela_novo_produto.protocol("WM_DELETE_WINDOW", lambda: None)  # Impede o fechamento da janela secundária

    top_frame = ctk.CTkFrame(janela_novo_produto)
    top_frame.pack(side=ctk.TOP, pady=50, fill=ctk.Y)

    registrar_produto_texto = ctk.CTkLabel(top_frame, text="Registrar produto")
    registrar_produto_texto.grid(row=0, column=0, columnspan=2, pady=10)

    entrada_nome = ctk.CTkEntry(top_frame, placeholder_text="Nome do produto", width=200)
    entrada_nome.grid(row=1, column=0, columnspan=2, pady=20, padx=10)

    entrada_preco = ctk.CTkEntry(top_frame, placeholder_text="Preço do produto", width=200)
    entrada_preco.grid(row=2, column=0, columnspan=2, padx=10)

    msg_erro = ctk.CTkLabel(top_frame, text="")
    msg_erro.grid(row=3, column=0, columnspan=2, pady=5)

    botao_adicionar_produto = ctk.CTkButton(top_frame, text="Adicionar produto", command=adicionar_produto)
    botao_adicionar_produto.grid(row=4, column=0, pady=10,padx=10)

    botao_sair = ctk.CTkButton(top_frame, text="Sair", command=janela_novo_produto.destroy)
    botao_sair.grid(row=4, column=1, pady=10, padx=10)

    janela_novo_produto.mainloop()