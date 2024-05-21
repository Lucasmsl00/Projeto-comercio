def cadastrarProduto(condb,nome,descricao,preco, quantEstoque, nome_cate, descricao_cate):
    mycursor = condb.cursor()
    sql = "INSERT INTO produtos(Nome, Descricao, Preco) VALUES (%s,%s,%s);"
    valores = (nome,descricao,preco)
    mycursor.execute(sql,valores)
    ID_Produto = mycursor.lastrowid
    sql1 = "INSERT INTO estoque (ID_Produto, Quantidade) VALUES (%s, %s);"
    val1 = (ID_Produto, quantEstoque)
    mycursor.execute(sql1, val1)
    sql2 = "INSERT INTO categoriasprodutos (ID_Categoria, Nome, Descricao) VALUES (%s, %s, %s);"
    val2 = (ID_Produto, nome_cate, descricao_cate)
    mycursor.execute(sql2, val2)
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

def cadastrarPromocoes(condb, nome, descricao, datainicio, datafim):
    mycursor = condb.cursor()
    sql = "INSERT INTO promocoes (Nome, Descricao, DataInicio, DataFim) VALUES (%s, %s, %s, %s);"
    valores = (nome, descricao, datainicio, datafim)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Promoção cadastrada com sucesso!")
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
    sql = "UPDATE clientes SET Nome = %s, Sobrenome = %s, Endereco = %s, Cidade = %s, Codigopostal = %s WHERE ID_Cliente = %s;"
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

def atualizarFuncionario(condb, nome, cargo, departamento):
    mycursor = condb.cursor()
    sql = "UPDATE funcionarios SET Nome = %s, Cargo = %s, Departamento = %s WHERE ID_Funcionario = %s;"
    valores = (nome, cargo, departamento)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Funcionário atualizado com sucesso!")
    mycursor.close()

def atualizarPromocao(condb, nome, descricao, datainicio, datafim, id_promocao):
    mycursor = condb.cursor()
    sql = "UPDATE promocoes SET Nome = %s, Descricao = %s, DataInicio = %s, DataFim = %s WHERE ID_Promocao = %s;"
    valores = (nome, descricao, datainicio, datafim, id_promocao)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Promoção atualizada com sucesso!")
    mycursor.close()

def deletarProduto(condb,nome):
    mycursor = condb.cursor()
    sql = "DELETE FROM produtos WHERE Nome = %s;"
    valores = (nome,)
    mycursor.execute(sql,valores)
    condb.commit()
    print("Produto excluído do banco de dados com sucesso!")
    mycursor.close()

def deletarPromocao(condb, nome):
    mycursor = condb.cursor()
    sql = ("DELETE FROM promocoes WHERE Nome = %s;")
    valores = (nome,)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Promoção deletada com sucesso!")
    mycursor.close()

def mostrartabelas(condb):
    mycursor = condb.cursor()
    mycursor.execute("SHOW Clientes, Produtos, Funcionarios, Fornecedores, Promocoes TABLES;")
    resultado = mycursor.fetchall()
    print('\n')
    for tabela in resultado:
        print(tabela[0])
    print('\n')
    mycursor.close()

def mostrarTabelas(condb):
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

def listarProdutos(condb):
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM produtos;")
    produtos = mycursor.fetchall()
    for produto in produtos:
        print(f"Id: {produto[0]} - Nome: {produto[1]} - Descrição: {produto[2]} - Preço: {produto[3]}")

def listarClientes(condb):
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM clientes;")
    clientes = mycursor.fetchall()
    for cliente in clientes:
        print(f"Id: {produto[0]} - Nome: {produto[1]} - Descrição: {produto[2]} - Preço: {produto[3]}")