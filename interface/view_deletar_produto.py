import customtkinter,os
import tkinter as tk
from tkinter import *
from requests import deleteProduct # type: ignore

def deletar_produto():

    # Função para deletar a linha no arquivo .txt com base no ID inserido
    def deletar():
        numeros_do_estoque = numeros_estoque()
        id_inserido = id_produto.get()
        if not id_inserido:
            mostrar_erro("Erro! ID inexistente")
        else:
            try:
                id_inserido = int(id_inserido)
                deleteProduct(id_inserido)
                if id_inserido in numeros_do_estoque:
                    mostrar_erro("Produto deletado com sucesso!", sucesso=True)
                else:
                    mostrar_erro("Erro ao deletar produto: ID inválido")

            except ValueError:
                mostrar_erro("Erro ao deletar produto: ID inválido")

    # Função para aparecer a mensagem conforme as condições da variavel id_inserido
    def mostrar_erro(mensagem, sucesso=False):
        msg_erro.configure(text=mensagem, text_color="green" if sucesso else "red")
        msg_erro.after(3000, ocultar_erro)

    # Função para apagar o texto
    def ocultar_erro():
        msg_erro.configure(text="")
            
    # Função para buscar os números de id dentro do arquivo .txt
    def numeros_estoque():
        # Abrir o arquivo para leitura
        caminho = os.path.join('interface', 'estoque.txt')
        with open(caminho, 'r') as f:
            linhas = f.readlines()  # Ler todas as linhas do arquivo
        # Inicializar uma lista para armazenar os números
        numeros = []
        # Iterar sobre cada linha do arquivo
        for linha in linhas:
            # Dividir a linha por vírgula para obter os elementos separados
            elementos = linha.strip().split(',')
            # Extrair o primeiro elemento que contém o número desejado
            numero = int(elementos[0].strip())
            # Adicionar o número à lista de números
            numeros.append(numero)
        return numeros

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

    msg_erro = customtkinter.CTkLabel(janela_deletar_produto, text="")
    msg_erro.pack(pady=10)

    botao_sair = customtkinter.CTkButton(janela_deletar_produto, text="Sair", command=janela_deletar_produto.destroy)
    botao_sair.place(x= 105, y=170)

    janela_deletar_produto.mainloop()
