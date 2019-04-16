data="*"
i=3
for n in range(i):
    print(data*(n+1))

for n in range(i,0,-1):
    print(data*n)


def outer():
    print("Outer")

    def inner():
        print("Inner")


outer()


counter=0

def hello():
    global counter
    counter += 1
    print(counter)

hello()
hello()
hello()