'''
Created on 26 Nov 2014

@author: b8605521
'''

class Shape():
    # we want something similar to the fields being final - immutable. height/width can just be changed
    def __init__(self, h, w):
        self.height = h
        self.width = w
    
    # width where default val is self.width?
    def line(self):
        return "#" * self.width + "\n"
    
    def shape(self):
        return self.line() * self.height

class Triangle(Shape):
    def __init__(self, height):
        Shape.__init__(self, height, height)
    
    def line(self, width):
        return "#" * width + "\n"
    
    def shape(self):
        shape = ""
        for w in range(1,self.height + 1):
            shape += self.line(w)
        return shape
        #return self.line(self.height - 1) * self.height
    
class Square(Shape):
    def __init__(self, height):
        Shape.__init__(self, height, height)
        
class Rectangle(Shape):
    def __init__(self, height, width):
        Shape.__init__(self, height, width)  

# easy to use methods
def triangle(height):
    triangle = Triangle(height)
    return triangle.shape()

def square(width):
    square = Square(width)
    return square.shape()

def rectangle(height, width):
    rectangle = Rectangle(height, width)
    return rectangle.shape()

if __name__ == '__main__':
    print(square(5))
    print(rectangle(6, 2))
    print(triangle(5))