# URL :- https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/memorise-me/

from collections import Counter

arrlen = int(input())
myinput = Counter(input().split())

qlen = int(input())
q = []
for i in range(qlen):
    myip = input()
    count = myinput.get(myip,"NOT PRESENT")
    q.append(count)
print(*q, sep="\n")
