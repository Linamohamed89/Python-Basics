


# Python Loops

# with while

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

i = 1
while i < 6:
  print(i)
  i += 1

x=0
while x<10:
    print(x)
    y=0
    while y<4:
        print(y)
        y +=1
    x +=1

print ('------------------------------------------------')










# For loop

for letter in 'python':
    print(letter)

for x in [1,2,3,4]:
    print(x)

for x in [1,2,3,4,[1,2,3]]:
    print(x)

#for x in 1234:
    #print(x)
    
# int object is not iterable ( X loop)


print ('------------------------------------------------')

# range

#range(start,end,step=1)
#range(10)  #0 1 2 3 4 5 6 7 8 9
#range(2,10)#2 3 4 5 6 7 8 9
#range(2,10,3)#2 5 8

#list(range(2,10,3))


for x  in range (1,11):
    print(x)

for x in range (1,11,2):
    print(x)

for x in range(1,6):
    for y in range(1,11):
        print(f'{x} X {y} = {x*y}')
    print('----------------------')

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


# x=1
#while x <=5:
   ### y=1
   # while y <=10:
       # print(f'{x}X{y}={x*y}')
      #  y +=1
       # peint('------------')False
   # x +=1


   # x=1
#while x <=5:
   # y=1
   # while y <=10:
       #print(f'{x}X{y}={x*y}')
       # y += 1
   # print('-------------------')
   # x += 1

print ('------------------------------------------------')




for i in range (4):
    for x in range (2):
        print(i,x)


print ('------------------------------------------------')


# Loop with lists

c=['hey','Lina',5]
for x in c:
    print(x)


    #list of lists

l =[[1,2,3],[4,5,6],[7,8,9]]
for x in l:
        print(x)

#x=[1,2,3]
#x=[4,5,6]
#x=[7,8,9]


l =[[1,2,3],[4,5,6],[7,8,9]]
for x in l:
    for y in x:
        print(y)

#

l =[[1,2,3],[4,5,6],[7,8,9]]
for x in l[0]:
    print(x)  #-->> just 1 , 2 , 3

# l[0] 1 ,2 ,3
# l[1] 4 ,5 ,6
# l[2] 7 ,8 ,9


print ('------------------------------------------------')


##Contol Statement

#Break

'''
x=0
while x < 10:
    if x ==5:
        break
    print(x)
'''


# 1
for x in range (10):
    print(x)


#2
    for x in range (10):
        if x ==5:
            break
        print(x)



#3
    for x in range (10):
        if x ==5:
            break
        print(x)
print('---------------------------------------')

#Continue

'''
x=0
while x < 10:
    if x==5 :
        continue
    print(x)
'''


for x in range (10):
    if x ==5:
        continue
    print(x)





for x in range (10):
    pass
print('-----------------')


def func1():
    pass
def func2():
    pass
print('welcome')

print('---------------------------------------')


# Loops Best Practices


print('Number              Square')
print('--------------------------')

x=1
while x<11 :
    print(x,'             ',x*x)
    x +=1



print('Number\tSquare')
print('------------------')

x=1
while x<11 :
    print(x,'\t',x*x)
    x +=1
    


for x in range (1,11):
    print(x,'\t',x*x)






