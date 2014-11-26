'''
Created on 26 Nov 2014

@author: b8605521
'''
import unittest
import Exercises6

class Test(unittest.TestCase):

    def testLineSize4(self):
        self.assertEqual("####\n", Exercises6.Shape.line(Exercises6.Shape(4,4)))
        
    def testLineSize7(self):
        self.assertEqual("#######\n", Exercises6.Shape.line(Exercises6.Shape(7,7)))

    def testShapeSize4(self):
        self.assertEqual("####\n####\n####\n####\n", Exercises6.Shape.shape(Exercises6.Shape(4,4)))

    def testShapeSize6(self):
        self.assertEqual("######\n######\n######\n######\n######\n######\n", Exercises6.Shape.shape(Exercises6.Shape(6,6)))
        
    def testShapeSize3By4(self):
        self.assertEqual("###\n###\n###\n###\n", Exercises6.Shape.shape(Exercises6.Shape(4,3)))
        
    def testRectangleSize2By6(self):
        self.assertEqual("######\n######\n", Exercises6.Shape.shape(Exercises6.Rectangle(2,6)))
        
    def testSquareSize6(self):
        self.assertEqual("######\n######\n######\n######\n######\n######\n", Exercises6.square(6))
        
    def testRectangleSize3By4(self):
        self.assertEqual("###\n###\n###\n###\n", Exercises6.rectangle(4,3))
        
    def testTriangleSize5(self):
        self.assertEqual("#\n##\n###\n####\n#####\n", Exercises6.triangle(5))
        
    def testTriangleSize9(self):
        self.assertEqual("#\n##\n###\n####\n#####\n######\n#######\n########\n#########\n", Exercises6.triangle(9))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()