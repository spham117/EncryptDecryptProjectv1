import random
import numpy as np
def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True
        for num in range(2, n):
            if n % num == 0:
                isPrime = False
        if isPrime:
            prime_list.append(n)
    return prime_list
prime_list = primesInRange(1, 1111)
key = []
string = input("enter string: ")
for i in string:
    x = (random.choice(prime_list))
    y = str(np.log(x*ord(i)))
    z = ''.join(y)
    print((z),end=',')
    key.append(x)

print(" PRIVATE KEY: ",key)
    


