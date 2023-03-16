from cryptography.fernet import Fernet
import os

'''
This will be encrypting the json data for transfer to the database.
Using crpytography we generate a random key to decrypt once in the DB 
This ensures no unauthorised access to the data
'''

class FileEncryption():
    def __init__(self) -> None:
        pass

    def encryptJson():
        encryptionKey = Fernet.generate_key()
        # This encrpytionKey variable gives a random algortihm to encypt data into an unreadable format later on
        InputPath = r'C:/Users/user/Documents/DB_Encryption/output/convertedData.json'
        if os.path.exists(InputPath) == False:
            with open(InputPath, 'r+') as noFile:
                pass
        else:
            with open(InputPath, 'rb') as convertedData:
                preEncrypedData = convertedData.read()
                print(f'Your encryption Key is, {encryptionKey}\nPlease keep this for reference')
                encrypt = Fernet(encryptionKey)
                encryptionProcess = encrypt.encrypt(preEncrypedData)
        outputPath = r'C:/Users/user/Documents/DB_Encryption/output/encryptedData.json'
        with open(outputPath, 'wb') as encryptedJson:
            encryptedJson.write(encryptionProcess)
            print(f'Data Encrypted in {outputPath}')


if __name__ == '__main__':
    FileEncryption()
    FileEncryption.encryptJson()