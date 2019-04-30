from threading import Thread,Lock

class MyThread(Thread):
    lock = Lock()
    def __init__(self, sourcefile, destifile):
        Thread.__init__(self)
        self.sourcefile=sourcefile
        self.destifile=destifile


    def run(self):
        MyThread.lock.acquire()
        for line in self.sourcefile:
            self.destifile.write(line)
        MyThread.lock.release()


mydestfile = open("output.txt","w")
mysourcefile1 = open("file1.txt","r")
mysourcefile2 = open("file2.txt","r")

t1 = MyThread(mysourcefile1,mydestfile)
t2 = MyThread(mysourcefile2,mydestfile)
t1.start()
t2.start()
t1.join()
t2.join()

mydestfile.close()
mysourcefile1.close()
mysourcefile2.close()



