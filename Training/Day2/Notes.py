'''
Created on 25 Nov 2014

@author: b8605521
'''
list = []
tuple = ()
#no order
dict = {}
#no order
set = {}
list = [2,3,4]
tuple = (2,3,4)
#can have mix of numbers and strings
dict = {0: 2, 1: 3, 2: 4, "num": "val"}
set = {2,3,4}
#can do things like
list(tuple)
set(list)
#slice
list[0:1] #2
list[1:] #3,4
list[-1] #3
list[1:-1] #3
#append
list.append(6) #[2,3,4,6]
#extend (iterable)
list += [7,8] #[2,3,4,6,7,8]
#delete
del list[1] #[2,4,6,7,8]
list[2] = [9,1] #[2,4,[9,1],7,8]
list[0:1] = [5,3,3] #[5,3,3,[9,1],7,8
# existence of a key using the in keyword
if 0 in dict: print('Yes')
#list comprehensions, generator expression
# see the [bla] makes list then prints. can use {} for set etc
print([x for x in range(1,40) if x * x % 10 == 0])
# [10,20,30] if is filter expression
#use in defs etc see what vars they have
print(locals())
def printDefaultVals(a='Hi', b='', c='Dude', d='.'):
    print(a + b + c + d)
#can call in diff ways- overwrites!
printDefaultVals(c='Lady')
#keyword args
def printExtra(a, **args):
    print(a + args['b'] + args['c'] + args['d'])
#any order. makes dictionary
printExtra(c='World', d='.', b='', a='Hello')
#lambda can pass in functions
def printApplication(function):
    print(function('Hello','world','.'))
printApplication(lambda a,b,c,d: a + b + c + d)
#from functools import wraps
''' these comments you can use pydoc to make the comments '''
# __call__(self) to make a callable method

