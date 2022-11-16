import os
import shutil

def parseAndGetAndroidManifest(directoryPath, outputPath):
    for directory in os.listdir(directoryPath):
        print(directory)
        if directory == '.DS_Store':
            continue
        inputFilePath = '/'+directory+'/AndroidManifest.xml'
        outputFileName = '/'+directory+'_AndroidManifest.xml'
        shutil.copyfile(directoryPath+inputFilePath, outputPath+outputFileName)
parseAndGetAndroidManifest('/Users/diyabiju/Documents/GitHub/software-security/Team28-CheckApkPermissions/extractedAPKs', '/Users/diyabiju/Documents/GitHub/software-security/Team28-CheckApkPermissions/extractedAndroidManifests')
