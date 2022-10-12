from typing import List
class CaesarsCipher:
    def __init__(self):
        self.getOperation()

    def getMessageAndKey(self, mode: str) -> List[str]:
        message = input("Enter message to be "+ mode + " : ")
        flag = True
        while flag:
            cipherKey = input("Enter the cipher key : ")
            if int(cipherKey) >=1 and int(cipherKey) <= 26:
                flag = False
                return [message, int(cipherKey)]
    
      
    def encrypt(self):
        encryptedText = ''
        inputParams = self.getMessageAndKey('encrypted')
        message, cipherKey = inputParams[0], inputParams[1]
        for char in message:
            if char.isalpha():
                shift = ord(char)+cipherKey
                if char.isupper():
                    if shift > 90:
                        shift -= 26
                    elif shift < 65:
                        shift += 26
                elif char.islower():
                    if shift > 122:
                        shift -= 26
                    elif shift < 97:
                        shift +=26
                encryptedText += chr(shift)
            else:
                encryptedText += char
        print(encryptedText)
    
    def decrypt(self):
        decryptedText = ''
        inputParams = self.getMessageAndKey('decrypted')
        message, cipherKey = inputParams[0], inputParams[1]
        for char in message:
            if char.isalpha():
                shift = ord(char)-cipherKey
                if char.isupper():
                    if shift > 90:
                        shift -= 26
                    elif shift < 65:
                        shift += 26
                elif char.islower():
                    if shift > 122:
                        shift -= 26
                    elif shift < 97:
                        shift +=26
                decryptedText += chr(shift)
            else:
                decryptedText += char
        print(decryptedText)
    
    global operationDict
    operationDict = {
        'encrypt': encrypt,
        'decrypt': decrypt
    }
    
    def getOperation(self):
        flag = True
        while flag:
            operation = input("Enter \"encrypt\" or \"decrypt\" : ").lower()
            if operation == 'encrypt' or operation == 'decrypt':
                flag = False
                return operationDict[operation](self)
CaesarsCipher()
