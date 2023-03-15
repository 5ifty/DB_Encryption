import mysql, mysql.connector

class DB():
    def __init__(self) -> None:
        pass

    def databaseConnection(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'collegedatabase'
        )
        if self.connection.is_connected():
            print('Connected!')
        else:
            print(':(')
    
    def createTables(self):
        pyController = self.connection.cursor()
        pyController.execute("CREATE TABLE  First_Name")

if __name__ == '__main__':
    db = DB()
    db.databaseConnection()
    db.createTables()