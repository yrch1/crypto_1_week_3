__author__ = 'yrch1'

import os
from Crypto.Hash import SHA256

check_video_h0 = '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8'
expected_h0 = '5b96aece304a1422224f9a41b228416028f9ba26b0d1058f400200f06a589949'
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
    if n == blockCount -1:
        ##Lasblock
        fileobject.seek(-lastBlockSize, os.SEEK_END) # move the cursor to the end of the file
        data = fileobject.read()
    else:
        ## FullBlock
        fileobject.seek(n*blockSize, os.SEEK_SET) # move the cursor to the end of the file
        data = fileobject.read(blockSize)


    fileobject.seek(originalPosition, os.SEEK_SET) # move the cursor to originalPosition
    return data


def readFile(filename):

    h = SHA256.new()
    with open(filename, "rb") as fileObject:
        fileSize = getSize(fileObject)
        blockCount = getBlocksCount(fileSize)
        lastBlockSize = getSizeLastChunk(fileSize)

        hn = ''
        for n in range(blockCount-1,-1,-1):
            blockData = getNBlock(fileObject, n,blockCount,lastBlockSize)
            sha = SHA256.new()
            sha.update(blockData)
            if(hn):
                sha.update(hn)
            hn = sha.digest()
    return hn





if __name__ == "__main__":

    print __author__

    mac = readFile("./resources/6 - 1 - Introduction (11 min).mp4")
    print mac.encode('hex')
    print expected_h0


