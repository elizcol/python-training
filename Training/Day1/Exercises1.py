import sys
import os
import turtle

#Write a Python program that prints out the number of parameters on the command line.
def countParams(params):
    return len(params)

#Write a Python program that prints out the number of files and directories in the current directory
def countFilesDirs():
    countParams(os.listdir(os.getcwd()))  

#Write a Python program using the turtle package to draw a square 100 pixels each side on the screen.
def draw():
    turtle._getpen()

if __name__ == '__main__':
    print(countParams(sys.argv))
    countFilesDirs()