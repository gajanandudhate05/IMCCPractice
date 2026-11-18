
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# STACK
class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.data

    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

    # Reverse Stack
    def reverse(self):
        st1 = Stack()
        temp = self.top

        while temp:
            st1.push(Node(temp.data))
            temp = temp.next

        self.top = st1.top


# QUEUE
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    def enqueue(self, new_node):
        if self.isempty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None

            if self.front is None:
                self.rear = None

            return temp.data

    def print(self):
        if self.isempty():
            print("Queue is empty")
        else:
            temp = self.front
            while temp:
                print(temp.data)
                temp = temp.next

    # Reverse Queue using Stack
    def reverse(self):
        st = Stack()

        while not self.isempty():
            value = self.dequeue()
            st.push(Node(value))

        while not st.isempty():
            value = st.pop()
            self.enqueue(Node(value))


# MAIN PROGRAM

# Stack
s = Stack()

s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.push(Node(50))

print("Original Stack:")
s.print()

s.reverse()

print("Reversed Stack:")
s.print()


# Queue
q = Queue()

q.enqueue(Node(100))
q.enqueue(Node(200))
q.enqueue(Node(300))
q.enqueue(Node(400))
q.enqueue(Node(500))

print("Original Queue:")
q.print()

q.reverse()

print("Reversed Queue:")
q.print()


# Stack using Linked List
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None
    
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            poped_data = temp.data
            self.top = self.top.next
            temp = None
            return poped_data

    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack Values")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

# Linear Queue
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):              # Added 'self' parameter
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.rear is None:
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def reverse_stack(s1):
    q1 = Queue()
    while not s1.isempty():      
        q1.enqueue(s1.pop())
    q1.printQueue()
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    s1.print()

st = Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.print()

print("Reversed Stack: ", end="")
reverse_stack(st)