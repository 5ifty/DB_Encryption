from cryptography.fernet import Fernet
import json

class Decryption():
    def __init__(self) -> None:
        pass
    def Decrypt(self, toDecryptPath = r'C:\Users\user\Documents\DB_Encryption\output\encryptedData.json'):
        with open(r'C:\Users\user\Documents\DB_Encryption\output\encryptionKey.json') as trueEncryptionKey:
            for line in trueEncryptionKey:
                key = json.loads(line)['key']
        with open(toDecryptPath, 'w') as toDecrypt:
            Fernet.decrypt(toDecryptPath, key)
        print(key)



if __name__ == '__main__':
    D = Decryption()
    D.Decrypt()