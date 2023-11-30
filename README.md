This is just the compailer in python that i have been working on there several other, and thats my atemnt to it.

Basicaly BrainF is a langaues that is base on these eight comands things <>-+.,[]
The way that BrainF works is by moving around in a 2D table array that just add and remove numbers from 0 to 127 as the ascii table.

By using the < or > it move by one step on the array base on where the pointer of the bracket with the Pointer Location.
By using the + or - it adds or subtractes 1 unit to the array where the Pointer Loction is.
The . it prints the number where the Pointer Location is on the array.
The , it asks for a number to read from the user and it replaces the number on the array where the Pointer Loction is.
When the [] square brackets are used is where the loop starts and ends until where the Pointer location is at the momnet and the array valeu is 0. 
E.g. if the code was this [-] it would never stop until the value of the that array is 0, or if the code was [->+<] it would move the number to the next array by subtracting 1 unit from the first and adding 1 unit to the second and it goes like this:

Exaple code : ",[->+<]>."

 !
[0][0]

,
"input: 2"

 !
[2][0]

[
 !
[2][0]

-
 !
[1][0]

>
   !
[1][0]

+
   !
[1][1]

<
 !
[1][1]

]
 !
[1][1]

-
 !
[0][1]

>
    !
[0][1]

+
    !
[0][2]

<
 !
[0][2]

]
 !
[0][2]

>
    !
[0][2]

.
"output: 2"
    !
[0][2]
