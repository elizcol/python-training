'''
Created on 25 Nov 2014

@author: b8605521
'''
import unittest
import Exercises4

class Test(unittest.TestCase):


    def testCalcPrimesTo(self):
        self.assertEqual([2,3,5,7], Exercises4.calcPrimesTo(10))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()