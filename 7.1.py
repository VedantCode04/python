#inheritance

class A():
    x = "from a"
class B(A):
    y = "from b"

obj = B()

print(obj.x, obj.y) #single level

class C(B):
    z = "from c"
obj2 = C()
print(obj2.x, obj2.y, obj2.z) #multilevel

class D():
    w = "from D"

class E(A, D):
    p = "from E"

obj3 = E()

print(obj3.x, obj3.w, obj3.p) #multiple


class F(A):
    q = "from f"

class R(B, F):
    r = "from r"

obj4 = R()

print(obj4.r, obj4.q, obj4.y, obj4.x) #hybrid