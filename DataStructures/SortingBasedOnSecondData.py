mdarray=[[3,8],[1,2],[2,1],[1,3],[3,6],[2,4]]
print(mdarray)

for i in range(len(mdarray)-1,0,-1):
    for j in range(i):
        if mdarray[j][1] > mdarray[j+1][1]:
            temp=mdarray[j+1]
            mdarray[j+1]=mdarray[j]
            mdarray[j]=temp

print(mdarray)
