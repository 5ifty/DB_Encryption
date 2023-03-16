import os
import json


'''
This script auto-deletes the unencrpyted Data to prevent data-leaks/Malicious individuals to read the data.
'''

class Delete():
    def __init__(self) -> None:
        pass

    def deleting(toDelete =  r'C:/Users/user/Documents/DB_Encryption/output/convertedData.json'):
        if os.path.exists(toDelete):
            os.remove(toDelete)
            print('Unencrypted Data Purged')
        else:
            print('This file does not exist')
        

if __name__ == '__main__':
    Delete()
    Delete.deleting()