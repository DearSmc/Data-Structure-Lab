# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.high = 1

#     def insert(self,data ,cur = -99):

#         if cur == -99:
#             cur = self

#         if self.data == None:
#             self.data = data
#             print("*")
#             return self

#         if cur == None:
#             print("*")
#             return Node(data)

#         if data >= cur.data:
#             print("R",end=" ")
#             cur.right = self.insert(data,cur.right)
#         else:
#             print("L",end=" ")
#             cur.left = self.insert(data,cur.left)

#         return cur

#     def printTree(self,node,level=0):
#         if node != None:
#             self.printTree(node.right,level+1)
#             print("    "*level + str(node.data))
#             self.printTree(node.left,level+1)

# root = Node(None)
# for i in [1,2,4,5,-1,3]:
#     root = root.insert(int(i))

# root.printTree(root)


# class Node:
#     def __init__(self,data=None):
#         self.data = data
#         self.right = None
#         self.left = None
#         self.high = 1

#     def insert(self,data,cur=-99):

#         if cur == -99:
#             cur = self

#         if cur == None:
#             print("*")
#             return  Node(data)

#         if cur.data == None:
#             cur.data = data
#             print("*")
#             return self

#         if data > cur.data:
#             print("R",end=" ")
#             cur.right = self.insert(data,cur.right)
#         elif data < cur.data:
#             print("L",end=" ")
#             cur.left = self.insert(data,cur.left)

#         return cur

#     def printTree(self,cur,level=0):
#         if cur != None:
#             self.printTree(cur.right,level+1)
#             print("    "*level + str(cur.data))
#             self.printTree(cur.left,level+1)

# root = Node()

# for i in [1,2,-1,4,6,-2,0]:
#     root = root.insert(int(i))

# root.printTree(root)


# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.heigh = 1

#     def insert(self, data=None, node=-99):
#         if node == -99:
#             node = self

#         if node is None:
#             return Node(data)

#         if node.data == None:
#             node.data = data
#             return node

#         if data > node.data:
#             node.right = self.insert(data, node.right)
#         elif data < node.data:
#             node.left = self.insert(data, node.left)

#         return node

#     def printTree(self, node, level=0):
#         if node != None:
#             self.printTree(node.right, level+1)
#             print("    "*level + str(node.data))
#             self.printTree(node.left, level+1)


# root = Node()
# for i in [1, 2, -1, 3, 0, 4, -2]:
#     root = root.insert(int(i))

# root.printTree(root)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1

    def insert(self, data, node=-99):
        if node == -99:
            node = self

        if node == None:
            return Node(data)

        if node.data == None:
            node.data = data
            return node

        if data > node.data:
            node.right = self.insert(data, node.right)
        elif data < node.data:
            node.left = self.insert(data, node.left)

        
        node.height = max(self.getHeight(node.left),self.getHeight(node.right)) + 1
        bal = self.getHeight(node.left) - self.getHeight(node.right)

        if bal > 1 and data < node.left.data:
            return self.rightRo(node)
        elif bal > 1 and data > node.left.data:
            node.left = self.leftRo(node.left)
            return self.rightRo(node)
        elif bal < -1 and data > node.right.data:
            return self.leftRo(node)
        elif bal < -1 and data < node.right.data:
            node.right = self.rightRo(node.right)
            return self.leftRo(node)

        return node

    def rightRo(self,cur):
        mid = cur.left
        cur.left = mid.right
        mid.right = cur
        print("right Rotage")
        cur.height = max(self.getHeight(cur.left),self.getHeight(cur.right))+1
        mid.height = max(self.getHeight(mid.left),self.getHeight(mid.right))+1
        return mid

    def leftRo(self,cur):
        mid = cur.right
        cur.right = mid.left
        mid.left = cur
        print("left Rotage")
        cur.height = max(self.getHeight(cur.left),self.getHeight(cur.right))+1
        mid.height = max(self.getHeight(mid.left),self.getHeight(mid.right))+1
        return mid

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level+1)
            print("    "*level + str(node.data))
            # print("    "*level + str(self.getHeight(node)))
            self.printTree(node.left, level+1)

    def preOder(self, node):
        if node != None:
            print(node.data, end=" ")
            self.preOder(node.left)
            self.preOder(node.right)

    def inOder(self, node):
        if node != None:
            self.inOder(node.left)
            print(node.data, end=" ")
            self.inOder(node.right)

    def postOder(self, node):
        if node != None:
            self.postOder(node.left)
            self.postOder(node.right)
            print(node.data, end=" ")

    def br(self, node):
        q = []
        q.append(node)
        while len(q) != 0:
            temp = q.pop(0)
            if temp != None:
                print(temp.data, end=" ")
                q.append(temp.left)
                q.append(temp.right)

    def getHeight(self, node):
        if node == None:
            return 0
        else:
            return node.height


root = Node()
for i in [1, 2, 3, 4, 5, -2, -1]:
    root = root.insert(int(i))
    root.printTree(root)
    print("-"*30)
    

# root.printTree(root)
# root.preOder(root)
# print("")
# root.inOder(root)
# print("")
# root.postOder(root)
# print("")
# root.br(root)
# print("\n", root.getHeight(root))
