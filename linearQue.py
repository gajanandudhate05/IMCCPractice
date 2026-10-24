class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        # Check before accessing the first node
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        print("Deleted node:", temp.data)

        # Move front to the next node
        self.front = self.front.next

        # If the last node was removed, reset rear too
        if self.front is None:
            self.rear = None
            print("Queue is empty now")

    def print(self):
        temp = self.front

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


que = LQueue()

que.enqueue(Node(23))
que.enqueue(Node(63))
que.enqueue(Node(3))
que.enqueue(Node(20))

que.print()

que.dequeue()
que.dequeue()
que.dequeue()

que.print()