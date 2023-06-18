


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

