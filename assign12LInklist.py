#3.	Traverse and print the node values
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def traverse(self):
        current = self
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


