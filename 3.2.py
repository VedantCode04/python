#Write a Python program to find whether a given string ends with a given character using
# Lambda.

str = "vedant"
length = len(str)

char = "t"

l = lambda x: True if str.endswith(char) else False

print("func = ", l(str))