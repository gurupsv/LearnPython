# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/polygon-possible/description/

testcount=int(input())
for i in range(testcount):
    poligonSize=int(input())
    poligonVertices=input().split()
    allDifferent=True
    for i in range(len(poligonVertices)):
        for j in range(i+1,len(poligonVertices)):
            if poligonVertices[i] == poligonVertices[j]:
                allDifferent=False
                break
    if allDifferent:
        print("YES")
    else:
        print("NO")