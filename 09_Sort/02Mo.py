def _ThisisRecursive(s, end, _max=-99999999, _max_i=0, i=0):
    if i == end:
        return _max_i
    if _max < s[i]:
        _max = s[i]
        _max_i = i
    _ThisisRecursive(s, end, _max, _max_i, i + 1)


def Selection(s):
    _Selection(s, len(s) - 1)


def _Selection(s, n):
    if n == 1:
        return
    i = _ThisisRecursive(s, len(s) - 1)
    s[n], s[i] = s[i], s[n]
    print('swap {} <-> {} : {}'.format(s[n], s[i], s))
    _Selection(s, n - 1)


s = [int(x) for x in input('Enter Input : ').split()]
Selection(s)
print(s)
