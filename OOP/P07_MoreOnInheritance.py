class A:
    def doThis(self):
        print("A")
        print("A")  # 🔥 duplicate

class B(A):
    pass

class C:
    def doThis(self):
        print("C")

class D(B, A):
    pass

d = D()
d.doThis()
d.doThis()  # 🔥 duplicate call

if True:
    pass
