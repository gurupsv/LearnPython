class A:
    def sayhi(self):
        print("Hello from Class A!")

class B(A):
    def sayhi(self):
        print("Hello from Class B")

class C(A,B):
    pass

myobj=C()
myobj.sayhi()
