x = 3
print(float(x))
a ="abcdffgsaaafafasasv"
print(a[3])
print(a[3:9:2])
b = "bua"
print(a+b)
print(a+str(x))
y = 4
print(x+y)
print(f'x+y')
for i in range(2,10,2):
    print(i)
x = 0
for i in range(10):
    x +=0.1
print(x==1)
print(x,"==",10*0.1)

x = float(input("Choose a number: "))
epsilon = float(input("Choose a number (e.g., 0.001): "))
low = 0
high = x
guess = x / 2
while abs(guess**3 - x) >= epsilon:
    if guess**3 > x:
        high = guess
    else:
        low = guess
    guess = (low + high) / 2
print(f'{guess} is close to the cube root of {x}')

def is_even(x):
    """
    input:x is a positive number
    return:true or false
    """
    return x%2==0
print(is_even(100))
my_fun=is_even
print(my_fun(100))

lambda x:x%2 ==0
print((lambda x:x%2 == 0)(100))

numbers=[1,2,34,5,46]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)

tu=(5)
print(type(tu))
tup=(5,)
print(type(tup))

x=5
y=6
(x,y)=(y,x)
print(x,y)

L=[1,2,3,4,5,6,7,8,9,'ds']
L[9]=10
print(L)
L.append(11)
print(L)

S="I will be good at cooding"
L=list(S)
print(L)
L2=S.split(' ')
print(L2)
L3=S.split('be')
print(L3)
A=' '.join(L)
B=' '.join(L2)
C='be'.join(L3)
print(A)
print(B)
print(C)

E=[3324,432,1213,435,5466,32,32,45,22,4]
E.sort()
print(E)
E.reverse()
print(E)
G=sorted(E)
print(G)
H=reversed(E)
print(list(H))

A=[2,1,2,3,4,56,6]
B=[21,32,435,665,77,8,1]
C=A+B
A.extend([100,200])
B.extend([[100,200],[300,400]])
print(A,'\n',B,'\n',C)
print(id(A))
A.clear()
print(A)
print(id(A))

import copy
x=[1,2]
A=[1,2,3,4,5,6,7,8,9,0,x]
print(A)
print(id(A))
A2=A.copy()
print(A2)
print(id(A2))
A3=copy.deepcopy(A)
print(A3)
print(id(A3))
A2[10][1]=3
print(A)
print(A2)
A3[10][1]=4
print(A)
print(A3)

A=[1,2,3,4,5,6]
del(A[2])
print(A)
print(A.pop())
a=A.pop()
print(a)
A.remove(1)
print(A)

def f(L):
    Lnew=[]
    for e in L:
        Lnew.append(e**2)
    return Lnew
L=[1,23,4,44,556]
print(f(L))
Lnew=[e**2 for e in L]
print(Lnew)

def bisection_root(x,epsilon=0.01):
    low=0
    high=x
    guess=(low+high)/2
    while abs(guess**2-x)>=epsilon:
        if guess**2-x<epsilon:
            low=guess
        else:
            high=guess
        guess=(low+high)/2
    return guess
a=bisection_root(123)
b=bisection_root(123,0.5)
c=bisection_root(epsilon=0.5,x=123)
print(a,b,c)

def sum_digits(s):
    total=0
    for char in s:
        try:
            val = int(char)
            total+=val
        except ValueError:
            continue
    return total
s='sacavv6a2s3455v'
print(sum_digits(s))

my_dic={}
d={4:16}
grades={'H':100,'J':200,'Y':300}
print(my_dic)
print(d)
print(grades)
print(grades['H'])
grades['H']=400
grades['M']=500
print(grades)
del(grades['H'])
print(grades)
print('H' in grades)
print('X' in grades)
grades.keys()
print(grades.values())
print(grades.items())

L=[1,2,5,6,667,22]
x=max(L)
print(x)
