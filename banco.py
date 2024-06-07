#criar banco de dados - enzo

import sqlite3 as lite

connection = lite.connect("dados.db")

#criando tabela base

with connection: #with irá abrir e fechar o banco de dados automaticamente
    cur = connection.cursor()
    cur.execute()