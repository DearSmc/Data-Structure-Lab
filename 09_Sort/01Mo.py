def ThisisRecursive(s, end):
    _ThisisRecursive(s, 0, end)


def _ThisisRecursive(s, i, end):
    if i == end:
        return
    if s[i] > s[i+1]:
        s[i], s[i+1] = s[i+1], s[i]
    _ThisisRecursive(s, i + 1, end)


def bubble(s):
    _bubble(s, len(s) - 1)


def _bubble(s, n):
    if n == 0:
        return
    ThisisRecursive(s, n)
    _bubble(s, n - 1)

s = [int(x) for x in input('Enter Input : ').split()]
bubble(s)
print(s)