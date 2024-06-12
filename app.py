from conexaoDB import conexao
from BD import *
from datetime import datetime, date


condb = conexao()

while True:
    opc = int(input("\vEscolha um das opções:\v\v0 => Sair\v1 => Cadastrar\v2 => Atualizar\v3 => Deletar\v4 => Listar\v5 => Realiza pedido: "))
    if opc == 0: break
    
    elif opc == 1:
        
        while True:
            opc_cadastrar = int(input("\vCADASTRAR\v\v0 => Sair\v1 => Cliente\v2 => Fornecedor\v3 => Produto\v4 => Funcionário\v5 => Promoções: "))
            if opc_cadastrar == 0: break
            
            elif opc_cadastrar == 1:
                nome = input("Digite o nome do cliente: ")
                sobrenome = input("Digite o sobrenome: ")
                endereco = input("Digite o endereço do cliente: ")
                cidade = input("Digite a sua cidade: ")
                codigopostal = input("Digite o código postal: ")
                cadastrarCliente(condb, nome, sobrenome, endereco, cidade, codigopostal)
                
            elif opc_cadastrar == 2:
                nome = input("Digite o nome do fornecedor: ")
                contato = input("Digite o contato do fornecedor: ")
                endereco = input("Digite o endereço: ")
                cadastrarFornecedor(condb, nome, contato, endereco)
            
            elif opc_cadastrar == 3:
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
                
            elif opc_cadastrar == 4:
                nome_fun = input("Digite o nome do funcionário: ")
                cargo_fun = input("O cargo do funcionário: ")
                departamento_fun = input("Digite o departamento do funcionário: ")
                cadastrarFuncionarios(condb, nome_fun, cargo_fun, departamento_fun)
                
            elif opc_cadastrar == 5:
                nome = input("Digite o nome da promoção: ")
                descricao = input("Digite a descrição: ")
                dataini = input("Digite a data de inicio DD-MM-YYYY: ")
                dataini = datetime.strptime(dataini, "%d-%m-%Y").strftime("%Y-%m-%d")
                datafim = input("Digite a data do fim DD-MM-YYYY: ")
                datafim = datetime.strptime(datafim, "%d-%m-%Y").strftime("%Y-%m-%d")
                cadastrarPromocoes(condb, nome, descricao, dataini, datafim)
    elif opc == 2:
        while True:
            opc_atualizar = int(input("\vAtualizar\v\v0 => Sair\v1 => Cliente\v2 => Fornecedor\v3 => Produto\v4 => Funcionários\v5 => Promoção: "))
            
            if opc_atualizar == 0: break
            
            elif opc_atualizar == 1:
                nome = input("Digite o nome do cliente: ")
                sobrenome = input("Digite o sobrenome: ")
                endereco = input("Digite o endereço do cliente: ")
                cidade = input("Digite a sua cidade: ")
                codigopostal = input("Digite o código postal: ")
                id_cliente = int(input("Digite o id do cliente que deseja atualizar: "))
                atualizarCliente(condb, nome, sobrenome, endereco, cidade, codigopostal, id_cliente)
            
            elif opc_atualizar == 2:
                nome = input("Digite o nome do fornecedor: ")
                contato = input("Digite o contato do fornecedor: ")
                endereco = input("Digite o endereço: ")
                id_fornecedor = int(input("Digite o id do fornecedor que deseja alterar as informações: "))
                atualizarFornecedor(condb, nome, contato, endereco, id_fornecedor)
                
            elif opc_atualizar == 3:
                print('\n')
                mostrarProdutos(condb)
                nome = input("Digite o nome do produto: ")
                descricao = input("Digite a descrição do produto: ")
                preco = float(input("Digite o preço do produto: "))
                id_produto = int(input("Digite o id do produto: "))
                atualizarProduto(condb,nome,descricao,preco,id_produto)
                
            elif opc_atualizar == 4:
                nome_fun = input("Digite o nome do funcionário: ")
                cargo_fun = input("O cargo do funcionário: ")
                departamento_fun = input("Digite o departamento do funcionário: ")
                id_fun = int(input("Digite o id do funcionário que deseja atualizar: "))
                atualizarFuncionario(condb, nome_fun, cargo_fun, departamento_fun, id_fun)
                
            elif opc_atualizar == 5:
                nome = input("Digite o nome da promoção: ")
                descricao = input("Digite a descrição: ")
                dataini = input("Digite a data de inicio DD-MM-YYYY: ")
                dataini = datetime.strptime(dataini, "%d-%m-%Y").strftime("%Y-%m-%d")
                datafim = input("Digite a data do fim DD-MM-YYYY: ")
                datafim = datetime.strptime(datafim, "%d-%m-%Y").strftime("%Y-%m-%d")
                id_promocao = int(input("Digite o id da promoção: "))
                atualizarPromocao(condb, nome, descricao,dataini, datafim,id_promocao)
                
    elif opc == 3:
        while True:
            
            opc_alterar = int(input("\vDELETAR\v\v0 => Sair\v1 => Cliente\v2 => Fornecedor\v3 => Produto\v4 => Funcionários\v5 => Promoção: "))
            
            if opc_alterar == 0: break
            
            elif opc_alterar == 1:
                nome = input("Digite o nome do cliente que deseja deletar: ")
                opc = input("Deseja realmente deletar esse cliente? Y/N ").capitalize()
                if opc == "Y":
                    deletarCliente(condb, nome)
                else:
                    print("Ação cancelada!!")
                    break
                
            elif opc_alterar == 2:
                nome = input("Digite o nome do fornecedor que deseja excluir: ")
                opc = input("Tem certeza que deseja EXCLUIR esse fornecedor: Y/N ").capitalize()
                if opc == "Y":
                    deletarFornecedor(condb, nome)
                else: 
                    print("Ação cancelada!!")
                    break
                
            elif opc_alterar == 3:
                nome = input("Digite o nome do produto que deseja deletar: ")
                opc = input("Deseja realmentte excluir esse produto Y/N? ").capitalize()
                if opc == 'Y':
                    deletarProduto(condb,nome)
                else:
                    print("Ação cancelada!!")
                    break
                
            elif opc_alterar == 4:
                try: 
                    nome = input("Digite o nome do funcionário que deseja deletar: ")
                    opc = input("Deseja realmente deletar esse funcionário: ")
                    if opc == "Y":
                        deletarFuncionario(condb, nome)
                    else:
                        print("Ação cancelada com sucesso!")
                        break
                except Exception as e:
                    print("Digite 'Y' ou 'N': ")
                
                finally:
                    if opc == 'Y':
                        print("\vFuncionário deletado com sucesso! ")
                
            
            elif opc_alterar == 5:
                nome = input("Digite o nome da promoção que deseja excluir: ")
                opc = input("Deseja realmentte excluir esse produto Y/N? ").capitalize()
                if opc == 'Y':
                    deletarPromocao(condb,nome)
                else:
                    print("Ação cancelada!!")
                    break
    elif opc == 4:
        while True:
            
            opc_listar = int(input("\vLISTAR\v\v0 => Sair\v1 => Cliente\v2 => Fornecedor\v3 => Produto\v4 => Funcionários\v5 => Promoção: "))
            
            if opc_listar == 0: break

            elif opc_listar == 1:
                listarClientes(condb)
                
            elif opc_listar == 2:
                listarFornecedores(condb)
                
            elif opc_listar == 3:
                listarProdutos(condb)
                
            elif opc_listar == 4:
                listarFuncionarios(condb)
                
            elif opc_listar == 5:
                listarPromocoes(condb)
                
    elif opc == 5:
        
        while True:
            opc = int(input("\vREALIZANDO PEDIDO\v0 => Sair\v1 => Realizar um pedido: "))
            if opc == 0:
                break
            elif opc == 1:
                opc_cli = input("O Cliente já tem cadastro na loja? Y/N ").capitalize()
                if opc_cli == 'Y':
                    nome_cli = input("Digite o nome do cliente: ")
                    sobrenome_cli = input("Digite o sobrenome do cliente: ")
                    endereco_cli = ''
                    cidade_cli = ''
                    codigoPostal_cli = ''
                    
                elif opc_cli == 'N':
                    print("=================== CADASTRANDO NOVO CLIENTE ===================")
                    nome_cli= input("Digite o nome do cliente: ")    
                    sobrenome_cli = input("Digite o sobrenome do cliente: ")
                    endereco_cli = input("Digite o endereço: ")
                    cidade_cli = input("Digite o nome da cidade: ")
                    codigoPostal_cli = input("Digite o codigo postal: ")

                data_atual = date.today()
                nome_produto = input("Digite o nome do produto que cliente deseja comprar: ")
                quantCompra_produto = int(input("Informe quantas unidades o cliente vai comprar: "))
                forma_de_pagamento = input("Informe a forma de pagamento: \v1 - Cartão de Crédito\v2 - Boleto Bancário\v3 - Cartão de Débito\v4 - Pix: ")
                if forma_de_pagamento == '1':
                    forma_de_pagamento = 'Cartão de Crédito'
                elif forma_de_pagamento == '2':
                    forma_de_pagamento = 'Boleto Bancário'
                elif forma_de_pagamento == '3':
                    forma_de_pagamento = 'Cartão de Débito'
                elif forma_de_pagamento == '4':
                    forma_de_pagamento = 'Pix'
                             
                realizarPedido(condb, nome_produto, quantCompra_produto, nome_cli, sobrenome_cli, endereco_cli, cidade_cli, codigoPostal_cli, data_atual, opc_cli, forma_de_pagamento)
                        
        