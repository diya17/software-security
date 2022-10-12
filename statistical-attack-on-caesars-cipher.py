from typing import Counter


class StatisticalAttackOnCaesarsCipher:
    global charFrequency
    charFrequency = {
        'A': 0.080,
        'B': 0.015,
        'C': 0.030,
        'D': 0.040,
        'E': 0.130,
        'F': 0.020,
        'G': 0.015,
        'H': 0.060,
        'I': 0.065,
        'J': 0.005,
        'K': 0.005,
        'L': 0.035,
        'M': 0.030,
        'N': 0.070,
        'O': 0.080,
        'P': 0.020,
        'Q': 0.002,
        'R': 0.065,
        'S': 0.060,
        'T': 0.090,
        'U': 0.030,
        'V': 0.010,
        'W': 0.015,
        'X': 0.005,
        'Y': 0.020,
        'Z': 0.002
    }
    def __init__(self, cipherText: str):
        self.cipherText = cipherText
        self.statisticalAttack(cipherText)
    
    def decrypt(self, cipherText: str, cipherKey: int) -> str:
        decryptedText = ''
        for char in cipherText:
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
        return decryptedText
    
    def statisticalAttack(self, cipherText):
        lengthOfString = len(cipherText)
        countOfCharInCipherText = Counter(cipherText)
        freqOfCipherChar = {}
        keyDecryptText = {}
        for i in range(lengthOfString):
            freqOfCipherChar[cipherText[i]] = countOfCharInCipherText[cipherText[i]]/lengthOfString
        for i in range(25):
            phiI = 0
            for char in cipherText:
                phiI += freqOfCipherChar[char]*charFrequency[list(charFrequency.keys())[((list(charFrequency.keys()).index(char.upper()))-i)]]
                keyDecryptText[i] = [phiI, self.decrypt(cipherText, i)]
        print("\n" + "-"*30)
        print(" \n The decrypted keys for " + cipherText + " are : \n")
        for i in range(25):
            print("Key: " + str(i))
            print("Decrypted Text: " +keyDecryptText[i][1])
            print("*"*30)

    
cipherTexts = []
n = int(input("Enter number of cipherTexts to attack: "))
print("\n Enter the cipher texts \n")
for i in range(n):
    cipher = input()
    cipherTexts.append(cipher)
for cipher in cipherTexts:
    StatisticalAttackOnCaesarsCipher(cipher)
