import tkinter as tk
from tkinter import ttk
import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def populate_treeview(tree, data):
    tree.delete(*tree.get_children())  # Limpar quaisquer itens existentes no Treeview
    for row in data:
        tree.insert('', 'end', values=row)

def main():
    filename = 'C:\VS Code\GitHub\Projeto Final RA\interface\seu_arquivo.csv'  # Insira o caminho do seu arquivo CSV aqui

    # Criar a janela principal
    root = tk.Tk()
    root.title("Exemplo de Treeview com dados de arquivo CSV")

    # Criar o Treeview
    tree = ttk.Treeview(root, columns=("Column 1", "Column 2", "Column 3"), show="headings")
    tree.heading("Column 1", text="Column 1")
    tree.heading("Column 2", text="Column 2")
    tree.heading("Column 3", text="Column 3")
    tree.pack(fill="both", expand=True)

    # Ler os dados do arquivo CSV
    data = read_csv_file(filename)

    # Preencher o Treeview com os dados do arquivo CSV
    populate_treeview(tree, data)

    root.mainloop()

if __name__ == "__main__":
    main()
