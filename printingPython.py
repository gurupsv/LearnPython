# print ("This is {0} first print statement".format("Guru's"))
# mystring = "Guruprasad loves Suneetha and Vaivaswatha!"
# print (mystring[::1])
# print (mystring[1::1])
# print (mystring[1:-1:1])
# print (mystring[1:-1:2])
#
# mystr1 = "Hello I am here!"
# mystr2 = "Hello I am Here!"
#
# if mystr1 == mystr2:
#     print ("They are Equal!!")
# else:
#     print ("They are not equal!!")


# print("Enter your age ->")
# myage=int(input())
# if (18 <= myage <= 30):
#     print("Welcome to 18-30 Holidays")
# else:
#     print("I am afraid, we cant let you in now!")

number="Blah blah blah 2,44,654,78,534,908,733,5,23,44"
onlynumber=''
for i in number:
    if i in "0123456789":
        onlynumber=onlynumber+i

print(onlynumber)

for i in range(0,10,2):
    print(i)

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

from collections import Counter

m=Counter("This is just a test")
print(m.most_common(3))
print(m.keys())