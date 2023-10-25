#Write a Python program to check whether a specified value is contained in a group of
# values using lambda function. Test Data: 3 -> [1, 5, 8, 3] : True -1 -> [1, 5, 8, 3] : False

x=[1, 5, 8, 3]
l=lambda n: True if n in x else False
print("7 is not present so " , l(7))
print("5 is present so " , l(5))