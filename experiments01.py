def myfunc(arg1):
    print(arg1)

def myfunc_ret(arg1):
    print(arg1)
    return "somthing extra!!"

print(myfunc("Hello"))
print ("=========================")
print (myfunc_ret("Good Bye!"))
print ("=========================")

def power(num, x=1):
    result=1
    for i in range(x):
        result=result*num
    return result

print(power(2))
print(power(2,3))
print(power(x=3,num=4))
print(power(1,2))

print('Hello World'.lower())

h="Hello"
h = h + " World"
print(h)