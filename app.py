from conexaoDB import conexao
from BD import *
from datetime import datetime


condb = conexao()

while True:
    mostrarTabelas(condb)
    opc = int(input("0. Sair\nEscolha a tabela que deseja fazer alterações: "))
    if opc == 0: break
    elif opc == 2:
        while True:
            opc = int(input('\n0 - Sair\n1 - Cadastrar um novo cliente\n2 - Atualizar cliente\n3 - Deletar cliente\n4. Listar cliente: '))
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
                print("\n==============LISTANDO CLIENTES==============\n")
                listarClientes(condb)

    elif opc == 11:
        while True:
            opc = int(input('\n0 - Sair\n1 - Cadastrar um novo produto\n2 - Atualizar produto\n3 - Deletar produto\n4. Listar produtos: '))
            if opc == 0: break
            elif opc == 1:
                nome = input("Digite o nome do produto: ")
                descricao = input("Digite a descrição do produto: ")
                preco = float(input("Digite o preço do produto: "))
                quantiEstoque = int(input("Digite a quantidade do produto no estoque: "))
                nome_cat = input("Digite a categoria do produto: ")
                descricao_cat = input("Digite a descrição da categoria do produto: ")
                cadastrarProduto(condb,nome,descricao,preco,quantiEstoque,nome_cat,descricao_cat)

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
                    print("\nOK!")
                    break

            elif opc == 4:
                listarProdutos(condb)

    elif opc == 12:
        while True:
            opc = int(input('\n0 - Sair\n1 - Cadastrar uma nova promoção\n2 - Atualizar promoção\n3 - Deletar promoção: '))
            if opc == 0: break

            elif opc == 1:
                nome = input("Digite o nome da promoção: ")
                descricao = input("Digite a descrição: ")
                dataini = input("Digite a data de inicio: ")
                dataini = datetime.strptime(dataini, "%d-%m-%Y").strftime("%Y-%m-%d")
                datafim = input("Digite a data do fim: ")
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
                    print("\nOK!")
                    break
# ajustes