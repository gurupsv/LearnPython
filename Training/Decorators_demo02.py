# Inner should be generic
from functools import wraps

def demo(a):
    @wraps(a)
    def inner(*c,**b):
        print("Calling ->",a.__name__)
        a(*c,**b)
    return inner

@demo
def sayhi():
    """This is nothing but doc """
    print("Say Hi to me!")

@demo
def sayhitoperson(b):
    print("Hello Mr.",b)

@demo
def helloguys(a,b):
    print("Hello Mr."+a+" and Mr."+b)

sayhi()
sayhitoperson("Guru")
helloguys("Guru","Anand")
print("======================")
print(sayhi.__name__)
print("======================")
print(sayhi.__doc__)
print("======================")