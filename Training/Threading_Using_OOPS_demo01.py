from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(1, 101):
            print(str(i) + self.name)


t1 = MyThread("Sachin")
t2 = MyThread("Rahul")
t1.start()
t2.start()
