


 # Input


start= int(input('Enter Start : '))
end=int(input('Enter End : '))

print (type(start))

print('Number\tSquare')
print('--------------')

for x in range(start,end):
    print(x,'\t',x*x)

'''##
    start= int(input('Enter Start : '))
end=int(input('Enter End : '))

print (type(start))

print('Number\tSquare')
print('--------------')

for x in range(start,end+1):
    print(x,'\t',x*x)
'''


## ********** x 5 
start= int(input('Enter Start : '))
end=int(input('Enter End : '))

for x in range (start):
        print('*'*end)

## ****-->>50x
start= int(input('Enter Start : '))
end=int(input('Enter End : '))

for x in range (start):
    for y in range (end):
        print('*',end='')

        
'''
## *** 10x
## *** 10x -->>5x

start= int(input('Enter Start : '))
end=int(input('Enter End : '))

for x in range (start):
    for y in range (end):
        print('*',end='')
    print('')
    '''


'''
*
**
***
****
'''

for x in range (0,9):
    print('*'*x)









