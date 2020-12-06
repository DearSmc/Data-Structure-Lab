text = input("Enter Input : ")
open = []
match = False
for txt in text:
    if txt in "([":
        open.append(txt)
    else:
        if len(open) != 0:
            op = open.pop()
            if (op == "[" and txt == "]") or (op=="(" and txt == ")"):       
                match = True
            else:
                match = False
                break
        else:
                match = False
                break
if len(open) != 0:
    match = False
if match:
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")