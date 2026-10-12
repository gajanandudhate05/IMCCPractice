# Singly Linear Linked List

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
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Positions start from 1
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        while temp is not None and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Position out of bounds")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete the first node matching the value
    def del_node(self, value):
        temp = self.head
        prev = None

        while temp is not None and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value is not there in the list")
            return

        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
    
    def reverse(self):
        curr = self.head
        prev = None

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        def concatenate(self, second_list):
        # If the first list is empty
            if self.head is None:
                self.head = second_list.head
            return

        temp = self.head

        # Find the last node of the first list
        while temp.next is not None:
            temp = temp.next

        # Connect it to the second list
        temp.next = second_list.head

    # Delete the middle node
    # For an even-length list, delete the second middle node
    def findmid_del(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        print("Deleted middle node:", slow.data)

        if prev is None:
            self.head = slow.next
        else:
            prev.next = slow.next

    # Delete nodes at positions 2, 4, 6, ...
    def delete_alternate(self):
        temp = self.head

        while temp is not None and temp.next is not None:
            temp.next = temp.next.next
            temp = temp.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


linked_list = LinkedList()

linked_list.append(Node(10))
linked_list.append(Node(20))
linked_list.append(Node(30))
linked_list.append(Node(40))
linked_list.append(Node(50))

print("Original list:")
linked_list.display()

linked_list.delete_alternate()

print("After deleting alternate nodes:")
linked_list.display()

linked_list.reverse()

print("After reversing:")
linked_list.display()

# Other operations:
# linked_list.insert(Node(100), 2)
# linked_list.del_node(100)
# linked_list.findmid_del()