class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(item)
        self.size += 1

    def addHead(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            p.next = self.head
            self.head = p
        self.size += 1

    def search(self, item):
        if self.head == None:
            return "Not Found"

        cur = self.head
        i = 0
        if cur.data == item:
            return "Found"

        while cur.data != item and i < self.size-1:
            i += 1
            cur = cur.next
            if cur.data == item:
                return "Found"
        else:
            return "Not Found"

    def index(self, item):
        # print("in index ->" + self.search(item))
        if self.search(item) == "Found":
            cur = self.head
            i = 0
            while cur.data != item:
                i += 1
                cur = cur.next
            else:
                return i
        else:
            return -1

    def sizes(self):
        return self.size

    def pop(self, pos):

        if pos == 0 and pos < self.size:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.size -= 1
            return "Success"
        elif pos < self.size and pos > 0:
            cur = self.head
            i = 0
            while i < pos-1:
                i += 1
                cur = cur.next
            temp = cur.next.next
            cur.next.next = None
            cur.next = temp
            self.size -= 1
            return "Success"
        else:
            return "Out of Range"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} {2} {3}".format(L.search(i[3:]), i[3:], "in", L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(str(L.sizes()), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], str(L.index(i[3:])), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k ==
              "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
