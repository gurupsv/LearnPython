# URL :- https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-2/practice-problems/algorithm/sum-of-primes-7/
import math


def prime_or_not(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for k in range(3, int(math.sqrt(num)) + 1, 2):
        if num % k == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        line = input()
        if line:
            testcount = int(line)
            for i in range(testcount):
                myrange = input().split()
                total_sum = 0
                for n in range(int(myrange[0]), int(myrange[1]) + 1):
                    if prime_or_not(n):
                        total_sum += n
                print(total_sum)
    except EOFError:
        pass
