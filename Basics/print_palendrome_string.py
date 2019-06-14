n=9

def dualrange(n):
    i,counter=1,1
    while i!=0:
        if i==n :
            counter=-1
        yield i
        i += counter

for i in dualrange(n):
    print(i,end="")

# for i in range(1,n+1):
#     print(i,end="")
# for i in range(n-1,0,-1):
#     print(i,end="")

print("")
balance=1000
new_balance=1000
print(id(balance))
print(id(new_balance))

balance += 250
print(id(balance))
print(id(new_balance))