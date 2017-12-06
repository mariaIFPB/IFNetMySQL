import mysql.connector
from database.configDB import config

class Usuario():
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
                            
    def  __str__ (self):
        retorno  " Usuario %s"  % (self.nome)

    def  __repr__ (self):
        retornar a  si mesmo . __str__ ()
