import customtkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

def adicionar_produto():
    
    def registrar_produto():
        data_produto = data.get()
        nome_produto = nome.get()
        preco_produto = preco.get()
        print(data_produto,",",nome_produto, ",","R$", preco_produto)


    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    janela_novo_produto = customtkinter.CTk()
    janela_novo_produto.title("Registrar Produto")
    janela_novo_produto.iconbitmap("interface/images/icon.ico")
    janela_novo_produto.geometry("650x350+600+250")
    janela_novo_produto.resizable(False, False)

    top_frame = customtkinter.CTkFrame(janela_novo_produto)
    top_frame.pack(side=tk.TOP, fill=tk.Y, pady= 60)
    data_texto = customtkinter.CTkLabel(top_frame, text="Registrar produto")
    data_texto.pack()
    data = customtkinter.CTkEntry(top_frame, placeholder_text="Data de inclusão (dd/mm/yyyy)", width=300, height=30)
    data.pack()
    nome = customtkinter.CTkEntry(top_frame, placeholder_text="Nome do produto", width=300, height=30)
    nome.pack(padx=10,pady=30)
    preco = customtkinter.CTkEntry(top_frame, placeholder_text="Preço do produto", width=300, height=30)
    preco.pack()

    botao_sair = customtkinter.CTkButton(janela_novo_produto, text="Sair", command=janela_novo_produto.destroy)
    botao_sair.place(x= 330, y=260)
    botao_adicionar_produto = customtkinter.CTkButton(janela_novo_produto, text="Adicionar produto", command=registrar_produto)
    botao_adicionar_produto.place(x= 170, y=260)

    janela_novo_produto.mainloop()