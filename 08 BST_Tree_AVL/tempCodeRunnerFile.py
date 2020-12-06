x = min(inp[2*cur+2], inp[2*cur+1])
    inp[cur] = x
    inp[2*cur+1] -= x
    i