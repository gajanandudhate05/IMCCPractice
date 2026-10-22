#Create Linked List-append (create nodes with positive and negative numbers )
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkList:
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
    
    def insert(self,data,n):
        new_node = Node(data)
        if n==1:
            new_node.next=self.head
            self.head=new_node
            
            print("Invalid position")
            return
            # Insert at the beginning
        if pos == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

    # def Traverse(self):
    #     temp = self.head
    #     while temp!= None:
    #         print(temp.data,end=" ")
    #         temp = temp.next
    #     print(None)
    def delete (self):
        curr=self.head
        while curr and curr.next:
            if curr.next.data<0:
                curr.next.data=None
                curr.next=curr.next.next
                temp.next=None
            else:
                curr=curr.next 
    def Traverse(self):
        temp = self.head
        while temp!= None:
            print(temp.data,end=" ")
            temp = temp.next
        print(None)


list=LinkList()
list.append(10)
list.append(-3)
list.append(5)
list.append(-12)
list.append(7)
list.append(50)
print("before:")
list.Traverse()

list.insert(node(60),5)
print("after:")
list.Traverse()
list.delete()
print("after deletion:")
list.Traverse()
