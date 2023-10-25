# Write a function to find out the factorial of a
# given number. I) without recursion II) with
# recursion

def fact(x):
    res = 1
    for i in range(1, x+1):
        res = res*i
    return res

def fact2(x):
    if x < 2:
        return 1
    else:
        return x * fact2(x-1)

x = int(input("enter value of x: "))

print("with loop ", fact(x))
print("with recurssion ", fact2(x))