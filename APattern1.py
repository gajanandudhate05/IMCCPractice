class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert(self, new_node, pos):
        if pos == 1:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
                return
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head
        else:
            p = 1
            temp = self.head
            # Traverse until the node before the target position
            while p < pos - 1 and temp.next != self.head:
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node

    def del_node(self, value):
        if self.head is None:
            print("List is empty")
            return

        # Case 1: Delete the head node
        if self.head.data == value:
            if self.head.next == self.head:  # Only one node in the list
                self.head = None
                return
            # Find the last node to update its pointer
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            return

        # Case 2: Delete a non-head node
        prev = self.head
        temp = self.head.next
        while temp != self.head:
            if temp.data == value:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next

        print("Value is not there in the list")

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                print("(head)")
                break

# Testing the corrected implementation
lst = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
lst.append(n1)
lst.append(n2)
lst.append(n3)
lst.insert(Node(40), 4)
lst.insert(Node(5), 1)

print("List after insertions:")
lst.display()

print("\nDeleting 20:")
lst.del_node(20)
lst.display()