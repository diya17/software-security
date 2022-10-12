from typing import List
class VigenereCipher():
    def __init__(self):
        self.getOperation()
    
    
    def getMessageAndKey(self, mode: str) -> List[str]:
        message = input("Enter message to be "+ mode + " : ")
        while True:
            print("Enter the key for " + mode)
            cipherKey = input()
            if(not len(cipherKey)<=0 or not len(cipherKey)>3):
                if not len(message) == len(cipherKey):
                    for i in range(len(message)-len(cipherKey)):
                        cipherKey += cipherKey[i%len(cipherKey)]
                return [message, cipherKey]
    
    def encrypt(self):
        encryptedText = ''
        inputParams = self.getMessageAndKey('encrypted')
        message, cipherKey = inputParams[0], inputParams[1]
        for i in range(len(message)):
            cipherChar = chr(((ord(message[i]) + ord(cipherKey[i])) % 26) + ord('A'))
            encryptedText += cipherChar
        print(encryptedText)

    def decrypt(self):
        decryptedText = ''
        inputParams = self.getMessageAndKey('decryption')
        message, cipherKey = inputParams[0], inputParams[1]
        for i in range(len(message)):
            decryptedChar = chr((((ord(message[i]) - ord(cipherKey[i])) + 26) % 26) + ord('A'))
            decryptedText += decryptedChar
        print(decryptedText)


    global operationDict
    operationDict = {
        'encrypt': encrypt,
        'decrypt': decrypt
    }
    
    def getOperation(self):
        while True:
            operation = input("Enter \"encrypt\" or \"decrypt\" : ").lower()
            if operation == 'encrypt' or operation == 'decrypt':
                flag = False
                return operationDict[operation](self)

VigenereCipher()
