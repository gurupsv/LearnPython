from threading import Thread


# def demo1():
#     for i in range(1, 101):
#         print(str(i) + "Sachin")
#
#
# def demo2():
#     for i in range(1, 101):
#         print(str(i) + "Rahul")
#
#
# t1 = Thread(target=demo1)
# t2 = Thread(target=demo2)
# t1.start()
# t2.start()


def demo(name):
    for i in range(1, 1010):
        print(str(i) + name)


t1 = Thread(target=demo, args=["Sachin"])
t2 = Thread(target=demo, args=["Rahul"])
t1.start()
t2.start()