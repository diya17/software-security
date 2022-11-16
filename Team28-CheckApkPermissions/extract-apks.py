import os

def parseAndDecompileApks(filePath):
    apkTool = "/opt/homebrew/Cellar/apktool/2.6.1/libexec/apktool_2.6.1.jar"
    for fileName in os.listdir(filePath):
        curFilePath = os.path.join(filePath, fileName)
        if curFilePath.endswith('.apk'):
            os.system("java -jar " + apkTool + " d " + curFilePath)

parseAndDecompileApks('/Users/diyabiju/Documents/GitHub/software-security/Team28-CheckApkPermissions/selectedAPKs')
