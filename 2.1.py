# Write a function to find out x^y. Function should
# find out the square of x in case of default
# argument passing.

def findpower(x, n=2):
    return x**n
x = int(input("enter x: "))
y = int(input("enter y: "))

result = findpower(x, y)
result2 = findpower(x)

print("with argument",result, " without argument", result2)