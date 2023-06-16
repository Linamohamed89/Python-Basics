 #operators

#1 Arithmetic op
# +
A=5+5
print(A)


# -
B=10-4
print(B)
#6


# *
C=2*8
print(C)
#16


# /
D=9/3
print(D)
#3.0 /=float
E=9/4
print(E)
#2.25

# //
F=9//4
print(F)
#2 //=int

# **
G=3**2
print(G)
#9

# %
H=9%4
print(H)
print(H)
#1 9-4=5-4=1

# = == !=
x=10
print(x==10)



###########################################

#2 Assignment op

# +=
x=10
x +=1
print(x)

# *=
x=10
x *=3
print(x)

# /=
x=30
x /=4
print(x)

###########################################

#3 Conditions op

# if else example

x=500
if x > 600:
    print('x is beigger than 600')
else:
    print('x is smaller than 600')

x=600
if x > 500:
    print('Hello')
elif x>400:
    print('x > 400')
else:
    print('-------')

    

###########################################

#4 Nested if

# Nested if Ex

x=100
if x < 200:
    print('x is less than 200')

    if x == 150:
        print('x=150')
    elif x== 50:
        print('x=50')
elif x<50:
    print('x is less than 50')



###########################################

#5 If with Boolean OP

name="Lina"
age=31
if name=="Lina" and age==31:
    print("welcome Lina")

if name=="Lina" or age==31:
    print("you are not Lina")

userrname= 'admin'
password=12345

if userrname=='admin' and password==12345:
    print('welcome')

if userrname=='admin' or password==123456:
    print('Hello')

###########################################

#6 Single if Statement

x=100
if x==100:print("x=100")

x=5
print('x=5') if x==5 else print('x !=5')



# true condition false
x=500
print('x>400') if x>400 else print('x')
    
    
age=20
userrname='admin'

isAllawed=True if age > 18 else False
print(isAllawed)

#isAlllawed with out '..'

ff= True if age > 18 and userrname == 'admin' else False
print(ff)

#Boolean variable(True-False)



###########################################

#7 Conditions Best Practices
#using condition with dictionary elements [in - not in ]


# in - not in

birds={"parakeet":1,"parrot":2}
if "parrot" in birds:
    print("there is a parrot")

birds={"parakeet":1,"parrot":2}
if "parrot" not in birds:
    print("there is a parrot")


names=['Lina','Ahmed','saif']
if 'Lina' in names :
    print('welcome Lina')
if 'basel' not in names :
    print('not found')


# all - any

x=5
y=6
z=7

if x==5 and y==6 and z==7 :
    print('welcome')

# with all or any -->> list + , ([  ,  ,  ])

if all ([x==5 , y==6 , z==7]) :
    print('welcome')
    

if x==5 or y==6 or z==7 :
    print('Hello')

if any ([x==5 , y==6 , z==7]) :
    print('Hello')


a=1
b=2

if a==1 and b==2:
    print(True)

if a==1 or b==2:
    print(True)

if not (a==1 and b==3):
    print(True)

if a !=0 and b !=3 :
    print(True)


x=1
if x in (0,2,4):
    print("match")
else:
    print("not found")
    
############################################


# Loop

#a While

x=0
while x <10 :
    print(x)
    x +=1

#0
#0>10 +=1 -->1
#1>10 +=1 -->2
#2>10 +=1 -->3
#3>10 +=1 -->4
#4>10 +=1 -->5
#5>10 +=1 -->6
#6>10 +=1 -->7
#7>10 +=1 -->8
#8>10 +=1 -->9


#infinite loop

#x=0
#while 0>10 :
#   print(x)


# Nested While

x=0
while x<10:
    print(x)
    y=0
    while y<4:
        print(y)
        y +=1
    x +=1

print ('------------------------------------------------')

x=1
while x <=5:
    print(x)
    x +=5
    
print ('------------------------------------------------')

x=1
while x <=5:
    y=1
    while y <=10:
        print(f'{x}X{y}={x*y}')
        y +=1
    x +=1


    x=1
while x <=5:
    y=1
    while y <=10:
        print(f'{x}X{y}={x*y}')
        y +=1
       # peint('------------')False
    x +=1


    x=1
while x <=5:
    y=1
    while y <=10:
        print(f'{x}X{y}={x*y}')
        y += 1
   # print('-------------------')
    x += 1

print ('------------------------------------------------')

         

# For loop

for letter in 'python':
    print(letter)

