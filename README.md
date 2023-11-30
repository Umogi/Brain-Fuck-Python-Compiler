## BRAIN FUCK
This is just the compailer in python that i have been working on there several other, and thats my atemnt to it.

Basicaly BrainF is a langaues that is base on these eight comands things <>-+.,[]
The way that BrainF works is by moving around in a 2D table array that just add and remove numbers from 0 to 127 as the ascii table.

By using the < or > it move by one step on the array base on where the pointer of the bracket with the Pointer Location.

By using the + or - it adds or subtractes 1 unit to the array where the Pointer Loction is.

The . it prints the number where the Pointer Location is on the array.

The , it asks for a number to read from the user and it replaces the number on the array where the Pointer Loction is.

When the [] square brackets are used is where the loop starts and ends until where the Pointer location is at the momnet and the array valeu is 0. 

E.g. if the code was this [-] it would never stop until the value of the that array is 0, or if the code was [->+<] it would move the number to the next array by subtracting 1 unit from the first and adding 1 unit to the second array.

## Code
```
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


codeReader(""code"")
```
## Codes

these are some of the Brain Fuck code that i have made

### ADDITION

addition with one unknown number
```
,>+++[->+<]
```

addition with two unknown numbers
```
,>,[->+<]
```
### SUBTRACTION

* **subtraction is trick without getting complicated ,because you can't there are no negative numbers therefor you need to subtract the smaller number to the biggerst 

### MULTIPLICATION

multiplication with one unknown number
```
,[->+++++<]>.
```

multiplication with two unknown numbers
```
,>,[<[->>+>+<<<]>>[_<<+>>]<-]<[-]>>>.
```

