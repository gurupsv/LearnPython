
def main():
    x = ("First", "Second", "Third", "Fourth")
    func_with_args(*x)
    func_with_args()


def func_with_args(*args):
    if len(args):
        for i in range(len(args)):
            print(args[i])
    else:
        print("Nothing is passed!!")


if __name__ == "__main__": main()