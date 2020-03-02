#RellFuzz Program for Assignmet 2 6135

#Read In JPG File
from array import array
import os
import subprocess


#modifying routine to modify the character array
def modify(orignalData):
    newData = array('B')
    newData = orignalData
    for i, byte in enumerate(orignalData):
        newData[i] = orignalData[i]
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


def main():
    #open the cross.jpg file
    crossJpg=openFile('cross.jpg')

    #write to a temp.jpg file with a character array that has been
    #modified from the original cross.jpg file
    writeFile('temp.jpg',modify(crossJpg))
    ret_code = subprocess.call("./jpg2bmp", shell=True)
    print(ret_code)


if __name__ == "__main__":
    main()
