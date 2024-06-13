import tkinter as tk
import customtkinter
from customtkinter import *
from tkinter import *
from view_principal import gestor

def login():
    email_inserido = email.get()
    senha_inserida = senha.get()
    if email_inserido == "admin" and senha_inserida == "admin12":
        gestor()
    else:
        msg_erro = customtkinter.CTkLabel(janela_login, text="Credenciais Incorretas!")
        msg_erro.pack(padx=10, pady=40)
        
janela_login = customtkinter.CTk()
janela_login.title("Gestor de Estoque")

#define dimensões, icone e onde a janela irá "nascer"
janela_login.geometry("400x350+680+200") 
janela_login.resizable(False, False)
janela_login.iconbitmap("interface/images/icon.ico")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Área de Login
texto = customtkinter.CTkLabel(janela_login, text="Fazer Login")
texto.pack(padx=10, pady=40)
email = customtkinter.CTkEntry(janela_login, placeholder_text="Seu e-mail", width=200, height=30)
email.pack()
senha = customtkinter.CTkEntry(janela_login, placeholder_text="Sua senha", show="*",  width=200, height=30)
senha.pack(padx=10, pady=20)

#Abre a janela do gestor
botao_login = customtkinter.CTkButton(janela_login, text="Entrar", command=login, width=90, height=30)
botao_login.place(x=100,y=220)
botao_sair = customtkinter.CTkButton(janela_login, text="Sair", command=janela_login.destroy,width=90, height=30)
botao_sair.place(x=210,y=220)


#executa a interface
<<<<<<< HEAD
janela_login.mainloop()
=======
janela_login.mainloop()
>>>>>>> main
