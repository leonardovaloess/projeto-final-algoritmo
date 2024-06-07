#criar connection com o banco de dados - Leo

import sqlite3 as lite

connection = lite.connect("dados.db")

#criando tabela base

with connection: #with irá abrir e fechar o banco de dados automaticamente
    cur = connection.cursor()
    
    #criando a tabela do banco
    cur.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(100), 
            price FLOAT, 
            description TEXT,
            imageurl TEXT, 
            stock INTEGER
        )
    """)   