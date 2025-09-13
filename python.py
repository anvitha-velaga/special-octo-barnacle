class Node1:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist1:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node1(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print ("None")

l1=Linkedlist1()
l1.append(10)
l1.append(20)
l1.append(30)

l1.display()


