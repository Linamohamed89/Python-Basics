

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

print(D.mro())
#[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]



print('-------------------------------')

'''
-create student
-add mark
-get avg


'''


class Student:
    def create_student(self,name):
        print(f'welcome {name}')
        self.marks=[]


    def add_mark(self,mark):
        self.marks.append(mark)
        print(self.marks)
        


    def get_avg(self):
        avg=sum(self.marks)/len(self.marks)
        print(avg)

s1=Student()
s1.create_student('Lina')
s1.add_mark(20)
s1.add_mark(30)
s1.add_mark(40)
s1.add_mark(60)
s1.add_mark(80)
s1.get_avg()

print('-----------------------------')



s2=Student()
s2.create_student('Margana')
s2.add_mark(25)
s2.add_mark(30)
s2.add_mark(43)
s2.add_mark(60)
s2.add_mark(100)
s2.get_avg()

print('-------------------------------')






class Student:
    def __init__(self,name):
        print(f'welcome {name}')



s1=Student('Lina')


print('-------------------------------')




'''
bank
   -create account :name,age,gender
   -deposite
   -withdrow
   -view balance
   -shaw all details
   '''


class Bank:
    def __init__ (self,name,age,gender):
        print(f'welcome {name}')
        self.balance=0


    def deposite(self,amount):
        self.balance +=amount
        print(f'your current balance:{self.balance}')


    def withdraw(self,amount):
        if amount > self.balance:
            print('not enough balance')
        else:
            self.balance -=amount
            print(f'your current balance:{self.balance}')


c1=Bank('Lina',30,'male')
c1.deposite(500)#your current balance:500
c1.deposite(600)#your current balance:1100
c1.withdraw(300)#your current balance:800
c1.withdraw(1000)#not enough balance

print('-------------------------------')


