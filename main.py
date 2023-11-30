def codeReader(code):
    array = [0] 
    lo = [0] 
    pl = 0 #pointer loaction of the array table
    i = 0 #pointer of the code 
    w = -1 #pointer of the loop table
    c = 0 #width of the array table
    q = 0 #width of the loop table 
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


codeReader(",>,[<[->>+>+<<<]>>[-<<+>>]<-]<[-].>.>.>.")
