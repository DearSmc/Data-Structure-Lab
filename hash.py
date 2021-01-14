
def hash_funtion(data):
    key = 0
    for i in range(len(data)):
        key += ord(i)
    return key

def hashing(data):
    
    key = hash_funtion(data)
    index = key % tableSize

    while table[index % tableSize] != -1:
        index += 1
    
    table[index%tableSize] = key

def lookup(data):
    key = hash_funtion(data)
    index = key % tableSize

    while table[index % tableSize] != -1 and table[index % tableSize] != data:
        return 
    return False


tableSize = 10
table = []*tableSize