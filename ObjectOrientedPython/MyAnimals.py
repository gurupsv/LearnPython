
class Animal():

    def __init__(self):
        print("Animal Created!")

    def who_am_i(self):
        print("I am an Animal!")


class Dog(Animal):

    def __init__(self, breed):
        Animal.__init__(self)
        print("Dog of {}".format(breed))
        self.breed=breed

    def bark(self):
        print("Woof.. Woof..")

    def who_am_i(self,var):
        print("I am Dog.. {}".format(var))


dog = Dog("Mudhol")
dog.who_am_i(12)
dog.bark()

