import mysql, mysql.connector
import json
from scripts.decryption import Decryption

class DB():
    def __init__(self) -> None:
        pass

    def databaseConnection(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'BD9vyfrx',
            database = 'collegedatabase'
        )
        if self.connection.is_connected():
            print('Connected!')
        else:
            print(':(')
    
    # For the sake of time consumption in this project- I have manually added in the tables to the database- all this loop is doing is getting the decrypted data
    # Then parsing it into the predefined Tables in the DB. This should do this simultaniously.
    def parseToDatabase(self):
        decryptEncryptedFile = (
            Decryption()
            
        )

if __name__ == '__main__':
    db = DB()
    db.databaseConnection()
    db.createTables()


# This should be useful for tomorrow - https://stackoverflow.com/questions/40450591/converting-json-to-sql-table