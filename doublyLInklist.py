class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
        new_node.prev = temp

    def del_node(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Search for the value
        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value is not there in the list")
            return

        # Update the previous node or move the head
        if temp.prev is None:
            self.head = temp.next
        else:
            temp.prev.next = temp.next

        # Update the next node's previous reference
        if temp.next is not None:
            temp.next.prev = temp.prev

        # Disconnect the deleted node
        temp.prev = None
        temp.next = None

        print("Deleted value:", value)

    def display(self):# display the list
        if self.head is None:# if the list is empty
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


linked_list = DoublyLinkedList()

linked_list.append(Node(10))
linked_list.append(Node(20))
linked_list.append(Node(30))
linked_list.append(Node(40))

print("Original list:")
linked_list.display()

value = int(input("Enter value to delete: "))
linked_list.del_node(value)

print("After deletion:")
linked_list.display()