from threading import Thread
from time import sleep

'''
Python process  waits only for non-daemon threads to finish execution.
It does take care of daemon threads.
Once all non-daemon threads will finish execution, Python process
will exit "EVEN IF" any daemon thread has still not finished its task.
'''


class MyThread(Thread):
    def __init__(self, name, delay):
        Thread.__init__(self)
        self.setName(name)
        self.delay = delay

    def run(self):
        for i in range(1, 11):
            sleep(self.delay)
            print(str(i) + self.name)


t1 = MyThread("Sachin", 1)
t2 = MyThread("Rahul", .5)
t3 = MyThread("Saurav", .3)
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
t3.start()