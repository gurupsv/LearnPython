from threading import Thread, activeCount, currentThread


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.setName(name)

    def run(self):
        for i in range(1, 101):
            print(str(i) + self.name)


t1 = MyThread("Sachin")
t2 = MyThread("Rahul")
t1.start()
t2.start()
t1.join()
t2.join()
print("Active Threads: ", activeCount())
print("Closing the log file!")
print("Exiting Mainthread!")