

#### string

s='welcome'
f="welcome"
a='''welcome'''
print(s)
print(f)
print(a)

print('-------------------------------')

f_name ='Lina'
L_name ='Muhammed'
print(f"{f_name} {L_name}")


print('-------------------------------')


f_name ='Lina'
L_name ='Muhammed'
print('Lina\nMuhammed')

print('Lina\tMuhammed')


print('-------------------------------')


text='my name is Lina , i am a python developer'
print(text.upper()) #ACCGJ......

print(text.lower()) #ahgjhg.....

print(text.title()) #Iam Python Dev....

print(text.replace('is','was')) #change word

print(text.split(','))

print(text.split(' '))


print(text[0]) #first litter
print(text[-1])#last letter
print(text[-2])#befor last letter
print(text[0:6])#letter 1 to 6
print(text[:6])# 0 to 6
print(text[6:])#6 to end


# List

l=[1,2,3,4,True,'welcome']

print(l[0]) #1
print(l[-1]) #'welcome'
l[0]=100
print(l[0]) #l=[100,2,3,4,True,'welcome'] jest in list



#list function

l=[1,2,3,4,True,'welcome']

l.append(1000)
print(l)

#[1, 2, 3, 4, True, 'welcome', 1000]
l.insert(0,200)
print(l)

#[200, 1, 2, 3, 4, True, 'welcome', 1000]
l.remove(1000)
print(l)

#[200, 1, 2, 3, 4, True, 'welcome']

'''
l.sort( )
print(l)
'''

x=[1,2,3,400,600]

x.reverse()
print(x)
#[600, 400, 3, 2, 1]

x.sort(reverse=True)
print(x)

#[600, 400, 3, 2, 1]


 
k=[1,20,30,40,100,60]
k.reverse()
print(k)
#[60, 100, 40, 30, 20, 1]

k.sort(reverse=True)
print(k)
#[100, 60, 40, 30, 20, 1]

k.pop()
print(k)

print(min(k))
print(max(k))

#[100, 60, 40, 30, 20] remove the last value


#tuple
t=(1,10,4,8,True)

min(t)
print(min(t))
print(max(t))










