#RellFuzz Program for Assignmet 2 6135

#Read In JPG File
from array import array
import os
import subprocess
import random


#modifying routine to modify the character array
def modify(orignalData):
    newData = array('B')
    newData = orignalData
    for i, byte in enumerate(orignalData):
        randInt = random.randint(0,10)
        newData[i] = orignalData[i]
        newData[i] = 1
    return newData

def openFile(name):
    with open(name, 'rb') as f:
        jpgData = array('B')
        filesize = os.path.getsize(name)
        jpgData.fromfile(f,filesize)
    return jpgData


def writeFile(name,data):
    with open(name, 'wb') as outFile:
        outFile.write(data)

def execute():
    ret_code = subprocess.call("./jpg2bmp temp.jpg temp.bmp", shell=True)
    return ret_code

def tryOneRandomByte(originalData):
    randomLocation = random.randint(0, len(originalData)-1)
    randomInteger = random.randint(0,255)
    originalData[randomLocation] = randomInteger
    writeFile('temp.jpg',originalData)
    retCode = execute()
    return retCode, originalData

def tryOneRandomZero(originalData):
    randomLocation = random.randint(0, len(originalData)-1)
    originalData[randomLocation] = 0
    writeFile('temp.jpg',originalData)
    retCode = execute()
    return retCode, originalData

def trySetValueAtLocation(originalData,location):
    value = random.randint(0,255)
    originalData[location] = value
    #originalData[location + 1] = value
    #originalData[location + 2] = value
    #originalData[location + 3] = value
    #originalData[location + 4] = value


    writeFile('temp.jpg',originalData)
    retCode = execute()
    return retCode, originalData

def tryMConsecutiveBytesToZero(originalData,M):
    randomLocation = random.randint(0, len(originalData)-M)
    #print("Random Location setting to zero %s with %s bytes set to zero "% (randomLocation,M))
    for byte in range(M):
        originalData[randomLocation + byte] = 0
    writeFile('temp.jpg',originalData)
    retCode = execute()
    return retCode, originalData


def tryMConsecutiveBytesToRandom(originalData,M):
    randomLocation = random.randint(0, len(originalData)-M)
    numBytesToChange = random.randint(0,M)
    #print("Random Location %s with %s bytes set "% (randomLocation,numBytesToChange))
    for byte in range(numBytesToChange):
        RandValue = random.randint(0, 255)
        originalData[randomLocation + byte] = RandValue
    writeFile('temp.jpg',originalData)
    retCode = execute()
    return retCode, originalData

def tryZeroInBound(originalData,M):
    randomLocation = random.randint(0, len(originalData)-M)
    print("Random Location setting to zero %s"% randomLocation)
    originalData[randomLocation] = 0
    writeFile('temp.jpg',originalData)
    retCode = execute()
    return retCode, originalData

def main():
    #open the cross.jpg file
    for attempt in range(10000):
        crossJpg = openFile('cross.jpg')
        #print("Attempt %s",attempt)
        returnCode, triggeringData = tryMConsecutiveBytesToRandom(crossJpg, 30)
        if returnCode != 0 and returnCode != 255:
            print("%s on attempt %s" % (returnCode, attempt))
            writeFile("Att_%s.jpg" % attempt, triggeringData)







if __name__ == "__main__":
    main()
