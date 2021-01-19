import unittest

class TestHelpers():

    @staticmethod
    def __prettyPrintByteComparison(bytes1: bytes, bytes2: bytes, markerPosition : int = -1):
        """
        docstring
        """

        #shortened
        print("\nMixed representation:")
        print("Expected: . . . %s" % bytes1)
        print("Test result:. . %s" % bytes2)

        if markerPosition > -1:
            marker = ''
            lenByteStr = len('%s' % bytes2[:markerPosition-1])
            for j in range(0, lenByteStr): marker += ' '
            for j in range(0, max( len( '%s' % hex(bytes1[markerPosition])), len( '%s' % hex(bytes2[markerPosition])) )): marker +=  '^'
            print("                %s" % marker)

        #extended
        print("Alternative representation:")
        print("Expected: . . . %s" % TestHelpers.__prettyPrintBytesExtended(bytes1) )
        print("Test result:. . %s" % TestHelpers.__prettyPrintBytesExtended(bytes2) )

        if markerPosition > -1:
            marker = ''
            for j in range(0, markerPosition): marker += '   '
            marker += ' ^^'
            print("                %s" % marker)

    @staticmethod
    def __prettyPrintBytesExtended(bytesParam: bytes) -> str:

        printStr = ''
        for j in range(0, len(bytesParam)):
            printStrElement = hex(bytesParam[j])[2:]
            if len(printStrElement) == 1: printStrElement = '0%s' % printStrElement
            printStr += ' %s' % printStrElement

        return printStr


    @staticmethod
    def compareBytesLength(testClass : unittest.TestCase, bytesExpected: bytes, bytesIs: bytes):

        bytesELength = len(bytesExpected)
        bytesILength = len(bytesIs)

        if bytesELength != bytesILength: 
            print("Expected: . . . %s" % TestHelpers.__prettyPrintBytesExtended(bytesExpected) )
            print("Test result:. . %s" % TestHelpers.__prettyPrintBytesExtended(bytesIs) )

        testClass.assertEqual(bytesELength, bytesILength, msg="Bytes length is not equal. Expected: %s bytes, is: %s bytes." % (bytesELength, bytesILength))


    @staticmethod
    def compareBytesBitByBit(testClass : unittest.TestCase, bytesExpected: bytes, bytesIs: bytes):
            '''
            bytesExpected: Expected
            bytesIs: Result of class-under-test
            '''
            if len(bytesIs) > 0:

                for i in range (0, min(len(bytesExpected)-1, len(bytesIs)-1)):

                    if bytesExpected[i] != bytesIs[i]:
                        TestHelpers.__prettyPrintByteComparison(bytesExpected, bytesIs, i)

                    msgText = "Deviation at offset %s. Expected: %s, is: %s." % ( i+1, hex(bytesExpected[i]), hex(bytesIs[i]) )
                    testClass.assertEqual(bytesExpected[i], bytesIs[i], msg= msgText)

    @staticmethod
    def readTemplateFile(filename: str) -> bytes:

        fileContent = b'\x00'
        with open(filename, 'rb') as readFile:
            fileContent = readFile.read()
            readFile.close()
        
        return fileContent