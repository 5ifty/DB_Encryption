from cryptography.fernet import Fernet
import os
import json
import base64

'''
This will be encrypting the json data for transfer to the database.
Using crpytography we generate a random key to decrypt once in the DB 
This ensures no unauthorised access to the data
'''

class FileEncryption():
    def __init__(self):
        pass

    def encryptionKey(self):
        # This encrpytionKey variable gives a random algortihm to encypt data into an unreadable format later on
        return Fernet.generate_key()
    
    def encryptJson(self, encryptionKey=None):
        InputPath = r'C:\Users\user\Documents\DB_Encryption\output\convertedData.json'
        if not os.path.exists(InputPath):
            with open(InputPath, 'w+') as noFile:
                pass
        else:
            with open(InputPath, 'rb') as convertedData:
                preEncrypedData = convertedData.read()
                encryptionKey = self.encryptionKey()
                print(f'Your encryption Key is, {encryptionKey}\nPlease keep this for reference')
                encryptThis = Fernet(encryptionKey)
                encryptionProcess = encryptThis.encrypt(preEncrypedData)
                outputPath = r'C:\Users\user\Documents\DB_Encryption\output\encryptedData.json'
                with open(outputPath, 'wb') as encryptedJson:
                    encryptedJson.write(encryptionProcess)
                    print(f'Data Encrypted in {outputPath}')
            # Parsing the Key into a .json file to keep from getting an invalid token error:
            with open(r'C:\Users\user\Documents\DB_Encryption\output\encryptionKey.json', 'w+') as encrpytionKeyOutput:
                toDump = {
                    'key': base64.b64encode(encryptionKey).decode()
                }
                encrpytionKeyOutput.write(json.dumps(toDump))

if __name__ == '__main__':
    FE = FileEncryption()
    FE.encryptJson()
