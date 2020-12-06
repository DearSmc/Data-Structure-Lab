
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.previous = self.tail
            self.tail.next = p
            self.tail = p
        self.sizes += 1

    def addHead(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.next = self.head
            self.head.previous = p
            self.head = p
        self.sizes += 1

    def insert(self, pos, item):
        p = Node(item)

        if pos >= self.sizes-1:
            self.append(item)
        elif pos < 0 and pos >= -self.sizes:
            # ตำแหน่ง  = sizes + pos -1
            cur = self.tail
            i = -1
            while i != pos:
                cur = cur.previous
                i -= 1
            p.next = cur
            p.previous = cur.previous
            cur.previous.next = p
            cur.previous = p
            self.sizes += 1
        else:
            self.addHead(item)

    def search(self, item):
        if self.isEmpty():
            return "Not Found"

        i = 0
        cur = self.head
        if cur.value == item:
            return "Found"
        while cur.value != item and i < self.sizes-1:
            i += 1
            cur = cur.next
            if cur.value == item:
                return "Found"
        else:
            return "Not Found"

    def index(self, item):
        if self.search(item) == "Found":
            i = 0
            cur = self.head
            if cur.value == item:
                return i
            while cur.value != item:
                i += 1
                cur = cur.next
                if cur.value == item:
                    return i
        else:
            return -1

    def size(self):
        return self.sizes

    def pop(self, pos):
        if pos < self.sizes and pos >= 0 and self.sizes > 0:
            self.sizes -= 1
            if pos == 0:
                temp = self.head
                self.head = self.head.next
                temp.previous = None
            elif pos == self.sizes-1:
                self.tail.previous.next = None
                self.tail = self.tail.previous
            else:
                i = 0
                cur = self.head

                while i < pos and i < self.sizes:
                    i += 1
                    cur = cur.next
                cur.previous.next = cur.next
                cur.next.previous = cur.previous
                cur.next = None
                cur.previous = None
            return "Success"
        else:
            return "Out of Range"


inp = input("Enter Input (L1,L2) : ").split()

L1 = LinkedList()
for i in inp[0].split("->"):
    L1.append(i)

L2 = LinkedList()
for i in inp[1].split("->"):
    L2.append(i)

print("L1    : "+str(L1))
print("L2    : "+str(L2))
print("Merge : {}{}".format(L1, L2.reverse()))
