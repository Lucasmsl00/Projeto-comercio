from mysql.connector import connect

def conexao():
    conBD = connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'comercio')
    return conBD