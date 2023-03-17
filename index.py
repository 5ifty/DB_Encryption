from scripts.autoDelete import Delete 
from scripts.conversion import SpreadsheetConverter
from scripts.encryption import FileEncryption
from scripts.decryption import Decryption

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

    
if __name__ == '__main__':
    M = Main()
    M.master()