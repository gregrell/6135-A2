#RellFuzz Program for Assignmet 2 6135

#Read In JPG File
from array import array
import os
import sys
import subprocess
import random


#mod

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
    file1 = openFile(sys.argv[1])
    file2 = openFile(sys.argv[2])
    if file1 != file2:
        for byte in range(len(file1)):
            if file1[byte] != file2[byte]:
                print("Byte %s is not the same File 1 : %s  File 2 : %s" % (byte,file1[byte],file2[byte]))



if __name__ == "__main__":
    main()
