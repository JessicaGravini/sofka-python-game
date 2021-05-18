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

    def insertarPodio(self, nombreJuego, jugador, puesto):
        self.cursor = self.connection.cursor()
        sql = f"INSERT INTO podio VALUES (0, '{nombreJuego}', '{puesto}', '{jugador}')"
        self.cursor.execute(sql)
        self.connection.commit()
