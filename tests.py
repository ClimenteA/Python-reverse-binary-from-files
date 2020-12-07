import os, unittest


class TestBinaryReverse(unittest.TestCase):

    def setUp(self):

        with open("testFile.txt", "w") as o:
            o.write("123")
        
        os.system("python3 binary_reverse.py testFile.txt")


    def tearDown(self):
        os.remove("testFile.txt")
        os.remove("reversed-testFile.txt")
        

    def testReversedBytes(self):

        with open("reversed-testFile.txt", "rb") as f:
            outByte = f.read(1)

        # we wrote "123" in testFile.txt 
        # so in the reversed first byte should be 3 
        self.assertEqual(outByte, b'3')


        
    
if __name__ == '__main__':
    unittest.main()

