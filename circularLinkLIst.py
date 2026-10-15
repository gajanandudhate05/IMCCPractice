# Doubly Linear Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None       # New link to previous node


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Add a node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    # 2. Insert a node at a specific position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return
            #temp.next=




        # Insert at the beginning
        if pos == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        # Find the node before the insertion position
        temp = self.head
        p = 1

        while temp is not None and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Position out of bounds")
            return

        new_node.next = temp.next
        new_node.prev = temp

        # Update the following node, if it exists
        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    # 3. Delete the first node containing the value
    def del_node(self, value):
        temp = self.head

        while temp is not None:
            if temp.data == value:
                break
            temp = temp.next

        if temp is None:
            print("Value is not there in the list")
            return

        # Update the previous node or head
        if temp.prev is None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next

        # Update the next node, if it exists
        if temp.next is not None:
            temp.next.prev = temp.prev

        # Disconnect the removed node
        temp.next = None
        temp.prev = None

    # 4. Reverse the list
    def reverse(self):
        curr = self.head
        new_head = None

        while curr is not None:
            # Save the original next node
            nextnode = curr.next

            # Swap the two links
            curr.next = curr.prev
            curr.prev = nextnode

            # Remember the latest processed node
            new_head = curr

            # Move along the original list
            curr = nextnode

        self.head = new_head

    # 5. Display from head to last node
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next

    # 6. Display from last node to head
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Reach the last node
        while temp.next is not None:
            temp = temp.next

        # Move backward using prev
        while temp is not None:
            print(temp.data)
            temp = temp.prev


# Create the linked list
dll = LinkedList()

dll.append(Node(10))
dll.append(Node(20))
dll.append(Node(30))

print("Original list:")
dll.display()

print("Backward display:")
dll.display_backward()

dll.reverse()

print("After reversing:")
dll.display()


# Try these operations:
# dll.insert(Node(40), 4)
# dll.insert(Node(5), 1)
# dll.del_node(20)
# dll.display()