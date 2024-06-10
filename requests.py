import sqlite3 as lite

connection = lite.connect("dados.db")

#CREATE

def createProduct(data):
    with connection: 
        cur = connection.cursor()
        query = "INSERT INTO produtos (name, price, description, imageurl, stock) VALUES (?, ?, ?, ?, ?)"
        cur.execute(query,data)    

#UPDATE

def editProduct(data):
    with connection: 
        cur = connection.cursor()
        query = f"UPDATE produtos SET name=? WHERE id=?"
        cur.execute(query,data)


#DELETE

def deleteProdut(id):
    with connection: 
        cur = connection.cursor()
        query = "DELETE FROM produtos WHERE id=?"
        cur.execute(query,id)

#READ
def fetchProducts():
    with connection:
        cur = connection.cursor()
        query = "SELECT * FROM produtos"
        cur.execute(query)
        info = cur.fetchall()
        print(info)

fetchProducts()
