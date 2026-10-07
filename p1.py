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
    def print(self):
        temp=self.head
        while temp.next:
            print(temp.data)
            temp=temp.next.next
            
        if temp:
            print(temp.data)

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
list.print()

