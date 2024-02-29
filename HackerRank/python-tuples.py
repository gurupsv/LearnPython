# n = int(input())
# d = input()
# mylist = [int(e) for e in d.split(" ")]
# print(hash(tuple(mylist)))

n = int(input())
print(hash(tuple(map(int,input().split()))))