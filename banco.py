#criar banco de dados - enzo

import sqlite3 as lite

connection = lite.connect("dados.db")

#criando tabela base

with connection: #with irá abrir e fechar o banco de dados automaticamente
    cur = connection.cursor()
    cur.execute("CREATE TABLE produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco )")
    
    
    
# CAIO, LE AQ, piá seguinte, criei uma estrutura de pasta q da pra gente usar no projeto, esse banco.py estou usando pra poder montar o banco de dados e montar as queries/chamadas


#o view.py vc pode usar pra criar a interface, sabe usar git?

#vamos dividir em branchs, eu ensino, vai ter a branch principal (main), e a gente divide entre leo caio e enzo, sempre ANTES DE QUALQUER COMMIT VC DA O PULL, senão vc perde oq eu fiz, então por exemplo, to mexendo na minha branch e quero commitar, volte pra branch principal e da um pull pra atualizar, depois vc da merge na sua (mergeia/puxa suas mudanças para dentro da principal), isso evita a gente de criar arquivo separado e facilita nossa vida pra poder fazer testes tlgd, sabe fazer?

#nao nao nao nao nao nao nao nao nao 

#vai ter uma principal

# 3 outras, uma pra mim, outra pra tu e outra pro enzo

# vou te mostrar os passos a passos aq

#linux do caralho

#presta atenção, vou ensinar a criar branch (git checkout -b nome_da_branch)]

#vou dar um exemplo de commit q vc vai fazer


#to na minha branch (leo-branch)

#esses textos q estou escrevendo após o commit só vai ficar na minha branch

#agora vc vai fazer o seguinte: irá dar merge

#calma, n dei push na minha branch

#pra te mostrar a mudançca

#o push foi só na minha branch

#olhe no log a diferença


# pra resetar as mudanças 

#nnn, antes do commit, foi pq fiz um bgl errado

#eu buguei a porra do git calma


#AQUI CARAI

#ta faldno q vai dar conflito se eu salvar entendeu? isso previne a gente de cagar com tudo

#esse (git merge nome_da_branch) serve pra poder juntar a minha branch na original

