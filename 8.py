

###


class A:
    def do(self):
        print('in A')


class B(A):
    pass


class C:
    def do (self):
        print('in C')

class D(B,C):
    pass


###

n=D()
print(n.do())
##in A

print('-------------------------------')



class A:
    def do(self):
        print('in A')


class B(A):
    pass


class C:
    def do (self):
        print('in C')

class D(C,B):
    pass


###

n=D()
print(n.do())
##in C
