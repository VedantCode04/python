#Write a python program to find out even numbers
# from a list using filter ().

l = [1,2,3,4,5, 6]

def isEven(x):
    return x%2 == 0 

ans = filter(isEven, l)

print(list(ans))