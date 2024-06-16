import tkinter as tk, os
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.title("Filtro de Busca no Estoque")

        # Criar frame para entrada de busca
        self.frame_busca = tk.Frame(self)
        self.frame_busca.pack(fill="x")

        # Criar label e entry para busca
        self.label_busca = tk.Label(self.frame_busca, text="Buscar:")
        self.label_busca.pack(side="left")
        self.entry_busca = tk.Entry(self.frame_busca, width=30)
        self.entry_busca.pack(side="left")

        # Criar botão de busca
        self.button_busca = tk.Button(self.frame_busca, text="Buscar", command=self.filtrar_estoque)
        self.button_busca.pack(side="left")

        # Criar treeview para exibir resultados
        self.tree_estoque = ttk.Treeview(self)
        self.tree_estoque.pack(fill="both", expand=True)

        # Definir colunas da treeview
        self.tree_estoque["columns"] = ("id", "data", "nome", "preço")
        self.tree_estoque.column("#0", width=0, stretch=tk.NO)
        self.tree_estoque.column("id", anchor=tk.W, width=50)
        self.tree_estoque.column("data", anchor=tk.W, width=100)
        self.tree_estoque.column("nome", anchor=tk.W, width=200)
        self.tree_estoque.column("preço", anchor=tk.W, width=100)

        # Definir cabeçalho da treeview
        self.tree_estoque.heading("#0", text="", anchor=tk.W)
        self.tree_estoque.heading("id", text="ID", anchor=tk.W)
        self.tree_estoque.heading("data", text="Data", anchor=tk.W)
        self.tree_estoque.heading("nome", text="Nome", anchor=tk.W)
        self.tree_estoque.heading("preço", text="Preço", anchor=tk.W)

    def filtrar_estoque(self):
        # Limpar treeview
        self.tree_estoque.delete(*self.tree_estoque.get_children())
        filename = os.path.join('interface', 'estoque.txt')
        # Ler arquivo de estoque
        with open(filename, "r") as arquivo:
            for linha in arquivo:
                # Separar informações da linha
                id, data, nome, preco = linha.strip().split(",")

                # Verificar se a palavra digitada está presente na linha
                if self.entry_busca.get().lower() in linha.lower():
                    # Inserir linha na treeview
                    self.tree_estoque.insert("", "end", values=(id, data, nome, preco))

if __name__ == "__main__":
    app = App()
    app.mainloop()