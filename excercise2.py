__author__ = 'yrch1'

import os
import pycrypto

expected_h0 = '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8'
blockSize = 1024


def getSize(fileobject):
    originalPosition = fileobject.tell()
    fileobject.seek(0, 2) # move the cursor to the end of the file
    size = fileobject.tell()
    fileobject.seek(originalPosition, os.SEEK_SET) # move the cursor to originalPosition
    return size

def getSizeLastChunk(filesize):
    return filesize - blockSize * (filesize / blockSize)


def getBlocksCount(fileSize):
    blocksCount = fileSize/blockSize
    if getSizeLastChunk(fileSize) !=0:
        blocksCount += 1
    return blocksCount


def getNBlock(fileobject, n, blockCount, lastBlockSize):

    originalPosition = fileobject.tell()
    if n < blockCount - 1:
        ## FullBlock
        fileobject.seek(n*blockSize, os.SEEK_SET) # move the cursor to the end of the file
        data = fileobject.read(blockSize)
    else:
        ##Lasblock
        fileobject.seek(-lastBlockSize, os.SEEK_END) # move the cursor to the end of the file
        data = fileobject.read()

    fileobject.seek(originalPosition, os.SEEK_SET) # move the cursor to originalPosition
    return data


def readFile(filename):
    with open(filename, "rb") as fileobject:
        fileSize = getSize(fileobject)
        blockCount = getBlocksCount(fileSize)
        lastBlockSize = getSizeLastChunk(fileSize)

        for i in range(blockCount,0,-1):
            print i


    return





if __name__ == "__main__":

    print __author__
    readFile("./resources/6 - 2 - Generic birthday attack (16 min).mp4")


