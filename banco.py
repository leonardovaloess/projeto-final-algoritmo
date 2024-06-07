#criar connection com o banco de dados - Leo

import sqlite3 as lite

connection = lite.connect("dados.db")

#criando tabela base

with connection: #with irá abrir e fechar o banco de dados automaticamente
    cur = connection.cursor()
    cur.execute("CREATE TABLE produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco )")
    