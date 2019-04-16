# Inner should be generic

def demo(a):
    def inner(*c,**b):
        print("Calling ->",a.__name__)
        a(*c,**b)
    return inner

@demo
def sayhi():
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