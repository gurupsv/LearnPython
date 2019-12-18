mystring="This is Python Code!"
revstring=""
for i in range(len(mystring)-1,-1, -1):
    revstring += mystring[i]

print(revstring)

mylist=['abcd','efgh']
a='abcd'
b='efgh'

print(id(mylist))
print(id([a,b]))