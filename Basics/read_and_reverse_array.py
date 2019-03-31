length = int(input())
arr = []
for i in range(length):
    #print(i)
    arr.append(int(input()))

for i in range(length-1, -1, -1):
    #print(i)
    print(arr[i])

