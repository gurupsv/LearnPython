from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, name, delay):
        Thread.__init__(self)
        self.setName(name)
        self.delay = delay

    def run(self):
        for i in range(1, 11):
            sleep(self.delay)
            print(str(i) + self.name)


t1 = MyThread("\tSachin", 1)
t2 = MyThread("\t\tRahul", .5)
t3 = MyThread("\t\t\tSaurav", .3)
t1.start()
t2.start()
t3.start()