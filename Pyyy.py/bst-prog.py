# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert node
    def insert(self, new_node):
        if self.root is None:  # BST is empty
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:  # Left subtree
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                else:  # Right subtree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # Inorder traversal (Left, Root, Right)
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            
# find minimum  value of node and maximum value of node
    def find_minmax(self,rt):
        temp=rt
        while temp .left:
            temp=temp.left
        print("\nmin value:",temp.data)

    # Preorder traversal (Root, Left, Right)
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    # Postorder traversal (Left, Right, Root)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    # Count total nodes
    def count(self, rt):
        if rt is None:
            return 0
        return 1 + self.count(rt.left) + self.count(rt.right)

    # Find minimum and maximum
    def findminmax(self):
        if self.root is None:
            print("BST is empty")
            return

        # Find minimum
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        print("\nMin:", temp.data)

        # Find maximum
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        print("Max:", temp.data)


# Create BST
b1 = BST()

# Insert nodes
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

# Inorder
print("\nInorder:")
b1.inorder(b1.root)

# Count nodes
print("\nNo of nodes:", b1.count(b1.root))

# Preorder
print("\nPreorder:")
b1.preorder(b1.root)

# Postorder
print("\nPostorder:")
b1.postorder(b1.root)

# Minimum and maximum
b1.findminmax()