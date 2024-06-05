from conexaoDB import conexao
from BD import *
from datetime import datetime, date


condb = conexao()

while True:
    mostrarTabelas(condb)
    opc = int(input("0. Sair\nEscolha a tabela que deseja fazer alterações: "))
    if opc == 0: break
    elif opc == 2:
        while True:
            opc = int(input('\n0 - Sair\n1 - Cadastrar um novo cliente\n2 - Atualizar cliente\n3 - Deletar cliente\n4 - Listar cliente: '))
            if opc == 0: break
            
            elif opc == 1:
                nome = input("Digite o nome do cliente: ")
                sobrenome = input("Digite o sobrenome: ")
                endereco = input("Digite o endereço do cliente: ")
                cidade = input("Digite a sua cidade: ")
                codigopostal = input("Digite o código postal: ")
                cadastrarCliente(condb, nome, sobrenome, endereco, cidade, codigopostal)
            
            elif opc == 2:
                nome = input("Digite o nome do cliente: ")
                sobrenome = input("Digite o sobrenome: ")
                endereco = input("Digite o endereço do cliente: ")
                cidade = input("Digite a sua cidade: ")
                codigopostal = input("Digite o código postal: ")
                id_cliente = int(input("Digite o id do cliente que deseja atualizar: "))
                atualizarCliente(condb, nome, sobrenome, endereco, cidade, codigopostal, id_cliente)
            
            elif opc == 3:
                nome = input("Digite o nome do cliente que deseja deletar: ")
                opc = input("Deseja realmente deletar esse cliente? Y/N").capitalize()
                if opc == "Y":
                    deletarCliente(condb, nome)
                else:
                    print("Ação cancelada!!")
                    break
                
            elif opc == 4:
                listarClientes(condb)
    elif opc == 5:
        mostrarEstoque(condb)
        
    elif opc == 6:
        while True:
            opc = int(input('\n0 - Sair\n1 - Cadastrar um novo fornecedor\n2 - Atualizar fornecedor\n3 - Deletar fornecedor\n4 - Listar fornecedores: '))
            if opc == 0: break
            elif opc == 1:
                nome = input("Digite o nome do fornecedor: ")
                contato = input("Digite o contato do fornecedor: ")
                endereco = input("Digite o endereço: ")
                cadastrarFornecedor(condb, nome, contato, endereco)

            elif opc == 2:
                nome = input("Digite o nome do fornecedor: ")
                contato = input("Digite o contato do fornecedor: ")
                endereco = input("Digite o endereço: ")
                id_fornecedor = int(input("Digite o id do fornecedor que deseja alterar as informações: "))
                atualizarFornecedor(condb, nome, contato, endereco, id_fornecedor)

            elif opc == 3:
                nome = input("Digite o nome do fornecedor que deseja excluir: ")
                opc = input("Tem certeza que deseja EXCLUIR esse fornecedor: Y/N ").capitalize()
                if opc == "Y":
                    deletarFornecedor(condb, nome)
                else: 
                    print("Ação cancelada!!")
                    break

            elif opc == 4:
                listarFornecedores(condb)

    elif opc == 9:
        while True:
            opc = int(input("0 - Sair e 1 - Realizar um pedido: "))
            if opc == 0:
                break
            elif opc == 1:
                opc_cli = input("O Cliente já tem cadastro na loja? Y/N ").capitalize()
                if opc_cli == 'Y':
                    nome_cli = input("Digite o nome do cliente: ")
                    sobrenome_cli = ''
                    endereco_cli = ''
                    cidade_cli = ''
                    codigoPostal_cli = ''
                    
                elif opc_cli == 'N':
                    print("=================== CRIANDO NOVO CLIENTE ===================")
                    nome_cli= input("Digite o nome do cliente: ")    
                    sobrenome_cli = input("Digite o sobrenome do cliente: ")
                    endereco_cli = input("Digite o endereço: ")
                    cidade_cli = input("Digite o nome da cidade: ")
                    codigoPostal_cli = input("Digite o codigo postal: ")

                data_atual = date.today()
                nome_produto = input("Digite o nome do produto que cliente deseja comprar: ")
                quantCompra_produto = int(input("Informe quantas unidades o cliente vai comprar: "))

                realizarPedido(condb, nome_produto, quantCompra_produto, nome_cli, sobrenome_cli, endereco_cli, cidade_cli, codigoPostal_cli, data_atual, opc_cli)



                
    elif opc == 11:
        while True:
            opc = int(input('\n0 - Sair\n1 - Cadastrar um novo produto\n2 - Atualizar produto\n3 - Deletar produto\n4 - Listar produtos: '))
            if opc == 0: break
            elif opc == 1:
                nome = input("Digite o nome do produto: ")
                descricao = input("Digite a descrição do produto: ")
                preco = float(input("Digite o preço do produto: "))
                quantiEstoque = int(input("Digite a quantidade do produto no estoque: "))
                
                listarCatProdutos(condb)
                opc_cat = input("A categoria do produto já existe? Y/N ").capitalize()

                if opc_cat == 'Y':
                    nome_categoria = input("Digite o nome da categoria que o produto pertence: ")
                    desc_categoria = ''
                else:
                    nome_categoria = input("Digite o nome da nova categoria: ")
                    desc_categoria = input("Digite a descrição da categoria: ")
                
                listarFornecedores(condb) 
                opc_forn = input("O produto é fornecido por um fornecedor existente? Y/N ").capitalize()
                if opc_forn == "Y":
                    nome_forn = input("Digite o nome do fornecedor: ")
                    contato_forn = ''
                    endereco_forn = ''

                else:
                    nome_forn = input("Digite o nome do fornecedor: ")
                    contato_forn =  input("Digite o contato do fornecedor: ")
                    endereco_forn =  input("Digite o endereço do fornecedor: ")
                cadastrarProduto(condb, nome, descricao, preco, quantiEstoque, nome_categoria, desc_categoria, nome_forn, contato_forn, endereco_forn, opc_cat, opc_forn)

            elif opc == 2:
                print('\n')
                mostrarProdutos(condb)
                nome = input("Digite o nome do produto: ")
                descricao = input("Digite a descrição do produto: ")
                preco = float(input("Digite o preço do produto: "))
                id_produto = int(input("Digite o id do produto: "))
                atualizarProduto(condb,nome,descricao,preco,id_produto)

            elif opc == 3: 
                nome = input("Digite o nome do produto que deseja deletar: ")
                opc = input("Deseja realmentte excluir esse produto Y/N? ").capitalize()
                if opc == 'Y':
                    deletarProduto(condb,nome)
                else:
                    print("Ação cancelada!!")
                    break

            elif opc == 4:
                listarProdutos(condb)

    elif opc == 12:
        while True:
            opc = int(input('\n0 - Sair\n1 - Cadastrar uma nova promoção\n2 - Atualizar promoção\n3 - Deletar promoção\n4 - Listar promoções: '))
            if opc == 0: break

            elif opc == 1:
                nome = input("Digite o nome da promoção: ")
                descricao = input("Digite a descrição: ")
                dataini = input("Digite a data de inicio DD-MM-YYYY: ")
                dataini = datetime.strptime(dataini, "%d-%m-%Y").strftime("%Y-%m-%d")
                datafim = input("Digite a data do fim DD-MM-YYYY: ")
                datafim = datetime.strptime(datafim, "%d-%m-%Y").strftime("%Y-%m-%d")
                cadastrarPromocoes(condb, nome, descricao, dataini, datafim)

            elif opc == 2:
                nome = input("Digite o nome da promoção: ")
                descricao = input("Digite a descrição: ")
                dataini = input("Digite a data de inicio DD-MM-YYYY: ")
                dataini = datetime.strptime(dataini, "%d-%m-%Y").strftime("%Y-%m-%d")
                datafim = input("Digite a data do fim DD-MM-YYYY: ")
                datafim = datetime.strptime(datafim, "%d-%m-%Y").strftime("%Y-%m-%d")
                id_promocao = int(input("Digite o id da promoção: "))
                atualizarPromocao(condb, nome, descricao,dataini, datafim,id_promocao)

            elif opc == 3:
                nome = input("Digite o nome da promoção que deseja excluir: ")
                opc = input("Deseja realmentte excluir esse produto Y/N? ").capitalize()
                if opc == 'Y':
                    deletarPromocao(condb,nome)
                else:
                    print("Ação cancelada!!")
                    break

            elif opc == 4:
                listarPromocoes(condb)
