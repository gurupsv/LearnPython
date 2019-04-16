def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        print(count)
    return inner

def multireturn():
    return 1,2,3,4

print(multireturn())
hello=outer()
hello()
hello()
outer()
hello()
hello()