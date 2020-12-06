class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self, root=None):
        pass

    def insert(self, node, data):
        if node is None:
            print("*")
            return Node(data)
        if data < node.data:
            print("L", end='')
            node.left = self.insert(node.left, data)
        else:
            print("R", end='')
            node.right = self.insert(node.right, data)
        return node

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


inp = input("Enter Input : ").split()
BT = BST()
root = None
for i in inp:
    root = BT.insert(root, int(i))
# BT.printTree(root)
