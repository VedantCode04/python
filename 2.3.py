# Write a program to find out Fibonacci series
# using recursion and function as an object.

def fibonacci(x):
    if x <= 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

x = int(input("Enter x: "))

for i in range(x):
    print(fibonacci(i))

class Fibo:
    @staticmethod
    def fibonacci(x):
        if x <= 1:
            return x
        else:
            return Fibo.fibonacci(x - 1) + Fibo.fibonacci(x - 2)

x = int(input("Enter x: "))
obj = Fibo()

for i in range(x):
    print(obj.fibonacci(i))
