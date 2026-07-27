'''1 занятие'''
'''a=int(input())
b=int(input())
if ((a+b)%2==0):
    print("yes")
else:
    print("no")'''
'''a=int(input())
if (a>0):
    print(1)
elif (a<0):
    print(-1)
else:
    print(0)'''
'''elif проверяет другое условие, а else если ни одно из условий не оказалось истинным'''

'''24.11 ДЗ на 25.11'''
'''#Задача1#
a=float(input())
b=float(input())
if (a>b):
    print(a)
else:
    print(b)

#Задача2#
a=int(input())
if (10<a<99)and (a%2==0):
    print("yes")
else:
    print("no")

#Задача3#
a=int(input())
b=int(input())
c=int(input())
d=(a+b+c)/3
print(d)'''

#Занятие 25.11#
'''x = 0
a = 96


print((not x and x) or (a%10==1 and a>=10 and a <= 100))


0 or 0 or 0 or 0 or 0 or 1 = 1

x y   x and y
0 0   0 and 0 = 0
0 1   0
1 0   0
1 1   1



x y   x or y
0 0   0 
0 1   1
1 0   1
1 1   1


   not 

x
0  1
1  0'''

#Задача1#
'''for i in range(10,101,1):
    if(i%2==0 and i%10==4):
        print(i)'''
#Задача2#
'''a=int(input())
b=int(input())
for i in range(b,a-1,-1):
    if(i%3==0):
        print(i)'''
#Задача3#
'''a=int(input())
d=1
for i in range(1,a+1,1):
    d=d*i
print(d)'''
#Задача4#   
'''a=int(input())
f=0
for i in range(2,a,1):
    if (a%i==0):
        f=1
if (f==0):
    print("простое")
elif (f==1):
    print("составное")'''
#Домашняя задача#
'''n=int(input())
s=0
proisv=1
ma=2
mi=3
for i in range(0,n,1):
    k=int(input())
    s=s+k
    proisv=proisv*k
    if(i==0):
        ma=k
        mi=k
    else:
        if(k>ma):
            ma=k
        if(k<mi):
            mi=k        
M=s/n
G=(proisv)**(1/n)
print(M,G,ma,mi)'''
#Занятие 27.11#
#Задача1#
'''sum1=0
while True:
    x=int(input())
    if(x<0):
        continue
    if(x==0):
        break
    sum1=sum1+x
print(sum1)'''
#Задача2#
'''x=0
while True:
    x=input()
    if(x=="stop"):
        break
    if(int(x)%2==0):
        print(int(x))'''

#Домашняя задача1#
'''import random
a=random.randint(1,5)
attempts=0
print("Я загадал число, попробуй отгадать")
while True:
    n=int(input())
    attempts +=1
    if(n>a):
        print("очень много")
    elif(n<a):
        print("очень мало")
    else:
        print(n)
        print("Угадал!")
        print(attempts)
        break'''
#Домашняя задача2#
'''n=int(input())
f1=0
f2=1
for i in range(n):
    v=f1+f2
    print(f1)
    f1=f2
    f2=v'''
'''n=int(input())
f1=0
f2=1
v=0
for i in range(n):
    v=f1+f2
    f1=f2
    f2=v
print(f1)'''
#Занятие 02.12#
'''amount=0
previous=None
flag=False
while True:
    a=int(input())
    if(a==0):
        break
    if(previous is not None): #если предыдущее не пустота#
        if(a>previous):       
            if(flag==False):  #рост только начался, те до этого мы не были на участке возрастания# 
                amount +=1  #тогда добавляем +1#
                flag=True   #и тогда вкл режим роста#
        else:
            flag=False      #а если a<prev, то выкл режим роста#
    previous=a
print(amount)'''

#Домашняя задача1#
'''x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())
S=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
print(S)
#Домашняя задача2#
Max=None
Min=None
while True:
    a=int(input())
    if(a==0):
        break
    if(a%2!=0 and a>0):
        if(Max is None or Min is None): 
            Max=a
            Min=a
        else:                             
            if(a>Max):
                Max=a
            if(a<Min):
                Min=a
print(Max)
print(Min)'''

#Занятие 04.12#
'''def aver(x):
    Sum=0
    for b in range(0, len(x),1):
        Sum=Sum+x[b]
    return Sum/len(x)
def geom(x):
    proisv=1
    for i in range(0, len(x),1):
        proisv=proisv*x[i]
    return proisv**(1.0/len(x))
amount=int(input())
a=[]
for i in range(0,amount,1):
    b=int(input())
    a.append(b)
print(geom(a))

a=[0]*10
for i in range
c=int(input())
a[i]=c'''
    
#Повторить теорию массивов#
#+максимальный и минимальный элемент#

#Домашняя задача1#
'''def decrease(x):
    amount=0
    flag=False
    for i in range(1,len(x),1):
        if(x[i]<x[i-1]):
            if (flag==False):
                amount+=1
                flag=True
        else:
            flag=False
    return amount
x=[5,6,7,5,4,9,8,7,6]
print(decrease(x))'''

'''a=[]
n=5
for i in range(0,n):
    b=int(input())
    a.append(b)
print(a)''' #Запись массива через цикл for#

#Домашняя задача2#
'''def maximum(a):
    max1=a[0]
    max2=a[1]
    for i in range(0,len(a),1):
        if(a[i]>max1):
            max1=a[i]
    for i in range(0,len(a),1):
        if(a[i]!=max1):
            max2=a[i]
            break
    for i in range(0,len(a),1):
        if(a[i]>max2 and a[i]!=max1):
            max2=a[i]    
    return max2
    

a=[]
n=5
for i in range(0,n):
    b=int(input())
    a.append(b)
print(maximum(a))'''

#Занятие 11.12#
'''a=[]
n=8
i=0
while (i<n):
    b=int(input())
    a.append(b)
    i+=1
c=[]
i=0
while (i<n):
    if(a[i]>0 and a[i]%2==0):
        c.append(a[i])
    i+=1
print(c)'''

#Домашняя задача1#
'''import random
a=[]
for i in range(10):
    a.append(random.randint(1,10))
print(a)
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)
#i=len(a)-1
while i>=0:
    b.append(a[i])
    i-=1
print(b)#

#task2#
a=int(input())
def двоичная(a):
    b=[]
    while a>0:
        b.append(a%2)
        a=a//2
    c = []
    for i in range(len(b)-1,-1,-1):
        c.append(b[i])
    return c
print(двоичная(a))'''

#Задача1#
'''import random
def increase(a):
    for i in range(0,len(a)):
        minimal=a[i]
        c=i
        for u in range(i,len(a)):
           if(a[u]<minimal):
               minimal=a[u]
               c=u
        if(c==i):
            continue
        a[c]=a[i]
        a[i]=minimal
    return a        
a=[]
for i in range(5):
    a.append(random.randint(1,10))
print(a)
        
print(increase(a))

#Домашние задачи#
def binary_search(x,target):
    left=0
    right=len(x)-1
    while left<=right:
        mid=(left + right)//2
        if x[mid]==target:
            return mid      
        elif x[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1  

def bubble_sort(x):
    n=len(x)
    for i in range(n):
        for j in range(0,n-i-1):
            if x[j]>x[j + 1]:
                x[j]=x[j+1]
                x[j+1]=x[j]
    return x'''


'''def insert(a):
    for i in range(1,len(a)):
        current=a[i]
        last=i-1
        while last>=0 and a[last]>current:
            a[last+1]=a[last]
            last-=1
        a[last+1]=current
    return a
a=[1,5,7,4,2]
print (insert(a))'''    

#занятие 18.12#
'''a=[]
n=4
m=2
for i in range(0,n):
    a.append([])
    for j in range(0,m):
        num=int(input())
        a[i].append(num)
for i in range(0,n):
    for j in range(0,m):
        print(a[i][j],end=' ')
    print()

maximum=a[0][0]
for i in range (0,n):
    for j in range(0,m):
        if(a[i][j]>maximum):
            maximum=a[i][j]
print(maximum)

summa=0
for i in range(0,n):
    for j in range(0,m):
        summa+=a[i][j]
aver=summa/(n*m)
print(aver)'''

#Домашние задачи
'''a=[]
n=2
m=2
for i in range(0,n):
    a.append([])
    for j in range(0,m):
        num=int(input())
        a[i].append(num)
for i in range(0,n):
    min_row=a[i][0]
    for j in range(0,m):
        if a[i][j]<min_row:
            min_row=a[i][j]
    print("Минимум в строке",i+1,"=",min_row)
for j in range(0,m):
    min_col=a[0][j]
    for i in range(0,n):
        if a[i][j]<min_col:
            min_col=a[i][j]
    print("Минимум в столбце",j+1,"=",min_col)

#Task2
a=[]
b=[]
n=3
m=3
for i in range(0,n):
    a.append([])
    for j in range(0,m):
        num=float(input())
        a[i].append(num)
for i in range(0,n):
    b.append([])
    for j in range(0,m):
        if a[i][j]<0:
            b[i].append(a[i][j])
print("Новая матрица",b)'''

#Занятие 23.12
'''import random
def quadro(a):
    return a**2
a=[]
b=[]
row=0
column=0
while True:
    print("Введите кол-во строк n")
    n=int(input())
    if 4<=n<=10:
        break
while True:
    print("Введите кол-во столбоц m")
    m=int(input())
    if 4<=m<=10:
        break
for i in range(0,n):
    a.append([])
    for j in range(0,m):
        a[i].append(random.randint(0,100))
print(a)
for i in range(1,n-1):
    b.append([])
    column=0
    for j in range(1,m-1):
        if a[i][j]<10:
            b[row].append(quadro(a[i][j]))
        else:
            b[row].append(a[i][j])
        column+=1
    row+=1   
for i in range(0,row):
    for j in range(0,column):
        print(b[i][j],end=' ')
    print()'''
            
#Task 2
'''import random
a=[]
b=[]
while True:
    print("Введите кол-во строк n")
    n=int(input())
    if 4<=n<=10:
        break
while True:
    print("Введите кол-во столбоц m")
    m=int(input())
    if 4<=m<=10:
        break
for i in range(0,n):
    a.append([])
    for j in range(0,m):
        a[i].append(random.randint(0,100))
for i in range(0,n):
    for j in range(0,m):
        print(a[i][j],end=' ')
    print()
for i in range(0,n):
    flag=False
    for j in range(1,m):
        if a[i][j]>a[i][j-1] or flag==True:
            b.append(a[i][j-1])
            flag=True
            if a[i][j]<a[i][j-1]:
                flag=False
        else:
            flag=False
    if flag==True:
        b.append(a[i][m-1])     
print("Массив B",b)'''

#Занятие 25.12

'''S="привет"
for i in range(len(S)-1,-1,-1):
    print(S[i],end='')'''

#Занятие 08.01
'''S=input()
print(S[0:6:1])
print(S[len(S)-4:len(S):1])
print(S[3:12:1])
print(S[0:len(S):2])
print(S[::-1])

#Task 1
a=[]
n=int(input())
m=int(input())
for i in range(0,n):
    a.append([])
    for j in range(0,m):
        a[i].append(input())
for i in range(0,n):
    for j in range(0,m):
        print(a[i][j],end=' ')
    print()


for i in range(0,n):
    for j in range(0,m):
        a_amount=0
        for k in range(0,len(a[i][j])):
            if a[i][j][k]=='а': 
                a_amount+=1
        if a_amount==3 and len(a[i][j])%2==0:
            print(a[i][j])'''   
        
#Домашние задачи
'''a=[]
print('ввести кол-во строк')
n=int(input())
print('ввести кол-во столбцов')
m=int(input())
for i in range(0,n):
    a.append([])
    for j in range(0,m):
        print('ввести строку для матрицы')
        a[i].append(input())
for i in range(0,n):
    for j in range(0,m):
        print(a[i][j],end=' ')
    print()

str_long=a[0][0]
str_short=a[0][0]

for i in range(0,n):
    for j in range(0,m):
        if len(a[i][j])>len(str_long):
            str_long=a[i][j]
        if len(a[i][j])<len(str_long):
            str_short=a[i][j]
print('Самая длинная строка', str_long)
print('Самая короткая строка',str_short)'''

#983+26-487

'''while True:
    s=input('Введите выражение (или stop для выхода):')
    if s=='stop':
        break

    result = 0
    number = 0
    sign = 1  # 1 — плюс, -1 — минус

    for i in s:
        if i.isdigit():
            number=number*10+int(i)
        elif i=='+':
            result+=sign*number
            number=0
            sign=1
        elif i=='-':
            result+=sign*number
            number=0
            sign=-1

    result+=sign*number
    print(result)'''


a=[5,2,9,1,7]
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        print(a)
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a)












                    
