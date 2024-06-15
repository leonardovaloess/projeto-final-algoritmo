import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from view_principal import gestor

def login():
    email_inserido = email.get()
    senha_inserida = senha.get()
    if email_inserido == "admin" and senha_inserida == "admin12":
        gestor(janela_login)
    else:
        msg_erro = ctk.CTkLabel(janela_login, text="Credenciais Incorretas!")
        msg_erro.pack(padx=10, pady=10)
        

# Define dimensões, icone e onde a janela irá "nascer"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
janela_login = ctk.CTk()
janela_login.title("Gestor de Estoque")
janela_login.geometry("350x390+780+250") 
janela_login.resizable(False, False)
janela_login.iconbitmap("interface/images/icon.ico")

# Área de Login
top_frame = ctk.CTkFrame(janela_login,fg_color="#1a1a1a")
top_frame.pack(side=ctk.TOP, pady=60, fill=ctk.Y)
top_frame.configure(ctk.set_appearance_mode("dark"))

texto = ctk.CTkLabel(top_frame, text="Fazer Login")
texto.grid(row=0, column=0, columnspan=2, pady=10)

email = ctk.CTkEntry(top_frame, placeholder_text="Seu e-mail", width=200, height=30)
email.grid(row=1, column=0, columnspan=2, pady=20, padx=10)

senha = ctk.CTkEntry(top_frame, placeholder_text="Sua senha", show="*",  width=200, height=30)
senha.grid(row=2, column=0, columnspan=2, padx=10)

botao_login = ctk.CTkButton(top_frame, text="Entrar", command=login, width=90, height=30)
botao_login.grid(row=4, column=0, pady=20,padx=5)

botao_sair = ctk.CTkButton(top_frame, text="Sair", command=janela_login.destroy,width=90, height=30)
botao_sair.grid(row=4, column=1, pady=20, padx=5)


# Checkbox para lembrar login
def verificar_checkbox():
    if checkbox_var.get():
        # Checkbox marcado
        email.insert(0,"admin")
        senha.insert(0,"admin12")
    else:
        # Checkbox desmarcado
        email.delete(0, tk.END)
        senha.delete(0, tk.END)
        email.insert(0,"")
        senha.insert(0,"")

checkbox_var = ctk.BooleanVar()
checkbox = ctk.CTkCheckBox(top_frame, text="Lembrar login", variable=checkbox_var,command=verificar_checkbox)
checkbox.grid(row=3, column=0, columnspan=2, pady=20)


# Executa a interface
janela_login.mainloop()
