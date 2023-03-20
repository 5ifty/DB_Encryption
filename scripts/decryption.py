from cryptography.fernet import Fernet
import json
import base64

class Decryption():
    def __init__(self) -> None:
        pass
    
    def Decrypt(self, toDecryptPath = r'C:\Users\user\Documents\DB_Encryption\output\encryptedData.json'):
        with open(r'C:\Users\user\Documents\DB_Encryption\output\encryptionKey.json') as trueEncryptionKey:
            for line in trueEncryptionKey:
                key = json.loads(line)['key']
                key = base64.b64decode(key)  # decode the base64-encoded key
                print(key)
        with open(toDecryptPath, 'rb') as toDecrypt:  # use 'rb' instead of 'w'
            encryptedData = toDecrypt.read()
            decryptThis = Fernet(key)
            decryptedData = decryptThis.decrypt(encryptedData)
            outputPath = r'C:\Users\user\Documents\DB_Encryption\output\decryptedData.json'
            with open(outputPath, 'wb') as decryptedJson:
                decryptedJson.write(decryptedData)
                print(f'Data Decrypted in {outputPath}')




if __name__ == '__main__':
    D = Decryption()
    D.Decrypt()