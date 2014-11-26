'''
Created on 25 Nov 2014

@author: b8605521
'''
import unittest
import Exercises5

class Test(unittest.TestCase):

    def testFactorial(self):
        self.assertEqual(120, Exercises5.factorial(5))

    def testFactorialSeven(self):
        self.assertEqual(5040, Exercises5.factorial(7))

    def testMeanVal(self):
        self.assertEqual(3, Exercises5.meanVal([1,2,3,4,5]))

    def testMeanValExSheet(self):
        self.assertAlmostEqual(4.28095228571428571428, Exercises5.meanVal([3.4, 5.6, 2.0, 4.5, 7.8, 4.666666, 2.0]),2)

    def testMeanValExSheet2(self):
        self.assertAlmostEqual(2.1, Exercises5.meanVal([1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0]),2)
        
    def testMedianValExSheet(self):
        self.assertAlmostEqual(4.5, Exercises5.median([3.4, 5.6, 2.0, 4.5, 7.8, 4.666666, 2.0]),2)

    def testMedianValExSheet2(self):
        self.assertAlmostEqual(2.0, Exercises5.median([1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0]),2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()