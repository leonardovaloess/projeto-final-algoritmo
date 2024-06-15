import os
from datetime import datetime

caminho = os.path.join('interface', 'estoque.txt')

#logica para pegar todos as linhas do arquivo txt e transformar em uma lista
def readProducts():
    caminho = os.path.join('interface', 'estoque.txt')
    if not os.path.exists(caminho):
        return []
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return linhas

# logica para adicionar o proximo id da lista
def get_next_id(caminho_estoque):
    if not os.path.exists(caminho_estoque):
        return 1
    with open(caminho_estoque, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        if not linhas:
            return 1
        else:
            ultima_linha = linhas[-1].strip()
            if not ultima_linha:
                return 1
            ultimo_id = int(ultima_linha.split(',')[0])
            return ultimo_id + 1

# Função para criar o produto com ID único
def createProduct(name, price):
    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%d/%m/%Y')
    
    caminho = os.path.join('interface', 'estoque.txt')
    
    id_unico = get_next_id(caminho)
    
    product = f'{id_unico},{data_formatada},{name},R$ {price}\n'
    
    with open(caminho, 'a', encoding='utf-8') as arquivo:
        arquivo.write(product)

# Teste da função createProduct


# Função para deletar um produto pelo ID
def deleteProduct(id):
    caminho = os.path.join('interface', 'estoque.txt')
    produtos = readProducts()
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        for produto in produtos:
            if int(produto.split(',')[0]) != id:
                arquivo.write(produto)



def editProduct(id, new_name, new_price):
    produtos = readProducts()
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        for produto in produtos:
            parts = produto.split(',')
            if int(parts[0]) == id:
                data_atual = datetime.now().strftime('%d/%m/%Y')
                produto = f'{id},{data_atual},{new_name},{new_price}\n'
            arquivo.write(produto)

nome = "uhul"
editProduct(13,nome,10)
