from scripts.autoDelete import Delete 
from scripts.conversion import SpreadsheetConverter
from scripts.encryption import FileEncryption


'''
This is adding all of the components in ../scripts/ and processing each stage before we move towards the DB
'''

class Main():
    def __init__(self) -> None:
        pass

    def master():
        SpreadsheetConverter.converter()
        FileEncryption.encryptJson()
        Delete.deleting()

if __name__ == '__main__':
    Main()
    Main.master()
    SpreadsheetConverter()
    FileEncryption()
    Delete()