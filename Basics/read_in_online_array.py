# arrlen = int(input())
# array = []
# myinput = input().split()
#
# qlen = int(input())
# q = []
# for i in range(qlen):
#     q.append(input())
# for i in range(qlen):
#     count=0
#     for j in range(arrlen):
#         #print(myinput[j], q[i])
#         if myinput[j] == q[i]:
#             count += 1
#     if count == 0:
#         print("NOT PRESENT")
#     else:
#         print(count)

from sys import stdin, stdout
from collections import Counter
input("Array elements :")
cnt = Counter(stdin.readline().rstrip().split())
input("Query Number :")
quers = stdin.read().splitlines()
rez = [str(cnt.get(i,'NOT PRESENT')) for i in quers]
stdout.write('\n'.join(rez))