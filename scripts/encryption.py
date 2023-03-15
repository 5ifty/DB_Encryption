from cryptography.fernet import Fernet

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
        with open(InputPath, 'rb') as convertedData:
            preEncrypedData = convertedData.read()

            encrypt = Fernet(encryptionKey)
            encryptionProcess = encrypt.encrypt(preEncrypedData)
        outputPath = r'C:/Users/user/Documents/DB_Encryption/output/encryptedData.json'
        with open(outputPath, 'wb') as encryptedJson:
            encryptedJson.write(encryptionProcess)


if __name__ == '__main__':
    FileEncryption()
    FileEncryption.encryptJson()