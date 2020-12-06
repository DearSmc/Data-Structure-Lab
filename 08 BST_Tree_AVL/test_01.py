class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if self.root is None:
            self.root = Node(data)
            print("*")
            return self.root

        if node is None:
            print("*")
            return Node(data)

        else:
            if node.data <= data:
                print("R", end="")
                node.right = self.insert(node.right, data)
            else:
                print("L", end="")
                node.left = self.insert(node.left, data)

        return node

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)



inp = input("Enter Input: ").split()
T = BST()
root = None
for i in inp:
    root = T.insert(root, int(i))
