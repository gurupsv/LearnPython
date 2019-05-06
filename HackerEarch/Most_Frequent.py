# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/golf/distinct-count-2/
from collections import Counter
t = int(input())
for i in range(t):
    m = Counter(input().split())
    print(m.most_common())
