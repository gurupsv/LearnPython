# URL : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/


testcount = int(input())
for i in range(testcount):
    m, n = (int(n) for n in input().split())
    c = [int(n) for n in input().split()]
    minimum = c[0]
    for i in range(m):
        if minimum > c[i]:
            minimum = c[i]
    print(n-minimum if n>minimum else 0)




