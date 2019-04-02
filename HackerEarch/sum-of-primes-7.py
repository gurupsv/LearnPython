# URL :- https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-2/practice-problems/algorithm/sum-of-primes-7/
import math


def prime_or_not(num):
    pr=True
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        pr = False
    else:
        for k in range(3, int(math.sqrt(num))+2, 2):
            if num % k == 0:
                pr = False
                break
    return pr


testcount = int(input())
for i in range(testcount):
    myrange = input().split()
    sum = 0
    for n in range(int(myrange[0]), int(myrange[1])+1):
        if prime_or_not(n):
            sum += n
    print(sum)


