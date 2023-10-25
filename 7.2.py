#method overloading

class A():
    def func(self):
        print("this is from class A")

class B(A):
    def func(self):
        print("this is from class B")

obj = B()

obj.func()

obj = A()

obj.func()