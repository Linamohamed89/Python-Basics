



### Defination a Function


def mysum(x,y):
    print(x+y)


    
## True
mysum(5,10)
mysum(15,100)

'''
False
mysum(5+10)
mysum(15+100)
'''

'''
##
5,10
#1---->100


def divdedby(x,y):
    for n in range(1,101):
        if n%x==0 and n%y==0:
            print(n)

divdedby(3,5)
'''

def mysum1(x,y):
    return x+y


def mysum2(x,y):
    print(x+y)

b=mysum1(5,10)
print(b)
n=mysum2(20,30)
print(n)
