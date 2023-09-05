#Diamond shape problem in inheritance

class A:
    def method(self):
        print('This method belongs to class A')

class B(A):
    def method(self):
        print('This method belongs to class B')
    pass

class C(A):
    def method(self):
        print('This method belongs to class C')
    pass

class D(C,B):
    pass

d = D()
#case1 - method will not be overiden in class B and C
d.method()
#case2 - method will be overiden in class B but not C
#case3 - method will be overiden in class C but not B
#case4 - method will be overiden in both class B and C