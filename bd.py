from app import solicitarNombreJugadores, solicitarNroJugadores
import pymysql
import mysql.connector

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='game'
        )

        self.cursor = self.connection.cursor()
    
        sql = "INSERT INTO game ("", VALUES (%s, %s)"
    
        self.cursor.execute(sql)


database = DataBase()





    





