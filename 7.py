

#inheritance
###

'''
class calculator:
    def sum (x,y):
    print(x+y)


c1=calculator()
c1.sum(2,3)

c2=calculator()
c2.sum(20,13)
'''

#True

class calculator:
    def sum (mystro,x,y):
        print(x+y)
 


c1=calculator()
c1.sum(2,3)

c2=calculator()
c2.sum(20,13)


print('--------------------------------')


class calculator:
    def sum (self,x,y):
        print(x+y)
 


c1=calculator()
c1.sum(2,3)

c2=calculator()
c2.sum(20,13)

print('--------------------------------')

class calculator:
    def mul (self,x,y):
        print(x*y)
 


c1=calculator()
c1.mul(2,3)

c2=calculator()
c2.mul(20,13)


print('--------------------------------')

'''
def __init__(self,name):
    print(f'welcome{name}')


c1=calculator('mahmoud')

'''
print('--------------------------------')

class calculator:
    def sum(self,x,y):
        print(x+y)

    def mul(self,x,y):
        print(x*y)


class  SciCalc:
    def sum(self,x,y):
        print(x+y)

    def mul(self,x,y):
        print(x*y)

    def power(self,x,y):
        print(x**y)



v=SciCalc()
v.sum(2,3)
v.mul(2,3)
v.power(2,3)

print('--------------------------------')

class calculator:
    def sum (self,x,y):
        print(x+y)

    def mul (self,x,y):
        print(x*y)

class SciCalc(calculator):
    def power (self,x,y):
        print(x**y)


v=SciCalc()
v.sum(2,3) #5
v.mul(2,3)
v.power(2,3)


print('--------------------------------')



class calculator:
    def sum (self,x,y):
        print(x+y)

    def mul (self,x,y):
        print(x*y)

class SciCalc(calculator):
     def sum (self,x,y):
        print('-------')

    
     def power(self,x,y):
         print(x**y)


v=SciCalc()
v.sum(2,3) ##'-------'
v.mul(2,3)
v.power(2,3)


print('--------------------------------')

class calculator:
    def __init__(self , name):
        print(f'welcome {name}')


    
    def sum (self,x,y):
        print(x+y)

    def mul (self,x,y):
        print(x*y)

class SciCalc(calculator):
    def power (self,x,y):
        print(x**y)


v=SciCalc('Lina')
v.sum(2,3) 
v.mul(2,3)
v.power(2,3)



'''
encapsulation:self
inheritance
polymoephism
abstraction


------------------


fully
partially

'''


