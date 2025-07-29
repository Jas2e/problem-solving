# Prime number or not...
import math

def isPrime(num):
    if num <= 1:
        return False
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(isPrime(num))