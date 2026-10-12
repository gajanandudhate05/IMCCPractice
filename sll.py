# STEP 1: Create the Node class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# STEP 2: Create the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # STEP 3: Add a new node at the end
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
    def concatenate(self, second_list):
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=second_list.head
    # STEP 4: Display the linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # STEP 5: Concatenate two separate linked lists
    def concatenate(self, second_list):
        if self is second_list:
            print("Cannot concatenate a list with itself")
            return

        # If the first list is empty, take the second list
        if self.head is None:
            self.head = second_list.head
        else:
            temp = self.head

            # Find the last node of the first list
            while temp.next is not None:
                temp = temp.next

            # Connect it to the first node of the second list
            temp.next = second_list.head

        # Move the second list's nodes into the first list
        second_list.head = None


# STEP 6: Create the first linked list
list1 = LinkedList()

list1.append(10)
list1.append(20)
list1.append(30)

# STEP 7: Create the second linked list
list2 = LinkedList()

list2.append(40)
list2.append(50)
list2.append(60)

# STEP 8: Display both lists
print("First linked list:")
list1.display()

print("Second linked list:")
list2.display()

# STEP 9: Concatenate the lists
list1.concatenate(list2)

# STEP 10: Display the combined list
print("Combined linked list:")
list1.display()