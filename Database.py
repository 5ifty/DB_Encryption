import mysql, mysql.connector

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
    
    def createTables(self):
        pyController = self.connection.cursor()
        pyController.execute("CREATE TABLE  First_Name")

if __name__ == '__main__':
    db = DB()
    db.databaseConnection()
    db.createTables()

# This should be useful for tomorrow - https://stackoverflow.com/questions/40450591/converting-json-to-sql-table