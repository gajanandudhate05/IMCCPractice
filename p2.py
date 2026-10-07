#singly linear linked list
class node:
    def __init__(self, val):
        self.val = val
        self.next = None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,New_node):
        if self.head is None:
            self.head=New_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=New_node  #appending new node at the end of the linked list
    def insert(self, New_node, pos):
        if pos == 1:
            New_node.next = self.head
            self.head = New_node
        else:
            temp = self.head
            for _ in range(pos - 2):
                if temp is None:
                    print("Position out of bounds")
                    return
                temp = temp.next
            if temp is None:
                print("Position out of bounds")
                return
            New_node.next = temp.next
            temp.next = New_node

#linkedlist2=linkedlist()
#linkedlist3=linkedlist()
#linkedlist4=linkedlist()
#linkedlist2.append(node(10))
#linkedlist3.append(node(20))
#linkedlist4.append(node(30))
#linkedlist2.print()
#linkedlist3.print()
#linkedlist4.print()
list=linkedlist()
n1=node(10)
n2=node(-20)
n3=node(30)
list.append(n1)
list.append(n2)
list.append(n3) 
list.append(node(40))
list.append(node(50))
list.append(node(-60))
list.append(node(-70))
list.insert(node(100), 1)
list.insert(node(200), 4)
list.disolay()
