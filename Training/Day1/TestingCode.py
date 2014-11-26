'''
Created on 24 Nov 2014

@author: b8605521
'''
import unittest
import BasicCode
import Exercises1
import subprocess

class Test_HelloWorld(unittest.TestCase):


    def test_helloWorld(self):
        self.assertEqual('hello world', BasicCode.helloWorld())

    def test_countParams(self):
        self.assertEqual(3, Exercises1.countParams(["this", "is", "three"]), "Testing that it is counting params") 

    # this method is checking against the terminal use in cmd line
    def test_script_HelloWorld(self):
        self.assertEqual('hello world\n', subprocess.check_output(('python3', 'BasicCode.py')).decode(), "Testing using subprocess")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()