import tkinter as tk
from tkinter import *

def transforma_texto():
    texto = "leonardo viado"
    texto_botão1["text"] = texto

janela = tk.Tk()
janela.title("Gestão de Estoque")

texto_orientação = Label(janela, text="Clique em uma das opções")
#FORMATAÇÃO DO TEXTO
texto_orientação.grid(column=0,row=0)

botao1 = Button(janela, text="Inserir um novo produto", command=transforma_texto) #command = "dar o comando do que o botão irá fazer"
botao2 = Button(janela, text="Verificar lista de produtos")

texto_botão1 = Label(janela, text='')
texto_botão1.grid(column=0,row=2)
#FORMATAÇÃO DO BOTÃO
botao1.grid(column=0,row=1)
#deu certo o merge
janela.mainloop()