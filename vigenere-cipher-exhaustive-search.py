import collections
import string
from itertools import product


class VigenereCipherExhaustiveSearch():
    def __init__(self, plainText, cipherText, keyNo):
        self.plainText = plainText
        self.cipherText = cipherText
        self.keyNo = keyNo
        self.findKey(plainText, cipherText, keyNo)

    def constructKey(self, message, cipherKey):
        if not len(message) == len(cipherKey):
            for i in range(len(message)-len(cipherKey)):
                cipherKey += cipherKey[i%len(cipherKey)]
        return cipherKey


    def decrypt(self, message, cipherKey):
        decryptedText = ''
        cipherKey = self.constructKey(message, cipherKey)
        for i in range(len(message)):
            decryptedChar = chr((((ord(message[i]) - ord(cipherKey[i])) + 26) % 26) + ord('A'))
            decryptedText += decryptedChar
        return decryptedText

    def getFrequencyOfCipherChars(self, cipherText):
        return collections.Counter(cipherText)
    
    def findIndexOfCoincidence(self, cipherTextSlice):
        frequency = self.getFrequencyOfCipherChars(cipherTextSlice)
        fiSum = 0
        cipherTextSliceLength = len(cipherTextSlice)
        for char in frequency.keys():
            fiSum += frequency[char]*(frequency[char]-1)
        return 26 * (fiSum / (cipherTextSliceLength * (cipherTextSliceLength-1)))

    def findPeriod(self, cipherText):
        periodNotFound = True
        periods = []
        period = 0
        while periodNotFound:
            period += 1
            cipherSlice = ['']*period
            for i in range(len(cipherText)):
                cipherSlice[i%period] += cipherText[i]
            sum = 0
            for i in range(period):
                sum += self.findIndexOfCoincidence(cipherSlice[i])
            ioc = sum/period
            if ioc >=1.7:
                periods.append(period)
            if period == 3:
                periodNotFound = False
        return periods

    def findKeyOfPeriodLength(self, plainText, cipherText, period):
        combinations = [''.join(i) for i in product(string.ascii_uppercase, repeat = period)]
        for key in combinations:
            plaintextByKey = self.decrypt(cipherText,key)
            if plaintextByKey == plainText:
                return key, combinations[0:combinations.index(key)+1]
        return '', combinations
    
    def findKey(self, plainText, cipherText, keyNo):
        with open("cipherKeyVigenere" + str(keyNo) +".txt","w") as file:
            periods = self.findPeriod(cipherText)
            key = ''
            keys = []
            for period in periods:
                key, keys = self.findKeyOfPeriodLength(plainText, cipherText, period)
                file.write("*"*80 + "\n")
                file.write("The plain text is " + plainText + "\n")
                file.write("The plain text is " + cipherText + "\n")
                file.write("-"*80 + "\n")
                file.write("The period in consideration " + str(period) + "\n")
                file.write("The keys are "+ ",".join(keys) + "\n")
                file.write("The number of keys considered is " + str(len(keys)) + "\n")
                if key != '':
                    file.write("The key used for encryption is " + key + "\n")
                file.write("-"*80 + "\n")
                file.write("*"*80 + "\n")

n = int(input("Enter number of keys to be found : "))
keysToBeFoundList = []
for i in range(n):
    plainText = input("Enter plain text ")
    cipherText = input("Enter cipher text ")
    keysToBeFoundList.append([plainText, cipherText])
for i in range(len(keysToBeFoundList)):
    VigenereCipherExhaustiveSearch(keysToBeFoundList[i][0], keysToBeFoundList[i][1], i)
