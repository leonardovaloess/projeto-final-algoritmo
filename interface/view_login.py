import tkinter as tk
import customtkinter
from customtkinter import *
from tkinter import *
from view_principal import gestor

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
texto.pack(padx=10, pady=30)
email = customtkinter.CTkEntry(janela_login, placeholder_text="Seu e-mail", width=300, height=30)
email.pack()
senha = customtkinter.CTkEntry(janela_login, placeholder_text="Sua senha", show="*",  width=300, height=30)
senha.pack(padx=10, pady=10)
checkbox = customtkinter.CTkCheckBox(janela_login, text="Lembrar Login", corner_radius=15, checkbox_height=30, checkbox_width=30)
checkbox.place(x= 130, y= 230)

#Abre a janela do gestor
botao_login = customtkinter.CTkButton(janela_login, text="Entrar", command=gestor)
botao_login.place(x=50,y=180)
botao_sair = customtkinter.CTkButton(janela_login, text="Sair", command=janela_login.destroy)
botao_sair.place(x=210,y=180)


#executa a interface
janela_login.mainloop()