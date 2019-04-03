
def main():
    arr=[3,6,7,4,2,1,8,9,5]
    print("Array Before Sorting :",arr)
    bubblesort(arr)
    print("Array After Sorting :", arr)


def bubblesort(args):
    for i in range(len(args)-1,0,-1):
        print(i)
        for j in range(i):
            if args[j]<args[j+1]:
                temp=args[j]
                args[j]=args[j+1]
                args[j+1]=temp


if __name__ == "__main__": main()
