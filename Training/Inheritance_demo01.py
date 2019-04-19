class person:
    nationality = "India"  # Class level Encapsulation

    def sayhi(self):
        print("Hi from " + self.fname + " " + self.lname)

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class employee(person):
    org = "Oracle"

    def work(self):
        print(self.fname + " is working!")

    def __init__(self, fname, lname, dept, eid):
        person.__init__(self, fname, lname)
        self.dept = dept
        self.eid = eid


class student(person):
    def study(self):
        print(self.fname + " is studying!")

    def __init__(self, fname, lname, sid, stream):
        person.__init__(self, fname, lname)
        self.sid = sid
        self.stream = stream


class intern(student, employee):
    def __init__(self, fname, lname, sid, stream, eid, dept):
        student.__init__(self, fname, lname, sid, stream)
        employee.__init__(self, fname, lname, dept, eid)


e1 = intern("Sachin", "Tendulkar", "10", "sports", "07", "batting")
print(e1.nationality)
e1.study()
e1.work()
e1.sayhi()
print(e1.__dict__)
print(intern.__bases__)