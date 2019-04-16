'''
def sayhi(name1,name2):
    return "Hi "+name1+" and "+name2
'''
data=(lambda name1,name2:"Hi "+name1+" and "+name2)("Guru", "Prasad")
print(data)

add=(lambda a,b:a+b)
print(add(1,3))