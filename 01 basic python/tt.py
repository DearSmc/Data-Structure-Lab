input = '# - - - - ,- # - - - ,- # - - - ,- - - - - ,- # # - - '
inp   = input.split(',')
inp_  = []
for x in inp:
    inp_.append([y for y in x.split(' ')])

for i in range(5):
    for j in range(5):
        #print(inp_[i][j])
        if inp_[i][j] != '#':
            inp_[i][j] = '0'

for i in range(5):
    for j in range(5):
        if inp_[i][j] == '#':
            for ii in range(-1,2):
                for jj in range(-1,2):
                    if 0 <= i+ii < 5 and 0 <= j+jj < 5 and inp_[i+ii][j+jj] != '#':
                        inp_[i+ii][j+jj] = str(int(inp_[i+ii][j+jj])+1)

for x in inp_:
    for y in x:
        print(y, end='')
    print()