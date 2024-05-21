from conexaoDB import connect
from BD import *

condb = connect()

while True:
    menu(condb)
    opc = int(input("Escolha a tabela que deseja fazer alterações: "))
    if opc == 0: 
        break
    if opc == 11:
        while True:
            opc = int(input('\n0 - Sair\n1 - Cadastrar um novo produto\n2 - Atualizar produto\n3 - Deletar produto: '))
            if opc == 0:
                break
            elif opc == 1:
                nome = input("Digite o nome do produto: ")
                descricao = input("Digite a descrição do produto: ")
                preco = float(input("Digite o preço do produto: "))
                cadastrarProduto(condb,nome,descricao,preco)
            elif opc == 2:
                print('\n')
                mostrarProdutos(condb)
                nome = input("Digite o nome do produto: ")
                descricao = input("Digite a descrição do produto: ")
                preco = float(input("Digite o preço do produto: "))
                id_produto = int(input("Digite o id do produto: "))
                atualizarProduto(condb,nome,descricao,preco,id_produto)
            elif opc == 3:
                mostrarProdutos(condb) 
                id_produto = int(input("Digite o id do produto que deseja deletar: "))
                deletarProduto(condb,id_produto)

# while True:
#     opc = int(input('0 - Sair, 1 - Cadastrar um novo produto, 2 - Listar tabelas, 3 - Atualizar produto, 4 - Deletar produto: '))
#     if opc == 0 :
#         break
#     elif opc == 1:
#         nome = input("Digite o nome do produto: ")
#         descricao = input("Digite a descrição do produto: ")
#         preco = float(input("Digite o preço do produto: "))
#         cadastrarProduto(condb,nome,descricao,preco)
#     elif opc == 2:
#         mostrartabelas(condb)
#     elif opc == 3:
#         nome = input("Digite o nome do produto: ")
#         descricao = input("Digite a descrição do produto: ")
#         preco = float(input("Digite o preço do produto: "))
#         id_produto = int(input("Digite o id do produto: "))
#         atualizarProduto(condb,nome,descricao,preco,id_produto)
#     elif opc == 4:
#         mostrarProdutosDeletar(condb) 
#         id_produto = int(input("Digite o id do produto que deseja deletar: "))
#         deletarProduto(condb,id_produto)


