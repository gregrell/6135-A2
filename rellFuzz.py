#RellFuzz Program for Assignmet 2 6135

#Read In JPG File
from array import array
import os
jpgData = array('B')

filesize = os.path.getsize('cross.jpg')





#modifying routine to modify the character array
def modify(orignalData):
    newData = array('B')
    newData = orignalData
    for i, byte in enumerate(orignalData):
        newData[i] = orignalData[i]
    return newData


#open the cross.jpg file
with open('cross.jpg', 'rb') as f:
    jpgData.fromfile(f,filesize)

#write to a temp.jpg file with a character array that has been
#modified from the original cross.jpg file
    with open('temp.jpg','wb') as outFile:
        outFile.write(modify(jpgData))

