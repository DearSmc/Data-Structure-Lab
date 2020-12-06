class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while(1):
                if data < cur.data:
                    if cur.left != None:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        return self.root
                else:
                    if cur.right != None:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def findMax(self):
        if self.root == None:
            return -1
        else:
            cur = self.root

            while cur.right != None:
                cur = cur.right
            return cur.data

    def findMin(self):
        if self.root == None:
            return -1
        else:
            cur = self.root
            while cur.left != None:
                cur = cur.left
            return cur.data

    def findNumLessOrEq(self, k, node=-1):
        t = 0
        if node == -1:
            node = self.root
        if node != None:
            if node.data <= int(k):
                t += 1
                t += self.findNumLessOrEq(k,node.left)
                t += self.findNumLessOrEq(k,node.right)
            else:
                t += self.findNumLessOrEq(k,node.left)
        return t


T = BST()
inp_, k = input('Enter Input : ').split('/')
inp = map(int, inp_.split())
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print(T.findNumLessOrEq(k))
