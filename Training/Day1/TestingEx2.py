'''
Created on 24 Nov 2014

@author: b8605521
'''
import unittest
import subprocess

class Test(unittest.TestCase):


    def test_interestTable(self):
        self.assertEqual('''years:  1  total=  2.06, total=  2.10, total=  2.14
years:  2  total=  2.12, total=  2.21, total=  2.29
years:  3  total=  2.19, total=  2.32, total=  2.45
years:  4  total=  2.25, total=  2.43, total=  2.62
years:  5  total=  2.32, total=  2.55, total=  2.81
years:  6  total=  2.39, total=  2.68, total=  3.00
years:  7  total=  2.46, total=  2.81, total=  3.21
years:  8  total=  2.53, total=  2.95, total=  3.44
years:  9  total=  2.61, total=  3.10, total=  3.68
years:  10  total=  2.69, total=  3.26, total=  3.93\n'''.splitlines(), subprocess.check_output(('python3', 'Exercises2.py', '2')).decode().splitlines())

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_interestTable']
    unittest.main()
