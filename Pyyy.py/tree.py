class node :
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
g1=BST()
g1.root = node(50)
print(g1.root.data)
g1.root.left = node(30)
g1.root.right = node(70)
print(g1.root.left.data)
print(g1.root.right.data)