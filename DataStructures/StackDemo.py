class Node():
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None



class StackDemo():
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
        count=0
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.head
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node
    def insert(self,prev_node,value):
        new_node=Node(value)
        new_node.next=prev_node.next
        new_node.prev=prev_node
        prev_node.next.prev=new_node
        prev_node.next=new_node
    def peek(self):
        return self.head.data
    def pop(self):
        last_node=self.head
        self.head=self.head.next
        return last_node.data

def printstack(head):
    while head != None:
        print(head.data)
        head=head.next

def printrevstack(tail):
    while tail != None:
        print(tail.data)
        tail=tail.prev

mystack=StackDemo()
mystack.push(10)
mystack.push(4)
mystack.push(3)
mystack.push(11)

printstack(mystack.head)
print("=================")
print(mystack.peek())
print(mystack.pop())
#print(mystack.peek())
print("=================")
printstack(mystack.head)
printrevstack(mystack.tail)