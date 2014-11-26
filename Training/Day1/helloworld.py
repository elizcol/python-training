print('Hello world')
print('Hello' + ' ' + 'World')
#strings immutable
theString = 'Hello world'
print(theString)
theFirst = 'Hello'
theSecond = 'world'
print(theFirst, theSecond)
#lists mutable
data = ['Hello', ' world']
print(data[0] + data[1])
#tuples are immutable
dataTuple = ('Hello', ' world')
print(dataTuple[0] + dataTuple[1])
result = ''
# : is new code block
for i in range(len(data)):
    result += data[i]
print(result)
result2 = ''
j = 0
while j < len(dataTuple) :
    result2 += data[j]
    j += 1
print(result2)
#these loops are not pythonic. would use map..?
#result = map(reduce, sequence)
print("".join(data))
#dictionaries
dataDict = {
    2: 'World',
    1: ' ',
    0: 'Hello',
    3: '.'
    }
#function
def helloWorld():
    print("hello world")
helloWorld()
#params are untyped
if __name__ == '__main__':
    helloWorld()
#args references
def hello(*args):
    print(''.join(args))
try:
    assert 1 == 0
except:
    print('Hello you failed')
a = 15
if a < 10:
    print(a)
elif a < 20:
    print(a)
else:
    print(a)
# different import ways
from subprocess import call
call(['echo', 'Hello'])
from subprocess import call as MyName
MyName(['echo', 'Hello'])