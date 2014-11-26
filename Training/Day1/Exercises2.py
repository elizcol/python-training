'''
Created on 24 Nov 2014

@author: b8605521
'''

import sys
import subprocess

# Write a Python program to output the table of values of simple compound interest for an 
# investment amount given on the command line for interest rates of 3%, 5%, and 7% for a period of 
# 10 years.

def interestTable(amount):
    def countUp(n, i):
        if n - i >= 0:
            print('years: ',i, ' total={:6.2f}, total={:6.2f}, total={:6.2f}'.format(amount * (1.03 ** i), amount * (1.05 ** i) , amount * (1.07 ** i)))
            countUp(n, i + 1)
    countUp(10, 1)

#Write a Python module that provides a function that counts all the characters, words and lines in a 
#file. (cf. wc on Linux/Solaris/Mac OS X/Unix.) The function should be able to take a string (the 
#name of a file to be opened) or a file-like object (of an already opened file) as a parameter.

def wordCount(file):
    print(subprocess.check_output('wc ' + file, shell=True))

if __name__ == '__main__':
    interestTable(int(sys.argv[1]))
    #wordCount(sys.argv[2])
