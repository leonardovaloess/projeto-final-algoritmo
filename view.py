import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title("Gestão de Estoque") #título da janela
janela.geometry("800x500+550+200") #definindo as dimensões da janela e onde ela irá "nascer"

janela.resizable(False, False) #A janela não será redimensionada manualmente
janela.iconbitmap("images/icon.ico") #definindo icone da janela

#definindo o botão
btn = Button(janela, text="Executar")
btn.pack()
janela.mainloop()