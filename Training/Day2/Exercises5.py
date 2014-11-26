'''
Write a Python module that provides an iterative and a recursive implementation of the factorial 
function
'''

# another pythonic way is to use reduce function

def factorial(n):
    # aka return 1 if n < 2 else n * factorial(n-1)
    def fact(n):
        if n == 0 or n == 1:
            return 1
        return n * fact(n - 1)
    return fact(n)

def tailFact(x):
    def _tailrec(x, t):
        return t if x < 2 else _tailrec(x-1, t*x)
    return _tailrec(x, 1)

def meanVal(values):
    def sum(values):
        if len(values) == 1:
            return values[0]
        return values[0] + sum(values[1:len(values)])
    return sum(values) / len(values)

def median(values):
    sorted(values)
    if len(values) % 2 == 0:
        return meanVal(values[int(((len(values) / 2) - 1)) : int((len(values) / 2) + 1)])
    return values[int((len(values) - 1 ) / 2)]

if __name__ == '__main__':
    print(factorial(7))
    values = [1,2,3,4,5]
    print(meanVal(values))
    print(median(values))
    