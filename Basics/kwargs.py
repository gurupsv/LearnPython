def main():
    dict1 = dict(MyName="Guru", MyManager="Sony", MyCollegue1="Chandu")
    func_with_kwargs(**dict1)
    func_with_kwargs()


def func_with_kwargs(**kwargs):
    if len(kwargs):
        for i in kwargs:
            print("{} is {}".format(i,kwargs[i]))
    else:
        print("Nothing is passed!!")


if __name__ == "__main__": main()