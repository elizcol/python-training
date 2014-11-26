'''
Write a Python module that provides two functions that calculate a sequence of prime numbers. 
One of the functions should calculate primes up to a given value, the other function should 
calculate a given number of primes.
A prime number is a number whose only factors are 1 and the number itself.
The first 10 primes, and the primes less than 30 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
'''
def calcTo(upper):
    return [i for i in range(2,upper) if isPrime(i)]

def isPrime(p):
    for x in range(2,p):
        if p % x == 0:
            break
    else: return True

def calcPrimesTo(upper):
    primes = []
   
    for i in (range(2,upper) ):
        for x in (range(2,i) ):
            if i % x == 0:
                break
        else:
            primes.append(i)
    else:
        return primes

def calcNPrimes(n):
    primes = []
    i = 2
    while len(primes) < n:
        #[i for x in range(2,i) if i % x == 0]
        if isPrime(i):
            primes.append(i)
        i += 1
    else:
        return primes
    
if __name__ == '__main__':
    print(calcPrimesTo(30))
    print(calcTo(20))
    print(calcNPrimes(25))
