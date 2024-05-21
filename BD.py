def cadastrarProduto(condb,nome,descricao,preco):
    mycursor = condb.cursor()
    sql = "INSERT INTO produtos(Nome, Descricao, Preco) VALUES (%s,%s,%s);"
    valores = (nome,descricao,preco)
    mycursor.execute(sql,valores)
    condb.commit()
    print("Produto cadastrado com sucesso!!")
    mycursor.close()

def cadastrarCliente(condb, nome, sobrenome, endereco, cidade, codigopostal):
    mycursor = condb.cursor()
    sql = "INSERT INTO Clientes (Nome , Sobrenome, Endereco, Cidade, Codigopostal) VALUES (%s, %s, %s, %s, %s);"
    valores = (nome, sobrenome, endereco, cidade , codigopostal)
    mycursor.execute(sql,valores)
    condb.commit()
    print("Cliente cadastrado com sucesso!")
    mycursor.close()

def cadastrarFornecedor(condb, nome, contato, endereco):
    mycursor = condb.cursor()
    sql = "INSERT INTO Fornecedores (Nome, Contato, Endereco) VALUES (%s, %s, %s);"
    valores = (nome, contato, endereco)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Fornecedor cadastrado com sucesso!")
    mycursor.close()
    
def cadastrarFuncionarios(condb, nome, cargo, departamento):
    mycursor = condb.cursor()
    sql = "INSERT INTO Funcionarios (Nome, Cargo, Departamento) VALUES (%s, %s, %s);"
    valores = (nome, cargo, departamento)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Funcionário cadastrado com sucesso!")
    mycursor.close()

def atualizarProduto(condb,nome,descricao,preco,ID_produto):
    mycursor = condb.cursor()
    sql = "UPDATE produtos SET Nome = %s, Descricao = %s, Preco = %s WHERE ID_Produto = %s;"
    valores = (nome,descricao,preco,ID_produto)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Produto atualizado com sucesso!")
    mycursor.close()
    
def atualizarCliente(condb, nome, sobrenome, endereco, cidade, codigopostal, id_cliente):
    mycursor = condb.cursor()
    sql = "UPDATE clientes SET Nome = %s, Sobrenome = %s, Endereco = %s, Cidade = %s, Codigopostal = %s WHERE Id_Cliente = %s;"
    valores = (nome,sobrenome,endereco,cidade,codigopostal,id_cliente)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Cliente cadastrado com sucesso!!")
    mycursor.close()
    
def atualizarFornecedor(condb, nome, contato, endereco, id_fornecedor):
    mycursor = condb.cursor()
    sql = "UPDATE fornecedores SET Nome = %s, Contato = %s, Endereco = %s WHERE ID_Fornecedor = %s;"
    valores = (nome, contato, endereco, id_fornecedor)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Funcionário atualizado com sucesso!!")
    mycursor.close()
    
def deletarProduto(condb,id_produto):
    mycursor = condb.cursor()
    sql = "DELETE FROM produtos WHERE ID_Produto = %s;"
    valores = (id_produto,)
    mycursor.execute(sql,valores)
    condb.commit()
    print("Produto excluído do banco de dados com sucesso!")
    mycursor.close()

def mostrartabelas(condb):
    mycursor = condb.cursor()
    mycursor.execute("SHOW TABLES;")
    resultado = mycursor.fetchall()
    print('\n')
    for tabela in resultado:
        print(tabela[0])
    print('\n')
    mycursor.close()

def menu(condb):
    mycursor = condb.cursor()
    mycursor.execute("SHOW TABLES;")
    resultado = mycursor.fetchall()
    for index, tabela in enumerate(resultado):
        print(f'{index+1} => {tabela[0]}')
    mycursor.close()
    
def mostrarProdutos(condb):
    mycursor = condb.cursor()
    mycursor.execute("SELECT ID_Produto,Nome FROM produtos;")
    produtos = mycursor.fetchall()
    for produto in produtos:
        print(f"Id: {produto[0]} - Nome: {produto[1]}")    