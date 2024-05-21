import mysql.connector

def connect():
    conBD = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'comercio')
    return conBD