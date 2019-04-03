
def main():
    myarray=[7,3,5,6,9,1,0,2,4,8]
    print("Before Sort : ",myarray)
    bubblesort(myarray)
    print("After Sort : ",myarray)


def bubblesort(arg):
    for i in range(len(arg)-1,0,-1):
        for j in range(i):
            if arg[j]<arg[j+1]:
                temp=arg[j]
                arg[j]=arg[j+1]
                arg[j+1]=temp


if __name__ == "__main__": main()