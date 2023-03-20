from scripts.autoDelete import Delete 
from scripts.conversion import SpreadsheetConverter
from scripts.encryption import FileEncryption
from scripts.decryption import Decryption
from Database import DB

'''
This is adding all of the components in ../scripts/ and processing each stage before we move towards the DB
'''

class Main():
    def __init__(self) -> None:
        pass

    def master(self):
        SSC = SpreadsheetConverter.converter(self)
        FE = FileEncryption()
        encryptionKey = FE.encryptionKey()
        FE.encryptJson(encryptionKey)
        Del = Delete.deleting()
        Decrypt = Decryption.Decrypt(self)
        Database = DB()
        Database.parseToDatabase()
    
    def cmd(self):
        password = 'root'
        print('Welcome to the Database upload tool, please select from the options below:\n')
        print('1: Repeat Upload process, this will upload everything to the database.')
        print('2: View Encryption Key')
        print('3. Query Database, this is based off the customers first name.')
        print('4.View Raw Data')

        userInput = int(input('Please type in the corresponding number to the action you wish to complete'))
        if userInput == 1:
            userInput = input('Please enter the security Key to access this')
            if userInput != password:
                print('Incorrect Security Key, please try again')
                Main.cmd()
            else:
                Main.master()
        if userInput == 2:
            userInput = input('Please enter the security Key to access this')
            if userInput != password:
                print('Incorrect Security Key, please try again')
                Main.cmd()
            else:
                with open(r'C:\Users\user\Documents\DB_Encryption\output\encryptionKey.json', 'r') as encryptionKey:
                    for key in encryptionKey:
                        print(key['key'])
        if userInput == 3:
            userInput = input('Please enter the security Key to access this')
            if userInput != password:
                print('Incorrect Security Key, please try again')
                Main.cmd()
            else:
                db = DB()
                name = input("Please enter the customer's first name:")
                dbQuery = db.queryDatabase(name)
                print(dbQuery)
        if userInput == 4:
            userInput = input('Please enter the security Key to access this')
            if userInput != password:
                print('Incorrect Security Key, please try again')
                Main.cmd()
            else:
                with open(r'C:\Users\user\Documents\DB_Encryption\output\CSVData.csv', 'r') as rawData:
                    print(rawData)
    

if __name__ == '__main__':
    M = Main()
    M.master()
    M.cmd()