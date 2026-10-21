#Create Linked List-append (create nodes with positive and negative numbers )
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linkList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def Traverse(self):
        temp = self.head
        while temp!= None:
            print(temp.data,end=" ")
            temp = temp.next
        print(None)
list=linkList()
list.append(10)
list.append(-3)
list.append(5)
list.append(-12)
list.append(7)
list.append(-20)
list.Traverse()