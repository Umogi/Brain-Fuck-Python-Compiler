def interpret(code):
    array = [0]
    lo = [0]
    pl = 0
    i = 0
    w = -1
    c = 0
    q = 0
    while i < len(code):
        if code[i] == "+":
            if array[pl] == 127:
                array[pl] = 0
            else:
                array[pl] += 1
        elif code[i] == "-":
            if array[pl] == 0:
                array[pl] = 127
            else:
                array[pl] -= 1
        elif code[i] == ".":
            print(array[pl])
        elif code[i] == ",":
            x = input()
            try:
                y = int(x)
            except ValueError:
                y = ord(x)
            array[pl] = y
        elif code[i] == ">":
            if c == pl:
                array.append(0)
                c += 1
            pl += 1
        elif code[i] == "<":
            if pl == 0:
                pl = c
            else:
                pl -= 1
        elif code[i] == "[":
            w += 1
            if w > q:
                lo.append(0)
                q += 1
            lo[w] = i
        elif code[i] == "]":
            if array[pl] == 0:
                w -= 1
            else:
                i = lo[w]
        i += 1


interpret(",>,[<[->>+>+<<<]>>[-<<+>>]<-]<[-].>.>.>.")
