#
# myarray=[8,4,5,1,9,9,3,4,6,2,3,7,10]
# first=0
# second=0
#
# #myarray.sort(reverse=1)
# for i in myarray:
#     if(i>first):
#         if ( first>second):
#             second=first
#             print(f"setting second =", second)
#         first=i
#         print(f"setting first =",first)
#     elif (i>second and i<first):
#         print(f"Second was ", second)
#         second=i
#         print(f"+setting second =",second)
#
# print("============")
# print(first)
# print(second)


mystring="This is testinG in Python"
print(mystring[4:1:-1])

print(mystring.count("i"))

myarray=[9,4,1,0,5,7,0,3,4]
print(len(myarray))
for i in range(len(myarray)-1):
    print(i)
    if (myarray[i]==0):
        print("changed")
        temp=myarray[i]
        myarray[i]=myarray[i+1]
        myarray[i+1]=temp

print(myarray)