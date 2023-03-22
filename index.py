from scripts.autoDelete import Delete 
from scripts.conversion import SpreadsheetConverter
from scripts.encryption import FileEncryption
from scripts.decryption import Decryption
from Database import DB
import json

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
        print('You will be brought back here after every action, everything is autosaved so exit the CMD when you are ready too.')

        userInput = int(input('Please type in the corresponding number to the action you wish to complete\n'))
        if userInput == 1:
            userInput = input('Please enter the security Key to access this\n')
            if userInput != password:
                print('Incorrect Security Key, please try again\n')
                self.cmd()
            else:
                self.master()
                self.cmd()
        if userInput == 2:
            userInput = input('Please enter the security Key to access this\n')
            if userInput != password:
                print('Incorrect Security Key, please try again')
                self.cmd()
            else:
                with open(r'C:\Users\oem\Documents\DB_Encryption\output\encryptionKey.json', 'r') as encryptionKeyJson:
                    encryptionKey = json.load(encryptionKeyJson)
                    print(encryptionKey['key'])
                    self.cmd()
        if userInput == 3:
            userInput = input('Please enter the security Key to access this\n')
            if userInput != password:
                print('Incorrect Security Key, please try again\n')
                self.cmd()
            else:
                db = DB()
                name = input("Please enter the customer's first name:\n")
                dbQuery = db.queryDatabase(name)
                print(dbQuery)
                self.cmd()
        if userInput == 4:
            userInput = input('Please enter the security Key to access this\n')
            if userInput != password:
                print('Incorrect Security Key, please try again\n')
                self.cmd()
            else:
                with open(r'C:\Users\oem\Documents\DB_Encryption\output\decryptedData.json', 'r') as rawData:
                    iterateJson = json.load(rawData)
                    for first_name in iterateJson:
                        openDict = iterateJson[first_name]
                        firstName = openDict['first_name']
                        lastName = openDict['last_name']
                        company = openDict['Company']
                        email = openDict['email']
                        risk = openDict['Risk']
                        contact = openDict['contact']
                        status = openDict['Status']
                        print(firstName, lastName, company, email, risk, contact, status)
            
            self.cmd()
    

if __name__ == '__main__':
    M = Main()
    M.master()
    M.cmd()