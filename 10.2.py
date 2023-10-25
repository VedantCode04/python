#threading
import threading as td

def square(x):
    print(x**2)
def cube(y):
    print(y**3)

t1 = td.Thread(target=square, args=(10,))
t2 = td.Thread(target=cube, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()