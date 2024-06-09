from mysql.connector import Error

def cadastrarProduto(condb,nome,descricao,preco,quantEstoque, nome_cate, descricao_cate, nome_forn, contato_forn, endereco_forn,opc_cat, opc_forn):
    
    try: 
        mycursor = condb.cursor()
        sql = "INSERT INTO produtos(Nome, Descricao, Preco) VALUES (%s,%s,%s);"
        valores = (nome,descricao,preco)
        mycursor.execute(sql,valores)
        ID_Produto = mycursor.lastrowid
        sql1 = "INSERT INTO estoque (ID_Produto, Quantidade) VALUES (%s, %s);"
        val1 = (ID_Produto, quantEstoque)
        mycursor.execute(sql1, val1)

        if opc_cat == 'Y':
            sql4 = ('SELECT ID_Categoria FROM categoriasprodutos WHERE Nome = %s')
            val4 = (nome_cate,)
            mycursor.execute(sql4,val4)
            ID_categoria = mycursor.fetchone()[0]
            int(ID_categoria)
            sql3 = ("UPDATE produtos SET ID_Categoria = %s WHERE ID_Produto = %s")
            val3 = (ID_categoria, ID_Produto)
            mycursor.execute(sql3,val3)
          
        else:
            sql2 = "INSERT INTO categoriasprodutos (Nome, Descricao) VALUES (%s, %s);"
            val2 = (nome_cate, descricao_cate)
            mycursor.execute(sql2, val2)
            ID_categoria = mycursor.lastrowid
            sql8 = ("UPDATE produtos SET ID_Categoria = %s WHERE ID_Produto = %s;")
            val8 = (ID_categoria, ID_Produto)
            mycursor.execute(sql8,val8)
            print("Categoria cadastrada com sucesso!")

        if opc_forn == 'Y':
            sql5 = ("SELECT ID_Fornecedor FROM fornecedores WHERE Nome = %s")
            val5 = (nome_forn,)
            mycursor.execute(sql5, val5)
            ID_Fornecedor = mycursor.fetchone()[0]
            int(ID_Fornecedor)
            sql6 = ("UPDATE produtos SET ID_Fornecedor = %s WHERE ID_Produto = %s")
            val6 = (ID_Fornecedor, ID_Produto)
            mycursor.execute(sql6,val6)

        else:
            sql7 = "INSERT INTO Fornecedores (Nome, Contato, Endereco) VALUES (%s, %s, %s);"
            val7 = (nome_forn, contato_forn, endereco_forn)
            mycursor.execute(sql7, val7)
            ID_Fornecedor = mycursor.lastrowid
            sql9 = "UPDATE produtos SET ID_Fornecedor = %s WHERE ID_Produto = %s;"
            val9 = (ID_Fornecedor, ID_Produto)
            mycursor.execute(sql9,val9)
            print("Fornecedor cadastrado com sucesso!")

        condb.commit()
        print("Produto cadastrado com sucesso!")
        
    except Exception as e:
        condb.rollback()
        print(f"Erro ao cadastrar produto {e}")
    
    finally:
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

def atualizarFuncionario(condb, nome, cargo, departamento, id_funcionario):
    mycursor = condb.cursor()
    sql = "UPDATE funcionarios SET Nome = %s, Cargo = %s, Departamento = %s WHERE ID_Funcionario = %s;"
    valores = (nome, cargo, departamento, id_funcionario)
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

def deletarProduto(condb,nome_produto):
    try:
        produto_id = obterIdProduto(condb, nome_produto)
        if not produto_id:
            return
        
        condb.start_transaction()
        with condb.cursor() as cursor:
            sql_detalhe_pedido = "DELETE FROM detalhespedido WHERE ID_produto = %s"
            cursor.execute(sql_detalhe_pedido, (produto_id,))
        with condb.cursor() as cursor:
            sql_estoque = "DELETE FROM estoque WHERE ID_Produto = %s"
            cursor.execute(sql_estoque, (produto_id,))
        
        with condb.cursor() as cursor:
            sql_produto = "DELETE FROM produto WHERE ID_Produto = %s"
            cursor.execute(sql_produto, (produto_id,))

        condb.commit()
        print("Produto deletado com sucesso!")

    except Error as e:
        condb.rollback()
        print("Ocorreu um erro ao deletar o produto!")
        
    finally:
        condb.close()
        
def deletarPromocao(condb, nome):
    mycursor = condb.cursor()
    sql = ("DELETE FROM promocoes WHERE Nome = %s;")
    valores = (nome,)
    mycursor.execute(sql, valores)
    condb.commit()
    print("Promoção deletada com sucesso!")
    mycursor.close()

def deletarCliente(condb, nome):
    mycursor = condb.cursor()
    sql = "DELETE FROM clientes WHERE Nome = %s;"
    val = (nome,)
    mycursor.execute(sql,val)
    condb.commit()
    print("\nCliente deletado com sucesso!\n")
    mycursor.close()

def deletarFornecedor(condb, nome):
    mycursor = condb.cursor()
    sql = "DELETE FROM fornecedores WHERE Nome = %s;"
    val = (nome,)
    mycursor.execute(sql, val)
    condb.commit()
    print("Fornecedor deletado com sucesso!")
    mycursor.close()
    
def deletarFuncionario(condb, nome):
    mycursor = condb.cursor()
    sql = "DELETE FROM funcionarios WHERE Nome = %s"
    val = (nome,)
    mycursor.execute(sql, val)
    condb.commit()
    mycursor.close()
    
def mostrarProdutos(condb): 
    mycursor = condb.cursor()
    mycursor.execute("SELECT ID_Produto,Nome FROM produtos;")
    produtos = mycursor.fetchall()
    for produto in produtos:
        print(f"Id: {produto[0]} - Nome: {produto[1]}") 

def listarProdutos(condb):
    print("\n============================ LISTANDO PRODUTOS ============================\n")
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM produtos;")
    produtos = mycursor.fetchall()
    for produto in produtos:
        print(f"Nome: {produto[1]}, Descrição: {produto[2]}, Preço: {produto[3]}\n")

def listarClientes(condb):
    print("\n============================ LISTANDO CLIENTES ============================\n")
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM clientes;")
    clientes = mycursor.fetchall()
    for cliente in clientes:
        print(f"Nome: {cliente[1]}, Descrição: {cliente[2]}, Preço: {cliente[3]}")

def listarFornecedores(condb):
    print("\n============================ LISTANDO FORNECEDORES ============================\n")
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM fornecedores;")
    fornecedores = mycursor.fetchall()
    for fornecedor  in fornecedores:
        print(f'Nome: {fornecedor[1]}, Contato: {fornecedor[2]}, Endereço: {fornecedor[3]}')

def listarPromocoes(condb):
    print("\n============================ LISTANDO PROMOÇÕES ============================\n")
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM promocoes;")
    promocoes = mycursor.fetchall()
    for promocao in promocoes:
        print(f'Nome: {promocao[1]}, Descrição: {promocao[2]}, Data de início: {promocao[3]}, Data de fim: {promocao[4]}')

def listarFuncionarios(condb):
    mycursor = condb.cursor()
    sql = "SELECT Nome, Cargo, Departamento FROM funcionarios"
    mycursor.execute(sql)
    funcionarios = mycursor.fetchall()
    for funcionario in funcionarios:
        print(f'Nome: {funcionario[0]}, Cargo: {funcionario[1]}, Departamento: {funcionario[2]}')

def listarCatProdutos(condb):
    print("\n============================ LISTANDO CATEGORIAS DE PRODUTOS ============================\n")
    mycursor = condb.cursor()
    mycursor.execute("SELECT Nome, Descricao FROM categoriasprodutos")
    categoriasprodutos = mycursor.fetchall()
    for categoriaproduto in categoriasprodutos:
        print(f'Nome: {categoriaproduto[0]}, Descrição: {categoriaproduto[1]}')
        
def mostrarEstoque(condb): # SEM USO
    "\n============================ QUANTIDADES DOS PRODUTOS EM ESTOQUE ============================\n"
    mycursor = condb.cursor()
    mycursor.execute("SELECT produtos.Nome, estoque.Quantidade FROM produtos INNER JOIN estoque ON produtos.ID_Produto = estoque.ID_Produto;")
    quant_produtos = mycursor.fetchall()
    for quant_produto in quant_produtos:
        print(f'Produto: {quant_produto[0]}, Quantidade em estoque: {quant_produto[1]},')

def obterIdProduto(condb,nome):
    try:
        # with condb.cursor() as cursor:
        #     sql = ("SELECT ID_Produto FROM produtos WHERE Nome = %s")
        #     cursor.execute(sql, (nome,))
        #     resultado = cursor.fetchone()

        mycursor = condb.cursor()
        sql = "SELECT ID_Produto FROM produtos WHERE Nome = %s" 
        mycursor.execute(sql, (nome,))
        resultado = int(mycursor.fetchone()[0])
        if resultado:
            return resultado
        else:
            print(f"Produto com nome: {nome}, não encontrado!")
    
    except Error as e:
        print(f"Ocorreu um erro ao obter Id do produto: {e}")
        return None

    finally:
        # condb.close()
        print("OK")

def obterIdCliente(condb, nome):
    try:
        # with condb.cursor() as cursor:
        #sql = "SELECT ID_Cliente FROM clientes WHERE Nome = %s"
        #cursor.execute(sql, (nome,))
        #esultado = cursor.fetchone()[0]
        #int(resultado)

        mycursor = condb.cursor()
        sql = "SELECT ID_Cliente FROM clientes WHERE Nome = %s" 
        mycursor.execute(sql, (nome,))
        resultado = int(mycursor.fetchone()[0])
        if resultado:
            return resultado
        else:
            print(f"Cliente com nome: {nome}, não encontrado")

    except Error as e:
        print(f"Ocorreu um erro ao obter o id do cliente")
        return None

    finally:
        # condb.close()
        print()
    
    # sql = "SELECT ID_Cliente FROM clientes WHERE Nome = %s"
    # val = (nome,)
    # mycursor.execute(sql, val)
    # condb.commit()
    # id_cliente = int(mycursor.fetchone()[0])
    # print(type(id_cliente))
    # print(id_cliente)
    # mycursor.close()
    
def realizarPedido(condb,nome_produto, quantCompra_produto, nome_cli,sobrenome_cli, endereco_cli, cidade_cli, codigoPostal_cli, data_atual, opc_cli):
    try:
        

        id_produto = obterIdProduto(condb, nome_produto)
        print(id_produto)
        if not id_produto:
            return

        
        mycursor = condb.cursor()
        if opc_cli == 'Y':
            id_cliente = obterIdCliente(condb, nome_cli)
            print(id_cliente)
            if not id_cliente:
                return

            sql = "SELECT Preco FROM produtos WHERE ID_Produto = %s"
            val = (id_produto,)
            mycursor.execute(sql,val)
            preco_prod = float(mycursor.fetchone()[0])

            sql1 = "INSERT INTO pedidos (Data_Pedido, ID_Cliente, Total) VALUES (%s,%s,%s)"
            val1 = (data_atual, id_cliente, (preco_prod*quantCompra_produto))
            mycursor.execute(sql1, val1)

            

        elif opc_cli == 'N':
            cadastrarCliente(condb, nome_cli, sobrenome_cli, endereco_cli, cidade_cli, codigoPostal_cli)
            id_cliente = obterIdCliente(condb, nome_cli)
            print(id_cliente)
            sql = "SELECT Preco FROM produtos WHERE ID_Produto = %s"
            val = (id_produto,)
            mycursor.execute(sql,val)
            preco_prod = float(mycursor.fetchone()[0])
            preco_total = preco_prod * quantCompra_produto

            sql1 = "INSERT INTO pedidos (Data_Pedido, ID_Cliente, Total) VALUES (%s,%s,%s)"
            val1 = (data_atual, id_cliente, preco_total)
            mycursor.execute(sql1, val1)
            
        #DIMINUINDO QUANTIDADE DO ESTOQUE
        sql2 = "SELECT Quantidade FROM estoque WHERE ID_Produto = %s"
        mycursor.execute(sql2, (id_produto,))
        quant_produto = mycursor.fetchone()[0]
        print(quant_produto)
        nova_quantidade = quant_produto - quantCompra_produto

        sql3 = "UPDATE estoque SET Quantidade = %s WHERE ID_Produto = %s"
        mycursor.execute(sql3, (nova_quantidade, id_produto))

        condb.commit()
        print("PEDIDO REALIZADO COM SUCESSO!")

    except Error as e:
        # condb.rollback()
        print(f"Erro: {e}")
    
    except Exception as e:
        # condb.rollback()
        print(f"Erro: {e}")

    finally:
        # condb.close()
        print("OK!")