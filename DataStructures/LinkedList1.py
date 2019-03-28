# Define Node


class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val=val

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next=next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    # TODO : Insert Logic to be implemented
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    # TODO : Logic to find the element
    def find(self,value):

        item = self.head

        while (item != None):
            if item.get_data() == value :
                return True
            else:
                item =  item.get_next()
        return False

    # TODO : Delete Logic
    def deleteAt(self, index):

        if index > self.count : return
        if self.head == None : return
        else :
            tempIdx = 0
            node=self.head
            while tempIdx < index-1:
                node=node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
        return True

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node : ",tempnode.get_data())
            tempnode = tempnode.get_next()


def main():
    print("Inside Main method...")
    itemlist = LinkedList()
    itemlist.insert(38)
    itemlist.insert(49)
    itemlist.dump_list()

    print("Item count: ", itemlist.get_count())
    print("Finding item: ", itemlist.find(38))
    print("Finding item: ", itemlist.find(78))

    itemlist.deleteAt(1)
    print("Item count: ", itemlist.get_count())
    itemlist.dump_list()

    print("Main method completed..")

if __name__ == "__main__" : main()

