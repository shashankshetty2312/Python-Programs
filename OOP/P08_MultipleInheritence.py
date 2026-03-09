class A(object):
    def doThis(self):
        print("Doing this in A")


class B(A):
    pass


class C(object):
    def doThis(self):
        print("Doing this in C")


class D(B, C):   # multiple inheritance
    pass


print("\n---- Multiple Inheritance Example ----")

d_obj = D()
d_obj.doThis()

print("MRO:", D.mro())
