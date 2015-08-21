__author__ = 'yrch1'

import excercise2
import unittest

class TestStringMethods(unittest.TestCase):

    def test_readFile(self):
        self.assertEquals(excercise2.readFile("./resources/6 - 2 - Generic birthday attack (16 min).mp4").encode("hex"),"03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8")


    def test_getBlocksCount(self):
        self.assertEqual(excercise2.getBlocksCount(16927313), 16531)

    def test_getSizeLastChunk(self):
        self.assertEqual(excercise2.getSizeLastChunk(1025), 1)
        self.assertEqual(excercise2.getSizeLastChunk(2050), 2)
        self.assertEqual(excercise2.getSizeLastChunk(16927313), 593)

    def test_getNBlock(self):
        with open("./resources/6 - 2 - Generic birthday attack (16 min).mp4", "rb") as fileObject:
            ##comprobamos el primer bloque
            fileSize = excercise2.getSize(fileObject)
            blockCount = excercise2.getBlocksCount(fileSize)
            lastBlockSize = excercise2.getSizeLastChunk(fileSize)
            blockData = excercise2.getNBlock(fileObject, 0,blockCount,lastBlockSize)
            blockDataHex = blockData.encode("hex")[0:100]
            self.assertEqual(blockDataHex, '000000206674797069736f6d0000020069736f6d69736f32617663316d7034310006f00c6d6f6f760000006c6d7668640000')
            self.assertEquals(len(blockData),1024)

    def test_getNBlock_Block1(self):
        with open("./resources/6 - 2 - Generic birthday attack (16 min).mp4", "rb") as fileObject:
            ##comprobamos el primer bloque
            fileSize = excercise2.getSize(fileObject)
            blockCount = excercise2.getBlocksCount(fileSize)
            lastBlockSize = excercise2.getSizeLastChunk(fileSize)
            blockData = excercise2.getNBlock(fileObject, 1,blockCount,lastBlockSize)
            blockDataHex = blockData.encode("hex")
            self.assertEqual(blockDataHex, '00010000000000000001000000010000000300000002000000010000000500000001000000020000000100000000000000010000000100000001000000050000000100000002000000010000000000000001000000010000000100000005000000010000000200000001000000000000000100000001000000010000000200000001000000050000000100000002000000010000000000000001000000010000000100000002000000010000000500000001000000020000000100000000000000010000000100000008000000020000000100000005000000010000000200000001000000000000000100000001000000010000000200000001000000050000000100000002000000010000000000000001000000010000000200000002000000010000000500000001000000020000000100000000000000010000000100000001000000050000000100000002000000010000000000000001000000010000000300000002000000010000000500000001000000020000000100000000000000010000000100000001000000050000000100000002000000010000000000000001000000010000000200000002000000010000000500000001000000020000000100000000000000010000000100000001000000050000000100000002000000010000000000000001000000010000000600000002000000010000000500000001000000020000000100000000000000010000000100000003000000020000000100000005000000010000000200000001000000000000000100000001000000060000000200000001000000050000000100000002000000010000000000000001000000010000000200000002000000010000000500000001000000020000000100000000000000010000000100000002000000020000000100000005000000010000000200000001000000000000000100000001000000020000000200000001000000050000000100000002000000010000000000000001000000010000000100000005000000010000000200000001000000000000000100000001000000020000000200000001000000050000000100000002000000010000000000000001000000010000000200000002000000010000000500000001000000020000000100000000000000010000000100000001000000050000000100000002000000010000000000000001000000010000000300000002000000010000000500000001000000020000000100000000000000010000000100000001000000050000000100000002000000010000000000000001000000010000000200000002000000010000000500000001000000020000000100000000000000010000000100000001000000050000000100000002000000010000000000000001000000010000')

    def test_getNBlock_LastBlock(self):
        with open("./resources/6 - 2 - Generic birthday attack (16 min).mp4", "rb") as fileObject:
            ##comprobamos el primer bloque
            fileSize = excercise2.getSize(fileObject)
            blockCount = excercise2.getBlocksCount(fileSize)
            lastBlockSize = excercise2.getSizeLastChunk(fileSize)
            blockData = excercise2.getNBlock(fileObject, 16530,blockCount,lastBlockSize)
            blockDataHex = blockData.encode("hex")
            self.assertEqual(blockDataHex, 'f8a6e99fb5e5c3d38595eeb29ba4d9bdba96ce14e3b3a67bb35b627e52da7e37bf93b9257baf42ed6b09ed2a39326caeb39923c26bb563c7664e516508f7c8380cfbedf5a57557d794f09e5f2e0fe5527ae6c299f6051d93e380dc643f366ccf1a10590894dbdfaff5860b368d8adfe0d892bee66f0597f4fec591a68efb4566e19f6f54b7f9bdf2f9cd270efcbef96f4ab69726442c555cf737aaa04e96307676d6b45669d48e16de73429d55077c415cfbe19ebb70f5d58f3d3865c0214afefff15668c564a5ed72a8bf23f0f49d8ca9af0189f1637b7ea59906dd9754b5f73bde8122aa6ada819b603195984e54f3eda091a7932430f3d1ed733af93d99f9996d83c756e6c1a0b6b5e3d9dcb5b18ad484b14a5d3efbf98ff8558821a849826e2cac0bb6a12224a7e86f55f6b756351b39d5acb0004fb52885641f505b7a85e59041a8b11097848efcd222db2391e305e358a734dafabbf417a3f79a7c3e5e254dd80af1595f86bf563e1ed1d1669ac62afd26889f82fc0ada95e0c15b68d64807d2691aec6be13d81df0b71be7907090ece981d5f98757886bd417ed0e9d02d076380214cfefffc25b92e653d75a97951a582525f9a774e39000000000000a985a05839a4000000000003c1581d3188000000000007c9fb8fd17f2d000fe0d5ff0ff08007ad7ae7e97fd97d57a5d5eea000001cef8b7d6be5bc5eebdd7cc8000007b0ecf4fd175bd4f83f7a000001e179be27bef0753ef7c1e4f2793c90000000008d629d6f83e0f83c9e48000000004520f07c1e4f2793c900000000000f07c1f07c1e4f83b0000000000000b41e8e')

if __name__ == '__main__':
    unittest.main()
