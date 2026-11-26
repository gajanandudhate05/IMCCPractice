
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
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # Search node
    def search(self, val):
        temp = self.root

        while temp is not None:
            if val == temp.data:
                print("Value found:", temp.data)
                return temp

            elif val < temp.data:
                temp = temp.left

            else:
                temp = temp.right

        print("Value not found")
        return None

    # Find minimum node
    def minimum(self, rt):
        temp = rt

        while temp.left is not None:
            temp = temp.left

        return temp

    # Delete node
    def delete(self, rt, val):
        if rt is None:
            return None

        if val < rt.data:
            rt.left = self.delete(rt.left, val)

        elif val > rt.data:
            rt.right = self.delete(rt.right, val)

        else:
            # Case 1 and Case 2: Zero or one child
            if rt.left is None:
                return rt.right

            elif rt.right is None:
                return rt.left

            # Case 3: Two children
            succ = self.minimum(rt.right)
            rt.data = succ.data
            rt.right = self.delete(rt.right, succ.data)

        return rt

    # Inorder traversal (Left, Root, Right)
    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # Preorder traversal (Root, Left, Right)
    def preorder(self, rt):
        if rt is None:
            return

        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    # Postorder traversal (Left, Right, Root)
    def postorder(self, rt):
        if rt is None:
            return

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

        # Minimum
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        print("Min:", temp.data)

        # Maximum
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
print("Inorder:")
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
print("\n")
b1.findminmax()

# Search
print("\n\nSearch:")
b1.search(65)

# Delete
print("\nDelete 10:")
b1.root = b1.delete(b1.root, 10)

# Display BST after deletion
print("Inorder after deletion:")
b1.inorder(b1.root)

print("\nTotal nodes after deletion:", b1.count(b1.root))



