import math
def isprime(n):
    prime = True
    if n == 2 :
        prime = True
    elif n > 2:
        i = 2
        while i <= math.sqrt(n):
            if n % i == 0:
                prime = False
                break
            i += 1
    else :
        prime = False
        
    return prime
    

n = int(input())
numbers = [ int(input()) for i in range(n)]

for number in numbers:
    if isprime(number):
        print("Prime")
    else:
        print("Not prime")
