import customtkinter
import tkinter as tk
from tkinter import *
from requests import createProduct  # type: ignore

def adicionar_produto():
    
    def registrar_produto():
        try:
            nome_produto = nome.get()
            preco_produto = preco.get()
            # Função do arquivo requests para criar um produto com ID
            # Com base no nome e preço fornecido
            createProduct(nome_produto,preco_produto)
            msg_ack = customtkinter.CTkLabel(top_frame, text="Produto cadastrado com sucesso!")
            msg_ack.pack()
        except:
            msg_erro = customtkinter.CTkLabel(top_frame, text="Erro ao cadastrar produto")
            msg_erro.pack()
    

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    janela_novo_produto = customtkinter.CTk()
    janela_novo_produto.title("Registrar Produto")
    janela_novo_produto.iconbitmap("interface/images/icon.ico")
    janela_novo_produto.geometry("650x350+600+250")
    janela_novo_produto.resizable(False, False)

    top_frame = customtkinter.CTkFrame(janela_novo_produto)
    top_frame.pack(side=tk.TOP, fill=tk.Y, pady= 60)
    registrar_produto_texto = customtkinter.CTkLabel(top_frame, text="Registrar produto")
    registrar_produto_texto.pack()
    nome = customtkinter.CTkEntry(top_frame, placeholder_text="Nome do produto", width=300, height=30)
    nome.pack(padx=10,pady=30)
    preco = customtkinter.CTkEntry(top_frame, placeholder_text="Preço do produto", width=300, height=30)
    preco.pack()

    botao_sair = customtkinter.CTkButton(janela_novo_produto, text="Sair", command=janela_novo_produto.destroy)
    botao_sair.place(x= 330, y=260)
    # Aqui irá enviar os dados para serem registrados no arquivo .txt
    botao_adicionar_produto = customtkinter.CTkButton(janela_novo_produto, text="Adicionar produto", command=registrar_produto)
    botao_adicionar_produto.place(x= 170, y=260)

    janela_novo_produto.mainloop()