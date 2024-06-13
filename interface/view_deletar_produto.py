import customtkinter
import tkinter as tk
from tkinter import *
from requests import deleteProduct # type: ignore

def deletar_produto():
    def deletar():
        try:
            id_inserido = id_produto.get()
            deleteProduct(id_inserido)
            msg_ack = customtkinter.CTkLabel(janela_deletar_produto, text="Produto deletado com sucesso!")
            msg_ack.pack(pady=10)
        except:
            msg_erro = customtkinter.CTkLabel(janela_deletar_produto, text="Erro! ID inexistente")
            msg_erro.pack(pady=10)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    janela_deletar_produto = customtkinter.CTk()
    janela_deletar_produto.title("Gestor de Estoque")
    janela_deletar_produto.iconbitmap("interface/images/icon.ico")
    janela_deletar_produto.geometry("350x250+600+250")
    janela_deletar_produto.resizable(False, False)

    id_produto = customtkinter.CTkEntry(janela_deletar_produto, placeholder_text="ID do produto", width=150, height=30)
    id_produto.pack(padx=10,pady=80)

    botao_deletar_produto = customtkinter.CTkButton(janela_deletar_produto, text="Deletar Produto", command=deletar)
    botao_deletar_produto.place(x=105,y=130)

    botao_sair = customtkinter.CTkButton(janela_deletar_produto, text="Sair", command=janela_deletar_produto.destroy)
    botao_sair.place(x= 105, y=170)

    janela_deletar_produto.mainloop()
