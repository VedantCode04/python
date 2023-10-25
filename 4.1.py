# #An interactive program where one module asks
# numbers from the user and the second module
# performs at least three arithmetic operations on them.

import  mymodule as md

a = int(input("enter a"))
b = int(input("enter b"))

print(md.add(a,b))
print(md.sub(a,b))
print(md.mul(a,b))

