# URL : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/

testcount = int(input())

a = [int(x) for x in input().split()]
b = ""
#print(a)
for j in range(len(a)):
    thenumber = True
    for k in range(j,len(a)):
        if a[j] < a[k]:
            thenumber = False
            break
    if thenumber:
        b = b + str(a[j])
print(b)
