import unittest
from functions import *
from myPowerList import *
from directoryOfUsers import *

class testDecimaltoRoman(unittest.TestCase):

    def testInputString(self):
        roman = decimalToRoman("1666")
        self.assertEqual(roman, "MDCLXVI")

    def testInputInt(self):
        roman = decimalToRoman(123)
        self.assertEqual(roman, "CXXIII")

    def testInputNegativeInt(self):
        roman = decimalToRoman(-5)
        self.assertEqual(roman, "Number needs to be a positive integer")

    def testInputLarge(self):
         roman = decimalToRoman(100000)
         self.assertEqual(roman, "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")

    def testInputNull(self):
        with self.assertRaises(TypeError):
            roman = decimalToRoman()

    def testMoreThanOneArgument(self):
        with self.assertRaises(TypeError):
            roman = decimalToRoman("123","roman")

    def testInputInvalid(self):
        roman = decimalToRoman("12312fdffd")
        self.assertEqual(roman, "Number needs to be a integer")


class testMathFunctions(unittest.TestCase):

    def testSampleMeanValidList(self):
        self.list = [1, 2, 3, 4]
        result = sampleMean(self.list )
        self.assertEqual(result, 2.5)

    def testSampleMeanInvalidList(self):
        self.invalidList = ["a", 1, 2, 3]
        result = sampleMean(self.invalidList)
        self.assertEqual(result, "List should contain only numbers")

    def testSampleMedianValidListEven(self):
        self.listEven = [1, 2, 3, 4]
        result = median(self.listEven)
        self.assertEqual(result, 2.5)

    def testSampleMedianValidListOdd(self):
        self.listOdd = [1, 2, 3, 4, 5]
        result = median(self.listOdd)
        self.assertEqual(result, 3)

    def testSampleMedianInvalidList(self):
        self.invalidList = ["a", 1, 2, 3]
        result = median(self.invalidList)
        self.assertEqual(result, "List should contain only numbers")

    def testStdDevValidList(self):
        self.list = [1, 2, 3, 4, 5]
        result = std_dev(self.list )
        self.assertEqual(result, 1.5811388300841898)

    def testStdDevInvalidList(self):
        self.invalidList = ["a", 1, 2, 3]
        result = std_dev(self.invalidList)
        self.assertEqual(result, "List should contain only numbers")

    def testnQuartilValidList1Quartil(self):
        self.list = [3, 5, 7, 8, 12, 13, 14, 18, 21]
        result = nQuartile(self.list, 1)
        self.assertEqual(result, 6)

    def testnQuartilValidList2Quartil(self):
        self.list = [3, 5, 7, 8, 12, 13, 14, 18, 21]
        result = nQuartile(self.list, 2)
        self.assertEqual(result, 12)

    def testnQuartilValidList3Quartil(self):
        self.list = [3, 5, 7, 8, 12, 13, 14, 18, 21]
        result = nQuartile(self.list, 3)
        self.assertEqual(result, 16)

    def testnQuartilVaildListInvalidQuartil(self):
        self.invalidList = ["a", 1, 2, 3]
        result = nQuartile(self.invalidList, 4)
        self.assertEqual(result, "Parameter should be between 1 and 3")

    def testnQuartilInvalidList(self):
        self.invalidList = ["a", 1, 2, 3]
        result = nQuartile(self.invalidList, 3)
        self.assertEqual(result, "List should contain only numbers")

    def testnPercentileValidList(self):
        self.list = [3, 5, 7, 8, 12, 13, 14, 18, 21]
        result = nPercentile(self.list, 5)
        self.assertEqual(result, 21)

    def testnPercentileInvalidList(self):
        self.invalidList = ["a", 1, 2, 3]
        result = nPercentile(self.invalidList, 5)
        self.assertEqual(result, "List should contain only numbers")

class testMyPowerList(unittest.TestCase):
    myPowerList = myPowerList()
    def testCorrectInput(self):
        result = myPowerList.readFromTextFile(self,"fileA.txt")
        ##print(result)
        self.assertEqual(result, 'This is a test.')

    def testInvalidInputsStrings(self):
        with self.assertRaises(FileNotFoundError):
                myPowerList.readFromTextFile(self, "fileB.txt")

    def test_invalidInputNoFile(self):
        result = myPowerList.readFromTextFile(self,"fileB.j")
        self.assertEqual(result, "Invalid file name")

class testDirectoryOfUrsers(unittest.TestCase):


    def testCreateCorrectRecord(self):
        adirectoryOfUsers = directoryOfUsers()
        adirectoryOfUsers.newRecord("Martin", "Test 123", "6621561167", "martinnoriega@me.com")
        result = str(adirectoryOfUsers.searchData('1'))
        self.assertEqual(result, "{'name': 'Martin', 'address': 'Test 123', 'phone': '6621561167', 'email': 'martinnoriega@me.com'}")

    def testGetDateIncorrect(self):
        testDirectoryofUser = directoryOfUsers()
        result = testDirectoryofUser.searchData('IncorrectKey')
        self.assertEqual(result, "Data not found")

    def testSaveWithIncorrectFileName(self):
        testDirectoryofUser = directoryOfUsers()
        result = testDirectoryofUser.saveAllRecords("incorrectName")
        self.assertEqual(result, "Incorrect file name.")

    def testSaveFile(self):
        testDirectoryofUser = directoryOfUsers()
        testDirectoryofUser.newRecord("Martin", "Test 123", "6621561167", "martinnoriega@me.com")
        testDirectoryofUser.saveAllRecords("results.txt")
        readFiles = myPowerList()
        result = readFiles.readFromTextFile("results.txt")
        self.assertEqual(result, "Martin~Test 123~6621561167~martinnoriega@me.com\n")

    def testloadile(self):
        testDirectoryofUser = directoryOfUsers()
        testDirectoryofUser.loadRecords("results.txt")
        result = str(testDirectoryofUser.searchData('1'))
        self.assertEqual(result, "{'name': 'Martin', 'address': 'Test 123', 'phone': '6621561167', 'email': 'martinnoriega@me.com\\n'}")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testDecimaltoRoman)
    unittest.TextTestRunner(verbosity=0).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(testMathFunctions)
    unittest.TextTestRunner(verbosity=0).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(testMyPowerList)
    unittest.TextTestRunner(verbosity=0).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(testDirectoryOfUrsers)
    unittest.TextTestRunner(verbosity=0).run(suite)